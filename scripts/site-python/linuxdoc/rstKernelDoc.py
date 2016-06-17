#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
# pylint: disable=C0330, R0903, R0914, R0912, R0915

u"""
    rstKernelDoc
    ~~~~~~~~~~~~

    Implementation of the ``kernel-doc`` reST-directive.

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL Version 2, June 1991 see linux/COPYING for details.

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
# imports
# ==============================================================================

import sys
import glob
from os import path
from io import StringIO
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.utils import SystemMessage
from docutils.statemachine import ViewList

from . import kernel_doc as kerneldoc

# ==============================================================================
# common globals
# ==============================================================================

# The version numbering follows numbering of the specification
# (Documentation/books/kernel-doc-HOWTO).
__version__  = '1.0'

PY3 = sys.version_info[0] == 3
PY2 = sys.version_info[0] == 2

if PY3:
    # pylint: disable=C0103, W0622
    unicode     = str
    basestring  = str

PARSER_CACHE = dict()

# ==============================================================================
def setup(app):
# ==============================================================================

    app.add_config_value('kernel_doc_raise_error', False, 'env')
    app.add_config_value('kernel_doc_verbose_warn', True, 'env')
    app.add_config_value('kernel_doc_mode', "reST", 'env')
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
        , "no_header"  : directives.flag

        , "export"     : directives.unchanged          # aka lines containing !E
        , "internal"   : directives.unchanged          # aka lines containing !I
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

    def getParserOptions(self, doc, env):

        fname     = self.arguments[0]
        src_tree  = kerneldoc.SRCTREE
        exp_files = []  # file pattern to search for EXPORT_SYMBOL

        if self.arguments[0].startswith("./"):
            # the prefix "./" indicates a relative pathname
            fname = self.arguments[0][2:]
            src_tree = path.dirname(path.normpath(doc.current_source))

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

        if env.config.kernel_doc_mode not in ["reST", "kernel-doc"]:
            raise self.errMsg(
                "unknow kernel-doc mode: %s" % env.config.kernel_doc_mode)

        # set parse adjustments

        ctx  = kerneldoc.ParserContext()
        opts = kerneldoc.ParseOptions(
            rel_fname       = fname
            , src_tree      = src_tree
            , id_prefix     = self.options.get("module", "").strip()
            , encoding      = self.options.get("encoding", env.config.source_encoding)
            , verbose_warn  = env.config.kernel_doc_verbose_warn
            , markup        = env.config.kernel_doc_mode
            ,)

        opts.set_defaults()

        if not path.exists(opts.fname):
            raise self.errMsg(
                "kernel-doc refers to nonexisting document %s" % opts.fname)

        if self.options:
            opts.skip_preamble = True
            opts.skip_epilog   = True

        if "doc" in self.options:
            opts.no_header = bool("no_header" in self.options)
            opts.use_names.append(self.options.get("doc"))

        if "export" in self.options:
            # gather exported symbols and add them to the list of names
            kerneldoc.Parser.gather_context(kerneldoc.readFile(opts.fname), ctx)
            exp_files.extend((self.options.get('export') or "").replace(","," ").split())
            opts.error_missing = False

        if "internal" in self.options:
            # gather exported symbols and add them to the ignore-list of names
            kerneldoc.Parser.gather_context(kerneldoc.readFile(opts.fname), ctx)
            exp_files.extend((self.options.get('internal') or "").replace(","," ").split())

        if "functions" in self.options:
            opts.error_missing = True
            opts.use_names.extend(
                self.options["functions"].replace(","," ").split())

        for pattern in exp_files:
            if pattern.startswith("./"): # "./" indicates a relative pathname
                pattern = path.join(
                    path.dirname(path.normpath(doc.current_source))
                    , pattern[2:])
            else:
                pattern = path.join(kerneldoc.SRCTREE, pattern)

            if (not glob.has_magic(pattern)
                and not path.lexists(pattern)):
                # if pattern is a filename (is not a glob pattern) and this file
                # does not exists, an error is raised.
                raise self.errMsg("file not found: %s" % pattern)

            for fname in glob.glob(pattern):
                env.note_dependency(path.abspath(fname))
                kerneldoc.Parser.gather_context(kerneldoc.readFile(fname), ctx)

        if "export" in self.options:
            if not ctx.exported_symbols:
                raise self.errMsg("using option :export: but there are no exported symbols")
            opts.use_names.extend(ctx.exported_symbols)

        if "internal" in self.options:
            opts.skip_names.extend(ctx.exported_symbols)

        return opts

    def errMsg(self, msg, lev=4):
        err = self.state_machine.reporter.severe(
            msg
            , nodes.literal_block(self.block_text, self.block_text)
            , line=self.lineno )
        return SystemMessage(err, lev)

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

    def insertOopsMsg(self, msg):
        self.state_machine.insert_input(
            self.getOopsEntry(unicode(msg)).split("\n")
            , self.arguments[0])

    def parseSource(self, env, opts):
        parser = PARSER_CACHE.get(opts.fname, None)

        if parser is None:
            env.note_dependency(opts.fname)
            #env.app.info("parse kernel-doc comments from: %s" % opts.fname)
            parser = KernelDocParser(env.app, opts, kerneldoc.NullTranslator())
            parser.parse()
            PARSER_CACHE[opts.fname] = parser

        return parser

    def run(self):
        doc = self.state.document
        env = doc.settings.env

        retVal = []
        try:
            if not doc.settings.file_insertion_enabled:
                raise self.errMsg('File insertion disabled')
            opts   = self.getParserOptions(doc, env)
            parser = self.parseSource(env, opts)
            retVal = self.getNodes(parser, opts)

        except SystemMessage as exc:
            if env.config.kernel_doc_raise_error:
                raise
            self.insertOopsMsg(exc)

        finally:
            pass
        return retVal


    def getNodes(self, parser, opts):

        rstout = StringIO()
        opts.out = rstout
        translator = kerneldoc.ReSTTranslator()
        parser.parse_dump_storage(opts, translator)

        #if "snippets" in self.options:
        #    parser.options.translator = kerneldoc.ReSTTranslator()

        # xxxxxxxxxxxxx
        lines = rstout.getvalue().split("\n")

        # After the file has been parsed, missing objects should be logged, not
        # raised. If we raise exceptions after parsing all the parsed content
        # get lost.  Instead of raising an exception, a Oops-message should be
        # inserted in the reST document and well parsed reST content should be
        # continued.

        if "functions" in self.options:
            selected  = self.options["functions"].replace(","," ").split()
            names     = translator.translated_names
            not_found = [ s for s in selected if s not in names]
            if not_found:
                self.insertOopsMsg(
                    "selected section(s) not found:\n    %s" % "\n    ,".join(not_found))

        if "export" in self.options:
            selected  = parser.options.use_names
            names     = translator.translated_names
            not_found = [ s for s in selected if s not in names]
            if not_found:
                self.insertOopsMsg(
                    "exported definitions not found:\n    %s" % "\n    ,".join(not_found))

        if "snippets" in self.options:
            selected  = self.options["snippets"].replace(","," ").split()
            names     = parser.ctx.snippets.keys()
            not_found = [ s for s in selected if s not in names]
            if not_found:
                self.insertOopsMsg(
                    "selected snippets(s) not found:\n    %s" % "\n    ,".join(not_found))

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

        reSTfname = self.state.document.current_source

        content = ViewList()
        for l in lines:
            content.append(l, reSTfname, self.lineno)

        node = nodes.section()

        buf = self.state.memo.title_styles, self.state.memo.section_level
        self.state.memo.title_styles, self.state.memo.section_level = [], 0
        try:
            self.state.nested_parse(content, self.lineno, node, match_titles=1)
        finally:
            self.state.memo.title_styles, self.state.memo.section_level = buf

        return node.children
