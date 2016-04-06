#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-

# pylint: disable=W0613,R0914,C0103

u"""
    media
    ~~~~~

    customizing part to convert linux_tv (media) DocBook to reST with the dbtools and
    XML-filter (aka dbxml.XMLTag)

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.
"""

# ==============================================================================
# imports
# ==============================================================================

import re
from common import FSPath, PContainer, CLI, xml_unescape
from dbxml import XMLTag, filterXML, subEntities, EntityContainer, hook_copy_file_resource, RESOUCE_FORMAT
from lxml import etree

# ==============================================================================
# setup
# ==============================================================================

from dbenv import CACHE, BOOKS_FOLDER, LINUX_DOCBOOK_ROOT

MSG = CLI.msg
ERR = CLI.err

LINUX_TV_CACHE  = CACHE / "linux_tv"
LINUX_TV_BOOK   = BOOKS_FOLDER / "linux_tv"

MEDIA_EXT = EntityContainer(LINUX_TV_CACHE / "media-entities-ext.container")
MEDIA_INT = EntityContainer(LINUX_TV_CACHE / "media-entities-int.container")
MEDIA_REFS = PContainer(LINUX_TV_CACHE / "media_refs.container")

# <!-- Subsections -->
# <!ENTITY sub-biblio SYSTEM "./biblio.xml">
EXT_SUBSECT_RE  = re.compile(r'''<!ENTITY\s+(?P<name>sub-\S+)\s+SYSTEM\s+"(?P<filename>\S+)"''')
# <!-- Function Reference -->
# <!ENTITY close SYSTEM "./func-close.xml">
EXT_FUNCTION_RE = re.compile(r'''<!ENTITY\s+(?P<name>(?!sub-)\S+)\s+SYSTEM\s+"(?P<filename>\S+)"''')
INT_ENTITY_RE   = re.compile(r'''<!ENTITY\s+(?P<name>\S+)\s+"(?P<replacement>.*)"''')

mainFile = FSPath("media_api.xml")

# ==============================================================================
def initMedia():
# ==============================================================================

    if LINUX_TV_CACHE.EXISTS:
        LINUX_TV_CACHE.rmtree()
    LINUX_TV_CACHE.makedirs()

    media_init_ENTITIES()

    fileList = getFileList()
    # only for debug requiered
    fileList.add(FSPath("media-entities.tmpl"))

    MSG("cache files ...")
    for fname in fileList:
        outFile = LINUX_TV_CACHE/fname.suffix(".xml_orig")
        outFile.DIRNAME.makedirs()
        (LINUX_DOCBOOK_ROOT/fname).copyfile(outFile)

    MSG("substitude entities ...")

    for fname in fileList:
        inFile  = fname.suffix(".xml_orig")
        outFile = fname.suffix(".xml_entity")
        subEntities( LINUX_TV_CACHE/inFile , LINUX_TV_CACHE/outFile ,
                     MEDIA_EXT, MEDIA_INT )

    inFile = mainFile.suffix(".xml_entity")
    MSG("run XML filter (mainFile) : %s --> %s" % (inFile, mainFile))
    filterXML(LINUX_TV_CACHE, inFile, mainFile
              , xmlFilter     = getMediaFilter()
              , parseIncludes = True )


# ==============================================================================
def installMedia():
# ==============================================================================

    MSG("install *Media-API* book : %s" % LINUX_TV_BOOK)

    if LINUX_TV_BOOK.EXISTS:
        LINUX_TV_BOOK.rmtree()
    LINUX_TV_BOOK.DIRNAME.makedirs()

    fileList = getFileList()

    for xmlFile in fileList:
        rstFile = xmlFile.suffix(".rst")
        MSG("install file %s" % rstFile)

        src = LINUX_TV_CACHE  / rstFile
        dst = LINUX_TV_BOOK / rstFile
        if rstFile == FSPath("media_api.rst"):
            dst = LINUX_TV_BOOK / FSPath("index.rst")
        folder = FSPath(RESOUCE_FORMAT % src.SKIPSUFFIX)

        dst.DIRNAME.makedirs()
        src.copyfile(dst)

        if folder.EXISTS:
            dstFolder = dst.DIRNAME / folder.BASENAME
            MSG("install file-folder %s" % dstFolder)
            folder.copytree(dstFolder)

# ==============================================================================
def getFileList():
# ==============================================================================

    fileList = set((mainFile, ))
    for val in MEDIA_EXT.values():
        fileList.add(FSPath(val))
    fileList.remove("media-entities.tmpl")
    fileList.remove("media-indices.tmpl")
    return fileList


# ==============================================================================
def getMediaFilter():
# ==============================================================================

    xmlFilter = XMLTag()
    for hook in [hook_media_create_chunks
                 , hook_media_rstInclude
                 , hook_media_insert_src_headers
                 , hook_media_mark_as_todo
                 , hook_media_table2variablelist
                 , hook_media_table2variablelist_2
                 , hook_media_fix_broken_pixfmt
                 , hook_media_fix_broken_tables
                 , hook_copy_file_resource(LINUX_DOCBOOK_ROOT) ]:
        xmlFilter.parseData.hooks.add(hook)
    return xmlFilter


# ==============================================================================
def media_init_ENTITIES():
# ==============================================================================

    """Reads *media* entities from a SGML files (ugly hack).

    The parsed entities will be cached within the *cache*"""

    MSG("init *media* entities")

    MEDIA_EXT.clear()
    MEDIA_INT.clear()
    addCharEntities(MEDIA_INT)

    # folder where the origin xml files should be in
    o_folder = LINUX_DOCBOOK_ROOT / "media"

    for entity_file in [ LINUX_DOCBOOK_ROOT / "media-entities.tmpl" ,
                         LINUX_DOCBOOK_ROOT / "media-indices.tmpl" ,
                         LINUX_DOCBOOK_ROOT / "media_api.tmpl" ]:

        with entity_file.openTextFile() as f:
            for line in f:
                line = line.strip()
                m = EXT_SUBSECT_RE.search(line)
                if m:
                    MEDIA_EXT.addNew(
                        m.group("name"), findOriginXML(o_folder, m.group("filename")))
                    continue
                m = EXT_FUNCTION_RE.search(line)
                if m:
                    MEDIA_EXT.addNew(
                        m.group("name"), findOriginXML(o_folder, m.group("filename")))
                    continue
                m = INT_ENTITY_RE.search(line)
                if m:
                    MEDIA_INT.addNew(m.group("name"), m.group("replacement"))

    MSG("store entity-container: \n* externel: %s\n* internal: %s"
        % (MEDIA_EXT.pFile, MEDIA_INT.pFile))
    MEDIA_EXT.writeToFile()
    MEDIA_INT.writeToFile()


# ==============================================================================
def hook_media_rstInclude(node, rstPrefix, parseData):
# ==============================================================================

    # The fragmentation into external entitys is arbitrary. The xml-fragments
    # partial are missing their enclosing root node (not parsable), somtimes
    # not. A valid XML file must have only one root node!

    # run this hook only on the root node
    if node.getparent() is not None:
        return node

    for incl in node.findall(".//%s" % XMLTag.rstInclude_tag):

        if incl.get("fname") == 'media-indices.tmpl':
            XMLTag.dropNode(incl)
            continue

        if incl.get("fname") == 'media/v4l/biblio.xml':
            chapter = incl.makeelement("chapter")
            title = incl.makeelement("title")
            title.text = "Bibliography"
            chapter.append(title)
            XMLTag.replaceNode(incl, chapter)
            chapter.append(incl)
            continue

        parent  = incl.getparent()
        if XMLTag.getStripedText(parent):
            # MSG("leave %s as is" % etree.tostring(incl))
            continue

        folder  = FSPath(parseData.folder)
        inFile  = (folder / incl.get("fname")).suffix(parseData.fname.SUFFIX)
        outFile = inFile

        ID      = parent.get("id")
        preTag  = "<%s id='%s'>" % (parent.tag, ID)
        postTag = "</%s>" % parent.tag
        content = inFile.readFile()
        if not content.startswith(preTag):
            with outFile.openTextFile("w") as out:
                out.write(preTag + content + postTag)
            MSG("moved %s to %s" % (preTag, outFile))
        else:
            MSG("allready moved %s to %s" % (preTag, outFile))
        parent.addprevious(incl)
        XMLTag.dropNode(parent)

    return node



# ==============================================================================
def hook_media_mark_as_todo(node, rstPrefix, parseData):
# ==============================================================================

    # handle some inappropriate and buggy tables

    if node.get("id") not in [
            # media/v4l/dev-sliced-vbi.xml
            "v4l2-sliced-vbi-format", "vbi-services2"
            , "v4l2-mpeg-vbi-fmt-ivtv-magic" , "v4l2-mpeg-vbi-itv0-line"
            , "v4l2-mpeg-vbi-fmt-ivtv", "v4l2-mpeg-vbi-itv0"
            # media/v4l/io.xml
            , "v4l2-buffer"
            # media-ioc-enum-entities.xml
            , "media-entity-desc"
            # media/v4l/media-ioc-g-topology.xml
            , "media-v2-entity"
            # media/v4l/pixfmt.xml
            , "v4l2-pix-format", "pixfmt-indexed"
            # media/v4l/pixfmt-packed-rgb.xml
            , "rgb-formats", "rgb-formats-deprecated"
            # media/v4l/pixfmt-packed-yuv.xml
            , "packed-yuv"
            # media/v4l/vidioc-querycap.xml
            , "v4l2-capability"
            # media/v4l/subdev-formats.xml
            , "v4l2-mbus-pixelcode-bayer"
            , "v4l2-mbus-pixelcode-rgb"
            , "v4l2-mbus-pixelcode-hsv"
            , "v4l2-mbus-pixelcode-yuv8"
            # /media/v4l/vidioc-enum-fmt.xml
            , "v4l2-fmtdesc"
            #
            , "v4l2-bt-timings"
            , "v4l2-ext-control"
            , "vbi-services"
            , "v4l2-dbg-match"
    ]:

        return node

    oldNode = None
    if node.get("id") == "packed-yuv":
        # find table and mark it as TODO
        oldNode = node
        node = node.find(".//table")

    intro = ""
    if node.get("id"):
        intro +=  "\n.. _%s:\n" % node.get("id")
    title = XMLTag.getFormatedTitle(node)
    if title:
        intro += ("\n" + title
                  + "\n" + ("=" * len(title)))

    intro += "\n\n::\n\n"
    intro += "    TODO ... \n\n"
    #literal = etree.tostring(node).decode("utf-8") + "\n\n"
    literal = etree.tostring(node, encoding='unicode') + "\n\n"
    literal = XMLTag.blockText("    ", literal)
    replaceText = intro + literal
    new      = XMLTag.getInjBlockTag()
    new.text += replaceText
    new.tail = node.tail
    XMLTag.replaceNode(node, new)
    if oldNode is not None:
        return oldNode
    else:
        dummy = node.makeelement("dummy")
        return dummy




# ==============================================================================
def hook_media_fix_broken_tables(node, rstPrefix, parseData):
# ==============================================================================

    if node.get("id") not in [
            "rc_standard_keymap"
            # ignore colspan in headers
            , "v4l2-mbus-pixelcode-rgb-lvds"
            , "v4l2-mbus-pixelcode-yuv8"
            , "input-status"
            , "v4l2-ext-controls"
            , "v4l2-framebuffer"
            , "v4l2-sliced-vbi-cap"
            , "v4l2-vbi-format"
            , "framebuffer-flags"
            , "v4l2-format"
            , "v4l2-outputparm"
            , "tuner-matrix"
            , "v4l2-tuner"
            , "v4l2-dv-timings" # missing entries
            , "name-v4l2-dbg-match" # missing entries
    ]:
        return node

    table = node
    tgroup = table.find("tgroup")
    cols = int(tgroup.get("cols"))
    thead = tgroup.find("thead")
    tbody = tgroup.find("tbody")

    if thead is not None:
        for row in thead.findall("row"):
            entries = row.findall("entry")
            if len(entries) > cols:
                cols = len(entries)
                tgroup.set("cols", str(cols))

    for row in tbody.findall("row"):
        entries = row.findall("entry")
        if len(entries) > cols:
            cols = len(entries)
            tgroup.set("cols", str(cols))

    if thead is not None:
        for row in thead.findall("row"):
            entries = row.findall("entry")
            if len(entries) < cols:
                for x in range(cols - len(entries)):
                    row.append(node.makeelement("entry"))

    for row in tbody.findall("row"):
        entries = row.findall("entry")

        if len(entries) < cols:
            for x in range(cols - len(entries)):
                row.append(node.makeelement("entry"))
    return node



# ==============================================================================
def hook_media_fix_broken_pixfmt(node, rstPrefix, parseData):
# ==============================================================================

    if not parseData.fname.BASENAME.startswith("pixfmt-"):
        return node

    # run this hook only on the root node
    if node.getparent() is not None:
        return node

    # These tables are complete broken, it is horrible
    for table in node.findall(".//informaltable"):
        tgroup = table.find("tgroup")
        cols = int(tgroup.get("cols"))
        tbody = tgroup.find("tbody")
        for row in tbody.findall("row"):
            entries = row.findall("entry")
            if len(entries) > cols:
                #print("correct from cols='%s' cols to cols='%s'" % (cols, len(entries))) 
                cols = len(entries)
                tgroup.set("cols", str(cols))

    for table in node.findall(".//informaltable"):
        tgroup = table.find("tgroup")
        cols = int(tgroup.get("cols"))
        tbody = tgroup.find("tbody")
        for row in tbody.findall("row"):
            entries = row.findall("entry")
            if len(entries) < cols:
                for x in range(cols - len(entries)):
                    row.append(node.makeelement("entry"))
    return node

# ==============================================================================
def hook_media_table2variablelist(node, rstPrefix, parseData):
# ==============================================================================

    # handle some inappropriate and buggy tables

    if node.get("id") not in [
            "mpeg-control-id" , "mfc51-control-id","cx2341x-control-id",
            "vpx-control-id", "camera-control-id", "fm-tx-control-id", "flash-control-id",
            "jpeg-control-id", "image-source-control-id", "image-process-control-id", "dv-control-id",
            "fm-rx-control-id", "detect-control-id", "rf-tuner-control-id"
    ]:
        return node

    section = node.makeelement("section")
    section.append(XMLTag.copyNode(node.find("title")))
    node.addprevious(section)

    tgroup = node.find("tgroup")
    tbody = tgroup.find("tbody")
    tableRows = tbody.findall("row")

    varentry = None
    varlist  = node.makeelement("variablelist")
    section.append(varlist)

    while tableRows:
        row = tableRows.pop(0)
        entry1, entry2 = (row.findall("entry") + [None, None])[:2]
        if entry1 is None:
            entrytbl = row.find("entrytbl")
            table    = XMLTag.copyNode(entrytbl, "table")
            table.attrib.clear()
            section.append(table)
            varlist  = node.makeelement("variablelist")
            section.append(varlist)

        elif entry1.get("spanname") == "id":
            varentry = node.makeelement("varlistentry")
            varlist.append(varentry)
            term = node.makeelement("term")
            varentry.append(term)
            constant = node.makeelement("constant")
            term.append(constant)
            constant.text = XMLTag.getStripedText(entry1) + " (" + XMLTag.getStripedText(entry2) +")"

        elif entry1.get("spanname") == "descr":
            listitem = node.makeelement("listitem")
            varentry.append(listitem)
            _descr = XMLTag.copyNode(entry1, "para")
            listitem.append(_descr)

        elif (entry2 is None
              and (entry1 is None or not XMLTag.getStripedText(entry1))):
            # skip delimiter row
            varentry = None
            continue
        else:
            #SDK.CONSOLE()
            raise Exception("should never happen / markup seems inconsistent")
    parent = node.getparent()
    parent.remove(node)
    return section

# ==============================================================================
def hook_media_table2variablelist_2(node, rstPrefix, parseData):
# ==============================================================================

    # handle some inappropriate and buggy tables

    ID = node.get("id")
    if ID not in [
            "v4l2-window", "v4l2-clip", "v4l2-rect" ]:
        return node

    section = node.makeelement("section")
    del node.attrib["id"]
    section.set("id", ID)

    footnote = node.find("title/footnote")

    if footnote is not None:
        #SDK.CONSOLE()
        section.append(footnote)
    section.append(XMLTag.copyNode(node.find("title")))
    node.addprevious(section)

    tgroup = node.find("tgroup")
    tbody = tgroup.find("tbody")
    tableRows = tbody.findall("row")

    varentry = None
    varlist  = node.makeelement("variablelist")
    section.append(varlist)

    while tableRows:
        row = tableRows.pop(0)
        entry1, entry2, entry3 = (row.findall("entry") + [None, None, None])[:3]

        if entry3 is not None and XMLTag.getStripedText(entry1):
            varentry = node.makeelement("varlistentry")
            varlist.append(varentry)
            term = node.makeelement("term")
            varentry.append(term)
            constant = node.makeelement("constant")
            term.append(constant)
            #SDK.CONSOLE()
            constant.text = XMLTag.getStripedText(entry1) + " " + XMLTag.getStripedText(entry2)
            listitem = node.makeelement("listitem")
            varentry.append(listitem)
            _descr = XMLTag.copyNode(entry3, "para")
            listitem.append(_descr)

        elif not XMLTag.getStripedText(entry1):
            subsect = XMLTag.copyNode(entry3, "section")
            section.append(subsect)
            varlist  = node.makeelement("variablelist")
            section.append(varlist)

        elif entry1.get("spanname") == "hspan":
            subsect = XMLTag.copyNode(entry1, "section")
            section.append(subsect)
            varlist  = node.makeelement("variablelist")
            section.append(varlist)
        else:
            SDK.CONSOLE()
            raise Exception("should never happen / markup seems inconsistent")

    parent = node.getparent()
    parent.remove(node)
    return section

# ==============================================================================
def hook_media_insert_src_headers(node, rstPrefix, parseData):
# ==============================================================================

    # run this hook only on the root node
    if node.getparent() is not None:
        return node
    childs = node.getchildren()
    if len(childs) == 1 and childs[0].tag=="programlisting":
        title = "file: %s" % parseData.fname.SKIPSUFFIX
        title = ("\n" + title
                 + "\n" + ("=" * len(title)))
        new      = XMLTag.getInjBlockTag()
        new.text += title
        node.insert(0, new)
        return childs[0]
    return node

# ==============================================================================
def hook_media_create_chunks(node, rstPrefix, parseData):
# ==============================================================================

    # run this hook only on the root node
    if node.getparent() is not None:
        return node

    for ID in ["legacy_dvb_apis", ]:
        elem = node.find(".//*[@id='%s']" % ID)
        if elem is not None and elem.get("chunkNode") is None:
            ext_entity = parseData.fname.DIRNAME / ("%s.xml" % ID)
            XMLTag.chunkNode(
                elem
                , parseData.folder
                , ext_entity.suffix(parseData.fname.SUFFIX))
            MEDIA_EXT.addNew(ID, ext_entity)
            MEDIA_EXT.writeToFile()

    return node

# ==============================================================================
def addCharEntities(container):
# ==============================================================================

    #container.addNew("nbsp", r" |nbsp| ")
    container.addNew("nbsp", r" ")
    for x in ["frac12", "frac13", "frac14", "times", "copy", "hellip", "le", "ge"
              , "sub", "sup", "micro", "plusmn", "mdash", "alpha" ]:
        container.addNew(x, xml_unescape("&%s;" % x))


# ==============================================================================
def findOriginXML(locateFolder, fname):
# ==============================================================================

    """Find XML file (origin) realtive to *locateFolder*

    If the xml file is not found within the *locateFolder*, the basename of
    *fname* is returned.
    """

    fname = FSPath(fname)
    orig = next(locateFolder.reMatchFind(fname.BASENAME), None)
    if orig:
        orig = orig.relpath(LINUX_DOCBOOK_ROOT)
    else:
        orig = fname.BASENAME
    #MSG(orig)
    return orig


# # ==============================================================================
# def mediaBuildSingleDocBook(folder, fname, out, level=0):
# # ==============================================================================
#
#     u"""Builds a single book from a media-DocBook starting file.
#
#     .. code-block::
#
#        media_init_ENTITIES()
#        fname = CACHE / "test_v4l2.xml"
#        with fname.openTextFile("w") as out:
#            mediaBuildSingleDocBook(LINUX_TV_CACHE, "media/v4l/v4l2.xml", out)
#     """
#
#     entity = re.compile(r'''&(?P<name>[a-zA-Z][0-9a-zA-Z_-]+);''')
#     folder = FSPath(folder)
#     fname  = folder / fname
#     # MSG("  " * level) + fname
#     with fname.openTextFile() as f:
#         for line in f:
#             l = entity.finditer(line)
#             c = 0
#             for match in l:
#                 name = match.group('name')
#                 subfile = MEDIA_EXT.get(name, None)
#                 if subfile:
#                     c += 1
#                     MSG( (" " * level) + "* %s" % subfile )
#                     mediaBuildSingleDocBook(folder, subfile, out, level+1)
#             if not c:
#                 out.write(line)
