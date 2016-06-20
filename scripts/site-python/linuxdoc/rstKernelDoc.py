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

    Here is a short overview of the options:

    .. code-block:: rst

        .. kernel-doc:: <src-filename>
            :doc: <section title>
            :no_header:
            :export:
            :internal:
            :functions: <function [, functions [, ...]]>
            :module: <prefix-id>
            :snippets:  <snippet [, snippets [, ...]]>
            :language:  <snippet-lang>
            :linenos:
            :debug:

    The argument ``<src-filename>`` is required, it points to a source file in the
    kernel source tree. The pathname is relativ to kernel's root folder.  The
    options have the following meaning, but be aware that not all combinations of
    these options make sense:

    ``doc <section title>``
        Include content of the ``DOC:`` section titled ``<section title>``.  Spaces
        are allowed in ``<section title>``; do not quote the ``<section title>``.

        The next option make only sense in conjunction with option ``doc``:

        ``no_header``
            Do not output DOC: section's title. Usefull, if the surrounding context
            already has a heading, and the DOC: section title is only used as an
            identifier. Take in mind, that this option will not supress any native
            reST heading markup in the comment (:ref:`reST-section-structure`).

    ``export [<src-fname-pattern> [, ...]]``
        Include documentation for all function, struct or whatever definition in
        ``<src-filename>``, exported using EXPORT_SYMBOL macro (``EXPORT_SYMBOL``,
        ``EXPORT_SYMBOL_GPL`` & ``EXPORT_SYMBOL_GPL_FUTURE``) either in
        ``<src-filename>`` or in any of the files specified by
        ``<src-fname-pattern>``.

        The ``<src-fname-pattern>`` (glob) is useful when the kernel-doc comments
        have been placed in header files, while EXPORT_SYMBOL are next to the
        function definitions.

    ``internal [<src-fname-pattern> [, ...]]``
        Include documentation for all documented definitions, **not** exported using
        EXPORT_SYMBOL macro either in ``<src-filename>`` or in any of the files
        specified by ``<src-fname-pattern>``.


    ``functions <name [, names [, ...]]>``
        Include documentation for each named definition.

    ``module <prefix-id>``
        The option ``:module: <id-prefix>`` sets a module-name. The module-name is
        used as a prefix for automatic generated IDs (reference anchors).

    ``snippets <name [, names [, ...]]>``
        Inserts the source-code passage(s) marked with the snippet ``name``. The
        snippet is inserted with a `code-block:: <http://www.sphinx-doc.org/en/stable/markup/code.html>`_
        directive.

        The next options make only sense in conjunction with option ``snippets``:

        ``language <highlighter>``
            Set highlighting language of the snippet code-block.

        ``linenos``
            Set line numbers in the snippet code-block.

    ``debug``
        Inserts a code-block with the generated reST source. This might somtimes
        helpful to see how the kernel-doc parser transforms the kernel-doc markup to
        reST markup.

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
from sphinx.ext.autodoc import AutodocReporter
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
        self.warnings += 1
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
class FaultyOption(Exception):
    pass

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

    def getParserOptions(self):

        fname     = self.arguments[0]
        src_tree  = kerneldoc.SRCTREE
        exp_files = []  # file pattern to search for EXPORT_SYMBOL

        if self.arguments[0].startswith("./"):
            # the prefix "./" indicates a relative pathname
            fname = self.arguments[0][2:]
            src_tree = path.dirname(path.normpath(self.doc.current_source))

        if "internal" in self.options and "export" in self.options:
            raise FaultyOption(
                "Options 'export' and 'internal' are orthogonal,"
                " can't use them togehter")

        if "snippets" in self.options:
            rest = set(self.options.keys()) - set(["snippets", "linenos", "language", "debug"])
            if rest:
                raise FaultyOption(
                    "kernel-doc 'snippets' has non of these options: %s"
                    % ",".join(rest))

        if self.env.config.kernel_doc_mode not in ["reST", "kernel-doc"]:
            raise FaultyOption(
                "unknow kernel-doc mode: %s" % self.env.config.kernel_doc_mode)

        # set parse adjustments

        ctx  = kerneldoc.ParserContext()
        opts = kerneldoc.ParseOptions(
            rel_fname       = fname
            , src_tree      = src_tree
            , id_prefix     = self.options.get("module", "").strip()
            , encoding      = self.options.get("encoding", self.env.config.source_encoding)
            , verbose_warn  = self.env.config.kernel_doc_verbose_warn
            , markup        = self.env.config.kernel_doc_mode
            ,)

        opts.set_defaults()

        if not path.exists(opts.fname):
            raise FaultyOption(
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
            opts.error_missing = True

        elif "internal" in self.options:
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
                    path.dirname(path.normpath(self.doc.current_source))
                    , pattern[2:])
            else:
                pattern = path.join(kerneldoc.SRCTREE, pattern)

            if (not glob.has_magic(pattern)
                and not path.lexists(pattern)):
                # if pattern is a filename (is not a glob pattern) and this file
                # does not exists, an error is raised.
                raise FaultyOption("file not found: %s" % pattern)

            for fname in glob.glob(pattern):
                self.env.note_dependency(path.abspath(fname))
                kerneldoc.Parser.gather_context(kerneldoc.readFile(fname), ctx)

        if "export" in self.options:
            if not ctx.exported_symbols:
                raise FaultyOption("using option :export: but there are no exported symbols")
            opts.use_names.extend(ctx.exported_symbols)

        if "internal" in self.options:
            opts.skip_names.extend(ctx.exported_symbols)

        return opts

    def errMsg(self, msg):
        msg = unicode(msg)
        error = self.state_machine.reporter.error(
            msg
            , nodes.literal_block(self.block_text, self.block_text)
            , line = self.lineno )

        # raise exception on error?
        if self.env.config.kernel_doc_raise_error:
            raise SystemMessage(error, 4)

        # insert oops/todo admonition
        todo = ("\n\n.. todo::"
                "\n\n    Oops: Document generation inconsistency."
                "\n\n    The template for this document tried to insert"
                " structured comment at this point, but an error occoured."
                " This dummy section is inserted to allow generation to continue.::"
                "\n\n")

        for l in error.astext().split("\n"):
            todo +=  "        " + l + "\n"
        todo += "\n\n"
        self.state_machine.insert_input(todo.split("\n"), self.arguments[0] )

    def parseSource(self, opts):
        parser = PARSER_CACHE.get(opts.fname, None)

        if parser is None:
            self.env.note_dependency(opts.fname)
            self.env.app.info("parse kernel-doc comments from: %s" % opts.fname)
            parser = KernelDocParser(self.env.app, opts, kerneldoc.NullTranslator())
            parser.parse()
            PARSER_CACHE[opts.fname] = parser
        else:
            parser.setOptions(opts)

        return parser

    def run(self):

        self.parser = None
        self.doc    = self.state.document
        self.env    = self.doc.settings.env
        self.nodes  = []

        try:
            if not self.doc.settings.file_insertion_enabled:
                raise FaultyOption('docutils: file insertion disabled')
            opts = self.getParserOptions()
            self.parser = self.parseSource(opts)
            self.nodes.extend(self.getNodes())

        except FaultyOption as exc:
            self.errMsg(exc)

        return self.nodes


    def getNodes(self):

        translator = kerneldoc.ReSTTranslator()
        lines      = ""
        content    = WriterList(self.parser)
        node       = nodes.section()

        # translate

        if "debug" in self.options:
            rstout = StringIO()
            self.parser.options.out = rstout
            self.parser.parse_dump_storage(translator=translator)
            code_block = "\n\n.. code-block:: rst\n    :linenos:\n"
            for l in rstout.getvalue().split("\n"):
                code_block += "\n    " + l
            lines = code_block + "\n\n"

        elif "snippets" in self.options:
            selected  = self.options["snippets"].replace(","," ").split()
            names     = self.parser.ctx.snippets.keys()
            not_found = [ s for s in selected if s not in names]
            if not_found:
                self.errMsg("selected snippets(s) not found:\n    %s"
                            % "\n    ,".join(not_found))

            code_block = "\n\n.. code-block:: %s\n" % self.options.get("language", "c")
            if "linenos" in self.options:
                code_block += "    :linenos:\n"

            snipsnap = ""
            while selected:
                snipsnap += self.parser.ctx.snippets[selected.pop(0)] + "\n\n"

            for l in snipsnap.split("\n"):
                code_block += "\n    " + l
            lines = code_block + "\n\n"

        else:
            self.parser.options.out = content
            self.parser.parse_dump_storage(translator=translator)

        # check translation

        if "functions" in self.options:
            selected  = self.options["functions"].replace(","," ").split()
            names     = translator.translated_names
            not_found = [ s for s in selected if s not in names]
            if not_found:
                self.errMsg(
                    "selected section(s) not found:\n    %s"
                    % "\n    ,".join(not_found))

        if "export" in self.options:
            selected  = self.parser.options.use_names
            names     = translator.translated_names
            not_found = [ s for s in selected if s not in names]
            if not_found:
                self.errMsg(
                    "exported definitions not found:\n    %s"
                    % "\n    ,".join(not_found))

        # add lines to content list
        reSTfname = self.state.document.current_source

        content.flush()
        if lines:
            for l in lines.split("\n"):
                content.append(l, reSTfname, self.lineno)

        buf = self.state.memo.title_styles, self.state.memo.section_level, self.state.memo.reporter
        self.state.memo.reporter = AutodocReporter(content, self.state.memo.reporter)
        self.state.memo.title_styles, self.state.memo.section_level = [], 0
        try:
            self.state.nested_parse(content, 0, node, match_titles=1)
        finally:
            self.state.memo.title_styles, self.state.memo.section_level, self.state.memo.reporter = buf

        return node.children


# ==============================================================================
class WriterList(ViewList):
# ==============================================================================
    u"""docutils ViewList with write method."""

    def __init__(self, parser, *args, **kwargs):
        ViewList.__init__(self, *args, **kwargs)
        self.parser = parser

        self.last_offset = -1
        self.line_buffer = ""

    def write(self, cont):
        if self.last_offset != self.parser.ctx.offset:
            self.flush()
            self.line_buffer = ""
            self.last_offset = self.parser.ctx.offset

        self.line_buffer += cont

    def flush(self):
        for i, l in enumerate(self.line_buffer.split("\n")):
            self.append(l, self.parser.options.fname, self.last_offset)
        self.line_buffer = ""
