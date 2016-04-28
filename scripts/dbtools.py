#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
u"""
    dbtools
    ~~~~~~~

    Collection of *hackish* tools to migrate DocBook-XML to reST.

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.

    I haven't found any XSL Template to convert DocBook to reST, and I'am not
    intrested in developing one. Thats why I compiled these small ``dbtools``
    toolbox, which uses existing tools and *hacked* a bit around them.  The
    ``dbtools`` uses the pandoc converter and implements some XML-filters and
    all theses stuff, where pandoc fails, e.g. cross references in a multipart
    DocBook document.

    Migration of DocBook-XML is a working process and these tools are not *ready
    to go*.  The ``dbtools`` script is a usefull base for DocBook to reST
    migration, it don't attempt to be a *converter* for your daily usage. The
    toolbox is developed in context of the Linux Kernel documentation. You might
    edit or add parts to the toolbox, by doing this, please take notice of the
    dbtools :ref:`xref_LICENSE`.
"""

# pylint: disable=W0603, C0103, C0325, C0321, R0914

# ==============================================================================
# imports
# ==============================================================================

import re
from common import CLI, FSPath
from common import PANDOC_EXE, xml2json, jsonFilter, json2rst
from dbxml import XMLTag, filterXML, subEntities, Table, RESOUCE_FORMAT, INT_ENTITES
from dbxml import hook_copy_file_resource, hook_chunk_by_tag, hook_fix_broken_tables
from dbxml import hook_flatten_tables, hook_drop_usless_informaltables, hook_html2db_table

#from pprint import pformat, pprint

import media

# ==============================================================================
# setup
# ==============================================================================

from dbenv import CACHE, BOOKS_FOLDER, LINUX_DOCBOOK_ROOT

MSG = CLI.msg
ERR = CLI.err

mainFOOTER="""

Retrieval
=========

* :ref:`genindex`
* :ref:`search`

"""

rstHEADER=""".. -*- coding: utf-8; mode: rst -*-
"""
rstFOOTER="""

.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
"""



# ==============================================================================
def main():
# ==============================================================================

    # pylint: disable=W0612

    cli = CLI(description="Tools to migrate DocBook-XML to reST.")

    # media2rst
    # ---------

    cmd = cli.addCMDParser(media2rst)
    cmd.add_argument(
        "--noinit", action = 'store_true'
        , help = "don't 'init the cache (default: %(default)s)" )
    cmd.add_argument(
        "--noconvert", action = 'store_true'
        , help = "don't 'convert xml2rst within the cache (default: %(default)s)" )
    cmd.add_argument(
        "--noinstall", action = 'store_true'
        , help = "don't install converted files (default: %(default)s)" )

    # db2rst
    # ------

    cmd = cli.addCMDParser(db2rst)
    cmd.add_argument(
        "--noconvert", action = 'store_true'
        , help = "don't 'convert xml2rst within the cache (default: %(default)s)" )
    cmd.add_argument(
        "--noinstall", action = 'store_true'
        , help = "don't install converted files (default: %(default)s)" )
    cmd.add_argument(
        "filename", nargs="+"
        , help="DocBook-XML file to convert to reST  (e.g 'kernel-hacking.xml')")


    # fiddle
    # ------

    cmd = cli.addCMDParser(fiddle)
    cmd.add_argument(
        "filename", nargs="?", default="media_api.xml_entity"
        , help="filename of the file for testing (default: %(default)s)")

    # cmd = cli.addCMDParser(inspectJSON)
    # cmd.add_argument(
    #     "jsonfile", nargs = "?", default = LINUX_TV_CACHE / "media_api.json"
    #     , help = "Pandoc json file (default: %(default)s)" )

    cli()


# ==============================================================================
def media2rst(cliArgs):                                  # pylint: disable=W0613
# ==============================================================================

    u"""convert *media* (linux_tv) DocBook documentation to reST.

    This is an attempt to convert the media (linux_tv) documentation -- written
    in DocBook markup -- to reST.

    Every *media* xml fragment is copied to the cache folder where the converion
    steps are applied on it.  """

    if not cliArgs.noinit:
        media.initMedia()

    if not cliArgs.noconvert:
        # convert files
        MSG("using %s to convert" % PANDOC_EXE)
        MSG("convert within folder: %s" % media.LINUX_TV_CACHE)

        fileList = media.getFileList()
        inFileList = [ f.suffix(".xml") for f in fileList ]
        for inFile in inFileList:
            MSG("\n::convert file:: %s" % inFile)
            convert_xml2rst(media.LINUX_TV_CACHE, inFile)

    # add footer to main reST file
    reSTRoot = media.LINUX_TV_CACHE/"media_api.rst"
    with reSTRoot.openTextFile(mode="a") as f:
        f.write(mainFOOTER)

    if not cliArgs.noinstall:
        media.installMedia()

# ==============================================================================
def db2rst(cliArgs):                                    # pylint: disable=W0613
# ==============================================================================

    u"""convert DocBook documentation to reST."""

    for fname in cliArgs.filename:
        origFile = FSPath(fname)
        _db2rst(cliArgs, origFile)

# ==============================================================================
def _db2rst(cliArgs, origFile):                          # pylint: disable=W0613
# ==============================================================================

    hook_list = [
        hook_chunk_by_tag("book", "part", "chapter", ".//refentry")
        , hook_copy_file_resource(LINUX_DOCBOOK_ROOT)
        , hook_html2db_table
        , hook_drop_usless_informaltables
        #, hook_fix_broken_tables(fname_list=["kernel-locking/cheatsheet", ])
        , hook_flatten_tables()
    ]

    folder = CACHE / origFile.SKIPSUFFIX

    MSG("==== convert DocBook %s to reST ====" % (origFile))

    if folder.EXISTS:
        folder.rmtree()
    folder.makedirs()

    # create a copy of the file
    mainFile = FSPath("index.xml_orig")
    outFile  = mainFile.suffix(".xml_orig")
    (LINUX_DOCBOOK_ROOT/origFile).copyfile(folder/outFile)

    inFile  = outFile
    outFile = outFile.suffix(".xml_entity")

    MSG("substitude entities ...")
    subEntities(folder/inFile, folder/outFile, None, INT_ENTITES)

    inFile  = outFile
    outFile = outFile.suffix(".xml")

    MSG("run XML filter: %s --> %s" % (inFile, outFile))

    # XML-filter
    xmlFilter = XMLTag()
    for hook in hook_list:
        xmlFilter.parseData.hooks.append(hook)

    filterXML(folder, inFile, outFile
              , xmlFilter     = xmlFilter
              , parseIncludes = True )

    # after chunking, we have a filelist ...
    fileList = [f.BASENAME for f in folder.reMatchFind(".*\\.xml$") ]

    if not cliArgs.noconvert:

        MSG("using %s to convert" % PANDOC_EXE)
        MSG("\nconvert within folder: %s" % folder)
        for inFile in fileList:
            MSG("::convert file:: %s" % inFile)
            convert_xml2rst(folder, inFile)

    # add footer to main reST file
    reSTRoot = folder/mainFile.suffix(".rst")
    with reSTRoot.openTextFile(mode="a") as f:
        f.write(mainFOOTER)

    if not cliArgs.noinstall:

        bookFolder = BOOKS_FOLDER / origFile.BASENAME.SKIPSUFFIX
        if bookFolder.EXISTS:
            bookFolder.rmtree()
        bookFolder.makedirs()

        for xmlFile in fileList:
            rstFile = xmlFile.suffix(".rst")
            MSG("install file %s" % xmlFile)
            src = folder/ rstFile
            dst = bookFolder / rstFile
            resource = FSPath(RESOUCE_FORMAT % src.SKIPSUFFIX)

            dst.DIRNAME.makedirs()
            src.copyfile(dst)

            if resource.EXISTS:
                dstFolder = dst.DIRNAME / folder.BASENAME
                MSG("install file-folder %s" % dstFolder)
                resource.copytree(dstFolder)

# ==============================================================================
def fiddle(cliArgs):                                     # pylint: disable=W0613
# ==============================================================================

    u"""Implement some stuff and yust fiddle a bit with it."""

    # raise NotImplementedError("You have not yet implemented any stuff to fiddle with.")

    # Example: fiddle with media files / you have to run::
    #
    #     media2rst --noinstall --noconvert
    #
    # before you can work on media files.

    inFile = FSPath(cliArgs.filename)
    outFile = inFile.suffix(".xml")
    MSG("run XML filter (mainFile) : %s --> %s" % (inFile, outFile))
    filterXML(media.LINUX_TV_CACHE, inFile, outFile
              , media.getMediaFilter()
              , parseIncludes = False)

    inFile = outFile
    MSG("\n::convert file:: %s" % inFile)
    convert_xml2rst(media.LINUX_TV_CACHE, inFile)



# ==============================================================================
def convert_xml2rst(folder, inFile):
# ==============================================================================

    u"""Convert a xml fragment to reST.

    :param str folder: Root-folder where conversion takes place.
    :param str inFile: Preprocess XML file.

    Description of the conversion steps:

    * convert to json-AST
    * apply json-filters
    * convert json to reST
    * apply pandoc reST bugfixes
    """

    folder  = FSPath(folder)

    outFile = inFile.suffix(".json_pre")
    MSG("convert xml --> json : %s" % outFile)
    xml2json(folder / inFile, folder / outFile, stdout = None, stderr=None)

    inFile, outFile  = outFile, outFile.suffix(".json")
    MSG("json / pandoc filter: %s" % outFile)
    jsonFilter(folder / inFile, folder / outFile, XMLTag.pandocFilter)

    inFile, outFile  = outFile, outFile.suffix(".rst_pre")
    MSG("convert json --> rst: %s" % outFile)
    json2rst(folder / inFile, folder / outFile, stdout = None, stderr=None)

    inFile, outFile = outFile, outFile.suffix(".rst")
    MSG("fix pandoc's rst: %s" % outFile)
    fixPandocRST(folder / inFile, folder / outFile)



# ==============================================================================
def fixPandocRST(src, dst):
# ==============================================================================

    u"""Fix common reST markup bugs from the pandoc reST writer.  """

    # fix malicious pandoc quoting
    # https://github.com/jgm/pandoc/blob/master/src/Text/Pandoc/Writers/RST.hs#L162
    # --> """escapeStringUsing (backslashEscapes "`\\|*_")"""
    backslashEscapes = re.compile(r"\\[`\|\||\*|_]")

    indent = ""
    with src.openTextFile() as src, dst.openTextFile("w") as dst:

        dst.write(rstHEADER)

        for line in src:
            line = line.replace(u"⋆", "*")
            striped = line.strip()
            if not striped:
                dst.write("\n")
                continue
            if striped == Table.tableStartMark:
                indent += Table.rstBlock
                continue
            if striped == Table.tableEndMark:
                indent = indent[:-len(Table.rstBlock)]
                continue

            line = indent + line

            if backslashEscapes.search(line):
                spaces = ""
                if "|" == line.strip()[0]:
                    # this is a table markup
                    buf  = ""
                    for c in line:
                        if c == "\\":
                            spaces += " "
                        elif spaces and c in ["\t", " ", "\n"]:
                            buf += spaces + c
                            spaces = ""
                        else:
                            buf += c
                    line = buf.rstrip() + "\n"
                else:
                    line = line.replace("\\", "")
            dst.write(line)

        dst.write(rstFOOTER)

# # ==============================================================================
# def inspectJSON(cliArgs):
# # ==============================================================================

#     u"""fiddle a bit with pandoc/json filtering"""

#     keys    = dict()

#     def getBanner(key, value, fmt, meta):
#         from pprint import pformat
#         return (
#             "---- (%s) key: %s ----" % (fmt, key)
#             + "\nmeta: %s" % pformat(meta, indent=4)
#             + "\nvalue:\n%s" % pformat(value, indent=4))

#     def inspect_filter(key, value, fmt, meta): # pylint: disable=W0613
#         keys[key] = keys.get(key, 0) + 1
#         if key in ('Link', 'Image', 'Code'):
#             SDK.CONSOLE(banner=getBanner(key, value, fmt, meta)) # pylint: disable=E0602

#     folder  = CACHE
#     inFile  = FSPath(cliArgs.jsonfile).BASENAME
#     outFile = inFile.suffix(".filtered_json")

#     # create a copy of the file
#     FSPath(cliArgs.xmlfile).copyfile( folder / inFile)

#     # inspect
#     jsonFilter(folder / inFile, folder / outFile, inspect_filter)

#     MSG("key types within this file:\n")
#     MSG("\n".join([ ("  * %-10s : %d" % x) for x in keys.items() ]) + "\n")
#     MSG("created %s" % outFile)

#     inFile  = outFile
#     outFile = outFile.suffix(".rst_pre")
#     MSG("convert  json --> rst : %s" % (outFile))
#     json2rst(inFile, outFile, stdout = None, stderr=None)

#     inFile  = outFile
#     outFile = outFile.suffix(".rst")
#     MSG("filter:  rst          : %s" % (outFile))
#     fixPandocRST(inFile, outFile)

# ==============================================================================
# run ...
# ==============================================================================

if __name__ == "__main__":
    main()
