#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
# pylint: disable=C0330, R0903

u"""
    rstKernelDoc
    ~~~~~~~~~~~~

    Implementation of the ``kernel-doc`` reST-directive.

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.

    The ``kernel-doc`` (:py:class:`KernelDoc`) directive includes contens from
    linux kernel source code comments.

    Options:

    * ``:doc: <section title>`` inserts the contents of the ``DOC:`` section
      titled ``<section title>`` from ``<filename>``.  Spaces are allowed in
      ``<section title>``; do not quote the ``<section title>``.

    * ``:export:`` inserts the documentation in ``<filename>`` of functions /
      structs or whatever are exported using EXPORT_SYMBOL (``EXPORT_SYMBOL()``,
      ``EXPORT_SYMBOL_GPL()`` & ``EXPORT_SYMBOL_GPL_FUTURE()``).

    * ``:internal:`` is replaced by the documentation of functions, structs,
      titles etc. that are documented, but not **not** exported using
      EXPORT_SYMBOL.

    * ``:functions: <function [, functions [, ...]]>`` is replaced by the
      documentation of function, struct or whatever object/title is documented
      <filename>.

    * The option ``:module: <prefix-id>`` sets a module-name, this name is used
      as prefix for automatic generated IDs (reference anchors).

    The following example shows how to insert documention from the source file
    ``/drivers/gpu/drm/drm_drv.c``. In this example the documention from the
    ``DOC:`` section with the title "driver instance overview" and the
    documentation of all exported symbols (EXPORT_SYMBOL) is included in the
    reST tree.

    .. code-block:: rst

        .. kernel-doc::  drivers/gpu/drm/drm_drv.c
            :export:
            :doc:        driver instance overview

    An other example is to use only one function description.

        .. kernel-doc::  include/media/i2c/tvp7002.h
            :functions:  tvp7002_config
            :module:     tvp7002

    This will produce the follwing reST markup to include:

    .. code-block:: rst

        .. _`tvp514x.tvp514x_platform_data`:

        struct tvp514x_platform_data
        ============================

        .. c:type:: tvp514x_platform_data


        .. _`tvp514x.tvp514x_platform_data.definition`:

        Definition
        ----------

        .. code-block:: c

            struct tvp514x_platform_data {
                bool clk_polarity;
                bool hs_polarity;
                bool vs_polarity;
            }

        .. _`tvp514x.tvp514x_platform_data.members`:

        Members
        -------

        clk_polarity
            Clock polarity of the current interface.

        hs_polarity
            HSYNC Polarity configuration for current interface.

        vs_polarity
            VSYNC Polarity configuration for current interface.

    The last example illustrates, that the option ``:module: tvp514x`` is used
    as a prefix for anchors. E.g. ```ref:`tvp514x.tvp514x_platform_data.members¸```
    refers to the to the member description of ``struct tvp514x_platform_data``.


"""

# ==============================================================================
# common globals
# ==============================================================================

# The version numbering follows numbering of the specification
# (Documentation/books/kernel-doc-HOWTO).
__version__  = '1.0'

# ==============================================================================
# imports
# ==============================================================================

from os import path
from io import StringIO
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.utils import SystemMessage
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles

import kernel_doc as kerneldoc

# ==============================================================================
def setup(app):
# ==============================================================================

    app.add_config_value('kernel_doc_raise_error', False, 'env')
    app.add_directive("kernel-doc", KernelDoc)

# ==============================================================================
class KernelDocParser(kerneldoc.Parser):
# ==============================================================================

    def __init__(self, app, *args, **kwargs):
        super(KernelDocParser, self).__init__(*args, **kwargs)
        self.app = app

    # -------------------------------------------------
    # bind the parser logging to the sphinx application
    # -------------------------------------------------

    def error(self, message, **replace):
        self.errors += 1
        self.app.warn(
            message % replace
            , location = "%s:%s [kernel-doc ERROR]" % (self.options.fname, self.ctx.line_no)
            , prefix = "" )

    def warn(self, message, **replace):
        self.app.warn(
            message % replace
            , location = "%s:%s [kernel-doc WARN]" % (self.options.fname, self.ctx.line_no)
            , prefix = "")

    def info(self, message, **replace):
        self.app.verbose(
            "%s:%s: [kernel-doc INFO]: " %(self.options.fname, self.ctx.line_no)
            + message % replace)

    def debug(self, message, **replace):
        if self.app.verbosity < 2:
            return
        replace.update(dict(fname=self.options.fname, line_no=self.ctx.line_no, logclass = "DEBUG"))
        message = "%(fname)s:%(line_no)s [kernel-doc %(logclass)s] : " + message
        self.app.debug(message, **replace)


# ==============================================================================
class KernelDoc(Directive):
# ==============================================================================

    u"""KernelDoc (``kernel-doc``) directive"""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    option_spec = {
        "doc"          : directives.unchanged_required # aka lines containing !P
        , "export"     : directives.flag               # aka lines containing !E
        , "internal"   : directives.flag               # aka lines containing !I
        , "functions"  : directives.unchanged_required # aka lines containing !F

        , "debug"      : directives.flag               # insert generated reST as code-block

        , "snippets"   : directives.unchanged_required
        , "language"   : directives.unchanged_required
        , "linenos"    : directives.flag

        # not yet supported:
        #
        # !C<filename> is replaced by nothing, but makes the tools check that
        # all DOC: sections and documented functions, symbols, etc. are used.
        # This makes sense to use when you use !F/!P only and want to verify
        # that all documentation is included.
        #
        #, "check"     : directives.flag      # aka lines containing !C

        # module name / used as id-prefix
        , "module"     : directives.unchanged_required

        # The encoding of the source file with the kernel-doc comments. The
        # default is the config.source_encoding from sphinx configuration and
        # this default is utf-8-sig
        , "encoding"   : directives.encoding

    }


    def getOopsEntry(self, msg):
        retVal = ("\n\n.. todo::"
                  "\n\n    Oops: Document generation inconsistency."
                  "\n\n    The template for this document tried to insert"
                  " structured comment at this point, but an error occoured."
                  " This dummy section is inserted to allow generation to continue.::"
                  "\n\n")

        for l in msg.split("\n"):
            retVal +=  "        " + l + "\n"
        retVal += "\n\n"
        return retVal

    def errMsg(self, msg, lev=4):
        err = self.state_machine.reporter.severe(
            msg
            , nodes.literal_block(self.block_text, self.block_text)
            , line=self.lineno )
        return SystemMessage(err, lev)

    def run(self):
        doc = self.state.document
        env = doc.settings.env

        retVal = []
        try:
            retVal = self._run(doc, env)
        except SystemMessage, exc:
            if env.config.kernel_doc_raise_error:
                raise
            self.state_machine.insert_input(
                self.getOopsEntry(unicode(exc)).split("\n")
                , self.arguments[0])

        finally:
            pass
        return retVal

    def _run(self, document, env):

        # do some checks

        if not document.settings.file_insertion_enabled:
            raise self.errMsg('File insertion disabled')

        fname    = self.arguments[0]
        src_tree = kerneldoc.SRCTREE

        if self.arguments[0].startswith("./"):
            # the prefix "./" indicates a relative pathname
            fname = self.arguments[0][2:]
            src_tree = path.dirname(path.normpath(document.current_source))

        if "internal" in self.options:
            if "export" in self.options:
                raise self.errMsg(
                    "Options 'export' and 'internal' are orthogonal,"
                    " can't use them togehter")

        if "snippets" in self.options:
            rest = set(self.options.keys()) - set(["snippets", "linenos", "language", "debug"])
            if rest:
                raise self.errMsg(
                    "kernel-doc 'snippets' has non of these options: %s"
                    % ",".join(rest))

        # set parse adjustments

        env.note_dependency(fname)
        rstout = StringIO()
        ctx  = kerneldoc.ParserContext()
        opts = kerneldoc.ParseOptions(
            fname           = fname
            , src_tree      = src_tree
            , id_prefix     = self.options.get("module", "").strip()
            , out           = rstout
            , encoding      = self.options.get("encoding", env.config.source_encoding)
            , translator    = kerneldoc.ReSTTranslator()
            ,)

        opts.set_defaults()
        if not path.exists(opts.fname):
            raise self.errMsg(
                "kernel-doc refers to nonexisting document %s" % fname)

        if self.options:
            opts.skip_preamble = True
            opts.skip_epilog   = True

        if "snippets" in self.options:
            opts.translator = kerneldoc.ReSTTranslator()

        if "doc" in self.options:
            opts.use_names.append(self.options.get("doc"))

        if "export" in self.options:
            # gather exported symbols and add them to the list of names
            kerneldoc.Parser.gather_context(kerneldoc.readFile(opts.fname), ctx)
            opts.use_names.extend(ctx.exported_symbols)
            opts.error_missing = False

        if "internal" in self.options:
            # gather exported symbols and add them to the ignore-list of names
            kerneldoc.Parser.gather_context(kerneldoc.readFile(opts.fname), ctx)
            opts.skip_names.extend(ctx.exported_symbols)

        if "functions" in self.options:
            opts.error_missing = True
            opts.use_names.extend(
                self.options["functions"].replace(","," ").split())

        parser = KernelDocParser(env.app, opts)
        env.app.info("parse kernel-doc comments from: %s" % fname)
        parser.parse()

        lines = rstout.getvalue().split("\n")

        if "functions" in self.options:
            selected  = self.options["functions"].replace(","," ").split()
            names     = parser.ctx.translated_names
            not_found = [ s for s in selected if s not in names]
            if not_found:
                raise self.errMsg(
                    "selected section(s) not found: %s" % ", ".join(not_found))

        if "snippets" in self.options:
            selected  = self.options["snippets"].replace(","," ").split()
            names     = parser.ctx.snippets.keys()
            not_found = [ s for s in selected if s not in names]
            if not_found:
                raise self.errMsg(
                    "selected snippets(s) not found: %s" % ", ".join(not_found))

            lines = ["", ".. code-block:: %s"
                     % self.options.get("language", "c"), ]
            if "linenos" in self.options:
                lines.append("    :linenos:")
            lines.append("")

            while selected:
                snippet = parser.ctx.snippets[selected.pop(0)].split("\n")
                lines.extend(["    " + l for l in snippet])
                if selected:
                    # delemit snippets with two newlines
                    lines.extend(["",""])

        if "debug" in self.options:
            code_block = "\n.. code-block:: rst\n    :linenos:\n\n".split("\n")
            for l in lines:
                code_block.append("    " + l)
            lines = code_block

        content = ViewList(lines)
        node = nodes.section()
        node.document = self.state.document
        nested_parse_with_titles(self.state, content, node)

        return node.children

