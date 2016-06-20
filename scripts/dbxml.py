#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-

u"""
    dbxml
    ~~~~~

    Library with XML-filters to convert DocBook-XML to reST

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.
"""

# pylint: disable=W0603, C0103, C0325, C0321, C0330, R0912

# ==============================================================================
# imports
# ==============================================================================

import re, sys
from common import FSPath, Container, PContainer,  xml_unescape
from lxml import etree

def MSG(msg):
    sys.stdout.write("dbxml:: %s\n" % msg)

RESOUCE_FORMAT = "%s_files"

INT_ENTITES = Container()
INT_ENTITES["nbsp"] = r" "
for x in ["frac12", "frac13", "frac14", "times", "copy", "hellip", "le", "ge"
          , "sub", "sup", "micro", "plusmn", "mdash", "alpha", "num", "ndash" ]:
    INT_ENTITES[x] = xml_unescape("&%s;" % x)

# ==============================================================================
def filterXML(
        folder, inFile, outFile
        , xmlFilter
        , parseIncludes = False
        , fragTag = None, ID = None ):
# ==============================================================================

    u"""Replace some xml-Markups with reST literals."""

    folder    = FSPath(folder)
    outFile   = FSPath(outFile)

    xmlFilter.parseData.update(
        outFile         = outFile
        , parseIncludes = parseIncludes )

    rootNode  = xmlFilter.parseFile(folder, inFile, fragTag=fragTag, ID=ID)
    xmlFilter.walk(rootNode)
    with (folder / outFile).openTextFile("w") as out:
        out.write(
            etree.tostring(rootNode, encoding='unicode') )

# ==============================================================================
def subTemplate(inFile, outFile):
# ==============================================================================

    u"""Substitude kenerle-doc place holder in docbook.tmpl files."""

    # detailed description see class ReSTTemplate
    import re
    tmpl_re = re.compile(r"^!([EIDFPC])([^\s]*)\s+(.*?)\s*$")
    tag_format = """<rstTemplate op="%s" fname="%s" args="%s"/>"""

    with inFile.openTextFile() as src, outFile.openTextFile("w") as dst:
        for lineno, orig_line in enumerate(src):
            line = orig_line
            if tmpl_re.match(orig_line):
                match = tmpl_re.match(orig_line)
                op, fname, args = match.groups()
                line = tag_format % (op, fname, args)
            dst.write(line)

# ==============================================================================
def subEntities(inFile, outFile, ext_entities, int_entities):
# ==============================================================================

    u"""Substitude internal and external entities.

    :param str folder: Root-folder where conversion takes place.
    :param str inFile: Preprocess XML file.

    :param ext_entities: container with the external entities
    :type ext_entities: EntityContainer or None

    :param int_entities: container with the internal entities
    :type int_entities: EntityContainer or None

    External entities will be replaced by a ``<rstInclude fname='%s'/>`` tag.
    XMLTag.rstInclude_tag
    """
    entity = re.compile(r'''&(?P<name>[a-zA-Z][0-9a-zA-Z_-]+);''')

    with inFile.openTextFile() as src, outFile.openTextFile("w") as dst:
        for orig_line in src:
            line = orig_line
            # FIXME: pass "*" as &#x22C6;
            line = line.replace("*", "&#x22C6;")
            for match in entity.finditer(orig_line):
                name = match.group('name')
                if int_entities:
                    sub = int_entities.get(name, None)
                    if sub:
                        line = line.replace("&%s;" % name, sub)
                if ext_entities:
                    sub  = ext_entities.get(name, None)
                    if sub is None:
                        sub  = ext_entities.get("chunk_" + name, None)
                    if sub:
                        line = line.replace(
                            "&%s;" % name
                            , "<%s fname='%s'/>" % (XMLTag.rstInclude_tag, sub))

            # internal entities within internal entities .. grrr
            if int_entities:
                for match in entity.finditer(line):
                    name = match.group('name')
                    sub  = int_entities.get(name, None)
                    if sub:
                        line = line.replace("&%s;" % name, sub)
            # write to file
            dst.write(line)

# ==============================================================================
class EntityContainer(PContainer):
# ==============================================================================

    u"""Variant of PContainer used by the dbtools."""

    def addNew(self, attr, val):
        unset = object()
        exists = self.get(attr, unset)
        for k,v in self.items():
            if v == val:
                MSG("two entity names with identical value %s <--> %s (%s)" % (attr, k,v))

        if exists != unset:
            if exists == val:
                MSG("double entity entry %r -->  %r" % (attr, exists))
            else:
                raise KeyError("name collision %r -->  old: %r <--> new: %r"
                               % (attr, exists, val))
        else:
            self[attr] = val

# ==============================================================================
def hook_copy_file_resource(srcFolder):
# ==============================================================================

    srcFolder = FSPath(srcFolder)

    def hookFunc(node, rstPrefix, parseData):  # pylint: disable=W0613

        # run this hook only on the root node
        if node.getparent() is not None:
            return node

        # are there any filerefs in?
        filerefList = node.findall(".//*[@fileref]")
        if not filerefList:
            return node

        thisFile   = FSPath(parseData.fname)
        bookBase   = FSPath(parseData.folder)

        bookOffset = thisFile.DIRNAME
        resFolder  = FSPath(RESOUCE_FORMAT % thisFile.BASENAME.SKIPSUFFIX)
        dstFolder  = bookBase / bookOffset / resFolder

        dstFolder.makedirs()

        for tag in filerefList:
            fileref = FSPath(tag.get("fileref")).BASENAME
            src = next(srcFolder.reMatchFind(fileref), None)
            if src is None:
                raise Exception("fileref: %s could not found in %s" % (fileref, srcFolder))
            src.copyfile(dstFolder)
            tag.set("fileref", resFolder / fileref )
            #SDK.CONSOLE()
        return node
    return hookFunc


# ==============================================================================
def hook_chunk_by_tag(*chunkPathes):
# ==============================================================================

    u"""
    Chunk DocBook XML document into XML fragments.

    Requirement for the division is an ID (e.g. ``<chapter id="intro" ...``)
    """
    chunkPathes = chunkPathes

    def hookFunc(node, rstPrefix, parseData): # pylint: disable=W0613

        # run this hook only on the root node
        if node.getparent() is not None:
            return node
        realNode = node

        if (node.tag == "dummy"
            and len(node) == 1
            and node[0].get("chunkNode") is not None):
            realNode = node[0]

        for tag in chunkPathes:
            chunkNodes = realNode.findall("%s" % tag)
            for elem in chunkNodes:
                if elem.get("chunkNode") is not None:
                    continue
                ID = elem.get("id")
                if ID is None:
                    # generate unique ID by counting preceding siblings on any
                    # hierarchy level.
                    _p = elem
                    ID = []
                    while _p is not None:
                        if _p.tag == "dummy":
                            break
                        ID.insert(0, len(list(_p.itersiblings(preceding=True))))
                        _p = _p.getparent()
                    ID = "-".join(["%03d" % x for x in ID])
                    ID = "%s-%s" % (parseData.fname.BASENAME.SKIPSUFFIX, ID)
                ext_entity = parseData.fname.DIRNAME / ("%s.xml" % ID)
                XMLTag.chunkNode(
                    elem
                    , parseData.folder
                    , ext_entity.suffix(parseData.fname.SUFFIX))
            if len(chunkNodes):
                break
        return node
    return hookFunc

# ==============================================================================
def hook_html2db_table(node, rstPrefix, parseData): # pylint: disable=W0613
# ==============================================================================
    u"""This hook converts a HTML table to a DocBook table

    This is done by simply change ``<tr>`` and ``<td>`` (``<th>``) tags to
    ``<row>`` and ``<entry>`` tags
    """
    # run this hook only on the root node
    if node.getparent() is not None:
        return node

    for elem in node.findall(".//tr"):
        newNode = XMLTag.copyNode(elem, "row", moveID=True)
        XMLTag.replaceNode(elem, newNode)

    for elem in node.findall(".//th") + node.findall(".//td"):
        newNode = XMLTag.copyNode(elem, "entry", moveID=True)
        XMLTag.replaceNode(elem, newNode)

    return node

# ==============================================================================
def hook_fix_broken_tables(fname_list=None, id_list=None):
# ==============================================================================

    u"""This hooks add missing colspecs to the *broken* table.

    A complete colspec definition is needed by pandoc, otherwise the build of
    the ASCII-art table fails within pandoc."""
    fname_list = fname_list or []
    id_list    = id_list    or []

    def hookFunc(node, rstPrefix, parseData): # pylint: disable=W0613

        if node.tag != "table":
            return node

        fname = parseData.folder.BASENAME / parseData.fname.SKIPSUFFIX
        if (node.get("id") not in id_list and fname not in fname_list):
            return node

        table  = node
        tgroup = table.find("tgroup")
        cols   = int(tgroup.get("cols"))
        thead  = tgroup.find("thead")
        tbody  = tgroup.find("tbody")

        if thead is not None:
            # is there any row in the header with more entries as defined cols?
            for row in thead.findall("row"):
                entries = row.findall("entry")
                if len(entries) > cols:
                    cols = len(entries)
                    tgroup.set("cols", str(cols))

        for row in tbody.findall("row"):
            # is there any row in the body with more entries as defined cols?
            entries = row.findall("entry")
            if len(entries) > cols:
                cols = len(entries)
                tgroup.set("cols", str(cols))

        if thead is not None:
            # add missing entries to header rows
            for row in thead.findall("row"):
                entries = row.findall("entry")
                if len(entries) < cols:
                    for _x in range(cols - len(entries)):
                        row.append(node.makeelement("entry"))

        # add missing entries to body rows
        for row in tbody.findall("row"):
            entries = row.findall("entry")

            if len(entries) < cols:
                for _x in range(cols - len(entries)):
                    row.append(node.makeelement("entry"))
        return node
    return hookFunc

# ==============================================================================
def hook_replaceTag(id2TagMap):
# ==============================================================================

    id2TagMap = id2TagMap

    def hookFunc(node, rstPrefix, parseData):  # pylint: disable=W0613
        # run this hook only on the root node
        if node.getparent() is not None:
            return node
        for ID, newTag in id2TagMap.items():
            elem = node.find(".//*[@id='%s']" % ID)
            if elem is not None:
                newNode = XMLTag.copyNode(elem, newTag, moveID=True)
                XMLTag.replaceNode(elem, newNode)
        return node
    return hookFunc


# ==============================================================================
def hook_drop_usless_informaltables(node, rstPrefix, parseData):
# ==============================================================================

    u"""Hook to convert useless informatables to (e.g) paragraphs"""
    # run this hook only on the root node
    if node.getparent() is not None:
        return node

    for table in node.findall(".//informaltable"):
        tbody = table.find(".//tbody")
        max_cols = 0
        for row in tbody.findall(".//row"):
            c = len(row.findall(".//entry"))
            if c > max_cols:
                max_cols = c
        section = node.makeelement("section")
        if max_cols < 2:
            for entry in tbody.find(".//entry"):
                para = XMLTag.copyNode(entry, "para", moveID=True)
                section.append(para)
            XMLTag.replaceNode(table, section)
    return node

# ==============================================================================
def hook_flatten_tables(table_id_list="all"):
# ==============================================================================

    u"""Hook to convert tables into a double-stage list.

    This hook converts a tables (by id or "all") into the ``flat-table``
    directive"""

    table_id_list = table_id_list

    def hookFunc(node, rstPrefix, parseData):   # pylint: disable=W0613
        # run this hook only on the root node
        if node.getparent() is not None:
            return node

        for table in node.findall(".//table") + node.findall(".//informaltable"):
            if (table_id_list == "all" or table.get("id") in table_id_list):

                # seek column widths and col-spans from DocBook is the hell,
                # particularly there are <entrytbl> which left up to the outer
                # table and broken colspec definitions which has not been
                # rejected by the docbook toolchains. These colspecs must be
                # *repaired* in any matter.

                colspec = {}
                colspecByNumber = {}

                for colspec_count, c in enumerate(table.findall(".//colspec")):
                    colnum = c.get("colnum")
                    if colnum is not None:
                        try:
                            colnum = int(colnum)
                        except:
                            pass
                    if colnum is None:
                        colnum = colspec_count
                    colname = c.get("colname")
                    if colname is None:
                        colname = ""
                    align = c.get("align")
                    colwidth = c.get("colwidth")
                    if colwidth is not None:
                        colwidth = colwidth.replace("*","")
                        # some colspec definition use the "&#x22C6;" entity
                        colwidth = colwidth.replace(u"⋆", "")
                        try:
                            colwidth = int(colwidth)
                        except:
                            colwidth = None
                    colspec[colname] = (colnum, align, colwidth )
                    colspecByNumber[colnum] = (colname, align, colwidth)

                spanspec = {}
                for item in table.findall(".//spanspec"):
                    spanname = item.get("spanname")
                    namest   = item.get("namest")
                    nameend  = item.get("nameend")
                    if spanname is None or namest is None or nameend is None:
                        continue
                    start = colspec.get(namest, [None, None,None])[0]
                    end   = colspec.get(nameend, [None, None,None])[0]
                    if start is None or end is None:
                        continue
                    spanspec[spanname] = end - start


                # convert table to double-stage list

                max_cols = 0
                row_count = 0
                flatTable = node.makeelement("itemizedlist")

                # eat all rows, include the rows from entrytbl

                for row in table.findall(".//row"):
                    row_count += 1
                    flatRow = node.makeelement("listitem")
                    row_id = row.get("id")
                    if row_id:
                        flatRow.text = ".. _`%s`:" % row_id
                    else:
                        flatRow.text = ".. row %s" % row_count
                    flatTable.append(flatRow)
                    colList = node.makeelement("itemizedlist")
                    flatRow.append(colList)
                    col_count = 0
                    for entry in row.findall(".//entry"):
                        col_count += 1
                        cspan = spanspec.get(entry.get("spanname"), 0)
                        if cspan == 0:
                            # the colspan attribut comes from tables which has
                            # been converted from html (see hook_html2db_table)
                            cspan = int(entry.get("colspan", 1)) - 1
                        newCol = node.makeelement("listitem")

                        # a ID in a cell needs some extras
                        cell_id = entry.get("id")
                        if cell_id is not None:
                            del entry.attrib["id"]
                            para_id= node.makeelement("para")
                            para_id.text = (".. _`%s`:\n\n" % cell_id)
                            newCol.append(para_id)

                        # move content of entry to a para and insert
                        # rat-spanning markup
                        para   = XMLTag.copyNode(entry, "para", moveID=False)
                        if cspan:
                            para.text = (":cspan:`%s` " % cspan) + (para.text or "")
                            col_count += cspan
                        morerows = entry.get("morerows", 0)
                        if morerows == 0:
                            # the rowspan attribut comes from tables which has
                            # been converted from html (see hook_html2db_table)
                            morerows = int(entry.get("rowspan", 1)) -1
                        if morerows:
                            para.text = (":rspan:`%s` " % morerows) + (para.text or "")
                        newCol.append(para)
                        colList.append(newCol)
                    if col_count > max_cols:
                        max_cols = col_count

                # estimate colwidths

                widths = []
                for i in range(max_cols):
                    colname, align, colwidth = colspecByNumber.get(i, (None, None, None))
                    if colwidth is None:
                        colwidth = 1
                    widths.append(str(colwidth))

                # use widths only when they are meaningful
                useWidth = False
                for w in widths:
                    if w != widths[0]:
                        useWidth = True
                        break
                if len(colspec) > max_cols:
                    # The colspec definition has more entries than columns
                    # existing in the table definition. This indicates, that the
                    # colspec definition is buggy. I don't use width definitions
                    # from buggy colspecs
                    useWidth = False

                # insert prefix

                ctx = Table().getContext(table)
                ctx.header_rows  = len(table.findall(".//thead/row") or [])
                ctx.stub_columns = 1 if table.get("rowheader") == "firstcol" else 0
                ctx.widths = " ".join(widths)

                preText = "\n" if not ctx.ID else Table.rstAnchor
                preText +=  "\n.. flat-table::%(title)s"
                preText += "\n    :header-rows:  %(header_rows)s"
                preText += "\n    :stub-columns: %(stub_columns)s"
                if useWidth:
                    preText += "\n    :widths:       %(widths)s"
                preText += "\n    "
                preText += "\n%(tableStartMark)s"
                new = XMLTag.getInjBlockTag()
                new.text += preText % ctx
                table.addprevious(new)

                # insert postfix

                rstPostText = "\n%(tableEndMark)s\n"
                new = XMLTag.getInjBlockTag()
                new.text += rstPostText % ctx
                table.addnext(new)

                # replace table

                XMLTag.replaceNode(table, flatTable)
        return node
    return hookFunc



# ==============================================================================
class XMLTagType(type):
# ==============================================================================

    typeList  = dict()
    undifined = object()

    def __new__(mcs, name, bases, namespace):
        tag = namespace.get("tag", mcs.undifined)
        if name == "XMLTag":
            tag = None
        if tag == mcs.undifined:
            tag = name.lower()
        namespace["tag"] = tag
        cls = super().__new__(mcs, name, bases, namespace)

        # tag = None -->  marks intermediate classes
        if tag is not None:
            if mcs.typeList.get(cls.tag, mcs.undifined) != mcs.undifined:
                raise KeyError("tag <%s> allready defined in class %r"
                               % (cls.tag, mcs.typeList[cls.tag]))
            mcs.typeList[cls.tag] = cls

        return cls

    @classmethod
    def getClassByTag(mcs, tagName):
        return mcs.typeList.get(tagName, None)

    @classmethod
    def getTagInstance(mcs, node, parseData):
        u"""Returns a XMLTag instance which fits to the tag or ``None``."""
        xmlTag = None
        TagCls = mcs.getClassByTag(node.tag)
        if TagCls is not None:
            xmlTag = TagCls()
            xmlTag.parseData.update(parseData)
        return xmlTag

# ==============================================================================
class XMLTag(metaclass=XMLTagType):
# ==============================================================================

    def __init__(self):
        super().__init__()

        # some metadata about the parsing process
        self.parseData = Container(
            # customers hooks to call first on every node
            hooks           = []
            # folder where the xml-file is located
            , folder        = None
            # relativ pathname of the xml-file (relative to self.folder)
            , fname         = None
            # rstInclude requires the outFile from it's parent, to guess the
            # filesuffix for the ouptut of the include files.
            , parseIncludes = False
            , outFile       = None
            )

    def walk(self, node, rstPrefix=""):
        u"""Walks through the node-tree and applies matching filters on each node."""

        # First, call the hooks. Hooks might build a complete new subtree, they
        # have to return the node to walk on and this node might have a differnt
        # tag type!

        for func in self.parseData.hooks:
            node = func(node, rstPrefix, self.parseData)
            if node is None:
                raise Exception("hook %r doesn't return a xml node!'" % func)

        xmlTag = XMLTagType.getTagInstance(node, self.parseData)
        if xmlTag is not None:
            xmlTag.applyFilter(node, rstPrefix)
            if xmlTag.breakFlag:
                return
        self.walkChilds(node, rstPrefix + self.rstBlock)

    def walkChilds(self, node, rstPrefix=""):
        for child in node.iterchildren():
            self.walk(child, rstPrefix)

    def parseFile(self, folder, fname, fragTag=None, ID=None):
        u"""Tries to parse the XML file with :py:mod:`lxml.etree`.

        A unknown entity within a xml (fragment) will cause an exception. In
        this case, run :py:func:`subEntities` first!"""

        self.parseData.update(
            # folder where the xml-file is located
            folder   = folder
            # relativ pathname of the xml-file (relative to self.folder)
            , fname  = fname
            )

        preTag  = ""
        postTag = ""
        if fragTag:
            preTag  = u"<%s%s>" % (fragTag, ' id="%s"' % ID if ID is not None else "")
            postTag = u"</%s>" % fragTag

        fname    = FSPath(folder / fname)
        xmlFlag  = False
        rootNode = None

        with fname.openTextFile() as f:
            if f.readline().startswith("<?xml"):
                xmlFlag = True
        if xmlFlag:
            rootNode = etree.parse(fname).getroot()
        else:
            content = fname.readFile()
            rootNode = etree.fromstring(
                u"<dummy>"
                + preTag
                + content
                + postTag
                + u"</dummy>")
        return rootNode


    @classmethod
    def insertAsRawHTML(cls, node):
        literal = etree.tostring(node, encoding="unicode")
        literal = literal.replace("\t","")
        literal = literal.strip()
        raw = "\n.. raw:: html\n%s\n\n" % cls.blockText("    ", literal)
        new = cls.getInjBlockTag()
        new.text += raw
        cls.replaceNode(node, new)

    @classmethod
    def chunkNode(cls, node, folder, fname):
        # break recursion, from the caller
        if node.get("chunkNode") is not None:
            return
        node.set("chunkNode", "1")
        folder = FSPath(folder)
        fname  = FSPath(fname)
        inclTag = node.makeelement(cls.rstInclude_tag)
        inclTag.set("fname", fname.suffix(".xml"))
        MSG("INFO: create chunk %s" % (etree.tostring(inclTag, encoding="unicode")))
        with (folder / fname).openTextFile("w") as out:
            out.write(
                etree.tostring(node, encoding='unicode') )
        cls.replaceNode(node, inclTag)

    # ---------------
    # nodes
    # ---------------

    @classmethod
    def copyNode(cls, node, tag=None, moveID=False):
        tag = tag or node.tag
        new = node.makeelement(tag)
        new.text = node.text
        new.tail = node.tail
        new[:] = node
        for k,v in node.items():
            new.set(k, v)
        if moveID:
            ID = node.get("id")
            if ID is not None:
                del node.attrib["id"]
                new.set("id", ID)
        return new

    @classmethod
    def dropNode(cls, node):
        parent = node.getparent()
        if parent is not None:
            parent.remove(node)
        else:
            raise Exception("node %s is the root node / can't droped" % node)

    @classmethod
    def replaceNode(cls, oldNode, newNode):
        parent = oldNode.getparent()
        if parent is not None:
            parent.replace(oldNode, newNode)
        else:
            Exception("node %s is the root node / can't replaced" % oldNode)


    # The <programlisting> content will be passed through *as is* by pandoc
    # DocBook reader and can be handled in the pandoc filter.

    rstInjection_sig = "!ri!"

    @classmethod
    def pandocFilter(cls, key, value, fmt, meta): # pylint: disable=W0613
        if key == 'CodeBlock':

            # DocBook injection --> "programlisting"
            # --------------------------------------
            txt = value[1]
            if txt.startswith(cls.rstInjection_sig):
                new = txt[len(cls.rstInjection_sig):]
                return {'t': 'Plain', 'c': [{'t': 'Str', 'c': new}]}

        if key == 'Code':

            # DocBook injection --> "code"
            # --------------------------------------

            txt = value[1]
            if txt.startswith(cls.rstInjection_sig):
                new = txt[len(cls.rstInjection_sig):]
                return {'t': 'Str', 'c': new}

    @classmethod
    def getInjInlineTag(cls):
        new = etree.Element("code")            # pandoc --> "CodeBlock"
        new.text = cls.rstInjection_sig
        new.set("rstInjection", "1")
        return new

    @classmethod
    def getInjBlockTag(cls):
        new = etree.Element("programlisting")  # pandoc --> "Code"
        new.text = cls.rstInjection_sig
        new.set("rstInjection", "1")
        return new

    def applyFilter(self, node, rstPrefix):

        if self.dropFlag:
            self.dropNode(node)
            return

        # injection is done as pandoc "Code" or "CodeBlock"
        def getInjTag():
            if self.injBlock:  new = self.getInjBlockTag()
            else:              new = self.getInjInlineTag()
            return new

        preText = self.preText(node, rstPrefix)
        if preText:
            new = getInjTag()
            new.text += preText
            node.addprevious(new)

        postText = self.postText(node, rstPrefix)
        if postText:
            new = getInjTag()
            new.text += postText
            node.addnext(new)

        replaceText = self.replaceText(node, rstPrefix)
        if replaceText:
            new = getInjTag()
            new.text += replaceText
            new.tail = node.tail
            self.replaceNode(node, new)

    # ---------------
    # reST
    # ---------------

    rstInclude_tag  = "rstInclude"
    rstTemplate_tag = "rstTemplate"

    @classmethod
    def normalizeID(cls, ID):
        # not needed, may be later
        #if ID is not None:
        #    ID = ID.replace("-","_")
        return ID

    @classmethod
    def getText(cls, *nodelist):
        u"""The text *as is* from ``node.itertext()``"""
        text = ""
        for node in nodelist:
            if node is not None:
                text += "".join([ txt for txt in node.itertext()])
        retVal = None
        if text != "":
            retVal = text
        return retVal

    @classmethod
    def getStripedText(cls, *nodelist):
        u"""The text from node.itertext() with reduced whitespaces"""
        text = cls.getText(*nodelist)
        if text is not None:
            return re.sub(r"\s+"," ", text).strip()

    @classmethod
    def getFormatedTitle(cls, node, from_tag="title"):
        u"""title as one line, prefixed with :py:attribute:`rstBlock`"""
        title = ""
        title_node = node.find(from_tag)
        if title_node is not None:
            title = cls.rstBlock + cls.getStripedText(title_node)
        return title

    @classmethod
    def blockText(cls, prefix, text):
        u"""Adds ``prefix`` to lines from ``text``, deletes trailing whitespaces"""
        if text is None:
            return None
        text = text.strip("\n")
        retVal = "\n"
        for line in text.split("\n"):
            line = line.rstrip()
            if line:
                retVal += prefix + line
            retVal += "\n"
        return retVal + "\n\n"

    # ---------------
    # Subclassing API
    # ---------------

    # xml tag-name e.g "section"
    tag = XMLTagType.undifined

    # inject rst as inline or as block
    injBlock = False

    # Tag-Filter breaks XML recursion
    breakFlag = False

    # Tag should be droped
    dropFlag = False

    # additional prefix for lines within *this* rst-Block
    rstBlock  = ""
    rstAnchor = "\n.. _%(ID)s:\n"
    rstMarkup = None

    # pylint: disable=W0613

    def getContext(self, node):
        return Container(
            ID = self.normalizeID(node.attrib.get('id')))

    def replaceText(self, node, rstPrefix):
        return None

    def preText(self, node, rstPrefix):
        return None

    def postText(self, node, rstPrefix):
        return None


# ==============================================================================
class LinkTag(XMLTag):
    tag = None
# ==============================================================================

    rstMarkup = ":ref:`%(text)s <%(linkend)s>`"

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.text = self.getStripedText(node)
        ctx.linkend = self.normalizeID(node.attrib.get("linkend"))
        return ctx

    def replaceText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = self.rstMarkup
        if not ctx.text:
            rst = ":ref:`%(linkend)s`"
        return rst % ctx

# ------------------------------------------------------------------------------
class Link(LinkTag): pass
class Xref(LinkTag): pass
# ------------------------------------------------------------------------------

# ==============================================================================
class Ulink(LinkTag):
# ==============================================================================

    rstMarkup = "`%(text)s <%(linkend)s>`__"

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.linkend = self.normalizeID(node.attrib.get("url"))
        return ctx

    def replaceText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = self.rstMarkup
        # FIXME: droped ref-text, because it is (mostly) redundant and long refs are killed by tables
        if not ctx.text:
            rst = "%(linkend)s"
        return rst % ctx

# ==============================================================================
class Constant(XMLTag):
# ==============================================================================

    # a inline literal should contain not any leading/trailing whitespace

    replaceTag = None

    def applyFilter(self, node, rstPrefix):
        if self.replaceTag is not None:
            # Structure tags like <refsection> and <section> are simmular
            newNode = self.copyNode(node, self.replaceTag, moveID=True)
            self.breakFlag = True
            self.replaceNode(node, newNode)
            #SDK.CONSOLE()
            self.walk(newNode, rstPrefix)
        else:
            if not node.text or not node.text.strip():
                # drop empty inline literals
                self.dropNode(node)
                self.breakFlag = True
            else:
                node.text = node.text.strip()
                super().applyFilter(node, rstPrefix=self.rstBlock)

# ------------------------------------------------------------------------------
class Property(Constant):      replaceTag = "constant"
class Token(Constant):         replaceTag = "constant"
class Filename(Constant):      replaceTag = "constant"
class Varname(Constant):       replaceTag = "constant"
# ------------------------------------------------------------------------------

# ==============================================================================
class Subtitle(XMLTag):
# ==============================================================================

    breakFlag = True
    injBlock  = True
    rstMarkup = "\n**%(title)s**\n\n"

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.title = self.getStripedText(node)
        return ctx

    def replaceText(self, node, rstPrefix):
        return self.rstMarkup % self.getContext(node)

# ==============================================================================
class StructureTag(XMLTag):
    tag = None
# ==============================================================================

    breakFlag      = False
    injBlock       = True
    rstPreMarkup   = "\n.. _%(ID)s:\n"
    rstTitleMarkup = "="
    replaceTag     = None

    def applyFilter(self, node, rstPrefix):

        if self.replaceTag is not None:
            # Structure tags like <refsection> and <section> are simmular
            newNode = self.copyNode(node, self.replaceTag, moveID=True)
            self.breakFlag = True
            self.replaceNode(node, newNode)
            #SDK.CONSOLE()
            self.walk(newNode, rstPrefix)
        else:
            # Structure tag resets the indentation rstPrefix
            super().applyFilter(node, rstPrefix=self.rstBlock)

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.title = self.getFormatedTitle(node)
        return ctx

    @classmethod
    def rstTitle(cls, title):
        return ("\n" + title
                + "\n" + (cls.rstTitleMarkup * len(title))
                + "\n\n")

    def preText(self, node, rstPrefix):
        #SDK.CONSOLE()
        rst = ""
        ctx = self.getContext(node)
        if ctx.ID is not None:
            rst += self.rstPreMarkup
        if ctx.title:
            rst += self.rstTitle(ctx.title)
        # drop no more needed child nodes!
        n = node.find("title")
        if n is not None:
            self.dropNode(n)
        #print("%r preText -->|%s|<--" % (node, (rst % ctx)))
        return rst % ctx

# ==============================================================================
class Section(StructureTag):
# ==============================================================================

    rstTitleMarkup = "="
    def applyFilter(self, node, rstPrefix):
        sectLevel = 0
        parent = node.getparent()
        while parent is not None:
            if parent.tag in ["section",]:
                #SDK.CONSOLE()
                sectLevel += 1
            parent = parent.getparent()
        self.rstTitleMarkup = '=-^"+'[sectLevel]
        super().applyFilter(node, rstPrefix="")

    def rstTitle(self, title):
        return ("\n" + title
                + "\n" + (self.rstTitleMarkup * len(title))
                + "\n\n")

# ------------------------------------------------------------------------------
class Appendix(StructureTag):       replaceTag = "chapter"
class Bibliography(StructureTag):   replaceTag = "chapter"
class Legalnotice(StructureTag):    replaceTag = "section"
class Para(StructureTag):           pass
class Sect1(StructureTag):          replaceTag = "section"
class Sect2(StructureTag):          replaceTag = "section"
class Sect3(StructureTag):          replaceTag = "section"
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
class Part(StructureTag):
# ------------------------------------------------------------------------------
    rstTitleMarkup = "#"

    def applyFilter(self, node, rstPrefix):
        partinfo = node.find("partinfo")
        if partinfo is not None:
            # move it to the end of the part
            chapter = self.copyNode(partinfo, "chapter", moveID=True)
            title   = partinfo.makeelement("title")
            title.text = "Revision and Copyright"
            chapter.insert(0, title)
            node.append(chapter)
            node.remove(partinfo)

        super().applyFilter(node, rstPrefix)

    @classmethod
    def rstTitle(cls, title):
        return ("\n"   + (cls.rstTitleMarkup * len(title))
                + "\n" + title
                + "\n" + (cls.rstTitleMarkup * len(title))
                + "\n\n")

class Bookinfo(StructureTag): replaceTag = "part"
class Setinfo(StructureTag): replaceTag = "part"

# ------------------------------------------------------------------------------
class Chapter(StructureTag):
# ------------------------------------------------------------------------------
    rstTitleMarkup = "*"

    @classmethod
    def rstTitle(cls, title):
        return ("\n"   + (cls.rstTitleMarkup * len(title))
                + "\n" + title
                + "\n" + (cls.rstTitleMarkup * len(title))
                + "\n")
# ------------------------------------------------------------------------------
class Preface(Chapter): rstTitleMarkup = "="
# ------------------------------------------------------------------------------


# ==============================================================================
class Refentry(XMLTag):
# ==============================================================================

    injBlock = True

    def getContext(self, node):
        ctx = super().getContext(node)

        refentrytitle = node.find("refmeta/refentrytitle")
        refname       = node.find("refnamediv/refname")

        ID = refname.attrib.get('id')
        if ID:
            ctx.ID  = self.normalizeID(ID)
        ctx.refname = self.getStripedText(refname)
        ctx.title   = ctx.refname
        if refentrytitle is not None:
            ctx.title   = self.getStripedText(refentrytitle)
        ctx.manvol  = self.getStripedText(node.find("refmeta/manvolnum"))
        ctx.refmiscinfo  = self.getStripedText(node.find("refmeta/refmiscinfo"))
        return ctx

    def preText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = "\n" if not ctx.ID else self.rstAnchor
        if ctx.title:
            rst += Chapter.rstTitle(ctx.title)
        if ctx.refname:
            rst += "\n*man %(refname)s(%(manvol)s)*\n"
        if ctx.refmiscinfo:
            rst += "\n*%(refmiscinfo)s*\n"
        # drop no more needed child nodes!
        for p in ["refmeta/refentrytitle" , "refmeta/manvolnum" ,
                   "refmeta/refmiscinfo", "refnamediv/refname" ]:
            n = node.find(p)
            if n is not None:
                self.dropNode(n)
        return rst % ctx


# ==============================================================================
class Refsynopsisdiv(Section):
# ==============================================================================

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.title = "Synopsis"
        return ctx

# ==============================================================================
class Refentryinfo(XMLTag):
# ==============================================================================

    # seems useless ...
    #
    # <refentryinfo>
    # <title>LINUX</title>
    # <productname>Kernel Hackers Manual</productname>
    # <date>April 2016</date>
    # </refentryinfo>

    dropFlag = True

# ------------------------------------------------------------------------------
class Refsection(Section):          replaceTag = "section"
class Refsect1(Sect1):              pass
class Refsect2(Sect2):              pass
class Refsect3(Sect3):              pass
class Refpurpose(StructureTag):     replaceTag = "para"
class Refnamediv(StructureTag):     replaceTag = "section"
# ------------------------------------------------------------------------------


# ==============================================================================
class Copyright(XMLTag):
# ==============================================================================

    breakFlag = True
    injBlock  = True

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.year = ", ".join([self.getStripedText(n) for n in node.findall("year")])
        ctx.holder = "/ ".join([self.getStripedText(n) for n in node.findall("holder")])
        return ctx

    def replaceText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = "\n**Copyright** %(year)s : %(holder)s\n"
        return rst % ctx

# ==============================================================================
class Trademark(XMLTag):
# ==============================================================================

    trademark = u"®"

    def applyFilter(self, node, rstPrefix):
        node.text = node.text + self.trademark
        super().applyFilter(node, rstPrefix)

# ==============================================================================
class Code(XMLTag):
# ==============================================================================

    breakFlag  = False

    def applyFilter(self, node, rstPrefix):
        # ignore injected rst-literals
        if node.get("rstInjection") is None:
            super().applyFilter(node, rstPrefix)
        else:
            self.breakFlag = True

# ------------------------------------------------------------------------------
class Computeroutput(Code):   pass
# ------------------------------------------------------------------------------

# ==============================================================================
class LiteralBlock(XMLTag):
    tag = None
# ==============================================================================

    breakFlag  = True
    rstBlock   = "    "
    injBlock   = True
    language   = "guess"
    rstMarkup  = "\n::\n\n%(literal)s\n\n"

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.language = node.get("language") or self.language
        # FIXME: pass "*" as &#x22C6;
        text = self.getText(node).replace(u"⋆", "*")
        text = text.replace("&#x22C6;", "*")  # comes from unnecessary ``<![CDATA[ ...`` usages
        ctx.literal  = self.blockText(self.rstBlock, text).strip("\n")
        return ctx

    def replaceText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = "\n" if not ctx.ID else self.rstAnchor
        rst += self.rstMarkup
        return rst % ctx

# ------------------------------------------------------------------------------
class Literallayout(LiteralBlock):    pass
class Screen(LiteralBlock):           pass
# ------------------------------------------------------------------------------

# ==============================================================================
class Programlisting(LiteralBlock):
# ==============================================================================

    # FIXME: einige <programlisting>'s sind ganze Dateien, sprich das
    # root-Element, das kann aber nicht so einfach ausgetauscht werden.

    language   = "c"
    rstMarkup = """\
.. code-block:: %(language)s

%(literal)s\n\n\n""" # pandocs eats some trailing newlines

    def applyFilter(self, node, rstPrefix):
        # ignore injected rst-literals
        if node.get("rstInjection") is None:
            super().applyFilter(node, rstPrefix)

# ------------------------------------------------------------------------------
class Funcsynopsisinfo(Programlisting): pass
class Synopsis(Programlisting): pass
# ------------------------------------------------------------------------------

# ==============================================================================
class Funcprototype(XMLTag):
# ==============================================================================

    injBlock   = True

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.funcdef = self.getStripedText(node.find("funcdef"))
        ctx.params = []
        for paramdef in node.findall("paramdef"):
            ctx.params.append(self.getStripedText(paramdef).replace(u"⋆", "*"))
        return ctx

    def replaceText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = "\n.. c:function::"
        rst += " %s" % ctx.funcdef
        rst += "( " + ", ".join(ctx.params) + " )"
        return rst

# ==============================================================================
class Function(XMLTag):
# ==============================================================================

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.func_call = self.getStripedText(node)
        if not ctx.func_call.endswith(")"):
            ctx.func_call += "()"
        return ctx

    def replaceText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = ":c:func:`%(func_call)s`"
        return rst % ctx

# ==============================================================================
class Structname(XMLTag):
# ==============================================================================

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.struct_name = self.getStripedText(node)
        if not ctx.struct_name.startswith("struct"):
            ctx.struct_name = "struct " + ctx.struct_name
        return ctx

    def replaceText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = ":c:type:`%(struct_name)s`"
        return rst % ctx

class Structfield(Constant):   replaceTag = "constant"

# ==============================================================================
class Mediaobject(XMLTag):
# ==============================================================================

    align    = "center"

    def getContext(self, node):
        img_files = []
        align = self.align
        for imagedata in node.findall(".//imagedata"):
            img_files.append(FSPath(imagedata.attrib.get("fileref")))
            if not align:
                align = imagedata.attrib.get("align")

        ctx = super().getContext(node)
        ctx.img_files = img_files
        ctx.align     = align
        ctx.glob      = None
        if img_files:
            ctx.glob  = FSPath(img_files[0]).suffix(".*")
        ctx.text      = self.getStripedText(*node.findall(".//textobject"))
        return ctx

# ==============================================================================
class Figure(XMLTag):
# ==============================================================================

    breakFlag  = True
    injBlock   = True
    rstBlock   = "    "
    rstMarkup = """
.. figure::  %(glob)s
    :alt:    %(alt)s
    :align:  %(align)s

%(title)s
"""

    def getContext(self, node):
        ctx = Mediaobject().getContext(node)
        ctx.update(super().getContext(node))
        ctx.alt = " / ".join([f.BASENAME for f in  ctx.img_files])
        ctx.title = self.getFormatedTitle(node)
        return ctx

    def replaceText(self, node, rstPrefix):
        # This implementation treats the time only figures with imagedata in.
        if node.findall(".//imagedata") is None:
            self.breakFlag = False
            return
        ctx = self.getContext(node)
        rst = "\n" if not ctx.ID else self.rstAnchor
        rst += self.rstMarkup
        if ctx.text:
            ctx.text = self.blockText(self.rstBlock, ctx.text)
            rst += "%(text)s"
        rst += "\n\n" # pandocs eats some trailing newlines
        return rst % ctx

# ------------------------------------------------------------------------------
class Informalfigure(Figure): pass
# ------------------------------------------------------------------------------

# ==============================================================================
class Table(XMLTag):
# ==============================================================================

    # pandoc doesn't render tables title and anchors well

    injBlock  = True
    rstBlock  = "    "
    breakFlag = False

    tableStartMark = "-- table start markup --"
    tableEndMark   = "-- table end markup --"

    rstPreText  = """
.. table::%(title)s

%(tableStartMark)s
"""
    rstPostText = "\n%(tableEndMark)s\n"

    def applyFilter(self, node, rstPrefix):
        if node.find("tbody/tr") is not None:
            self.insertAsRawHTML(node)
            self.breakFlag = True
            return
        node.set("pgwide", "1")
        self.assert_tgroup(node)
        super().applyFilter(node, rstPrefix)

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.tableStartMark = self.tableStartMark
        ctx.tableEndMark = self.tableEndMark
        title_node = node.find("title")
        ctx.title  = ""
        if title_node is not None:
            ctx.title = " " + self.getStripedText(title_node)
        return ctx

    def preText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = "\n" if not ctx.ID else self.rstAnchor
        rst += self.rstPreText
        # drop no more needed child nodes!
        title_node = node.find("title")
        if title_node is not None:
            self.dropNode(title_node)
        return rst % ctx

    def postText(self, node, rstPrefix):
        ctx = self.getContext(node)
        return self.rstPostText % ctx

    @classmethod
    def assert_tgroup(cls, node):
        # To render the rst output well, pandoc requires a tgroup with col
        # definitions.
        tgroup = node.find("tgroup")
        if tgroup is None:
            tgroup = node.makeelement("tgroup")
            node.insert(0, tgroup)
            cols = len(node.find("tbody/row").findall("./entry"))
            tgroup.set("cols", str(cols))
            w = 1
            for c in range(1, cols+1):
                if cols < 3 or (cols + 1) == c:
                    w += 1
                colspec = node.makeelement("colspec")
                colspec.set("colname", "c%s" % c)
                colspec.set("colwidth", "%s*" % w)
                tgroup.append(colspec)
            tbody = node.find("tbody")
            tgroup.append(tbody)
        else:
            colspec_s = tgroup.findall("colspec")
            cols = len(colspec_s)
            c = w = 1
            for colspec in colspec_s:
                c += 1
                if colspec.get("colwidth") is None:
                    if cols < 3 or (cols + 1) == c:
                        w += 1
                    colspec.set("colwidth", "%s*" % w)



# ==============================================================================
class Informaltable(Table):
# ==============================================================================

    injBlock  = True
    breakFlag = False

    # Informaltable within media DocBook are often used to draw a border around
    # a paragraph. This breaks the separation of *presentation from content*.

    def applyFilter(self, node, rstPrefix):
        tgroup = node.find("tgroup")
        cols = int(tgroup.attrib.get("cols"))
        if 1 == cols:
            self.dropUselessTable(node, rstPrefix)
        else:
            super().applyFilter(node, rstPrefix)

    def dropUselessTable(self, node, rstPrefix):
        self.breakFlag = True
        etree.strip_tags(node, "tgroup", "tbody", "row", "entry")
        section = self.copyNode(node, "section", moveID=True)
        self.replaceNode(node, section)
        self.walk(section, rstPrefix + self.rstBlock)

# ==============================================================================
class Tgroup(XMLTag):
# ==============================================================================

    injBlock  = True
    breakFlag = False

    # There is a entity within the media_api.xml:
    #
    # <!ENTITY cs-def  "<colspec colname='c1' colwidth='3*' /> \
    #                  <colspec colname='c2' colwidth='1*' />  \
    #                  <colspec colname='c3' colwidth='4*' /> \
    #                  <spanspec spanname='hspan' namest='c1' nameend='c3' />">
    #
    # This cs-def entity defines 3 columns, but it is partial used in tables
    # with 2 columns, which is mistakeable /  e.g.: frontend_legacy_api.p1_xml the
    #
    # <table pgwide="1" frame="none" id="fe-bandwidth">
    #     <title>enum fe_bandwidth</title>
    #     <tgroup cols="2">   <!-- TWO cols   !!! -->
    #         &cs-def;        <!-- THREE cols !!! -->


    def applyFilter(self, node, rstPrefix):
        self.repairTableDef(node, rstPrefix)
        super().applyFilter(node, rstPrefix)

    @classmethod
    def repairTableDef(cls, node, rstPrefix):  # pylint: disable=W0613
        cols = int(node.attrib.get("cols"))
        colspec_cols = len(node.findall("colspec"))
        if cols != colspec_cols:
            for colspec in node.iterchildren("colspec"):
                node.remove(colspec)
            for spanspec in node.iterchildren("spanspec"):
                node.remove(spanspec)
            cols = len(node.find("tbody/row").findall("./entry"))
            node.set("cols", str(cols))
            for c in range(cols):
                colspec = node.makeelement("colspec")
                colspec.set("colname", "c%s" % c)
                colspec.set("colwidth", "1*")
                node.insert(c, colspec)


# ==============================================================================
class Entrytbl(XMLTag):
# ==============================================================================

    # flatten these braindead inner-tables

    breakFlag  = True

    def applyFilter(self, node, rstPrefix):

        newEntry = node.makeelement("entry")
        for subEntry in node.findall(".//entry"):
            para = self.copyNode(subEntry, "para", moveID=True)
            newEntry.append(para)
        #SDK.CONSOLE()
        self.replaceNode(node, newEntry)
        self.walk(newEntry, rstPrefix + self.rstBlock)




# ==============================================================================
class Authorgroup(XMLTag):
# ==============================================================================

    breakFlag = True
    injBlock  = True

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.authorlist = []
        for author in (node.findall("author") + node.findall("corpauthor")):
            trademark = []
            for tm in author.findall("trademark"):
                trademark.append(self.getStripedText(tm) + Trademark.trademark)
            trademark = ", ".join(trademark)
            corpauthor = trademark
            if author.tag == "corpauthor":
                corpauthor = self.getStripedText(author) + trademark
            a = Container(
                firstname     = self.getStripedText(*author.findall("firstname"))   or ""
                , surname     = self.getStripedText(*author.findall("surname"))     or ""
                , othername   = self.getStripedText(*author.findall("othername"))   or ""
                , affiliation = self.getStripedText(*author.findall("affiliation"))
                , corpauthor  = corpauthor
                , contrib     = self.getStripedText(*author.findall("contrib"))
            )
            ctx.authorlist.append(a)
        return ctx

    def replaceText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = ""
        if ctx.authorlist:
            for author in ctx.authorlist:
                r = "\n:author:   "
                if author.surname:      r += " %(surname)s"
                if author.firstname:    r += " %(firstname)s"
                if author.othername:    r += " (*%(othername)s*)"
                if author.corpauthor:   r += " %(corpauthor)s"
                if author.affiliation:  r += "\n:address:   %(affiliation)s"
                if author.contrib:      r += "\n:contrib:   %(contrib)s"
                rst += r % author
                rst += "\n"
        return rst % ctx



# ==============================================================================
class Revremark(StructureTag): replaceTag = "para"
class Revision(XMLTag):
# ==============================================================================

    injBlock  = True
    rstBlock  = "    "

    def applyFilter(self, node, rstPrefix):
        super().applyFilter(node, rstPrefix)
        self.walkChilds(node, rstPrefix + self.rstBlock)

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.revnumber      = self.getStripedText(*node.findall("revnumber"))   or ""
        ctx.date           = self.getStripedText(*node.findall("date"))        or ""
        ctx.authorinitials = self.getStripedText(*node.findall("authorinitials"))
        return ctx

    def preText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = "\n:revision: %(revnumber)s / %(date)s"
        if ctx.authorinitials:
            rst += " (*%(authorinitials)s*)"
        #rst += "\n:remark:   %(revremark)s"
        rst += "\n\n\n"

        # drop no more needed child nodes!
        for p in ["revnumber", "date" ]:
            n = node.find(p)
            if n is not None:
                self.dropNode(n)
        return rst % ctx


# ==============================================================================
class Biblioentry(XMLTag):
# ==============================================================================

    # DocBooks biblioentrie's are usually misapplied, e.g.::
    #
    #     <biblioentry id="cea608">
    #       <abbrev>CEA 608-E</abbrev>
    #       <authorgroup>
    # 	<corpauthor>Consumer Electronics Association ...</corpauthor>
    #       </authorgroup>
    #       <title>CEA-608-E R-2014 "Line 21 Data Services"</title>
    #     </biblioentry>
    #
    # The abbrev-Tag contains whitespaces which doesn't fits to common citation
    # reference conzept.  Within old DocBook version they are refered by ID
    # (``<xref linkend="cea608"/>``) and note by ``<citation>CEA608E</citation>``.
    #
    # To solve this problem in multipart documents, more work is needed. This
    # here is just POV implementation.

    injBlock  = True
    rstBlock  = "    "

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.abbrev   = self.getStripedText(node.find("abbrev"))
        ctx.title    = self.getStripedText(node.find("title"))
        ctx.subtitle = self.getStripedText(node.find("subtitle"))
        return ctx

    def preText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = "\n" if not ctx.ID else self.rstAnchor
        if ctx.abbrev:       rst += Section().rstTitle(ctx.abbrev)
        if ctx.title:        rst += "\n:title:     %(title)s"
        if ctx.subtitle:     rst += "\n:subtitle:  %(subtitle)s"

        # drop no more needed child nodes!
        for p in ["abbrev", "title", "subtitle" ]:
            n = node.find(p)
            if n is not None:
                self.dropNode(n)
        return rst % ctx

## ==============================================================================
#class Example(Tag):
## ==============================================================================

class Informalexample(StructureTag):     replaceTag = "para"

# ==============================================================================
class ReSTTemplate(XMLTag):
# ==============================================================================

    # !E<filename> is replaced by the documentation, in <filename>, for
    # functions that are exported using EXPORT_SYMBOL: the function list is
    # collected from files listed in Documentation/DocBook/Makefile.

    # !I<filename> is replaced by the documentation for functions that are
    # _not_ exported using EXPORT_SYMBOL.

    # !D<filename> is used to name additional files to search for functions
    # exported using EXPORT_SYMBOL.   NOT USED ANYMORE!!!!!!!!!!!!!

    # !F<filename> <function [functions...]> is replaced by the
    # documentation, in <filename>, for the functions listed.

    # !P<filename> <section title> is replaced by the contents of the DOC:
    # section titled <section title> from <filename>.
    # Spaces are allowed in <section title>; do not quote the <section title>.

    # !C<filename> is replaced by nothing, but makes the tools check that
    # all DOC: sections and documented functions, symbols, etc. are used.
    # This makes sense to use when you use !F/!P only and want to verify

    tag = XMLTag.rstTemplate_tag
    injBlock = True
    rstMarkup = """
.. kernel-doc:: %(fname)s
%(options)s

"""

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.op      = node.get("op")
        ctx.fname   = node.get("fname")
        ctx.args    = node.get("args")
        ctx.options = ""
        if ctx.op == "E":
            ctx.options += "    :export:\n"
        if ctx.op == "I":
            ctx.options += "    :internal:\n"
        if ctx.op == "F":
            ctx.options += "    :functions: %s\n" % ctx.args
        if ctx.op == "P":
            ctx.options += "    :doc: %s\n" % ctx.args
        return ctx

    def replaceText(self, node, rstPrefix):
        ctx = self.getContext(node)
        rst = self.rstMarkup
        if ctx.op in ["C", "D"]:
            rst = "\n\n.. NOT SUPPORTED: '!%(op)s%(fname)s %(args)s'\n\n"
        retVal = rst % ctx
        return retVal

# ==============================================================================
class ReSTInclude(XMLTag):
# ==============================================================================

    tag = XMLTag.rstInclude_tag
    breakFlag  = False
    injBlock   = True
    rstBlock   = "    "
    rstMarkup  = """
.. toctree::
    :maxdepth: 1

%(entries)s


"""
    def applyFilter(self, node, rstPrefix):

        if not self.parseData.parseIncludes:
            folder   = FSPath(self.parseData.folder)
            thisFile = folder / self.parseData.fname
            inclFile = folder / FSPath(node.get("fname"))
            MSG("INFO: <rstInclude fname='%s'> will not be parsed!" % inclFile.relpath(thisFile.DIRNAME))
        else:
            folder    = FSPath(self.parseData.folder)
            inFile    = FSPath(node.get("fname")).suffix(self.parseData.fname.SUFFIX)
            outFile   = inFile.suffix(self.parseData.outFile.SUFFIX)
            xmlFilter = XMLTag()
            xmlFilter.parseData.update(self.parseData)

            MSG("parsing: <rstInclude fname='%s'>" % inFile)
            filterXML(folder, inFile, outFile, xmlFilter = xmlFilter, parseIncludes = True )

        # insert rst toctree directive
        super().applyFilter(node, rstPrefix)


    def get_toctree_entry(self, node):
        folder   = FSPath(self.parseData.folder)
        thisFile = folder / self.parseData.fname
        inclFile = folder / FSPath(node.get("fname"))
        toctree  = self.rstBlock + str(inclFile.relpath(thisFile.DIRNAME).SKIPSUFFIX)
        return toctree

    def getContext(self, node):
        ctx = super().getContext(node)
        ctx.entries = []
        nextNode = node
        while (nextNode is not None
               and nextNode.tag == self.rstInclude_tag
               and nextNode.get("ignoreToctree") is None):
            ctx.entries.append(self.get_toctree_entry(nextNode))
            nextNode.set("ignoreToctree", "True")
            nextNode = nextNode.getnext()
            while isinstance(nextNode, etree._Comment):
                nextNode = nextNode.getnext()

        ctx.entries = "\n".join(ctx.entries)
        return ctx

    def replaceText(self, node, rstPrefix):
        ctx = self.getContext(node)
        if ctx.entries:
            return self.rstMarkup % ctx
        else:
            return None







