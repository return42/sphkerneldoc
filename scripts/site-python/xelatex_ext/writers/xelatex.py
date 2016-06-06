# -*- coding: utf-8; mode: python -*-
# pylint: disable=C0103, C0330, R0903, W0613

u"""
    sphinx.writers.xelatex
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright:  Copyright (C) 2016 Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.

    TODO: documenting ....

"""

# ==============================================================================
#  imports ...
# ==============================================================================

import sys
from contextlib import contextmanager

from six import text_type

from docutils import nodes, writers
from docutils.writers.lantex2e import CharMaps, SortableDict, PreambleCmds

from sphinx import highlighting


# ==============================================================================
class cmap(CharMaps):
# ==============================================================================

    IDs = CharMaps.special.copy()
    IDs.update({ 0x00AD : r'\string-'})

    @classmethod
    def mask(cls, txt, translation_map=None):
        _map = translation_map or cls.special
        return text_type(txt).translate(_map)

    @classmethod
    def maskID(cls, ID):
        return text_type(txt).translate(cls.IDs)

# ==============================================================================
class collected_footnote(nodes.footnote):
# ==============================================================================

    """Footnotes that are collected are assigned this class."""

    pass

# ==============================================================================
class tex(object):
# ==============================================================================

    u"""A Namespace with somecommon (La)TeX-helper functions"""

    @staticmethod
    def widest_label(labels):
        u"""Find the *widest* label (string) in a list of labels.

        The *widest* in sense of counting characters, not in sense auf layout.
        """
        retVal = ""
        for l in labels:
            if len(retVal) < len(l):
                retVal = l
        return retVal

    @staticmethod
    def begin(environment, outList=None):
        outList = outList or []
        outList.append("\\begin{%s}\n" % environment)
        yield outList
        outList.append("\\begin{%s}\n" % environment)

    @staticmethod
    def renewcommand(cls, cmd, defn, nargs=0, optarg=None):
        u"""LaTeX's renewcommand.

        .. code-block: python

          >>> renewcommand("plusbinomial", "(#2 + #3)^#1", nargs=3, optarg=4)
          '\\newcommand{\plusbinomial}[3][4]{(#2 + #3)^#1}'
        """
        if nargs:
            nargs  = "[%d]" % nargs
        if optarg:
            optarg = "[%s]" % optarg
        return u"\\renewcommand{\\%s}%s%s{%s}\n" % (cmd, defn, nargs, optarg)


# ==============================================================================
class SimpleFILO(list):
# ==============================================================================

    u"""Simple *first in, last out* stack implementation."""

    push = list.append

    def is_empty(self):
        return not bool(self)

# ==============================================================================
class SectCounter(list):
# ==============================================================================

    def __init__(self):   self.incrLevel()
    def incrLevel(self):  self.append(1)
    def decrLevel(self):  self.pop()
    def incrNum(self):    self[-1] += 1
    def decrNum(self):    self[-1] -= 1

# ==============================================================================
class XeLaTeXWriter(writers.Writer):
# ==============================================================================

    """A writer for Unicode-based LaTeX variants (XeTeX, LuaTeX)

    Supports 'xetex', 'xelatex' and 'luatex' writers and implements the
    ``self.translator_class`` as ``XeLaTeXTranslator``.

    ``XeLaTeXWriter`` inherits from docutils's ``writers.Writer``.

    Not (yet) supported config values:

    * numfig, numfig_format,  numfig_secnum_depth

    .. hint::

       Some of the configurations will never be supported, because they conflict
       with other concepts in LaTeX and LaTeX packages like polyglossia (aka
       babel). Editing the preamble is always a possibility of customizing.

    """

    supported = ('lxtex', 'xetex','xelatex','luatex', 'lualatex')
    """Formats this writer supports."""

    def __init__(self, builder):
        writers.Writer.__init__(self)
        self.output  = None
        self.builder = builder
        self.translator_class = XeLaTeXTranslator

    def translate(self):
        """Do final translation of `self.document` into `self.output`.

        Called from `write`.
        """
        visitor = self.translator_class(self.document, self.builder)
        self.document.walkabout(visitor)
        self.output = visitor.astext()


# ==============================================================================
class Translator(object):
# ==============================================================================

    u"""
    "Visitor" pattern abstract superclass implementation for document tree
    traversals.

    The *visitor/depart* methods are called with two arguments. First argument
    is ``node``, the node-object, second is ``ctx`` the context of the node.

    The *visitor* method can add or modify the context (a python dict), e.g push
    to the ``ctx.body`` or push needed *end-tags* via ``ctx.end_tags``.  The
    *depart* method can use this context, e.g. to extend the *overall-body* with
    the ``ctx.body`` and/or close the tags, the *visitor* opened.

    and pushed to the context"""

    def __init__(self, document):
        self.document     = document
        self.ctx_stacks   = dict()
        self.sectCounter  = SectCounter()

    def push_ctx(self, name, val):
        stack = self.ctx_stacks.get(name, None)
        if stack is None:
            stack = SimpleFILO()
            self.ctx_stacks[name] = stack
        stack.push(val)

    def pop_ctx(self, name):
        return self.ctx_stacks[name].pop()

    def dispatch_visit(self, node):
        """
        Call self."``visit_`` + node class name" with `node` as
        parameter.  If the ``visit_...`` method does not exist, call
        self.unknown_visit.
        """
        node_name = node.__class__.__name__
        method = getattr(self, 'visit_' + node_name, self.unknown_visit)
        self.document.reporter.debug(
            'Translator.dispatch_visit calling %s for %s'
            % (method.__name__, node_name))

        # push context onto the node stack
        ctx  = dict(
            # predefined names in the ctx object
            end_tags    = SimpleFILO()
            , body        = SimpleFILO()
            , sectCounter = self.sectCounter
        )
        self.push_ctx(node_name, ctx)
        return method(node, ctx)

    def dispatch_departure(self, node):
        """
        Call self."``depart_`` + node class name" with `node` as
        parameter.  If the ``depart_...`` method does not exist, call
        self.unknown_departure.
        """
        node_name = node.__class__.__name__
        method = getattr(self, 'depart_' + node_name, self.unknown_departure)
        self.document.reporter.debug(
            'Translator.dispatch_departure calling %s for %s'
            % (method.__name__, node_name))

        # pop context from the node stack
        ctx  = self.pop_ctx(node_name)
        return method(node, ctx)

    def unknown_visit(self, node):
        """
        Called when entering unknown `Node` types.

        Raise an exception unless overridden.
        """
        if  (self.document.settings.strict_visitor
             or node.__class__.__name__ not in self.optional):
            raise NotImplementedError(
                '%s visiting unknown node type: %s'
                % (self.__class__, node.__class__.__name__))

    def unknown_departure(self, node):
        """
        Called before exiting unknown `Node` types.

        Raise exception unless overridden.
        """
        if  (self.document.settings.strict_visitor
             or node.__class__.__name__ not in self.optional):
            raise NotImplementedError(
                '%s departing unknown node type: %s'
                % (self.__class__, node.__class__.__name__))

# ==============================================================================
# Templates of the XeLaTeXTranslator
# ==============================================================================

class XeLaTeX_TEMPLATES(object):
    """Building blocks for XeLaTeX templates

    * HEADER
    * BEGIN_DOC
    * FOOTER
    """

    HEADER = r"""%% Generated by Sphinx.
\documentclass[%(paper_size)s,%(font_size)s%(classoptions)s]{%(docclass)s}
%% set program xelatex
\usepackage{fixltx2e}
\usepackage{fontspec}

%(requirements)s

%% Custom LaTeX preamble
%(preamble)s

%% User specified packages and stylesheets
%% $stylesheet

%% Fallback definitions for Docutils-specific commands
%(fallbacks)s
$pdfsetup
$titledata
%%% Body
\begin{document}
$body_pre_docinfo$docinfo$dedication$abstract$body
\end{document}




%(tocdepth)s


\title{%(title)s}
\date{%(date)s}
\release{%(release)s}
\author{%(author)s}
\newcommand{\sphinxlogo}{%(logo)s}
\renewcommand{\releasename}{%(releasename)s}
%(makeindex)s
"""

    BEGIN_DOC = r"""
\begin{document}
%(maketitle)s
%(tableofcontents)s
"""

    FOOTER = r"""
\renewcommand{\indexname}{%(indexname)s}
%(printindex)s
\end{document}
"""

# ==============================================================================
class XeLaTeXTranslator(Translator):
# ==============================================================================

    u"""Docutils *visitor* pattern of the XeLaTeX writer.

    The ``XeLaTeXTranslator`` class inherits from the
    ``sphinx.writers.latex.LaTeXTranslator`.
    """

    TEMPLATES    = XeLaTeX_TEMPLATES
    sectionnames = ["part", "chapter", "section", "subsection", "subsubsection", "paragraph", "subparagraph"]

    default_ctx = {
        'papersize':         'letterpaper'
        , 'pointsize':       '12pt'
        , 'classoptions':    ''
        , 'longtable':       '\\usepackage{longtable}'
        , 'preamble':        ''
        , 'title':           ''
        , 'date':            ''
        , 'release':         ''
        , 'author':          ''
        , 'logo':            ''
        , 'releasename':     'Release'
        , 'makeindex':       '\\makeindex'
        , 'maketitle':       '\\maketitle'
        , 'tableofcontents': '\\tableofcontents'
        , 'footer':          ''
        , 'printindex':      '\\printindex'
        }

    def __init__(self, document, builder):
        Translator.__init__(self, document)

        self.builder  = builder
        self.settings = document.settings

        # elements
        # --------

        #self.elements  = self.default_ctx.copy()
        # TODO ...
        #self.elements.update(self.document.docCfg)


        # common flags & stacks
        # ---------------------

        self.out               = []
        self.bodystack          = []
        self.requirements       = SortableDict({
            "__static" : r'\usepackage{ifthen}'
        })

        self.fallbacks          = SortableDict() # made a list in depart_document()

        self.bibitems           = []
        self.otherlanguages     = dict()

        self.table              = None
        self.next_table_colspec = None

        self.curfilestack     = []

        self.compact_list       = 0
        self.first_document     = 1
        self.first_param        = 0
        self.in_caption         = 0
        self.in_container_literal_block = 0
        self.in_merged_cell     = 0
        self.in_minipage        = 0
        self.in_production_list = 0
        self.in_term            = 0
        self.in_title           = 0
        self.literal_whitespace = 0
        self.no_contractions    = 0
        self.remember_multirow  = {}
        self.remember_multirowcol = {}
        self.this_is_the_title  = 1
        self.handled_abbrs      = set()

        self.next_hyperlink_ids = {}
        self.next_section_ids = set()

        # footnotes
        # ---------

        self.in_footnote         = 0
        self.footnotestack       = []
        self.footnote_restricted = False
        self.pending_footnotes   = []

        # sectioning
        # ----------

        self.next_section_ids = set()
        self.next_figure_ids  = set()
        self.next_table_ids   = set()

        self.top_sectionlevel = self.sectionnames.index(self.docCfg.toplevel_sectioning)
        self.sectionlevel     = self.top_sectionlevel
        if self.docCfg.get('tocdepth'):
            self.elements['tocdepth'] = (r'\setcounter{tocdepth}{%d}' % self.docCfg.get('tocdepth'))

        # code highlighter
        # ----------------

        # XeLaTeX makes no use of the sphinx.util.texescape, but the
        # sphinx.highlighting.PygmentsBridge uses the *tex_hl_escape_map_new*
        # which has to be initialized.
        from sphinx.util import texescape
        texescape.init()

        self.highlighter = highlighting.PygmentsBridge(
            'latex'
            , self.builder.config.pygments_style or 'tango'  # prefer tango as default
            , self.builder.config.trim_doctest_flags
        )
        # stack of [language, linenothreshold] settings per file the first item
        # here is the default and must not be changed the second item is the
        # default for the master file and can be changed by .. highlight::
        # directive in the master file

        self.hlsettingstack = 2 * [
            [self.builder.config.highlight_language, sys.maxint]
            ]

    def pushbody(self, newbody):
        self.bodystack.append(self.body)
        self.body = newbody

    def popbody(self):
        body = self.body
        self.body = self.bodystack.pop()
        return body

    def push_hyperlink_ids(self, figtype, ids):
        hyperlink_ids = self.next_hyperlink_ids.setdefault(figtype, set())
        hyperlink_ids.update(ids)

    def pop_hyperlink_ids(self, figtype):
        return self.next_hyperlink_ids.pop(figtype, set())

    def restrict_footnote(self, node):
        if self.footnote_restricted is False:
            self.footnote_restricted = node
            self.pending_footnotes = []

    def unrestrict_footnote(self, node):
        if self.footnote_restricted == node:
            self.footnote_restricted = False
            for footnode in self.pending_footnotes:
                footnode['footnotetext'] = True
                footnode.walkabout(self)
            self.pending_footnotes = []

    def astext(self):
        return (
            self.TEMPLATES.HEADER % self.elements
            + self.highlighter.get_stylesheet()
            + u''.join(self.body)
            + '\n' + self.elements['footer'] + '\n'
            + self.generate_indices()
            + self.TEMPLATES.FOOTER % self.elements
            )

    # ------------------------------------------------------------
    # common visitors
    # ------------------------------------------------------------

    def visit_inline(self, node, ctx): # <span>, i.e. custom roles
        for cls in node['classes']:

            if cls == 'align-center':
                self.fallbacks['align-center'] = PreambleCmds.align_center
                ctx.end_tags.push('}')

            if cls.startswith('language-'):
                tags = self.polyglossia.foreignlanguage(cls[9:])
                if tags is not None:
                    startTag, endTag = tags
                    ctx.body.push(startTag)
                    ctx.end_tags.push(endTag)
            else:
                self.fallbacks['inline'] = PreambleCmds.inline
                ctx.body.push(r'\DUrole{%s}{' % cls)
                ctx.end_tags.push('}')

    def depart_inline(self, node):
        self.out.extend(ctx.body)
        self.out.extend(ctx.end_tags)

    def visit_docinfo_item(self, node, ctx, name):
        if name == 'author':
            self.pdfauthor.append(self.attval(node.astext()))
        ctx.body.append('\\textbf{%s}: &\n\t' % name)
        if name == 'address':
            self.insert_newline = True
            ctx.body.append('{\\raggedright\n')
            ctx.end_tag.push(' } \\\\\n')
        else:
            ctx.end_tag.push(' \\\\\n')

    def depart_docinfo_item(self, node):
        self.out.extend(ctx.body)
        self.out.extend(ctx.end_tags)

    def default_depart(self, node, ctx):
        self.out.extend(ctx.body)
        self.out.extend(ctx.end_tags)

    # ------------------------------------------------------------
    # visitors
    # ------------------------------------------------------------

    def visit_section(self, node, ctx):
        # increment parent's (current) section counter and add a new level
        ctx.sectCounter.incrNum()
        ctx.sectCounter.incrLevel()

    def depart_section(self, node, ctx):
        # decrement section level (parents counter continues)
        ctx.sectCounter.decrLevel()
        self.default_depart(node, ctx)

    depart_Text = default_depart
    def visit_Text(self, node, ctx):
        ctx.body.append(cmap.mask(node.astext()))

    depart_abbreviation = depart_inline
    def visit_abbreviation(self, node, ctx):
        node['classes'].insert(0, 'abbreviation')
        self.visit_inline(node, ctx)

    depart_acronym = depart_inline
    def visit_acronym(self, node, ctx):
        node['classes'].insert(0, 'acronym')
        self.visit_inline(node, ctx)

    depart_address = depart_docinfo_item
    def visit_address(self, node, ctx):
        self.visit_docinfo_item(node, ctx, 'address')

    depart_admonition = default_depart
    def visit_admonition(self, node, ctx):
        self.fallbacks['admonition'] = PreambleCmds.admonition
        if 'error' in node['classes']:
            self.fallbacks['error'] = PreambleCmds.error
        # strip the generic 'admonition' from the list of classes
        node['classes'] = [c for c in node['classes'] if c != 'admonition']
        ctx.body.push('\n\\DUadmonition[%s]{\n' % ','.join(node['classes']))
        ctx.end_tag.push('}\n')

    depart_author = default_depart
    def visit_author(self, node, ctx):
        self.visit_docinfo_item(node, ctx, 'author')

    def visit_authors(self, node, ctx):
        # not used: visit_author is called anyway for each author.
        pass
    def depart_authors(self, node, ctx):
        pass

    depart_block_quote = default_depart
    def visit_block_quote(self, node, ctx):
        ctx.body.push('%\n\\begin{quote}\n')
        ctx.end_tag.push('\n\\end{quote}\n')
        if node['classes']:
            self.visit_inline(node, ctx)

    depart_bullet_list = default_depart
    def visit_bullet_list(self, node, ctx):
        if self.is_toc_list:
            ctx.body.push('%\n\\begin{list}{}{}\n')
            ctx.end_tag.push('\n\\end{list}\n')
        else:
            ctx.body.push('%\n\\begin{itemize}\n')
            ctx.end_tag.push('\n\\end{itemize}\n')

    depart_superscript = default_depart
    def visit_superscript(self, node, ctx):
        ctx.body.push(r'\textsuperscript{')
        ctx.end_tag.push('}')
        if node['classes']:
            self.visit_inline(node, ctx)

    depart_subscript = default_depart
    def visit_subscript(self, node, ctx):
        ctx.body.push(r'\textsubscript{') # FIXME: requires `fixltx2e`?
        ctx.end_tag.append('}')
        if node['classes']:
            self.visit_inline(node, ctx)

    depart_caption = default_depart
    def visit_caption(self, node):
        ctx.body.push('\n\\caption{')
        ctx.end_tag.push('}\n')

    depart_title_reference = default_depart
    def visit_title_reference(self, node, ctx):
        self.fallbacks['titlereference'] = PreambleCmds.titlereference
        ctx.body.push(r'\DUroletitlereference{')
        ctx.end_tags.push( '}' )
        if node['classes']:
            self.visit_inline(node, ctx)
TODO:
    def visit_citation(self, node, ctx):
        # TODO maybe use cite bibitems
        # bibitem: [citelabel, citetext, docname, citeid]
        self.bibitems.append(['', '', '', ''])

    def depart_citation(self, node, ctx):
        size = self.context.pop()
        text = ''.join(self.body[size:])
        del self.body[size:]
        self.bibitems[-1][1] = text

    def visit_citation_reference(self, node):
        # This is currently never encountered, since citation_reference nodes
        # are already replaced by pending_xref nodes in the environment.
        self.body.append('\\cite{%s}' % self.idescape(node.astext()))

xxxxxxxxxxxxx
    # ------------------------------------------------------------
    # ID's & hyperrefs
    # ------------------------------------------------------------

    def hypertarget(self, ID, withdoc=True, anchor=True):
        if withdoc:
            ID = self.curfilestack[-1] + ':' + ID
        return (anchor and '\\phantomsection' or '') + \
            '\\label{%s}' % cmap.maskID(ID)

    def hyperlink(self, ID):
        return '{\\hyperref[%s]{' % cmap.maskID(ID)

    def hyperpageref(self, ID):
        return '\\autopageref*{%s}' % cmap.maskID(ID)

    def generate_indices(self):
        def generate(content, collapsed):
            for i, (letter, entries) in enumerate(content):
                if i > 0:
                    ret.append('\\indexspace\n')
                ret.append('%s\n' % cmap.mask(letter))
                for entry in entries:
                    if not entry[3]:
                        continue
                    ret.append('\\item {\\texttt{%s}}' % cmap.mask(entry[0]))
                    if entry[4]: # add "extra" info
                        ret.append(' \\emph{(%s)}' % cmap.mask(entry[4]))
                    ret.append(', \\pageref{%s:%s}\n' % (entry[2], cmap.maskID(entry[3])))

        ret = []
        # latex_domain_indices can be False/True or a list of index names
        indices_config = self.docCfg.domain_indices
        if indices_config:
            for domain in itervalues(self.builder.env.domains):
                for indexcls in domain.indices:
                    indexname = '%s-%s' % (domain.name, indexcls.name)
                    if (isinstance(indices_config, list)
                        and indexname not in indices_config):
                        continue
                    content, collapsed = indexcls(domain).generate(self.builder.docnames)
                    if not content:
                        continue
                    ret.append(tex.renewcommand(indexname, indexcls.localname))
                    with latex.begin("theindex", ret):
                        generate(content, collapsed)

        return ''.join(ret)

    def visit_document(self, node):
        self.footnotestack.append(self.collect_footnotes(node))
        self.curfilestack.append(node.get('docname', ''))

        if self.first_document == 1:
            # the first document is all the regular content ...
            self.body.append(self.TEMPLATES.BEGIN_DOC % self.elements)
            self.first_document = 0

        elif self.first_document == 0:
            # ... and all others are the appendices
            self.body.append(u'\n\\appendix\n')
            self.first_document = -1

        if 'docname' in node:
            self.body.append(self.hypertarget(':doc'))

        # "- 1" because the level is increased before the title is visited
        self.sectionlevel = self.top_sectionlevel - 1


    def depart_document(self, node):

        if self.bibitems:
            widest = latex.widest_label([bi[0] for bi in self.bibitems])
            self.body.append(u'\n\\begin{thebibliography}{%s}\n' % widest)
            for bi in self.bibitems:
                target = self.hypertarget(bi[2] + ':' + bi[3], withdoc=False)
                self.body.append(
                    u'\\bibitem[%s]{%s}{%s %s}\n'
                    % (cmap.mask(bi[0]), cmap.maskID(bi[0]), target, bi[1]))
            self.body.append(u'\\end{thebibliography}\n')
            self.bibitems = []

    def visit_start_of_file(self, node):
        # collect new footnotes
        self.footnotestack.append(self.collect_footnotes(node))
        # also add a document target
        self.next_section_ids.add(':doc')
        self.curfilestack.append(node['docname'])
        # use default highlight settings for new file
        self.hlsettingstack.append(self.hlsettingstack[0])

    def collect_footnotes(self, node):
        def footnotes_under(n):
            if isinstance(n, nodes.footnote):
                yield n
            else:
                for c in n.children:
                    if isinstance(c, addnodes.start_of_file):
                        continue
                    for k in footnotes_under(c):
                        yield k
        fnotes = {}
        for fn in footnotes_under(node):
            num = fn.children[0].astext().strip()
            newnode = collected_footnote(*fn.children, number=num)
            fnotes[num] = [newnode, False]
        return fnotes

    def depart_start_of_file(self, node):
        self.footnotestack.pop()
        self.curfilestack.pop()
        self.hlsettingstack.pop()

    def visit_highlightlang(self, node):
        self.hlsettingstack[-1] = [node['lang'], node['linenothreshold']]
        raise nodes.SkipNode


    def visit_problematic(self, node):
        self.body.append(r'{\color{red}\bfseries{}')

    def depart_problematic(self, node):
        self.body.append('}')

    def visit_topic(self, node):
        self.in_minipage = 1
        self.body.append('\n\\begin{SphinxShadowBox}\n')

    def depart_topic(self, node):
        self.in_minipage = 0
        self.body.append('\\end{SphinxShadowBox}\n')
    visit_sidebar = visit_topic
    depart_sidebar = depart_topic
