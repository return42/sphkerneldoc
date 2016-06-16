#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
# pylint: disable= C0330, C0103, C0410, R0903, R0913, R0912, R0914, R0915, C0302

u"""
    kernel_doc
    ~~~~~~~~~~

    Implementation of the ``kernel-doc`` parser.

    :copyright:  Copyright (C) 2016  Markus Heiser
    :license:    GPL Version 2, June 1991 see linux/COPYING for details.

    The kernel-doc parser extracts documention from linux kernel's source code
    comments. This is a rewrite of the kernel-doc perl script.

    This module provides an API -- which could used by a sphinx-doc generator
    extension -- and a commandline interface, see ``--help``::

        $ ./kernel_doc.py --help

    About the rewrite:

      The rewrite has additional features like *parse options* (see below) for a
      smooth integration of restructuredText (reST) markup in the kernel's
      source code comments. In addition, this rewrite brings the
      functionalities, which has been spread in *docproc* and make files
      (e.g. working with *EXPORTED_SYMBOLS*) back to the kernel-doc parse
      process. In combination with a (separate) *kernel-doc* reST directive
      which uses this module, the documentation generation becomes much more
      clear and flexible.

    About reST integration into the kerne-doc markup:

      In general, the markup of the linux kernel's source code comments remains
      unchanged and the reST markup within the comments is passed through the
      output. A closer lookup to the *kernel-doc* and *reST* markup revals, that
      there are some conflicts between reST (inline) markup and kernel-doc
      markup. This conflicts could be handled fine grained with the *parse
      options*. Parse options are comments like: ``/* parse-{option-name}:
      {value} */``, examples about conflicts and *parse options* see below.

    As long as kernel's source code comments remain unchanged, the description
    *here* is mainly a copy of the kernel-doc origin, except for the additions
    which are decribed at the end.

    In the following examples,

    * ``(...)?`` signifies optional structure and
    * ``(...)*`` signifies 0 or more structure elements

    Format of comments.::

        /**
         * function_name(:)? (- short description)?
        (* @parameterx: (description of parameter x)?)*
        (* a blank line)?
         * (Description:)? (Description of function)?
         * (section header: (section description)? )*
         (*)?*/

    So, the trivial example would be::

        /**
         * my_function
         */

    If the Description: header tag is omitted, then there must be a blank line
    after the last parameter specification.::

        /**
         * my_function - does my stuff
         * @my_arg: its mine damnit
         *
         * Does my stuff explained.
         */

    or, could also use::

        /**
         * my_function - does my stuff
         * @my_arg: its mine damnit
         * Description: Does my stuff explained.
         */

    Besides functions you can also write documentation for ``structs``,
    ``unions``, ``enums`` and ``typedefs``. Instead of the function name you
    must write the name of the declaration; the struct / union / enum / typedef
    must always precede the name. Nesting of declarations is not supported.  Use
    the argument mechanism to document members or constants.::

        /**
         * struct my_struct - short description
         * @a: first member
         * @b: second member
         *
         * Longer description
         */
        struct my_struct {
            int a;
            int b;
        /* private: */
            int c;
        };

    All descriptions can be multiline, except the short function description.
    For really longs structs, you can also describe arguments inside the body of
    the struct.::

        /**
         * struct my_struct - short description
         * @a: first member
         * @b: second member
         *
         * Longer description
         */
        struct my_struct {
            int a;
            int b;
            /**
             * @c: This is longer description of C
             *
             * You can use paragraphs to describe arguments
             * using this method.
             */
            int c;
        };

    This should be used only for struct/enum members.

    You can also add additional sections. When documenting kernel functions you
    should document the ``Context:`` of the function, e.g. whether the functions
    can be called form interrupts. Unlike other sections you can end it with an
    empty line.

    A non-void function should have a ``Return:`` section describing the return
    value(s).  Example-sections should contain the string ``EXAMPLE`` so that
    they are marked appropriately in the output format.::

        /**
         * user_function - function that can only be called in user context
         * @a: some argument
         * Context: !in_interrupt()
         *
         * Some description
         *
         * Example:
         *    user_function(22);
         */

    All descriptive text is further processed, scanning for the following special
    patterns, which are highlighted appropriately.

    * ``funcname()``   - function
    * ``$ENVVAR``      - environmental variable
    * ``&struct_name`` - name of a structure (up to two words including ``struct``)
    * ``@parameter``   - name of a parameter
    * ``%CONST``       - name of a constant.

    With the following comment lines, highlighting could be switched on or off::

         /* parse-highlight: on */
         /* parse-highlight: off */

    In addition you could use the *plain-text markup* restructuredText (reST /
    http://www.sphinx-doc.org/rest.html) in the descriptive text, which will
    passed through.

    Determined by the historical development of the kernel-doc comments, the
    *classic* kernel-doc comments contain characters like ``*`` or strings with
    e.g. leading/trailing underscore (``_``), which are inline markups in
    reST. Here a schort example from a *classic* comment::

        <SNIP> -----
        * In contrast to the other drm_get_*_name functions this one here returns a
        * const pointer and hence is threadsafe.
        <SNAP> -----

    In reST markup, the wildcard in the string ``drm_get_*_name`` has to be
    masked: ``drm_get_\\*_name``. Some more examples from reST markup:

    * Emphasis "*":  like ``*emphasis*`` or ``**emphasis strong**``

    * Leading "_" :  is a *anchor* in reST markup (``_foo``).

    * Trailing "_:  is a reference in reST markup (``foo_``).

    * interpreted text: "`"

    * inline literals: "``"

    * substitution references: "|"

    These special strings will be masked in the output and can't be used as
    *plain-text markup*.  To get in use of the fully reST markup (stop masking
    special characters) add the following comment (e.g.) at the top of your
    source code file.::

       /* parse-markup: reST */

    To toggle back to *classic* kernel-doc behavior (masking special characters
    in the output) type the following line::

       /* parse-markup: kernel-doc */

    Additional hints for ``kernel-doc.py`` developers:

    If you like to inspect a selective part of the kernel's source comments, you
    could toggle the global ``INSPECT`` variable with::

       /* parse-INSPECT: on */
       /* parse-INSPECT: off */

    And with an additional *breakpoint* in the ``kernel_doc.py`` script::

        INSPECT and CONSOLE()

    a console for introspection pops up (see examples in kernel_doc.py sources).

"""

# ==============================================================================
# imports
# ==============================================================================

import sys, os, argparse, codecs, collections, textwrap
import re

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

# ==============================================================================
# regular expresssions and helper used by the parser and the translator
# ==============================================================================

class RE(object):
    u"""regexp that stores last match (like perl's ``=~`` operator)"""

    def __init__(self, *args, **kwargs):
        self.re = re.compile(*args, **kwargs)
        self.last_match = None

    def match(self, *args, **kwargs):
        self.last_match = self.re.match(*args, **kwargs)
        return self.last_match

    def search(self, *args, **kwargs):
        self.last_match = self.re.search(*args, **kwargs)
        return self.last_match

    def __getattr__(self, attr):
        return getattr(self.re, attr)

    def __getitem__(self, group):
        if group < 0 or group > self.groups - 1:
            raise IndexError("group index out of range (max %s groups)" % self.groups )
        if self.last_match is None:
            raise IndexError("nothing hase matched / no groups")
        return self.last_match.group(group + 1)

# these regular expresions has been *stolen* from the kernel-doc perl script.

doc_start        = RE(r"^/\*\*\s*$")  # Allow whitespace at end of comment start.
doc_end          = RE(r"\s*\*+/")
doc_com          = RE(r"\s*\*\s*")
doc_com_body     = RE(r"\s*\* ?")
doc_decl         = RE(doc_com.pattern + r"(\w+)")
doc_decl_ident   = RE(r"\s*([\w\s]+?)\s*[-:]")
doc_decl_purpose = RE(r"[-:](.*)$")

# except pattern like "http://", a whitespace is required after the colon
doc_sect_except  = RE(doc_com.pattern + r"(.*?):[^\s]")

#doc_sect = RE(doc_com.pattern + r"([" + doc_special.pattern + r"]?[\w\s]+):(.*)")
# "section header:" names must be unique per function (or struct,union, typedef,
# enum). Additional condition: the header name should have 3 characters at least!
doc_sect  = RE(doc_com.pattern
               + r"("
               + r"@\w[^:]*"                                 # "@foo: lorem" or
               + r"|" + r"\@\.\.\."                          # ellipsis "@...: lorem" or
               + r"|" + r"\w[\w\s]+\w"                       # e.g. "Return: lorem"
               + r")"
               + r":(.*?)\s*$")   # this matches also strings like "http://..." (doc_sect_except)

doc_sect_reST = RE(doc_com.pattern
               + r"("
               + r"@\w[^:]*"                                 # "@foo: lorem" or
               + r"|" + r"\@\.\.\."                          # ellipsis "@...: lorem" or
               # a tribute to vintage markups, when in reST mode ...
               + r"|description|context|returns?|notes?|examples?|introduction|intro"
               + r")"
               + r":(.*?)\s*$"    # this matches also strings like "http://..." (doc_sect_except)
               , flags = re.IGNORECASE)

reST_sect = RE(doc_com.pattern
               + r"("
               r"\w[\w\s]+\w"
               + r")"
               + r":\s*$")

doc_content      = RE(doc_com_body.pattern + r"(.*)")
doc_block        = RE(doc_com.pattern + r"DOC:\s*(.*)?")

# state: 5 - gathering documentation outside main block
doc_state5_start = RE(r"^\s*/\*\*\s*$")
doc_state5_sect  = RE(r"\s*\*\s*(@[\w\s]+):(.*)")
doc_state5_end   = RE(r"^\s*\*/\s*$")

# match expressions used to find embedded type information
type_enum_full    = RE(r"(?<!\\)\&(enum)\s*([_\w]+)")
type_struct_full  = RE(r"(?<!\\)\&(struct)\s*([_\w]+)")
type_typedef_full = RE(r"(?<!\\)\&(typedef)\s*([_\w]+)")
type_union_full   = RE(r"(?<!\\)\&(union)\s*([_\w]+)")
type_member       = RE(r"(?<!\\)\&([_\w]+)((\.|->)[_\w]+)")
type_member_func  = RE(type_member.pattern + r"\(\)")
type_func         = RE(r"(\w+)(?<!\\)\(\)")
type_constant     = RE(r"(?<!\\)\%([-_\w]+)")
type_param        = RE(r"(?<!\\)\@(\w+)")
type_env          = RE(r"(?<!\\)(\$\w+)")
type_struct       = RE(r"(?<!\\)\&((struct\s*)*[_\w]+)")

esc_type_prefix  = RE(r"\\([\@\%\&\$\(])")

CR_NL            = RE(r"[\r\n]")
C99_comments     = RE(r"//.*$")
C89_comments     = RE(r"/\*.*?\*/")

C_STRUCT         = RE(r"struct\s+(\w+)\s*{(.*)}")
C_UNION          = RE(r"union\s+(\w+)\s*{(.*)}")
C_STRUCT_UNION   = RE(r"(struct|union)\s+(\w+)\s*{(.*)}")
C_ENUM           = RE(r"enum\s+(\w+)\s*{(.*)}")
C_TYPEDEF        = RE(r"typedef.*\s+(\w+)\s*;")

# typedef of a function pointer
C_FUNC_TYPEDEF   = RE(r"typedef\s+(\w+)\s*\(\*\s*(\w\S+)\s*\)\s*\((.*)\);")

MACRO            = RE(r"^#")
MACRO_define     = RE(r"^#\s*define\s+")

SYSCALL_DEFINE   = RE(r"^\s*SYSCALL_DEFINE.*\(")
SYSCALL_DEFINE0  = RE(r"^\s*SYSCALL_DEFINE0")

TP_PROTO                 = RE(r"TP_PROTO\((.*?)\)")
TRACE_EVENT              = RE(r"TRACE_EVENT")
TRACE_EVENT_name         = RE(r"TRACE_EVENT\((.*?),")
DEFINE_EVENT             = RE(r"DEFINE_EVENT")
DEFINE_EVENT_name        = RE(r"DEFINE_EVENT\((.*?),(.*?),")
DEFINE_SINGLE_EVENT      = RE(r"DEFINE_SINGLE_EVENT")
DEFINE_SINGLE_EVENT_name = RE(r"DEFINE_SINGLE_EVENT\((.*?),")

FUNC_PROTOTYPES = [
    # RE(r"^(\w+)\s+\(\*([a-zA-Z0-9_]+)\)\s*\(([^\(]*)\)") # match: void (*foo) (int bar);
    RE(r"^()([a-zA-Z0-9_~:]+)\s*\(([^\(]*)\)")
    , RE(r"^(\w+)\s+([a-zA-Z0-9_~:]+)\s*\(([^\(]*)\)")
    , RE(r"^(\w+\s*\*)\s*([a-zA-Z0-9_~:]+)\s*\(([^\(]*)\)")
    , RE(r"^(\w+\s+\w+)\s+([a-zA-Z0-9_~:]+)\s*\(([^\(]*)\)")
    , RE(r"^(\w+\s+\w+\s*\*+)\s*([a-zA-Z0-9_~:]+)\s*\(([^\(]*)\)")
    , RE(r"^(\w+\s+\w+\s+\w+)\s+([a-zA-Z0-9_~:]+)\s*\(([^\(]*)\)")
    , RE(r"^(\w+\s+\w+\s+\w+\s*\*)\s*([a-zA-Z0-9_~:]+)\s*\(([^\(]*)\)")
    , RE(r"^()([a-zA-Z0-9_~:]+)\s*\(([^\{]*)\)")
    , RE(r"^(\w+)\s+([a-zA-Z0-9_~:]+)\s*\(([^\{]*)\)")
    , RE(r"^(\w+\s*\*)\s*([a-zA-Z0-9_~:]+)\s*\(([^\{]*)\)")
    , RE(r"^(\w+\s+\w+)\s+([a-zA-Z0-9_~:]+)\s*\(([^\{]*)\)")
    , RE(r"^(\w+\s+\w+\s*\*)\s*([a-zA-Z0-9_~:]+)\s*\(([^\{]*)\)")
    , RE(r"^(\w+\s+\w+\s+\w+)\s+([a-zA-Z0-9_~:]+)\s*\(([^\{]*)\)")
    , RE(r"^(\w+\s+\w+\s+\w+\s*\*)\s*([a-zA-Z0-9_~:]+)\s*\(([^\{]*)\)")
    , RE(r"^(\w+\s+\w+\s+\w+\s+\w+)\s+([a-zA-Z0-9_~:]+)\s*\(([^\{]*)\)")
    , RE(r"^(\w+\s+\w+\s+\w+\s+\w+\s*\*)\s*([a-zA-Z0-9_~:]+)\s*\(([^\{]*)\)")
    , RE(r"^(\w+\s+\w+\s*\*\s*\w+\s*\*\s*)\s*([a-zA-Z0-9_~:]+)\s*\(([^\{]*)\)/")
]

EXPORTED_SYMBOLS = RE(
    r"^\s*(EXPORT_SYMBOL)(_GPL)?(_FUTURE)?\s*\(\s*(\w*)\s*\)\s*", flags=re.M)

# MODULE_AUTHOR("..."); /  MODULE_DESCRIPTION("..."); / MODULE_LICENSE("...");
#
MODULE_INFO = RE(r'^\s*(MODULE_)(AUTHOR|DESCRIPTION|LICENSE)\s*\(\s*"([^"]+)"', flags=re.M)

WHITESPACE = RE(r"\s+", flags=re.UNICODE)

def normalize_ws(string):
    u"""strip needles whitespaces.

    Substitute consecutive whitespaces with one single space and strip
    trailing/leading whitespaces"""

    string = WHITESPACE.sub(" ", string)
    return string.strip()

ID_CHARS = RE(r"[^A-Za-z0-9\._]")

def normalize_id(ID):
    u"""substitude invalid chars of the ID with ``-`` and mak it lowercase"""
    return ID_CHARS.sub("-", ID).lower()

def map_text(text, map_table):
    for regexpr, substitute in map_table:
        if substitute is not None:
            text = regexpr.sub(substitute, text)
    return text

# ==============================================================================
# helper
# ==============================================================================

def openTextFile(fname, mode="r", encoding="utf-8", errors="strict", buffering=1):
    return codecs.open(
        fname, mode=mode, encoding=encoding
        , errors=errors, buffering=buffering)

def readFile(fname, encoding="utf-8", errors="strict"):
    with openTextFile(fname, encoding=encoding, errors=errors) as f:
        return f.read()

class Container(dict):
    # pylint: disable=C0321
    @property
    def __dict__(self):               return self
    def __getattr__(self, attr):      return self[attr]
    def __setattr__(self, attr, val): self[attr] = val

class OS_ENV(dict):
    # pylint: disable=C0321
    @property
    def __dict__(self):                return os.environ
    def __getattr__(self, attr):       return os.environ[attr]
    def __setattr__(self, attr, val):  os.environ[attr] = val
    def get(self, attr, default=None): return os.environ.get(attr, default)

OS_ENV = OS_ENV()

KBUILD_VERBOSE = int(OS_ENV.get("KBUILD_VERBOSE", "0"))
KERNELVERSION  = OS_ENV.get("KERNELVERSION", "unknown kernel version")
SRCTREE        = OS_ENV.get("srctree", "")
GIT_REF        = "Linux kernel source tree: `%(rel_fname)s <https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/%(rel_fname)s>`_"

# ==============================================================================
# Logging stuff
# ==============================================================================

STREAM = Container(
    # pipes used by the application & logger
    appl_out   = sys.__stdout__
    , log_out  = sys.__stderr__
    , )

VERBOSE = bool(KBUILD_VERBOSE)
DEBUG   = False
INSPECT = False
QUIET   = False

class SimpleLog(object):

    LOG_FORMAT = "%(logclass)s: %(message)s\n"

    def error(self, message, **replace):
        message = message % replace
        replace.update(dict(message = message, logclass = "ERROR"))
        STREAM.log_out.write(self.LOG_FORMAT % replace)

    def warn(self, message, **replace):
        if QUIET:
            return
        message = message % replace
        replace.update(dict(message = message, logclass = "WARN"))
        STREAM.log_out.write(self.LOG_FORMAT % replace)

    def info(self, message, **replace):
        if not VERBOSE:
            return
        message = message % replace
        replace.update(dict(message = message, logclass = "INFO"))
        STREAM.log_out.write(self.LOG_FORMAT % replace)

    def debug(self, message, **replace):
        if not DEBUG:
            return
        message = message % replace
        replace.update(dict(message = message, logclass = "DEBUG"))
        STREAM.log_out.write(self.LOG_FORMAT % replace)

LOG = SimpleLog()

# ==============================================================================
def main():
# ==============================================================================

    global VERBOSE, DEBUG # pylint: disable=W0603

    CLI = argparse.ArgumentParser(
        description = (
            "Parse *kernel-doc* comments from source code"
            " and print them (with reST markup) to stdout." )
        , formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    CLI.add_argument(
        "files"
        , nargs   = "+"
        , help    = "source file(s) to parse.")

    CLI.add_argument(
        "--id-prefix"
        , default = ""
        , help    = (
            "A prefix for generated IDs. IDs are used as anchors by cross"
            " references. They are automaticly gernerated based on the declaration"
            " and / or section names. Declartions like 'open' or section names"
            " like 'Intro' are very common, to make them unique, a prefix is needed."
            " Mostly you will choose the *module* or *include filename* as prefix." ))

    CLI.add_argument(
        "--verbose", "-v"
        , action  = "store_true"
        , help    = "verbose output with log messages to stderr" )

    CLI.add_argument(
        "--debug"
        , action  = "store_true"
        , help    = "debug messages to stderr" )

    CLI.add_argument(
        "--skip-preamble"
        , action  = "store_true"
        , help    = "skip preamble in the output" )

    CLI.add_argument(
        "--skip-epilog"
        , action  = "store_true"
        , help    = "skip epilog in the output" )

    CLI.add_argument(
        "--list-internals"
        , choices = Parser.DOC_TYPES + ["all"]
        , nargs   = "+"
        , help    = "list symbols, titles or whatever is documented, but *not* exported" )

    CLI.add_argument(
        "--list-exports"
        , action  = "store_true"
        , help    = "list all symbols exported using EXPORT_SYMBOL" )

    CLI.add_argument(
        "--use-names"
        , nargs   = "+"
        , help    = "print documentation of functions, structs or whatever title/object")

    CLI.add_argument(
        "--exported"
        , action  = "store_true"
        , help    = ("print documentation of all symbols exported"
                     " using EXPORT_SYMBOL macros" ))

    CLI.add_argument(
         "--internal"
        , action  = "store_true"
        , help    = ("print documentation of all symbols that are documented,"
                     " but not exported" ))


    CMD     = CLI.parse_args()
    VERBOSE = CMD.verbose
    DEBUG   = CMD.debug

    LOG.debug(u"CMD: %(CMD)s", CMD=CMD)

    retVal     = 0

    for fname in CMD.files:
        opts = ParseOptions(
            fname           = fname
            , id_prefix     = CMD.id_prefix
            , skip_preamble = CMD.skip_preamble
            , skip_epilog   = CMD.skip_epilog
            , out           = STREAM.appl_out
            , translator    = ReSTTranslator()
            ,)
        opts.set_defaults()

        if CMD.list_exports or CMD.list_internals:
            opts.gather_context = True
            opts.translator     = ListTranslator(CMD.list_exports, CMD.list_internals)

        elif CMD.use_names:
            opts.use_names  = CMD.use_names

        elif CMD.exported or CMD.internal:
            # gather exported symbols ...
            src   = readFile(opts.fname)
            ctx   = ParserContext()
            Parser.gather_context(src, ctx)

            opts.translator    = ReSTTranslator()
            opts.error_missing = False
            opts.use_names     = ctx.exported_symbols
            opts.skip_names    = []

            if CMD.internal:
                opts.use_names  = []
                opts.skip_names = ctx.exported_symbols

        parser = Parser(opts)
        parser.parse()
        if parser.errors:
            retVal = 1

    return retVal

# ==============================================================================
# API
# ==============================================================================

# ------------------------------------------------------------------------------
class TranslatorAPI(object):
# ------------------------------------------------------------------------------
    u"""
    Abstract kernel-doc translator.

    :cvar list HIGHLIGHT_MAP:  highlight mapping
    :cvar tuple LINE_COMMENT:  tuple with start-/end- comment tags
    """

    HIGHLIGHT_MAP = [
        ( type_constant      , None )
        , ( type_func        , None )
        , ( type_param       , None )
        , ( type_struct_full , None )
        , ( type_struct      , None )
        , ( type_enum_full   , None )
        , ( type_env         , None )
        , ( type_member_func , None )
        , ( type_member      , None )
        , ]

    LINE_COMMENT = ("# ", "")

    def __init__(self):
        self.options = None
        self.parser  = None

    def setParser(self, parser):
        self.options = parser.options
        self.parser = parser

    def highlight(self, cont):
        u"""returns *highlighted* text"""
        if self.options.highlight:
            return map_text(cont, self.HIGHLIGHT_MAP)
        return cont

    @classmethod
    def comment(cls, cont):
        u"""returns *commented* text"""

        start, end = cls.LINE_COMMENT
        if not start and not end:
            return cont

        retVal = []
        for line in cont.split("\n"):
            if line.strip():
                retVal.append(start + line + end)
            else:
                retVal.append("")
        return "\n".join(retVal)

    def write(self, *objects):
        u"""Write *objects* to stream.

        Write unicode-values of the *objects* to :py:attr:``self.options.out``.

        :param *objects: The positional arguments are the objects with the
            content to write.
        """
        for obj in objects:
            cont = unicode(obj)
            self.options.out.write(cont)

    def write_comment(self, *objects):
        u"""Write *objects* as comments to stream."""
        for obj in objects:
            cont = unicode(obj)
            self.write(self.comment(cont))

    def eof(self):
        if self.options.eof_newline:
            self.write("\n")

    # API
    # ---

    def output_preamble(self):
        raise NotImplementedError

    def output_epilog(self):
        raise NotImplementedError

    def output_doc_section(
            self
            , sections         = None # ctx.sections
            , ):
        raise NotImplementedError

    def output_function_decl(
            self
            , function         = None # ctx.decl_name
            , return_type      = None # ctx.return_type
            , parameterlist    = None # ctx.parameterlist
            , parameterdescs   = None # ctx.parameterdescs
            , parametertypes   = None # ctx.parametertypes
            , sections         = None # ctx.sections
            , purpose          = None # ctx.decl_purpose
            , ):
        raise NotImplementedError

    def output_struct_decl(
            self
            , decl_name        = None # ctx.decl_name
            , decl_type        = None # ctx.decl_type
            , parameterlist    = None # ctx.parameterlist
            , parameterdescs   = None # ctx.parameterdescs
            , parametertypes   = None # ctx.parametertypes
            , sections         = None # ctx.sections
            , purpose          = None # ctx.decl_purpose
            , ):
        raise NotImplementedError

    def output_union_decl(self, *args, **kwargs):
        self.output_struct_decl(*args, **kwargs)

    def output_enum_decl(
            self
            , enum             = None # ctx.decl_name
            , parameterlist    = None # ctx.parameterlist
            , parameterdescs   = None # ctx.parameterdescs
            , sections         = None # ctx.sections
            , purpose          = None # ctx.decl_purpose
            , ):
        raise NotImplementedError

    def output_typedef_decl(
            self
            , typedef          = None # ctx.decl_name
            , sections         = None # ctx.sections
            , purpose          = None # ctx.decl_purpose
            , ):
        raise NotImplementedError

# ------------------------------------------------------------------------------
class NullTranslator(object):
# ------------------------------------------------------------------------------
    u"""
    Null translator, translates nothing, just parse.
    """
    HIGHLIGHT_MAP = []
    LINE_COMMENT = ("", "")
    # pylint: disable=C0321
    def output_preamble(self, *args, **kwargs):      pass
    def output_epilog(self, *args, **kwargs):        pass
    def output_doc_section(self, *args, **kwargs):   pass
    def output_function_decl(self, *args, **kwargs): pass
    def output_struct_decl(self, *args, **kwargs):   pass
    def output_union_decl(self, *args, **kwargs):    pass
    def output_enum_decl(self, *args, **kwargs):     pass
    def output_typedef_decl(self, *args, **kwargs):  pass

# ------------------------------------------------------------------------------
class ListTranslator(TranslatorAPI):
# ------------------------------------------------------------------------------

    u"""
    Generates a list of kernel-doc symbols.
    """

    def __init__(self, list_exported, list_internal_types
                 , *args, **kwargs):
        super(ListTranslator, self).__init__(*args, **kwargs)

        self.list_exported       = list_exported
        self.list_internal_types = list_internal_types

        self.names = dict()
        for t in Parser.DOC_TYPES:
            self.names[t] = []

    def get_type(self, name):
        for t, l in self.names.items():
            if name in l:
                return t
        return None

    def output_preamble(self):
        pass

    def output_epilog(self):
        pass

    def output_doc_section(self, sections = None):
        for header in sections.keys():
            self.names["DOC"].append(header)

    def output_function_decl(self, **kwargs):
        self.names["function"].append(kwargs["function"])

    def output_struct_decl(self, **kwargs):
        self.names["struct"].append(kwargs["decl_name"])

    def output_union_decl(self, **kwargs):
        self.names["union"].append(kwargs["decl_name"])

    def output_enum_decl(self, **kwargs):
        self.names["enum"].append(kwargs["enum"])

    def output_typedef_decl(self, **kwargs):
        self.names["typedef"].append(kwargs["typedef"])

    def eof(self):

        if self.list_exported:
            self.parser.info("list exported symbols")
            for name in self.parser.ctx.exported_symbols:
                t = self.get_type(name)
                if t is None:
                    self.parser.warn("exported symbol '%(name)s' is undocumented"
                                     , name = name)
                    t = "undocumented"
                self.write("[exported %-10s] %s \n" % (t, name))

        if self.list_internal_types:
            self.parser.info("list internal names")
            for t, l in self.names.items():
                if not ("all" in self.list_internal_types
                        or t in self.list_internal_types):
                    continue
                for name in l:
                    if name not in self.parser.ctx.exported_symbols:
                        self.write("[internal %-10s] %s \n" % (t, name))

# ------------------------------------------------------------------------------
class ReSTTranslator(TranslatorAPI):
# ------------------------------------------------------------------------------

    u"""
    Translate kernel-doc to reST markup.

    :cvar list HIGHLIGHT_map: Escape common reST (inline) markups.  Classic
        kernel-doc comments contain characters and strings like ``*`` or
        trailing ``_``, which are inline markups in reST. These special strings
        has to be masked in reST.

    """
    INDENT       = "    "
    LINE_COMMENT = (".. ", "")

    HIGHLIGHT_MAP = [
        # the regexpr are partial *overlapping*, mind the order!
        (   type_enum_full   , r"\ :c:type:`\1 \2 <\2>`\ " )
        , ( type_struct_full , r"\ :c:type:`\1 \2 <\2>`\ " )
        , ( type_typedef_full, r"\ :c:type:`\1 \2 <\2>`\ " )
        , ( type_union_full  , r"\ :c:type:`\1 \2 <\2>`\ " )
        , ( type_member_func , r"\ :c:type:`\1\2() <\1>`\ " )
        , ( type_member      , r"\ :c:type:`\1\2 <\1>`\ " )
        , ( type_func        , r"\ :c:func:`\1`\ ")
        , ( type_constant    , r"\ ``\1``\ " )
        , ( type_param       , r"\ ``\1``\ " )
        , ( type_env         , r"\ ``\1``\ " )
        , ( type_struct      , r"\ :c:type:`struct \1 <\1>`")
        # at least replace escaped %, & and $
        , ( esc_type_prefix  , r"\1")
        , ]

    MASK_REST_INLINES = [
        (RE(r"(\*)")        , r"\\\1")  # emphasis
        , (RE(r"(`)")       , r"\\\1")  # interpreted text & inline literals
        , (RE(r"(_\s)")     , r"\\\1")  # trailing underline
        , (RE(r"(\s)_(\w)") , r"\1_\2") # leading underline
        , (RE(r"(\|)")      , r"\\\1")  # substitution references
        , ]

    FUNC_PTR = RE(r"([^\(]*\(\*)\s*\)\s*\(([^\)]*)\)")
    BITFIELD = RE(r"^(.*?)\s*(:.*)")

    def highlight(self, text):
        if self.options.markup == "kernel-doc":
            text = map_text(text, self.MASK_REST_INLINES + self.HIGHLIGHT_MAP )
        elif self.options.markup == "reST":
            text = map_text(text, self.HIGHLIGHT_MAP )
        return text

    def format_block(self, content):
        u"""format the content (string)"""
        lines = []
        if self.options.markup == "kernel-doc":
            lines = [ l.strip() for l in content.split("\n")]
        elif self.options.markup == "reST":
            lines = [ l.rstrip() for l in content.split("\n")]
        return "\n".join(lines)

    def write_anchor(self, refname):
        ID = refname
        if self.options.id_prefix:
            ID = self.options.id_prefix + "." + ID
        ID = normalize_id(ID)
        self.write("\n.. _`%s`:\n" % ID)

    HEADER_TAGS = (
        "#"   # level 0 / part with overline
        "="   # level 1 / chapter with overline
        "="   # level 2 / sec
        "-"   # level 3 / subsec
        "-"   # level 4 / subsubsec
        '"' ) # level 5 / para

    def write_header(self, header, sec_level=2):
        header = self.highlight(header)
        sectag = self.HEADER_TAGS[sec_level]
        if sec_level < 2:
            self.write("\n", (sectag * len(header)))
        self.write("\n%s" % header)
        self.write("\n", (sectag * len(header)), "\n")

    def write_section(self, header, content, sec_level=2, ID=None):
        if not self.options.no_header:
            if ID:
                self.write_anchor(ID)
            self.write_header(header, sec_level=sec_level)
        if (header.lower() == "example"):
            self.write("\n.. code-block:: c\n\n")
            for l in textwrap.dedent(content).split("\n"):
                if not l.strip():
                    self.write("\n")
                else:
                    self.write(self.INDENT, l, "\n")
        else:
            content = self.format_block(content)
            content = self.highlight(content)
            self.write("\n" + content)

        self.write("\n")

    def write_definition(self, term, definition, prefix=""):
        term  = normalize_ws(term) # term has to be a "one-liner"
        term  = self.highlight(term)
        if definition != Parser.undescribed:
            definition = self.format_block(definition)
            definition = self.highlight(definition)
        self.write("\n", prefix, term)
        for l in textwrap.dedent(definition).split("\n"):
            self.write("\n", prefix)
            if l.strip():
                self.write(self.INDENT, l)
        self.write("\n")

    def write_func_param(self, param, descr):
        param = self.highlight(param)
        self.write("\n", self.INDENT, param)

        if descr != Parser.undescribed:
            descr = self.format_block(descr)
            descr = self.highlight(descr)
        for l in textwrap.dedent(descr).split("\n"):
            self.write("\n")
            if l.strip():
                self.write(self.INDENT * 2, l)
        self.write("\n")

    def output_preamble(self):
        if self.options.mode_line:
            self.write_comment(
                "-*- coding: %s; mode: rst -*-\n"
                % (getattr(self.options.out, "encoding", "utf-8") or "utf-8").lower())

        if self.options.preamble:
            self.write(self.options.preamble, "\n")

        if self.options.top_title:
            self.write_anchor(self.options.top_title)
            self.write_header(self.options.top_title, 0)
            if self.options.top_link:
                self.write("\n", self.options.top_link % self.options, "\n")

    def output_epilog(self):
        if self.options.epilog is not None:
            self.write(self.options.epilog)

    def output_doc_section(self, sections = None):
        for header, content in sections.items():
            self.write_section(header, content, sec_level=2, ID=header)

    def output_function_decl(
            self
            , function         = None # ctx.decl_name
            , return_type      = None # ctx.return_type
            , parameterlist    = None # ctx.parameterlist
            , parameterdescs   = None # ctx.parameterdescs
            , parametertypes   = None # ctx.parametertypes
            , sections         = None # ctx.sections
            , purpose          = None # ctx.decl_purpose
            , ):
        self.write_anchor(function)
        self.write_header(function, sec_level=2)

        # write function definition

        self.write("\n.. c:function:: ")
        if return_type and return_type.endswith("*"):
            self.write(return_type, function, "(")
        else:
            self.write(return_type, " ", function, "(")

        p_list = []

        for p_name in parameterlist:
            p_type = parametertypes[p_name]

            if self.FUNC_PTR.search(p_type):
                # pointer to function
                p_list.append("%s) %s (%s"
                              % (self.FUNC_PTR[0], p_name, self.FUNC_PTR[1]))
            elif p_type.endswith("*"):
                # pointer
                p_list.append("%s%s" % (p_type, p_name))
            else:
                p_list.append("%s %s" % (p_type, p_name))

        self.write(", ".join(p_list), ")\n")

        # purpose

        if purpose:
            self.write("\n", self.INDENT, self.highlight(purpose), "\n")

        # parameter descriptions

        for p_name in parameterlist:

            p_type = parametertypes[p_name]
            p_name = re.sub(r"\[.*", "", p_name)
            p_desc = parameterdescs[p_name]

            param = ""
            if self.FUNC_PTR.search(p_type):
                # pointer to function
                param = ":param (%s) %s (%s):" % (self.FUNC_PTR[0], p_name, self.FUNC_PTR[1])
            elif p_type.endswith("*"):
                # pointer & pointer to pointer
                param = ":param %s%s:" % (p_type, p_name)
            elif p_name == "...":
                param = ":param %s :" % (p_name)
            else:
                param = ":param %s %s:" % (p_type, p_name)

            self.write_func_param(param, p_desc)

        # sections

        for header, content in sections.items():
            self.write_section(
                header
                , content
                , sec_level = 3
                , ID = function + "." + header)

        # INSPECT and CONSOLE() # pylint: disable=W0106

    def output_struct_decl(
            self
            , decl_name        = None # ctx.decl_name
            , decl_type        = None # ctx.decl_type
            , parameterlist    = None # ctx.parameterlist
            , parameterdescs   = None # ctx.parameterdescs
            , parametertypes   = None # ctx.parametertypes
            , sections         = None # ctx.sections
            , purpose          = None # ctx.decl_purpose
            , ):
        self.write_anchor(decl_name)
        self.write_header("%s %s" % (decl_type, decl_name), sec_level=2)

        # write struct definition

        self.write("\n.. c:type:: %s\n\n" % decl_name)

        # purpose

        if purpose:
            self.write(self.INDENT, self.highlight(purpose), "\n")

        # definition

        self.write_anchor(decl_name + "." + Parser.section_def)
        self.write_header(Parser.section_def, sec_level=3)
        self.write("\n.. code-block:: c\n\n")
        self.write(self.INDENT, decl_type, " ", decl_name, " {\n")

        for p_name in parameterlist:
            p_type = parametertypes[p_name]

            if MACRO.match(p_name):
                self.write(self.INDENT * 2, "%s\n" % p_name)

            elif self.FUNC_PTR.search(p_type):
                # pointer to function
                self.write(
                    self.INDENT * 2
                    , "%s %s) (%s);\n" % (self.FUNC_PTR[0], p_name, self.FUNC_PTR[1]))

            elif self.BITFIELD.match(p_type):
                self.write(
                    self.INDENT * 2
                    , "%s %s%s;\n" % (self.BITFIELD[0], p_name, self.BITFIELD[1]))
            elif p_type.endswith("*"):
                # pointer
                self.write(
                    self.INDENT * 2
                    , "%s%s;\n" % (p_type, p_name))

            else:
                self.write(
                    self.INDENT * 2
                    , "%s %s;\n" % (p_type, p_name))

        self.write(self.INDENT, "}\n")

        # member description

        self.write_anchor(decl_name + "." + Parser.section_members)
        self.write_header(Parser.section_members, sec_level=3)

        for p_name in parameterlist:
            if MACRO.match(p_name):
                continue
            p_name = re.sub(r"\[.*", "", p_name)
            p_desc = parameterdescs.get(p_name, None)
            if p_desc is None:
                continue
            self.write_definition(p_name, p_desc)

        # sections

        for header, content in sections.items():
            self.write_section(
                header
                , content
                , sec_level = 3
                , ID = decl_name + "." + header)

        # INSPECT and CONSOLE() # pylint: disable=W0106

    def output_enum_decl(
            self
            , enum             = None # ctx.decl_name
            , parameterlist    = None # ctx.parameterlist
            , parameterdescs   = None # ctx.parameterdescs
            , sections         = None # ctx.sections
            , purpose          = None # ctx.decl_purpose
            , ):
        self.write_anchor(enum)
        self.write_header("enum %s" % enum, sec_level=2)

        # write union definition

        self.write("\n.. c:type:: %s\n\n" % enum)

        # purpose

        if purpose:
            self.write(self.INDENT, self.highlight(purpose), "\n")

        # definition

        self.write_anchor(enum + "." + Parser.section_def)
        self.write_header(Parser.section_def, sec_level=3)
        self.write("\n.. code-block:: c\n\n")
        self.write(self.INDENT, "enum ", enum, " {")

        e_list = parameterlist[:]
        while e_list:
            e = e_list.pop(0)
            self.write("\n", self.INDENT *2, e)
            if e_list:
                self.write(",")
        self.write("\n", self.INDENT, "};\n")

        # constants description

        self.write_anchor(enum + "." + Parser.section_constants)
        self.write_header(Parser.section_constants, sec_level=3)

        for p_name in parameterlist:
            p_desc = parameterdescs.get(p_name, None)
            if p_desc is None:
                continue
            self.write_definition(p_name, p_desc)

        # sections

        for header, content in sections.items():
            self.write_section(
                header
                , content or "???"
                , sec_level = 3
                , ID = enum + "." + header)

        # INSPECT and CONSOLE() # pylint: disable=W0106

    def output_typedef_decl(
            self
            , typedef          = None # ctx.decl_name
            , sections         = None # ctx.sections
            , purpose          = None # ctx.decl_purpose
            , ):
        self.write_anchor(typedef)
        self.write_header("typedef %s" % typedef, sec_level=2)

        # write typdef definition

        self.write("\n.. c:type:: %s\n\n" % typedef)
        if purpose:
            self.write(self.INDENT, self.highlight(purpose), "\n")

        for header, content in sections.items():
            self.write_section(
                header
                , content or "???"
                , sec_level = 3
                , ID = typedef + "." + header)

        # INSPECT and CONSOLE() # pylint: disable=W0106


# ------------------------------------------------------------------------------
class ParseOptions(Container):
# ------------------------------------------------------------------------------

    PARSE_OPTION_RE = r"^/\*+\s*parse-%s:\s*([a-zA-Z0-9_-]*?)\s*\*/+\s*$"
    PARSE_OPTIONS   = [
        ("highlight", ["on","off"], "setOnOff")
        , ("INSPECT", ["on","off"], "setINSPECT")
        , ("markup",  ["reST", "kernel-doc"], "setVal")
        , ("SNIP",    [], "setVal")
        , ("SNAP",    [], "snap")
        , ]

    def __init__(self, *args, **kwargs):

        self.id_prefix      = None  # A prefix for generated IDs.
        self.out            = None  # File descriptor for output.
        self.eof_newline    = True  # write newline on end of file
        self.translator     = None  # Translator object.

        self.src_tree       = SRCTREE # root of the kernel sources
        self.rel_fname      = ""      # pathname relative to src_tree
        self.fname          = ""      # absolute pathname

        # self.encoding: the input encoding (encoding of the parsed source
        # file), the output encoding could be seeked from the file-descriptor at
        # self.out.

        self.encoding       = "utf-8"

        # control which content to print

        self.use_names     = []    # positiv list of names to print / empty list means "print all"
        self.skip_names    = []    # negativ list of names (not to print)
        self.no_header     = False # skip section header
        self.error_missing = True  # report missing names as errors / else warning
        self.verbose_warn  = True  # more warn messages

        # self.gather_context: [True/False] Scan additional context from the
        # parsed source. E.g.: The list of exported symbols is a part of the
        # parser's context. If the context of exported symbols is needed, we
        # have to parse twice. First to find exported symbols, store them in the
        # context and a second once for *normal* parsing within this modified
        # *context*.

        self.gather_context    = False

        # epilog / preamble

        self.skip_preamble  = False
        self.skip_epilog    = False
        self.mode_line      = True  # write mode-line in the very first line
        self.top_title      = ""    # write a title on top of the preamble
        self.top_link       = ""    # if top_title, add link to the *top* of the preamble
        self.preamble       = ""    # additional text placed into the preamble
        self.epilog         = ""    # text placed into the epilog

        # default's of filtered PARSE_OPTIONS

        self.opt_filters    = dict()
        self.markup         = "reST"
        self.highlight      = True  # switch highlighting on/off
        self.add_filters(self.PARSE_OPTIONS)

        # SNIP / SNAP
        self.SNIP = None

        super(ParseOptions, self).__init__(self, *args, **kwargs)

        # absolute and relativ filename

        if self.src_tree and self.fname and os.path.isabs(self.fname):
            # if SCRTREE and abspath fname is given, determine relativ pathname
            self.rel_fname = os.path.relpath(self.fname, self.src_tree)

        if self.src_tree and self.fname and not os.path.isabs(self.fname):
            # if SCRTREE and relative fname is given, drop fname and set rel_fname
            self.rel_fname = self.fname
            self.fname = ""

        if self.src_tree and self.rel_fname:
            self.fname = os.path.join(self.src_tree, self.rel_fname)
        else:
            LOG.warn("no relative pathname given / no SRCTREE: "
                     " features based on these settings might not work"
                     " as expected!")
        if not self.fname:
            LOG.error("no source file given!")

    def set_defaults(self):

        # default top title and top link

        if self.fname and self.top_title == "":
            self.top_title = os.path.basename(self.fname)
        if self.top_title:
            self.top_title = self.top_title % self

        if self.top_link == "":
            if self.rel_fname:
                self.top_link  = GIT_REF % self
            else:
                LOG.warn("missing SRCTREE, can't set *top_link* option")
        if self.top_link:
            self.top_link = self.top_link % self

        # default preamble

        if self.preamble == "":
            self.preamble = self.translator.comment("src-file: %s" % (self.rel_fname or self.fname))
        if self.preamble:
            self.preamble = self.preamble % self

        # default epilog

        if self.epilog == "":
            self.epilog = self.translator.comment(
                "\nThis file was automatic generated / don't edit.")
        if self.epilog:
            self.epilog = self.epilog % self

    def add_filters(self, parse_options):

        # pylint: disable=W0613, W0603

        def setINSPECT(name, val):
            global INSPECT
            INSPECT = bool(val == "on")

        _actions = dict(
            setOnOff     = lambda name, val: ( name, bool(val == "on") )
            , setVal     = lambda name, val: ( name, val )
            , snap       = lambda name, val: ( "SNIP", "" )
            , setINSPECT = setINSPECT
            , )

        for option, val_list, action in parse_options:
            self.opt_filters[option] = (
                RE(self.PARSE_OPTION_RE % option), val_list, _actions[action])

    def filter_opt(self, line, parser):

        for name, (regexpr, val_list, action) in self.opt_filters.items():
            if regexpr.match(line):
                line  = None
                value = regexpr[0]
                if val_list and value not in val_list:
                    parser.error("unknown parse-%(name)s value: '%(value)s'"
                               , name=name, value=value)
                else:
                    opt_val = action(name, value)
                    if opt_val  is not None:
                        name, value = opt_val
                        self[name]  = value
                    parser.info(
                        "set parse-option: %(name)s = '%(value)s'"
                        , name=name, value=value)
                break
        return line

# ------------------------------------------------------------------------------
class ParserContext(Container):
# ------------------------------------------------------------------------------

    def __init__(self, *args, **kwargs):
        self.line_no           = 0

        self.contents          = ""
        self.section           = Parser.section_default

        # self.sections: ordered dictionary (list) of sections as they appear in
        # the source. The sections are set by Parser.dump_section
        self.sections          = collections.OrderedDict()
        self.sectcheck         = []

        self.prototype         = ""

        # self.parameterlist: ordered list of the parameters as they appear in
        # the source. The parameterlist is set by Parser.push_parameter and
        # Parser.dump_enum
        self.parameterlist     = []

        # self.parametertypes: dictionary of <parameter-name>:<type>
        # key/values of the parameters. Set by Parser.push_parameter
        self.parametertypes    = dict()

        # self.parameterdescs: dictionary of <'@parameter'>:<description>
        # key/values of the parameters. Set by Parser.dump_section
        self.parameterdescs    = dict()

        # self.constants: dictionary of <'%CONST'>:<description>
        # key/values. Set by Parser.dump_section
        self.constants         = dict()

        self.decl_name         = ""
        self.decl_type         = ""  # [struct|union|enum|typedef|function]
        self.decl_purpose      = ""
        self.return_type       = ""

        # record ranslated names
        self.translated_names  = []

        #self.struct_actual     = ""

        # Additional context from the parsed source

        # self.exported: list of exported symbols
        self.exported_symbols  = []

        # self.mod_xxx: Module informations
        self.mod_authors       = []
        self.mod_descr         = ""
        self.mod_license       = ""

        # SNIP / SNAP
        self.snippets  = collections.OrderedDict()

        super(ParserContext, self).__init__(self, *args, **kwargs)

    def new(self):
        return self.__class__(
            line_no            = self.line_no
            , exported_symbols = self.exported_symbols
            , translated_names = self.translated_names
            , snippets         = self.snippets )


class ParserBuggy(RuntimeError):
    u"""Exception raised when the parser implementation seems buggy.

    The parser implementation perform some integrity tests at runtime.  This
    exception type mainly exitst to improve the regualar expressions which are
    used to parse and analyze the kernels source code.

    In the exception message the last position the parser parsed is stored, this
    positon may, but does not need to be related with the exception (it is only
    an additional information which might help).

    Under normal circumstances, exceptions of this type should never arise,
    unless the implementation of the parser is buggy."""

    def __init__(self, parserObj, message):

        message = ("last parse position %s:%s\n"
                   % (parserObj.ctx.line_no, parserObj.options.fname)
                   + message)
        super(ParserBuggy, self).__init__(message)
        self.parserObj = parserObj

# ------------------------------------------------------------------------------
class Parser(SimpleLog):
# ------------------------------------------------------------------------------

    u"""
    kernel-doc comments parser

    States:

    * 0 - normal code
    * 1 - looking for function name
    * 2 - scanning field start.
    * 3 - scanning prototype.
    * 4 - documentation block
    * 5 - gathering documentation outside main block (see Split Doc State)

    Split Doc States:

    * 0 - Invalid (Before start or after finish)
    * 1 - Is started (the /** was found inside a struct)
    * 2 - The @parameter header was found, start accepting multi paragraph text.
    * 3 - Finished (the */ was found)
    * 4 - Error: Comment without header was found. Spit a error as it's not
          proper kernel-doc and ignore the rest.
    """

    LOG_FORMAT = "%(fname)s:%(line_no)s :%(logclass)s: %(message)s\n"

    # DOC_TYPES: types of documentation gathered by the parser
    DOC_TYPES      = ["DOC", "function", "struct", "union", "enum", "typedef"]

    undescribed      = "*undescribed*"

    section_descr     = "Description"
    section_def       = "Definition"
    section_members   = "Members"
    section_constants = "Constants"
    section_intro     = "Introduction"
    section_context   = "Context"
    section_return    = "Return"
    section_default   = section_descr

    def __init__(self, parse_options):
        super(Parser, self).__init__()
        self.options = parse_options
        self.ctx     = ParserContext()

        self.translator = self.options.translator
        self.translator.setParser(self)

        # raw data akku
        self.rawdata    = ""

        # flags:
        self.state = 0
        self.split_doc_state   = 0
        self.in_intro          = True
        self.in_doc_sect       = False
        self.in_purpose        = False
        self.brcount           = 0
        self.warnings          = 0
        self.errors            = 0
        self.anon_struct_union = False

    def reset_state(self):
        self.ctx = self.ctx.new()
        self.state             = 0
        self.split_doc_state   = 0
        self.in_doc_sect       = False
        self.in_purpose        = False
        self.brcount           = 0
        self.anon_struct_union = False

    # ------------------------------------------------------------
    # Log
    # ------------------------------------------------------------

    def error(self, message, **replace):
        replace.update(dict(fname=self.options.fname, line_no=self.ctx.line_no))
        self.errors += 1
        super(Parser, self).error(message, **replace)

    def warn(self, message, **replace):
        replace.update(dict(fname=self.options.fname, line_no=self.ctx.line_no))
        self.warnings += 1
        super(Parser, self).warn(message, **replace)

    def info(self, message, **replace):
        replace.update(dict(fname=self.options.fname, line_no=self.ctx.line_no))
        super(Parser, self).info(message, **replace)

    def debug(self, message, **replace):
        replace.update(dict(fname=self.options.fname, line_no=self.ctx.line_no))
        super(Parser, self).debug(message, **replace)

    # ------------------------------------------------------------
    # state parser
    # ------------------------------------------------------------

    def parse(self, src=None):
        if src is not None:
            for line in src:
                self.feed(line)
        else:
            with openTextFile(self.options.fname, encoding=self.options.encoding) as src:
                for line in src:
                    self.feed(line)
        self.close()

    @classmethod
    def gather_context(cls, src, ctx):
        u"""Scan source about context informations.

        Scans *whole* source (e.g. :py:attr:`Parser.rawdata`) about data relevant
        for the context (e.g. exported symbols).

        Names of exported symbols gathered in :py:attr:`ParserContext.exported`.
        The list contains names (symbols) which are exported using the
        EXPORT_SYMBOL macro.

        * ``EXPORT_SYMBOL(<name>)``
        * ``EXPORT_SYMBOL_GPL(<name>)``
        * ``EXPORT_SYMBOL_GPL_FUTURE(<name>)``)

        .. hint::

          A exported symbol does not necessarily have a corresponding source code
          comment with a documentation.

        Module information comes from the ``MODULE_xxx`` macros.  Module
        informations are gathered in ``ParserContext.module_xxx``:

        * ``MODULE_AUTHOR("...")``: Author entries are collected in a list in
          :py:attr:`ParserContext.mod_authors`

        * ``MODULE_DESCRIPTION("...")``: A concatenated string in
          :py:attr:`ParserContext.mod_descr`

        * ``MODULE_LICENSE``("..."): String with comma seprated licences in
          :py:attr:`ParserContext.mod_license`.

        .. hint::

           While parsing header files, about kernel-doc, you will not find the
           ``MODULE_xxx`` macros, because they are commonly used in the ".c"
           files.
        """

        LOG.debug("gather_context() regExp: %(pattern)s", pattern=EXPORTED_SYMBOLS.pattern)
        for match in EXPORTED_SYMBOLS.findall(src):
            name = match[3]
            LOG.info("exported symbol: %(name)s", name = name)
            ctx.exported_symbols.append(name)

        LOG.debug("gather_context() regExp: %(pattern)s", pattern=MODULE_INFO.pattern)

        for match in MODULE_INFO.findall(src):
            info_type = match[1]
            content   = match[2]
            if info_type == "AUTHOR":
                ctx.mod_authors.append(content)
            elif info_type == "DESCRIPTION":
                ctx.mod_descr   += content + " "
            elif info_type == "LICENSE":
                ctx.mod_license += content + ", "

        LOG.info("mod_authors: %(x)s",  x = ctx.mod_authors)
        LOG.info("mod_descr: %(x)s",    x = ctx.mod_descr)
        LOG.info("mod_license : %(x)s", x = ctx.mod_license)

    def close(self):
        self._parse(eof=True)

    def feed(self, data):
        self.rawdata = self.rawdata + data
        self._parse()

    def _parse(self, eof=False):

        if self.options.gather_context:
            # Scan additional context from the parsed source. For this, collect
            # all lines in self.rawdata until EOF. On EOF, scan rawdata about
            # (e.g.) exported symbols and after this, continue with the *normal*
            # parsing.
            if not eof:
                return
            else:
                self.gather_context(self.rawdata, self.ctx)

        lines = self.rawdata.split("\n")

        if not eof:
            # keep last line, until EOF
            self.rawdata = lines[-1]
            lines = lines[:-1]

        if self.in_intro:
            self.dump_preamble()
            self.in_intro = False

        for l in lines:
            self.ctx.line_no += 1
            l = self.options.filter_opt(l, self)
            if l is None:
                continue

            if self.options.SNIP:
                # record snippet
                val = self.ctx.snippets.get(self.options.SNIP, "")
                if val or l:
                    self.ctx.snippets[self.options.SNIP] = val + l + "\n"

            state = getattr(self, "state_%s" % self.state)
            try:
                state(l)
            except Exception:
                self.warn("total errors: %(errors)s / warnings: %(warnings)s"
                           , errors=self.errors, warnings=self.warnings)
                self.warnings -= 1
                self.error("unhandled exception in line: %(l)s", l=l)
                raise

        if eof:
            self.dump_epilog()
            self.translator.eof()

            # log requested but missed documentation
            log_missed = self.error
            if not self.options.error_missing:
                log_missed = self.warn

            for name in self.options.use_names:
                if name not in self.ctx.translated_names:
                    log_missed("no documentation for '%(name)s' found", name=name)

            if self.errors or self.warnings:
                self.warn("total errors: %(errors)s / total warnings: %(warnings)s"
                          , errors=self.errors, warnings=self.warnings)
                self.warnings -= 1
            global INSPECT
            INSPECT = False

    def state_0(self, line):
        u"""state: 0 - normal code"""

        if doc_start.match(line):
            self.debug("START: kernel-doc comment / switch state 0 --> 1")
            self.state = 1
            self.in_doc_sect = False

    def state_1(self, line):
        u"""state: 1 - looking for function name"""

        if doc_block.match(line):
            self.debug("START: DOC block / switch state 1 --> 4")
            self.state = 4
            self.ctx.contents = ""
            self.ctx.section =  self.section_intro
            if doc_block[0].strip():
                self.ctx.section = self.sect_title(doc_block[0])
            self.info("DOC: %(sect)s", sect=self.ctx.section)

        elif doc_decl.match(line):
            self.debug("START: declaration / switch state 1 --> 2")
            self.state = 2

            identifier = doc_decl[0].strip()
            if doc_decl_ident.search(line):
                identifier = doc_decl_ident[0]

            self.ctx.decl_type = "function"
            for t in ["struct", "union", "enum", "typedef"]:
                if identifier.startswith(t):
                    self.ctx.decl_type = t
                    break

            self.debug("FLAG: in_purpose=True")
            self.in_purpose = True

            self.info("scanning doc for: %(t)s '%(i)s'", t=self.ctx.decl_type, i = identifier)

            self.ctx.decl_purpose = ""
            if doc_decl_purpose.search(line):
                self.ctx.decl_purpose = doc_decl_purpose[0].strip()

            if not self.ctx.decl_purpose:
                self.warn("missing initial short description of '%(i)s' on line -->|%(line)s|<--"
                          , i=identifier, line=line)


        else:
            self.warn("can't understand: -->|%(line)s|<--"
                      " - I thought it was a doc line" , line=line)
            self.state = 0

    def sect_title(self, title):
        u"""Normalize common section titles"""
        # fix varius notations for the "Return:" section

        retVal = title

        if title.lower() in ["description", ]:
            retVal = self.section_descr

        elif title.lower() in ["introduction", "intro"]:
            retVal = self.section_intro

        elif title.lower() in ["context", ]:
            retVal = self.section_context

        elif title.lower() in ["return", "returns"]:
            retVal = self.section_return

        return retVal

    def state_2(self, line):
        u"""state: 2 - scanning field start. """

        new_sect = ""
        new_cont = ""

        if not doc_sect_except.match(line):

            # probe different sect start pattern ...

            if self.options.markup == "reST":
                if doc_sect_reST.match(line):
                    # this is a line with a parameter definition or vintage
                    # section "Context: lorem", "Return: lorem" etc.
                    new_sect = self.sect_title(doc_sect_reST[0].strip())
                    new_cont = doc_sect_reST[1].strip()
                elif reST_sect.match(line):
                    # this is a line with a section definition "Section name:\n"
                    new_sect = self.sect_title(reST_sect[0].strip())
                    new_cont = ""
            else:  # kernel-doc vintage mode
                if doc_sect.match(line):
                    # this is a line with a parameter or section definition
                    new_sect = self.sect_title(doc_sect[0].strip())
                    new_cont = doc_sect[1].strip()

        if new_sect:

            # a new section starts *here*

            self.debug("found new section --> %(sect)s", sect=new_sect)

            if self.ctx.contents.strip():
                if not self.in_doc_sect:
                    self.warn("contents before sections '%(c)s'" , c=self.ctx.contents.strip())
                self.dump_section(self.ctx.section, self.ctx.contents)
                self.ctx.section  = self.section_default
                self.ctx.contents = ""

            self.debug("new_sect: '%(sec)s' / desc: '%(desc)s'", sec = new_sect, desc = new_cont)

            self.in_doc_sect = True
            self.in_purpose  = False
            self.debug("FLAGs: in_doc_sect=%(s)s / in_purpose=%(p)s", s=self.in_doc_sect, p=self.in_purpose)

            self.ctx.section  = new_sect
            if new_cont:
                self.ctx.contents = new_cont + "\n"
            self.info("section: %(sec)s" , sec=self.ctx.section)

        elif doc_end.match(line):

            # end of the comment-block

            if self.ctx.contents:
                self.dump_section(self.ctx.section, self.ctx.contents)
                self.ctx.section  = self.section_default
                self.ctx.contents = ""

            # look for doc_com + <text> + doc_end:
            if RE(doc_com.pattern + r"[a-zA-Z_0-9:\.]+" + doc_end.pattern).match(line):
                self.warn("suspicious ending line")

            self.ctx.prototype = ""
            self.debug("END doc block / switch state 2 --> 3")
            self.debug("end of doc comment, looking for prototype")
            self.state   = 3
            self.brcount = 0

        elif doc_content.match(line):

            # a comment line with *content* of a section or a *purpose*

            cont_line = doc_content[0]

            if not cont_line.strip():

                if self.in_purpose:

                    # empty line after short description (*purpose*) introduce the
                    # "Description" section

                    self.debug("found empty line in *purpose* --> start 'Description' section")
                    if self.ctx.contents.strip():
                        if not self.in_doc_sect:
                            self.warn("contents before sections '%(c)s'" , c=self.ctx.contents.strip())
                        self.dump_section(self.ctx.section, self.ctx.contents)
                    self.ctx.section  = self.section_descr
                    self.ctx.contents = ""
                    self.in_doc_sect  = True
                    self.in_purpose   = False
                    self.debug("FLAGs: in_doc_sect=%(s)s / in_purpose=%(p)s", s=self.in_doc_sect, p=self.in_purpose)

                elif (self.ctx.section.startswith("@")
                      or self.ctx.section == self.section_context):

                    # miguel-style comment kludge, look for blank lines after @parameter
                    # line to signify start of description

                    self.debug("blank lines after @parameter --> start 'Description' section")
                    self.dump_section(self.ctx.section, self.ctx.contents)
                    self.ctx.section  = self.section_descr
                    self.ctx.contents = ""
                    self.in_doc_sect  = True
                    self.debug("FLAGs: in_doc_sect=%(s)s / in_purpose=%(p)s", s=self.in_doc_sect, p=self.in_purpose)

                else:
                    self.ctx.contents += "\n"

            elif self.in_purpose:
                # Continued declaration purpose, dismiss leading whitespace
                if self.ctx.decl_purpose:
                    self.ctx.decl_purpose += " " + cont_line.strip()
                else:
                    self.ctx.decl_purpose = cont_line.strip()
            else:
                self.ctx.contents += cont_line + "\n"

        else:
            # i dont know - bad line?  ignore.
            self.warn("bad line: '%(line)s'", line = line.strip())

    def state_3(self, line):
        u"""state: 3 - scanning prototype."""

        if doc_state5_start.match(line):
            self.debug("FLAG: split_doc_state=1 / switch state 3 --> 5")
            self.state = 5
            self.split_doc_state = 1
            if self.ctx.decl_type == 'function':
                self.error("odd construct, gathering documentation of a function"
                           " outside of the main block?!?")

        elif self.ctx.decl_type == 'function':
            self.process_state3_function(line)
        else:
            self.process_state3_type(line)

    def state_4(self, line):
        u"""state: 4 - documentation block"""

        if doc_block.match(line):
            # a new DOC block arrived, dump the last section and pass the new
            # DOC block to state 1.
            self.dump_doc_section(self.ctx.section, self.ctx.contents)
            self.ctx = self.ctx.new()
            self.debug("END & START: DOC block / switch state 4 --> 1")
            self.state = 1
            self.state_1(line)

        elif doc_end.match(line):
            # the DOC block ends here, dump it and reset to state 0
            self.debug("END: DOC block / dump doc section / switch state 4 --> 0")
            self.dump_doc_section(self.ctx.section, self.ctx.contents)
            self.ctx = self.ctx.new()
            self.state = 0

        elif doc_content.match(line):
            cont = doc_content[0]
            if (not cont.strip() # dismiss leading newlines
                and not self.ctx.contents):
                pass
            else:
                self.ctx.contents += doc_content[0] + "\n"

    def state_5(self, line):
        u"""state: 5 - gathering documentation outside main block"""

        if (self.split_doc_state == 1
            and doc_state5_sect.match(line)):

            # First line (split_doc_state 1) needs to be a @parameter
            self.ctx.section  = self.sect_title(doc_state5_sect[0].strip())
            self.ctx.contents = doc_state5_sect[1].strip()
            self.split_doc_state = 2
            self.debug("SPLIT-DOC-START: '%(param)s' / split-state 1 --> 2"
                       , param = self.ctx.section)
            self.info("section: %(sec)s" , sec=self.ctx.section)

        elif doc_state5_end.match(line):
            # Documentation block end
            self.debug("SPLIT-DOC-END: ...")

            if not self.ctx.contents.strip():
                self.debug("SPLIT-DOC-END: ... no description to dump")

            else:
                self.dump_section(self.ctx.section, self.ctx.contents)
                self.ctx.section  = self.section_default
                self.ctx.contents = ""

            self.debug("SPLIT-DOC-END: ... split-state --> 0  / state = 3")
            self.state = 3
            self.split_doc_state = 0

        elif doc_content.match(line):
            # Regular text
            if self.split_doc_state == 2:
                self.ctx.contents += doc_content[0] + "\n"

            elif self.split_doc_state == 1:
                self.split_doc_state = 4
                self.error("Comment without header was found split-state --> 4")
                self.warn("Incorrect use of kernel-doc format: %(line)s"
                          , line = line)

    # ------------------------------------------------------------
    # helper to parse special objects
    # ------------------------------------------------------------

    def process_state3_function(self, line):

        self.debug("PROCESS-FUNCTION: %(line)s", line=line)
        line = C99_comments.sub("", line) # strip C99-style comments to end of line
        line = line.strip()

        stripProto = RE(r"([^\{]*)")

        # ?!?!? MACDOC does not (no more?) exists
        # if ($x =~ m#\s*/\*\s+MACDOC\s*#io || ($x =~ /^#/ && $x !~ /^#\s*define/)) {
        #   do nothing
        # }

        if line.startswith("#") and not MACRO_define.search(line):
            # do nothing
            pass
        elif stripProto.match(line):
            self.ctx.prototype += " " + stripProto[0]

        if (MACRO_define.search(line)
            or "{" in line
            or ";" in line ):

            # strip cr&nl, strip C89 comments, strip leading whitespaces
            self.ctx.prototype = C89_comments.sub(
                "", CR_NL.sub(" ", self.ctx.prototype)).lstrip()

            if SYSCALL_DEFINE.search(self.ctx.prototype):
                self.ctx.prototype = self.syscall_munge(self.ctx.prototype)

            if (TRACE_EVENT.search(line)
                or DEFINE_EVENT.search(line)
                or DEFINE_SINGLE_EVENT.search(line) ):
                self.ctx.prototype = self.tracepoint_munge(self.ctx.prototype)

            self.ctx.prototype = self.ctx.prototype.strip()
            self.info("prototype --> '%(proto)s'", proto=self.ctx.prototype)
            self.dump_function(self.ctx.prototype)
            self.reset_state()

    def syscall_munge(self, prototype):
        self.debug("syscall munge: '%(prototype)s'" , prototype=prototype)
        void = False

        # strip needles whitespaces
        prototype = normalize_ws(prototype)

        if SYSCALL_DEFINE0.search(prototype):
            void = True
        prototype = SYSCALL_DEFINE.sub("long sys_", prototype)

        if re.search(r"long (sys_.*?),", prototype):
            prototype = prototype.replace(",", "(", 1)
        elif void:
            prototype = prototype.replace(")","(void)",1)

        # now delete all of the odd-number commas in $prototype
        # so that arg types & arg names don't have a comma between them

        retVal = prototype
        if not void:
            x = prototype.split(",")
            y = []
            while x:
                y.append(x.pop(0) + x.pop(0))
            retVal = ",".join(y)
        self.debug("syscall munge: retVal '%(retVal)s'" , retVal=retVal)
        return retVal

    def tracepoint_munge(self, prototype):
        self.debug("tracepoint munge: %(prototype)s" , prototype=prototype)

        retVal  = prototype
        tp_name = ""
        tp_args = ""

        if TRACE_EVENT_name.match(prototype):
            tp_name = TRACE_EVENT_name[0]

        elif DEFINE_SINGLE_EVENT_name.match(prototype):
            tp_name = DEFINE_SINGLE_EVENT_name[0]

        elif DEFINE_EVENT_name.match(prototype):
            tp_name = DEFINE_EVENT_name[1]

        tp_name = tp_name.lstrip()

        if TP_PROTO.match(prototype):
            tp_args = TP_PROTO[0]

        if not (tp_name.strip() and tp_args.strip()):
            self.warn("Unrecognized tracepoint format: %(prototype)s"
                      , prototype=prototype)
        else:
            retVal = ("static inline void trace_%s(%s)"
                      % (tp_name, tp_args))
        return retVal

    def process_state3_type(self, line):
        self.debug("PROCESS-TYPE: %(line)s", line=line)

        # strip cr&nl, strip C99 comments, strip leading&trailing whitespaces
        line = C99_comments.sub("", CR_NL.sub(" ", line)).strip()

        if MACRO.match(line):
            # To distinguish preprocessor directive from regular declaration
            # later.
            line += ";"

        m = RE(r"([^{};]*)([{};])(.*)")

        while True:
            if m.search(line):
                self.ctx.prototype += m[0] + m[1]
                if m[1] == "{":
                    self.brcount += 1
                if m[1] == "}":
                    self.brcount -= 1
                if m[1] == ";" and self.brcount == 0:
                    self.info("prototype --> '%(proto)s'", proto=self.ctx.prototype)
                    self.debug("decl_type: %(decl_type)s", decl_type=self.ctx.decl_type)
                    if self.ctx.decl_type == "union":
                        self.dump_union(self.ctx.prototype)
                    elif self.ctx.decl_type == "struct":
                        self.dump_struct(self.ctx.prototype)
                    elif self.ctx.decl_type == "enum":
                        self.dump_enum(self.ctx.prototype)
                    elif self.ctx.decl_type == "typedef":
                        self.dump_typedef(self.ctx.prototype)
                    else:
                        raise ParserBuggy(
                            self, "unknown decl_type: %s" % self.ctx.decl_type)

                    self.reset_state()
                    break
                line = m[2]
            else:
                self.ctx.prototype += line
                break

    # ------------------------------------------------------------
    # selective translation
    # ------------------------------------------------------------

    def mark_as_translated(self, name):
        u"""Test if content should be translated"""
        retVal = False
        if name in self.options.skip_names:
            retVal = False
        elif not self.options.use_names:
            retVal = True
        elif name in self.options.use_names:
            retVal = True
        if retVal:
            self.ctx.translated_names.append(name)
        return retVal

    # ------------------------------------------------------------
    # dump objects
    # ------------------------------------------------------------

    def dump_preamble(self):
        if not self.options.skip_preamble:
            self.translator.output_preamble()

    def dump_epilog(self):
        if not self.options.skip_epilog:
            self.translator.output_epilog()

    def dump_section(self, name, cont):
        u"""Store section's *content* under it's name.

        :param str name: name of the section
        :param str cont: content of the section

        Stores the *content* under section's *name* in one of the *container*. A
        container is a hash object, the section name is the *key* and the
        content is the *value*.

        Container:

        * self.ctx.constants:       holds constant's descriptions
        * self.ctx.parameterdescs:  holds parameter's descriptions
        * self.ctx.sections:        holds common sections like "Return:"

        There are the following contai
        """
        self.debug("dump_section(): %(name)s", name = name)
        name = name.strip()
        cont = cont.rstrip() # dismiss trailing whitespace
        if type_constant.match(name):  # '%CONST' - name of a constant.
            name = type_constant[0]
            self.debug("constant section '%(name)s'",  name = name)
            if self.ctx.constants.get(name, None):
                self.error("duplicate constant definition '%(name)s'"
                           , name = name)
            self.ctx.constants[name] = cont

        elif type_param.match(name):   # '@parameter' - name of a parameter
            name = type_param[0]
            self.debug("parameter definition '%(name)s'", name = name)
            if self.ctx.parameterdescs.get(name, None):
                self.error("duplicate parameter definition '%(name)s'", name = name)
            self.ctx.parameterdescs[name] = cont
            self.ctx.sectcheck.append(name)

        elif name == "@...":
            self.debug("parameter definiton '...'")
            name = "..."
            if self.ctx.parameterdescs.get(name, None):
                self.error("parameter definiton '...'")
            self.ctx.parameterdescs[name] = cont
            self.ctx.sectcheck.append(name)
        else:
            self.debug("other section '%(name)s'", name = name)
            if self.ctx.sections.get(name, None):
                self.warn("duplicate section name '%(name)s'", name = name)
                self.ctx.sections[name] += "\n\n" + cont
            else:
                self.ctx.sections[name] = cont

    def dump_function(self, proto):
        self.debug("dump_function(): (1) '%(proto)s'", proto=proto)
        hasRetVal = True
        proto = re.sub( r"^static +"         , "", proto )
        proto = re.sub( r"^extern +"         , "", proto )
        proto = re.sub( r"^asmlinkage +"     , "", proto )
        proto = re.sub( r"^inline +"         , "", proto )
        proto = re.sub( r"^__inline__ +"     , "", proto )
        proto = re.sub( r"^__inline +"       , "", proto )
        proto = re.sub( r"^__always_inline +", "", proto )
        proto = re.sub( r"^noinline +"       , "", proto )
        proto = re.sub( r"__init +"          , "", proto )
        proto = re.sub( r"__init_or_module +", "", proto )
        proto = re.sub( r"__meminit +"       , "", proto )
        proto = re.sub( r"__must_check +"    , "", proto )
        proto = re.sub( r"__weak +"          , "", proto )

        define = bool(MACRO_define.match(proto))
        proto = MACRO_define.sub("", proto )

        proto = re.sub( r"__attribute__\s*\(\([a-z,]*\)\)" , "", proto )

        # Yes, this truly is vile.  We are looking for:
        # 1. Return type (may be nothing if we're looking at a macro)
        # 2. Function name
        # 3. Function parameters.
        #
        # All the while we have to watch out for function pointer parameters
        # (which IIRC is what the two sections are for), C types (these
        # regexps don't even start to express all the possibilities), and
        # so on.
        #
        # If you mess with these regexps, it's a good idea to check that
        # the following functions' documentation still comes out right:
        # - parport_register_device (function pointer parameters)
        # - atomic_set (macro)
        # - pci_match_device, __copy_to_user (long return type)

        self.debug("dump_function(): (2) '%(proto)s'", proto=proto)

        x = RE(r"^()([a-zA-Z0-9_~:]+)\s+")

        if define and x.match(proto):
            # This is an object-like macro, it has no return type and no
            # parameter list.  Function-like macros are not allowed to have
            # spaces between decl_name and opening parenthesis (notice
            # the \s+).
            self.ctx.return_type = x[0]
            self.ctx.decl_name   = x[1]
            hasRetVal = False
            self.debug("dump_function(): (hasRetVal = False) '%(proto)s'"
                       , proto=proto)
        else:
            matchExpr = None
            for regexp in FUNC_PROTOTYPES:
                if regexp.match(proto):
                    matchExpr = regexp
                    self.debug("dump_function(): (matchExpr = %(pattern)s) '%(proto)s'"
                               , pattern = matchExpr.pattern, proto=proto)
                    break

            if matchExpr is not None:
                self.debug("dump_function(): return_type='%(x)s'", x=matchExpr[0])
                self.ctx.return_type = matchExpr[0]
                self.debug("dump_function(): decl_name='%(x)s'", x=matchExpr[1])
                self.ctx.decl_name   = matchExpr[1]
                self.create_parameterlist(matchExpr[2], ",")
            else:
                self.warn("can't understand function proto: '%(prototype)s'"
                          , **self.ctx)
                return

        self.check_sections(self.ctx.decl_name
                            , self.ctx.decl_type
                            , self.ctx.sectcheck
                            , self.ctx.parameterlist
                            , "")
        if hasRetVal:
            self.check_return_section(self.ctx.decl_name, self.ctx.return_type)

        if self.mark_as_translated(self.ctx.decl_name):
            self.translator.output_function_decl(
                function           = self.ctx.decl_name
                , return_type      = self.ctx.return_type
                , parameterlist    = self.ctx.parameterlist
                , parameterdescs   = self.ctx.parameterdescs
                , parametertypes   = self.ctx.parametertypes
                , sections         = self.ctx.sections
                , purpose          = self.ctx.decl_purpose )
        else:
            self.debug("skip translation of %(t)s: '%(n)s'"
                       , t=self.ctx.decl_type, n=self.ctx.decl_name)

    def dump_doc_section(self, name, cont):
        if self.mark_as_translated(name):
            self.dump_section(name, cont)
            self.translator.output_doc_section(sections=self.ctx.sections)
        else:
            self.debug("skip translation of DOC: '%(n)s'", n=name)

    def dump_union(self, proto):
        if not self.prepare_struct_union(proto):
            self.error("can't parse union!")
            return

        if self.mark_as_translated(self.ctx.decl_name):
            self.translator.output_union_decl(
                decl_name          = self.ctx.decl_name
                , decl_type        = self.ctx.decl_type
                , parameterlist    = self.ctx.parameterlist
                , parameterdescs   = self.ctx.parameterdescs
                , parametertypes   = self.ctx.parametertypes
                , sections         = self.ctx.sections
                , purpose          = self.ctx.decl_purpose )
        else:
            self.debug("skip translation of %(t)s: '%(n)s'"
                       , t=self.ctx.decl_type, n=self.ctx.decl_name)

    def dump_struct(self, proto):
        if not self.prepare_struct_union(proto):
            self.error("can't parse struct!")
            return

        if self.mark_as_translated(self.ctx.decl_name):
            self.translator.output_struct_decl(
                decl_name          = self.ctx.decl_name
                , decl_type        = self.ctx.decl_type
                , parameterlist    = self.ctx.parameterlist
                , parameterdescs   = self.ctx.parameterdescs
                , parametertypes   = self.ctx.parametertypes
                , sections         = self.ctx.sections
                , purpose          = self.ctx.decl_purpose )
        else:
            self.debug("skip translation of %(t)s: '%(n)s'"
                       , t=self.ctx.decl_type, n=self.ctx.decl_name)

    def prepare_struct_union(self, proto):
        self.debug("prepare_struct_union(): '%(proto)s'", proto=proto)

        retVal  = False
        members = ""
        nested  = ""

        if C_STRUCT_UNION.match(proto):

            if C_STRUCT_UNION[0] != self.ctx.decl_type:
                self.error("determine of decl_type is inconsistent: '%s' <--> '%s'"
                           "\nprototype: %s"
                           % (C_STRUCT_UNION[0], self.ctx.decl_type, proto))
                return False

            self.ctx.decl_name = C_STRUCT_UNION[1]
            members = C_STRUCT_UNION[2]

            # ignore embedded structs or unions
            embeded_re = RE(r"({.*})")
            if embeded_re.search(proto):
                nested  = embeded_re[0]
                members = embeded_re.sub("", members)

            # ignore members marked private:
            members = re.sub(r"/\*\s*private:.*?/\*\s*public:.*?\*/", "", members, flags=re.I)
            members = re.sub(r"/\*\s*private:.*", "", members, flags=re.I)

            # strip comments:
            members = C89_comments.sub("", members)
            nested  = C89_comments.sub("", nested)

            # strip kmemcheck_bitfield_{begin,end}.*;
            members =  re.sub(r"kmemcheck_bitfield_.*?;", "", members)

            # strip attributes
            members = re.sub(r"__attribute__\s*\(\([a-z,_\*\s\(\)]*\)\)", "", members, flags=re.I)
            members = re.sub(r"__aligned\s*\([^;]*\)", "", members)
            members = re.sub(r"\s*CRYPTO_MINALIGN_ATTR", "", members)

            # replace DECLARE_BITMAP
            members = re.sub(r"DECLARE_BITMAP\s*\(([^,)]+), ([^,)]+)\)"
                             , r"unsigned long \1\[BITS_TO_LONGS(\2)\]"
                             , members )

            self.create_parameterlist(members, ';')
            self.check_sections(self.ctx.decl_name
                                , self.ctx.decl_type
                                , self.ctx.sectcheck
                                , self.ctx.parameterlist # self.ctx.struct_actual.split(" ")
                                , nested)
            retVal = True

        else:
            retVal = False

        return retVal

    def dump_enum(self, proto):
        self.debug("dump_enum(): '%(proto)s'", proto=proto)

        proto = C89_comments.sub("", proto)
        # strip #define macros inside enums
        proto = re.sub(r"#\s*((define|ifdef)\s+|endif)[^;]*;", "", proto)

        splitchar = ","
        RE_NAME = RE(r"^\s*(\w+).*")

        if C_ENUM.search(proto):
            self.ctx.decl_name = C_ENUM[0]
            members = normalize_ws(C_ENUM[1])

            # drop trailing splitchar, if extists
            if members.endswith(splitchar):
                members = members[:-1]

            for member in members.split(splitchar):
                name = RE_NAME.sub(r"\1", member)
                self.ctx.parameterlist.append(name)
                if not self.ctx.parameterdescs.get(name, None):
                    self.warn(
                        "Enum value '%(name)s' not described"
                        " in enum '%(decl_name)s'"
                        , name = name,  decl_name=self.ctx.decl_name )
                    self.ctx.parameterdescs[name] = Parser.undescribed

            if self.mark_as_translated(self.ctx.decl_name):
                self.translator.output_enum_decl(
                    enum               = self.ctx.decl_name
                    , parameterlist    = self.ctx.parameterlist
                    , parameterdescs   = self.ctx.parameterdescs
                    , sections         = self.ctx.sections
                    , purpose          = self.ctx.decl_purpose )
            else:
                self.debug("skip translation of %(t)s: '%(n)s'"
                           , t=self.ctx.decl_type, n=self.ctx.decl_name)
        else:
            self.error("can't parse enum!")

    def dump_typedef(self, proto):
        self.debug("dump_typedef(): '%(proto)s'", proto=proto)

        proto = C89_comments.sub("", proto)

        if C_FUNC_TYPEDEF.search(proto):
            # Parse function prototypes

            self.ctx.return_type = C_FUNC_TYPEDEF[0]
            self.ctx.decl_name   = C_FUNC_TYPEDEF[1]
            self.check_return_section(self.ctx.decl_name, self.ctx.return_type)

            f_args = C_FUNC_TYPEDEF[2]
            self.create_parameterlist(f_args, ',')

            if self.mark_as_translated(self.ctx.decl_name):
                self.translator.output_function_decl(
                    function           = self.ctx.decl_name
                    , return_type      = self.ctx.return_type
                    , parameterlist    = self.ctx.parameterlist
                    , parameterdescs   = self.ctx.parameterdescs
                    , parametertypes   = self.ctx.parametertypes
                    , sections         = self.ctx.sections
                    , purpose          = self.ctx.decl_purpose)
            else:
                self.debug("skip translation of %(t)s: '%(n)s'"
                           , t=self.ctx.decl_type, n=self.ctx.decl_name)

        else:
            self.debug("dump_typedef(): '%(proto)s'", proto=proto)
            x1 = RE(r"\(*.\)\s*;$")
            x2 = RE(r"\[*.\]\s*;$")

            while x1.search(proto) or x2.search(proto):
                proto = x1.sub(";", proto)
                proto = x2.sub(";", proto)

            self.debug("dump_typedef(): '%(proto)s'", proto=proto)

            if C_TYPEDEF.match(proto):
                self.ctx.decl_name = C_TYPEDEF[0]

                if self.mark_as_translated(self.ctx.decl_name):
                    self.translator.output_typedef_decl(
                        typedef            = self.ctx.decl_name
                        , sections         = self.ctx.sections
                        , purpose          = self.ctx.decl_purpose )
                else:
                    self.debug("skip translation of %(t)s: '%(n)s'"
                               , t=self.ctx.decl_type, n=self.ctx.decl_name)
            else:
                self.error("can't parse typedef!")

    def create_parameterlist(self, parameter, splitchar):
        self.debug("create_parameterlist(): splitchar='%(x)s' params='%(y)s'"
                   , x=splitchar, y=parameter)
        parameter = normalize_ws(parameter)
        pointer_to_func = RE(r"\(.+\)\s*\(")

        # temporarily replace commas inside function pointer definition
        m = RE(r"(\([^\),]+),")

        while m.search(parameter):
            parameter = m.sub(r"\1#", parameter)
        # drop trailing splitchar, if extists
        if parameter.endswith(splitchar):
            parameter = parameter[:-1]

        for c, p in enumerate(parameter.split(splitchar)):

            p = C99_comments.sub("", p)
            p = p.strip()

            self.debug("  parameter#%(c)s: %(p)s", c=c, p=p)
            p_type = None
            p_name = None

            if MACRO.match(p):

                # Treat preprocessor directive as a typeless variable just to
                # fill corresponding data structures "correctly". Catch it later
                # in output_* subs.
                self.debug("  parameter#%(c)s: (MACRO) %(p)s=''" , c=c, p=p)
                self.push_parameter(p, "")

            elif pointer_to_func.search(p):

                # pointer-to-function
                p = p.replace("#", ",") # reinsert temporarily removed commas
                self.debug("  parameter#%(c)s: (pointer to function) %(p)s", c=c, p=p)
                m = RE(r"[^\(]+\(\*?\s*(\w*)\s*\)")
                m.match(p)
                p_name = m[0]
                p_type  = p
                p_type = re.sub(r"([^\(]+\(\*?)\s*"+p_name, r"\1", p_type)
                #self.save_struct_actual(p_name)
                self.push_parameter(p_name, p_type)

            else:
                p = re.sub(r"\s*:\s*", ":", p)
                p = re.sub(r"\s*\["  , "[", p)
                self.debug("  parameter#%(c)s: (common) %(p)s", c=c, p=p)

                p_args = re.split(r"\s*,\s*", p)
                if re.match(r"\s*,\s*", p_args[0]):
                    p_args[0] = re.sub(r"(\*+)\s*", r" \1", p_args[0])

                self.debug("  parameter#%(c)s : (1) p_args = %(p_args)s"
                           , c=c, p_args=repr(p_args))

                first_arg = []
                m = RE(r"^(.*\s+)(.*?\[.*\].*)$")
                if m.match(p_args[0]):
                    p_args.pop(0)
                    first_arg.extend(re.split(r"\s+", m[0]))
                    first_arg.append(m[1])
                else:
                    first_arg.extend(re.split(r"\s+", p_args.pop(0)))

                p_args = [first_arg.pop() ] + p_args
                self.debug("  parameter#%(c)s : (2) p_args=%(p_args)s"
                           , c=c, p_args=repr(p_args))
                p_type = " ".join(first_arg)

                ma = RE(r"^(\*+)\s*(.*)")
                mb = RE(r"(.*?):(\d+)")

                for p_name in p_args:
                    self.debug("  parameter#%(c)s : (3) p_name='%(p_name)s'"
                               , c=c, p_name=p_name)

                    if ma.match(p_name):
                        p_type = "%s %s" % (p_type, ma[0])
                        p_name = ma[1]

                    elif mb.match(p_name):
                        if p_type:  # skip unnamed bit-fields
                            p_name = mb[0]
                            p_type = "%s:%s" % (p_type, mb[1])

                    self.debug("  parameter#%(c)s : (4) p_name='%(p_name)s' / p_type='%(p_type)s'"
                               , c=c, p_name=p_name, p_type=p_type)
                    #self.save_struct_actual(p_name)
                    self.push_parameter(p_name, p_type)

    def push_parameter(self, p_name, p_type):
        self.debug(
            "push_parameter(): p_name='%(p_name)s' / p_type='%(p_type)s'"
            , p_name=p_name, p_type=p_type)

        p_name  = p_name.strip()
        p_type  = p_type.strip()

        if (self.anon_struct_union
            and not p_type
            and p_name == "}"):
            # ignore the ending }; from anon. struct/union
            return

        self.anon_struct_union = False

        self.debug(
            "push_parameter(): (1) p_name='%(p_name)s' / p_type='%(p_type)s'"
            , p_name=p_name, p_type=p_type)

        if not p_type and re.search(r"\.\.\.$", p_name):
            if not self.ctx.parameterdescs.get(p_name, None):
                self.ctx.parameterdescs[p_name] = "variable arguments"

        elif not p_type and (not p_name or p_name == "void"):
            p_name = "void"
            self.ctx.parameterdescs[p_name] = "no arguments"

        elif not p_type and (p_name == "struct" or p_name == "union"):
            # handle unnamed (anonymous) union or struct:
            p_type  = p_name
            p_name = "{unnamed_" + p_name + "}"
            self.ctx.parameterdescs[p_name] = "anonymous\n"
            self.anon_struct_union = True

        self.debug(
            "push_parameter(): (2) p_name='%(p_name)s' /  p_type='%(p_type)s'"
            , p_name=p_name, p_type=p_type)

        # strip array from paramater name / e.g. p_name is "modes[]" from a
        # parmeter defined by: "const char * const modes[]"

        p_name_doc = re.sub(r"\[.*", "", p_name)

        # warn if parameter has no description (but ignore ones starting with
        # '#' as these are not parameters but inline preprocessor statements);
        # also ignore unnamed structs/unions;

        if not self.anon_struct_union:

            if (not self.ctx.parameterdescs.get(p_name_doc, None)
                and not p_name.startswith("#")):

                if p_type == "function" or p_type == "enum":
                    self.warn("Function parameter or member '%(p_name)s' not "
                              "described in '%(decl_name)s'."
                              , p_name = p_name
                              , decl_name = self.ctx.decl_name)
                else:
                    self.warn("no description found for parameter '%(p_name)s'"
                              , p_name = p_name)
                self.ctx.parameterdescs[p_name] = Parser.undescribed

        self.debug(
            "push_parameter(): (3) p_name='%(p_name)s' /  p_type='%(p_type)s'"
            , p_name=p_name, p_type=p_type)

        self.ctx.parameterlist.append(p_name)
        self.ctx.parametertypes[p_name] = p_type.strip()

    # def save_struct_actual(self, actual):
    #     # strip all spaces from the actual param so that it looks like one
    #     # string item
    #     self.debug("save_struct_actual(): actual='%(a)s'", a=actual)
    #     actual = WHITESPACE.sub("", actual)
    #     self.ctx.struct_actual += actual + " "
    #     self.debug("save_struct_actual: '%(a)s'", a=self.ctx.struct_actual)


    def check_sections(self, decl_name, decl_type
                       , sectcheck, parameterlist, nested):
        self.debug("check_sections(): decl_name='%(n)s' / decl_type='%(t)s' /"
                   " sectcheck=%(sc)s / parameterlist=%(pl)s / nested='%(nested)s'"
                   , n=decl_name, t=decl_type, sc=sectcheck, pl=parameterlist, nested=nested)

        for sect in sectcheck:
            err = True
            for para in parameterlist:
                para = re.sub(r"\[.*\]", "", para)
                #para = re.sub(r"/__attribute__\s*\(\([A-Za-z,_\*\s\(\)]*\)\)/", "", para)
                if para == sect:
                    err = False
                    break
            if err:
                if decl_type == "function":
                    self.warn("excess function parameter '%(sect)s' description in '%(decl_name)s'"
                              , sect = sect, decl_name = decl_name)
                elif not re.search(r"\b(" + sect + ")[^a-zA-Z0-9]", nested):
                    self.warn("excess %(decl_type)s member '%(sect)s' description in '%(decl_name)s'"
                              , decl_type = decl_type, decl_name = decl_name, sect = sect)
            else:
                self.debug("check_sections(): parameter '%(sect)s': description exists / OK"
                           , sect=sect)

    def check_return_section(self, decl_name, return_type):
        self.debug("check_return_section(): decl_name='%(n)s', return_type='%(t)s"
                   , n=decl_name, t=return_type)
        # Ignore an empty return type (It's a macro) and ignore functions with a
        # "void" return type. (But don't ignore "void *")

        if (not return_type
            or re.match(r"void\s*\w*\s*$", return_type)):
            self.debug("check_return_section(): ignore void")
            return

        if self.options.verbose_warn and not self.ctx.sections.get(self.section_return, None):
            self.warn("no description found for return-value of function '%(func)s()'"
                      , func = decl_name)
        else:
            self.debug("check_return_section(): return-value of %(func)s() OK"
                      , func = decl_name)

# ==============================================================================
# 2cent debugging & introspection
# ==============================================================================

def CONSOLE(arround=5, frame=None):
    import inspect, code, linecache
    # pylint: disable=C0321
    sys.stderr.flush()
    sys.stdout.flush()

    frame  = frame or inspect.currentframe().f_back
    fName  = frame.f_code.co_filename
    lineNo = frame.f_lineno

    ns = dict(**frame.f_globals)
    ns.update(**frame.f_locals)

    histfile = os.path.join(os.path.expanduser("~"), ".kernel-doc-history")
    try:
        import readline, rlcompleter  # pylint: disable=W0612
        readline.set_completer(rlcompleter.Completer(namespace=ns).complete)
        readline.parse_and_bind("tab: complete")
        readline.set_history_length(1000)
        if os.path.exists(histfile):
            readline.read_history_file(histfile)
    except ImportError:
        readline = None
    lines  = []
    for c in range(lineNo - arround, lineNo + arround):
        if c > 0:
            prefix = "%-04s|" % c
            if c == lineNo:   prefix = "---->"
            line = linecache.getline(fName, c, frame.f_globals)
            if line != '':    lines.append(prefix + line)
            else:
                if lines: lines[-1] = lines[-1] + "<EOF>\n"
                break
    banner =  "".join(lines) + "file: %s:%s\n" % (fName, lineNo)
    try:
        code.interact(banner=banner, local=ns)
    finally:
        if readline is not None:
            readline.write_history_file(histfile)

# ==============================================================================
# run ...
# ==============================================================================

if __name__ == "__main__":
    sys.exit(main())
else:
    # FIXME: just for testing
    __builtins__["CONSOLE"] = CONSOLE

