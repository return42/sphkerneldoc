#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
# pylint: disable=C0330

u"""
    rstKernelDoc
    ~~~~~~~~~~~~

    Implementation of the ``kernel-doc`` reST-directive.

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.

    The ``kernel-doc`` (:py:class:`KernelDoc`) directive includes contens from
    linux kernel source code comments.

    Options:

    * ``:doc: <section title>`` is replaced by the contents of the ``DOC:`` section
      titled ``<section title>`` from ``<filename>``.  Spaces are allowed in
      ``<section title>``; do not quote the ``<section title>``.

    * ``:exported:`` is replaced by the documentation, in ``<filename>``, for
      functions that are exported using EXPORT_SYMBOL (``EXPORT_SYMBOL()``,
      ``EXPORT_SYMBOL_GPL()`` & ``EXPORT_SYMBOL_GPL_FUTURE()``)

    * ``:internal:`` is replaced by the documentation for functions that are
      documented, but not **not** exported using EXPORT_SYMBOL.

    * ``:functions: <function [, functions [, ...]]>`` is replaced by the
      documentation, in <filename>, for the functions listed.

    The following example shows how to include documention from the source file
    ``/drivers/gpu/drm/drm_drv.c``. In this example the documention from the
    ``DOC:`` section with title "driver instance overview" and the documentation
    of all exported symbols (EXPORT_SYMBOL) from this file is included.

    .. code-block:: rst

        Device Instance and Driver Handling
        ===================================

        .. kernel-doc::  /drivers/gpu/drm/drm_drv.c
            :exported:
            :doc:        driver instance overview

"""

# ==============================================================================
# imports
# ==============================================================================

import codecs
from docutils.parsers.rst import Directive, directives

# ==============================================================================
def init():
# ==============================================================================

    directives.register_directive("kernel-doc", KernelDoc)

# ==============================================================================
class KernelDoc(Directive):
# ==============================================================================

    u"""KernelDoc (``kernel-doc``) directive"""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    option_spec = {
        'name'         : directives.unchanged
        , "encoding"   : directives.encoding
        , "doc"        : directives.unchanged # aka lines containing !P
        , "exported"   : directives.flag      # aka lines containing !E
        , "internal"   : directives.flag      # aka lines containing !I
        , "functions"  : directives.unchanged # aka lines containing !F
        , "sectag"     : directives.unchanged # =-+~.^
        #
        # not yet supported:
        #
        # !C<filename> is replaced by nothing, but makes the tools check that
        # all DOC: sections and documented functions, symbols, etc. are used.
        # This makes sense to use when you use !F/!P only and want to verify
        # that all documentation is included.
        #
        #, "check"     : directives.flag      # aka lines containing !C
    }

    def run(self):
        document = self.state.document

        if not document.settings.file_insertion_enabled:
            return [document.reporter.warning(
                'File insertion disabled', line=self.lineno)]

        env = document.settings.env
        rel_filename, filename = env.relfn2path(self.arguments[0])

        encoding = self.options.get('encoding', env.config.source_encoding)
        codec_info = codecs.lookup(encoding)

        # TODO ....



# ==============================================================================
# init
# ==============================================================================

init()

