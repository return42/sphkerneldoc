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
from dbxml import XMLTag, filterXML, subEntities, EntityContainer
from dbxml import hook_copy_file_resource, RESOUCE_FORMAT, hook_replaceTag
from dbxml import hook_flatten_tables, hook_drop_usless_informaltables
from lxml import etree

# ==============================================================================
# setup
# ==============================================================================

from dbenv import CACHE, MIGRATION_FOLDER, LINUX_DOCBOOK_ROOT

MSG = CLI.msg
ERR = CLI.err

LINUX_TV_CACHE  = CACHE / "linux_tv"
LINUX_TV_BOOK   = MIGRATION_FOLDER / "linux_tv"

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
        for name in LINUX_TV_BOOK.reMatchFind("[^(conf.py)]"):
            name.delete()
    else:
        LINUX_TV_BOOK.makedirs()

    fileList = getFileList()

    for xmlFile in fileList:
        rstFile = xmlFile.suffix(".rst")

        src = LINUX_TV_CACHE  / rstFile
        dst = LINUX_TV_BOOK / rstFile
        if rstFile == FSPath("media_api.rst"):
            dst = LINUX_TV_BOOK / FSPath("index.rst")
        folder = FSPath(RESOUCE_FORMAT % src.SKIPSUFFIX)

        dst.DIRNAME.makedirs()
        MSG("install file %s" % dst)
        src.copyfile(dst)

        if folder.EXISTS:
            dstFolder = dst.DIRNAME / folder.BASENAME
            MSG("install file-folder %s" % dstFolder)
            folder.copytree(dstFolder)
            for svgFile in dstFolder.reMatchFind(".*\.svg$"):
                if not svgFile.suffix(".pdf").EXISTS:
                    try:
                        import cairosvg
                        MSG("convert %s to PDF" % svgFile)
                        cairosvg.svg2pdf(url=svgFile, write_to=svgFile.suffix(".pdf"))
                    except ImportError:
                        ERR("missing cairosvg, can't convert %s to PDF" % svgFile)

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

    id2TagMap = {}

    for ID in [ "capture", "overlay", "output", "osd", "codec", "effect", "raw-vbi"
                , "sliced", "ttx", "radio", "rds", "sdr", "event", "subdev"
                , "Remote_controllers_Intro", "remote_controllers_sysfs_nodes"
                , "Remote_controllers_tables", "Remote_controllers_table_change"
    ]:
        id2TagMap[ID] = "chapter"

    id2TagMap["planar-apis"]  = "chapter"

    for ID in [
            "pixfmt", "io", "common"  # v4l
            , "dvb_frontend","net", "dvbproperty", "frontend_fcalls" # dvb
            , "frontend_legacy_api"
            , "dvb_demux", "dvb_ca", "net", "dvb_video", "dvb_audio", "net_fcalls"
            , "lirc_device_interface" ]:
        id2TagMap[ID] = "part"

    xmlFilter = XMLTag()
    for hook in [hook_replaceTag(id2TagMap)
                 , hook_media_table2variablelist
                 , hook_media_table2variablelist_2
                 , hook_media_fix_misc
                 , hook_media_handle_subsec
                 , hook_media_create_chunks
                 , hook_media_rstInclude
                 , hook_media_insert_src_headers
                 , hook_drop_usless_informaltables
                 , hook_flatten_tables()
                 , hook_copy_file_resource(LINUX_DOCBOOK_ROOT) ]:
        xmlFilter.parseData.hooks.append(hook)
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
def hook_media_fix_misc(node, rstPrefix, parseData):
# ==============================================================================

    # run this hook only on the root node
    if node.getparent() is not None:
        return node

    if node.find(".//*[@id='%s']" % "packed-yuv") is not None:
        # insert missing cells in the table in this section
        table = node.find(".//table")
        headrow = table.find(".//thead/row")
        headrow.insert(4,node.makeelement("entry"))
        headrow.insert(6,node.makeelement("entry"))
        headrow.insert(8,node.makeelement("entry"))
    return node

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

        parent  = incl.getparent()

        if (XMLTag.getStripedText(parent)
            or parent.tag == "dummy"):
            # can not moved / should not move
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
def hook_media_table2variablelist(node, rstPrefix, parseData):
# ==============================================================================

    # This hooks transforms some tables to definition lists.

    # run this hook only on the root node
    if node.getparent() is not None:
        return node

    for ID in [ "control-id" ]:
        elem = node.find(".//*[@id='%s']" % ID)
        if (elem is not None
            and elem.tag == "table" ):
            table2variablelist_3cols(elem, rstPrefix, parseData)

    for ID in [
            "control-id", "mpeg-control-id" , "mfc51-control-id", "cx2341x-control-id",
            "vpx-control-id", "camera-control-id", "fm-tx-control-id", "flash-control-id",
            "jpeg-control-id", "image-source-control-id", "image-process-control-id", "dv-control-id",
            "fm-rx-control-id", "detect-control-id", "rf-tuner-control-id" ]:
        elem = node.find(".//*[@id='%s']" % ID)
        if (elem is not None
            and elem.tag == "table" ):
            table2variablelist(elem, rstPrefix, parseData)
    return node

def table2variablelist(node, rstPrefix, parseData):

    ID = node.get("id")
    section = node.makeelement("section")
    section.append(XMLTag.copyNode(node.find("title")))

    tgroup = node.find("tgroup")
    tbody = tgroup.find("tbody")

    tableRows = tbody.findall("row")

    varentry = None
    varlist  = node.makeelement("variablelist")
    section.append(varlist)

    while tableRows:
        row = tableRows.pop(0)
        row_id = row.get("id")
        entry1, entry2 = (row.findall("entry") + [None, None])[:2]

        if entry1 is None:
            entrytbl = row.find("entrytbl")
            table    = XMLTag.copyNode(entrytbl, "table")
            table.attrib.clear()
            if row_id is not None:
                table.set("id", row_id)
            section.append(table)
            varlist  = node.makeelement("variablelist")
            section.append(varlist)

        elif entry1.get("spanname") == "id":
            if row_id is not None:
                new      = XMLTag.getInjInlineTag()
                new.text = "\n\n.. _`%s`:\n\n" % row_id
                section.append(new)
                varlist  = node.makeelement("variablelist")
                section.append(varlist)
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
    parent.replace(node, section)
    section.set("id", ID)


def table2variablelist_3cols(node, rstPrefix, parseData):

    ID = node.get("id")
    section = node.makeelement("section")
    section.append(XMLTag.copyNode(node.find("title")))

    tgroup = node.find("tgroup")
    tbody = tgroup.find("tbody")

    tableRows = tbody.findall("row")

    varentry = None
    varlist  = node.makeelement("variablelist")
    section.append(varlist)

    while tableRows:
        row = tableRows.pop(0)
        row_id = row.get("id")
        entry1, entry2, entry3 = (row.findall("entry") + [None, None, None])[:3]

        if entry3 is None:
            entrytbl = row.find("entrytbl")
            table    = XMLTag.copyNode(entrytbl, "table")
            if row_id is not None:
                table.set("id", row_id)
            table.attrib.clear()
            section.append(table)
            varlist  = node.makeelement("variablelist")
            section.append(varlist)

        elif entry1 is not None and entry2 is not None:
            if row_id is not None:
                new      = XMLTag.getInjInlineTag()
                new.text = "\n\n.. _`%s`:\n\n" % row_id
                section.append(new)
                varlist  = node.makeelement("variablelist")
                section.append(varlist)

            varentry = node.makeelement("varlistentry")
            varlist.append(varentry)
            term = node.makeelement("term")
            varentry.append(term)

            constant = node.makeelement("constant")
            term.append(constant)
            constant.text = XMLTag.getStripedText(entry1)

            if XMLTag.getStripedText(entry2):
                constant.tail = " "
                _type = node.makeelement("constant")
                term.append(_type)
                _type.text = "(" + XMLTag.getStripedText(entry2) +")"

            listitem = node.makeelement("listitem")
            varentry.append(listitem)
            _descr = XMLTag.copyNode(entry3, "para")
            listitem.append(_descr)

        else:
            #SDK.CONSOLE()
            raise Exception("should never happen / markup seems inconsistent")

    parent = node.getparent()
    parent.replace(node, section)
    section.set("id", ID)


# ==============================================================================
def hook_media_table2variablelist_2(node, rstPrefix, parseData):
# ==============================================================================

    # This hooks transforms some tables to definition lists.

    # run this hook only on the root node
    if node.getparent() is not None:
        return node

    for ID in ["v4l2-window", "v4l2-clip", "v4l2-rect" ]:
        elem = node.find(".//*[@id='%s']" % ID)
        if (elem is not None and elem.tag == "table" ):
            table2variablelist_2(elem, rstPrefix, parseData)

    return node

def table2variablelist_2(node, rstPrefix, parseData):

    ID = node.get("id")

    section = node.makeelement("section")
    del node.attrib["id"]
    section.set("id", ID)

    footnote = node.find("title/footnote")

    if footnote is not None:
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
            #SDK.CONSOLE()
            raise Exception("should never happen / markup seems inconsistent")

    parent = node.getparent()
    parent.remove(node)

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

    if parseData.fname.BASENAME.SKIPSUFFIX == "v4l2":
        # there is one appendix, which missed the id attribut
        for n in node.findall(".//appendix"):
            if n.get("id") is None:
                n.set("id", "common-defs")
                break

    for ID in [
            # v4l2.xml
            "devices", "user-func", "common-defs", "videodev"
            , "capture-example", "v4l2grab-example"
            # dvbapi.xml
            , "legacy_dvb_apis", "audio_h", "ca_h"
            , "dmx_h", "frontend_h" , "net_h", "video_h"
            , "frontend_fcalls", "frontend_f_open", "frontend_f_close"
            , "Remote_controllers_Intro", "remote_controllers_sysfs_nodes"
            , "Remote_controllers_tables", "Remote_controllers_table_change"
            , "media-controller-intro", "media-controller-model" ]:

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
def hook_media_handle_subsec(node, rstPrefix, parseData):
# ==============================================================================

    if not parseData.fname.BASENAME.SKIPSUFFIX in [
            # v4l
            "pixfmt", "io", "common", "controls", "selection-api"
            , "libv4l", "compat", "selections-common"
            # dvb
            , "frontend", "net", "dvbproperty", "frontend_fcalls"
            , "frontend_legacy_api"
            , "demux", "ca", "net", "video", "audio", "net_fcalls"
            , "lirc_device_interface" ]:
        return node

    # Some IDs cause a name collision, because, there are also entities with
    # simmular names e.g."func-open.xml", which is refered by "open".
    mapID = {
        #"mmap"       : "streaming-io"
        #, "open"     : "open-close-device"
        #, "querycap" : "v4l2-querycap"
        #, "control"  : "user-controls"
    }

    xpath = "*/section"
    if parseData.fname.BASENAME.SKIPSUFFIX in ["controls"]:
        xpath = "./section"

    count = 1
    for section in node.findall(xpath):
        count +=1
        newNode = XMLTag.copyNode(section, "chapter", moveID=True)
        XMLTag.replaceNode(section, newNode)
        ID = newNode.get("id")
        if ID is None:
            ID = "%s-%03d" % (parseData.fname.BASENAME.SKIPSUFFIX, count)
        else:
            ID = mapID.get(ID, ID)
            newNode.set("id", ID)

        ext_entity = parseData.fname.DIRNAME / ("%s.xml" % ID)
        XMLTag.chunkNode(
            newNode
            , parseData.folder
            , ext_entity.suffix(parseData.fname.SUFFIX))
        MEDIA_EXT.addNew("chunk_" + ID, ext_entity)
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
