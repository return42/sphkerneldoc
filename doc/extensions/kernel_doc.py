#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
# pylint: disable= C0330, C0103, C0410

u"""
    kernel-doc
    ~~~~~~~~~~

    Implementation of the ``kernel-doc`` parser.

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.

    The kernel-doc parser extracts documention from linux kernel source code
    comments.

"""

# ==============================================================================
# imports
# ==============================================================================

import sys, argparse

# ==============================================================================
# globals
# ==============================================================================

VERBOSE = 0

PY3 = sys.version_info[0] == 3
PY2 = sys.version_info[0] == 2

if PY3:
    # pylint: disable=C0103
    unicode     = str
    basestring  = str

_OUT = sys.__stdout__
_ERR = sys.__stderr__

# ==============================================================================
# helper
# ==============================================================================

def msg(message, prefix=u""):
    # pylint: disable=W0702,C0321
    try:      message = unicode(message)
    except:   message = repr(message)
    _ERR.write(prefix + message)

def err(message, prefix=u""):
    # pylint: disable=W0702,C0321
    try:      message = unicode(message)
    except:   message = repr(message)
    _ERR.write(prefix + message)

def log(message):
    err(message, "LOG: ")

# ==============================================================================
def main():
# ==============================================================================

    CLI = argparse.ArgumentParser(
        description = (
            "Parse *kernel-doc* comments from source code"
            " and print them (with reST markup) to stdout." ))

    CLI.add_argument(
        "--doc"
        , help    = "print documentation of ``DOC: <section title>``")

    CLI.add_argument(
        "--exported"
        , action  = "store_true"
        , help    = ("print documentation of all symbols exported"
                     " using EXPORT_SYMBOL" ))

    CLI.add_argument(
        "--internal"
        , action  = "store_true"
        , help    = ("print documentation of all symbols tha are documented,"
                     " but not exported" ))

    CLI.add_argument(
        "--function"
        , nargs   = "+"
        , help    = "print documentation of function(s)")

    CLI.add_argument(
        "--list-exports"
        , action  = "store_true"
        , help    = "list all symbols exported using EXPORT_SYMBOL" )

    CLI.add_argument(
        "--verbose", "-v"
        , action  = "store_true"
        , help    = "verbose output with log messages to stderr" )

    CLI.add_argument(
        "files"
        , nargs   = "+"
        , help    = "source file(s) to parse.")

    cmd = CLI.parse_args()
    if cmd.verbose:
        log(u"argparse --> %s\n" % cmd)


# ==============================================================================
# run ...
# ==============================================================================

if __name__ == "__main__":
    main()
