#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
# pylint: disable=C0330

# ------------------------------------------------------------------------------
# imports
# ------------------------------------------------------------------------------

import sys
from os.path import join as pathjoin
from os.path import abspath, dirname
import argparse

import six

from common import FSPath, Container

BASE_FOLDER = dirname(__file__)
sys.path.append(abspath(pathjoin(BASE_FOLDER, "site-python")))
from linuxdoc import kernel_doc as kerneldoc


# ------------------------------------------------------------------------------
# config
# ------------------------------------------------------------------------------

MARKUP = "kernel-doc" # "reST"
MSG    = lambda msg: sys.__stderr__.write("INFO : %s\n" % msg)
ERR    = lambda msg: sys.__stderr__.write("ERROR: %s\n" % msg)
FATAL  = lambda msg: sys.__stderr__.write("FATAL: %s\n" % msg)

TEMPLATE_INDEX="""\
.. -*- coding: utf-8; mode: rst -*-

================================================================================
%(title)s
================================================================================

.. toctree::
    :maxdepth: 1

"""


# ------------------------------------------------------------------------------
def main():
# ------------------------------------------------------------------------------
    # pylint: disable=C0103

    CLI = argparse.ArgumentParser(
        description = ("Parse *kernel-doc* comments from source code")
        , formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    CLI.add_argument(
       "srctree"
       , help    = "folder with linux source tree in"
       , type    = lambda x: FSPath(x).ABSPATH)

    CLI.add_argument(
       "doctree"
       , help    = "folder to place reST documentation"
       , type    = lambda x: FSPath(x).ABSPATH)

    CMD = CLI.parse_args()

    if not CMD.srctree.EXISTS or not CMD.srctree.ISDIR:
        ERR("%s does not exists or is not a folder" % CMD.srctree)
        sys.exit(42)

    if CMD.doctree.EXISTS:
        ERR("%s is in the way, remove it first" % CMD.doctree)
        sys.exit(42)

    for fname in CMD.srctree.reMatchFind(r"^.*\.[ch]$"):
        if fname.startswith(CMD.srctree/"Documentation"):
            continue
        autodoc_file(fname, CMD.srctree, CMD.doctree)

    insert_index_files(CMD.doctree)

# ------------------------------------------------------------------------------
def autodoc_file(fname, src_folder, doc_folder):
# ------------------------------------------------------------------------------

    fname = fname.relpath(src_folder)
    opts = kerneldoc.ParseOptions(
        rel_fname       = fname
        , src_tree      = src_folder
        #, verbose_warn  = True
        , markup        = MARKUP
        ,)
    parser = kerneldoc.Parser(opts, kerneldoc.NullTranslator())
    try:
        parser.parse()
    except Exception as exc: # pylint: # pylint: disable=W0703,W0612
        FATAL("kernel-doc markup of %s seems buggy / can't parse" % opts.fname)
        return

    if not parser.ctx.dump_storage:
        # no kernel-doc comments found
        MSG("parsed NONE: %s" % fname)
        return

    MSG("parsed: %4d comments: %s" % (len(parser.ctx.dump_storage),fname))

    try:
        rst = six.StringIO()
        translator = kerneldoc.ReSTTranslator()
        opts.out   = rst

        # First try to output reST, this might fail, because the kernel-doc
        # parser part is to tollerant ("bad lines", "function name and function
        # declaration are different", etc ...).
        parser.parse_dump_storage(translator=translator)

        outFile = doc_folder / fname.replace(".","_") + ".rst"
        outFile.DIRNAME.makedirs()
        with outFile.openTextFile(mode="w") as out:
            out.write(rst.getvalue())

    except Exception as exc: # pylint: disable=W0703
        FATAL("kernel-doc markup of %s seems buggy / can't parse" % opts.fname)
        return

# ------------------------------------------------------------------------------
def insert_index_files(folder):
# ------------------------------------------------------------------------------

    for folder, dirnames, filenames in folder.walk():
        ctx = Container( title = folder.FILENAME )
        dirnames.sort()
        filenames.sort()
        indexFile = folder / "index.rst"
        MSG("create index: %s" % indexFile)
        with indexFile.openTextFile(mode="w") as index:
            index.write(TEMPLATE_INDEX % ctx)
            for d in dirnames:
                index.write("    %s/index\n" % d.FILENAME)
            for f in filenames:
                if f.FILENAME == "index":
                    continue
                index.write("    %s\n" % f.FILENAME)

main()
