# -*- coding: utf-8; mode: python -*-
# pylint: disable=C0330, R0903

u"""
    doccfg
    ~~~~~~

    :copyright:  Copyright (C) 2016 Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.

    Manage *per-document* configuration of a set of documents.

    This module provide an extend concept to handle configurations to build
    individual documents out of one spninx-doc project.

    With the *normal* e.g. ``latex_documents`` configuration abilities from a
    sphinx-doc project, you are not able to set a preamble or a papersize on a
    *per-document* basis. Yes, you can change some paramters like papersize on
    the command line (or in your make file), but this scatter the build process.
    It is the same to other configurations like ``texinfo_no_detailmenu``, they
    can't be set per document.

    The :py:class:`DocSet` facilitate a *single point of definition* in the
    build process and a *per-document* configuration for e.g. (Xe)LaTeX, manual
    pages or texinfo output.

    With a small additional work (in the future) it migth be also possible to
    generate multiple individual epub or html outputs from one single
    sphinx-project, all defined in one conf.py file."""

# ==============================================================================
#  imports
# ==============================================================================

from docutils import nodes
from sphinx import addnodes
from sphinx.errors import ConfigError
from sphinx.locale import _
from sphinx.util.osutil import SEP

# ==============================================================================
class DocData(dict):
# ==============================================================================

    u"""Encapsulate the *per document* configuration names/values.

    Additional configuration names, which values can be inited from a node tree
    (see :py:meth:`initFromTree`):

    :ivar str contentsname: The Name of the content from <toctree>'s ``caption``
      attribute

    :ivar str tocdepth: The TOC depth from <toctree>'s ``maxdepth`` attribute.
    """
    def __init__(self, master_cfg, **kwargs):
        super(DocData, self).__init__(**kwargs)
        self.__master_cfg = master_cfg
        self.contentsname = None
        self.tocdepth     = None

    def __getattr__(self, attr):
        try:
            # if it is a *per-document* setting
            return self[attr]
        except KeyError:
            try:
                # if it is a setting from the *document-set*
                return getattr(self.__master_cfg, attr)
            except KeyError:
                # if it is a setting in the global conf.py
                return getattr(self.__master_cfg.app, attr)

    def __setattr__(self, attr, val):
        self[attr] = val

    def initFromTree(self, tree):
        self._set_contentsname(tree)
        self._set_tocdepth(tree)

    def _set_tocdepth(self, tree):
        # read maxdepth from "TOC tree" of the *startdocname*
        toc_trees = tree.traverse(addnodes.toctree)
        if toc_trees and toc_trees[0].get('maxdepth') > 0:
            self.tocdepth = toc_trees[0].get('maxdepth')

    def _set_contentsname(self, tree):
        for toctree in tree.traverse(addnodes.toctree):
            if toctree['caption']:
                self.contentsname = toctree['caption']
                break


# ==============================================================================
class DocSet(object):
# ==============================================================================

    u"""Encapsulate the *per-document* settings of a set of documents.

    This class captures the aspects of the e.g ``xelatex_documents`` items from
    the sphinx configuration (``conf.py``).  The :py:class:`DocSet` is a
    abstraction, for a detailed implementation and usage see
    :py:class:`XeLatexDocSet`.

    :ivar list docs: A list of configured documents (:py:class:`DocData`
        instances)

    In the sphinx-doc configuration (conf.py) a *per-document* setting is a
    dictionary and a set of these dictionaries is the *DocSet*. An abstract
    example:

    .. code-block:: python

        # conf.py

        documents = [

            # A book with default DIN A4
            dict(docname        = "my_book"
                 , targetname   = "my_book-a4")

            # An alternativ format:  US-letter
            , dict(docname      = "my_book"
                   , targetname = "my_book-letter"
                   , paper_size = "letter" ) ]

    :cvar str cfg_name: Name of the configuration with the *docset*
      (e.g. ``xelatex_documents``).

    :cvar list req_names: A list of strings with additional required names in
        each *per-document* configuration.  Minimal required names in a
        *per-document* dictionary:

        * ``docname``    Name of the start file (in file / the *startdocname*)
        * ``targetname`` Name of the target file (out file)
    """

    cfg_name  = None
    req_names = []


    def __init__(self, app):
        self.app  = app
        self.docs = []

    def getDocCfg(self, docname):
        for docCfg in self.docs:
            if docCfg.docname == docname:
                return docCfg

    @property
    def docnames(self):
        u"""List of all start-doc names in the configuration set."""
        return [cfg.docname for cfg in self.docs]

    @property
    def targetnames(self):
        u"""List of all out-file names in the configuration set."""
        return [cfg.targetname for cfg in self.docs]

    @property
    def titles(self):
        for cfg in self.docs:
            docname = cfg.docname
            if docname.endswith(SEP+'index'):
                docname = docname[:-5]
            yield (docname, cfg.title)

    def loadDocData(self, **defaults):
        self.docs = []
        if self.cfg_name is None:
            raise RuntimeError("Config name (self.cfg_name) is unset.")

        cfg = self.app.config.get(self.cfg_name, None)
        if not cfg:
            self.app.warn("no or empty '%s' config value found;"
                          " no documents will be written"
                          % self.cfg_name)
            return

        pos = 0
        for docCfg in cfg:
            pos += 1

            # assert min. required configuration
            # ----------------------------------
            docname    = docCfg.get("docname", None)
            targetname = docCfg.get("targetname", None)

            if not docname:
                raise ConfigError("'%s' config value at position %s missed"
                                  " it's *docname*" % (self.cfg_name, pos))

            if docname not in self.app.env.all_docs:
                self.app.warn("'%s' config value at position %s will be"
                              " ignored; reference to unknown *%s*"
                              % (self.cfg_name, pos, docname))
                continue

            if not targetname:
                raise ConfigError("'%s' config value at position %s missed"
                                  " it's *targetname* configuration"
                                  % (self.cfg_name, pos))

            if targetname in self.targetnames:
                raise ConfigError("'%s' the *targetname* '%s' used twice,"
                                  " different out-file names are needed!"
                                  % (self.cfg_name, targetname))

            # assert additional required names
            # --------------------------------
            unset = object()
            for name in self.req_names:
                if docCfg.get(name, unset) is unset:
                    raise ConfigError("'%s' config value at position %s missed"
                                      " it's *%s* configuration"
                                      % (self.cfg_name, pos, name))

            # init cfg
            # --------
            cfg = DocData(self, **defaults)
            cfg.update(docCfg)
            self.docs.append(cfg)



# ==============================================================================
class XeLatexDocSet(DocSet):
# ==============================================================================

    u"""Extended (Xe)LaTeX *per-document* settings.

    Required config-names according to the latex_documents setting:

    docname
      document name that is the "root" of the LaTeX file.

    targetname
      file name of the LaTeX file in the output directory.

    documentclass
      LaTeX document class

    toctree_only
      Must be True or False. Only the documents referenced by the
      master TOC trees are included

    To get more infomations consult `latex_documents
    <http://www.sphinx-doc.org/en/stable/config.html#confval-latex_documents>`_

    Optional config-names with defaults from the *global* ``latex_*`` settings:

    * paper_size: The paper size (e.g. 'letter' or 'a4').

    * font_size: The font size (e.g. '10pt', '11pt' or '12pt').

    * use_parts: If this is true, then toplevel headings are parts, not
      chapters. If this is an integer, its value is used as *top-section-level*

    * show_urls: If true, show URL addresses after external links.

    * preamble: Additional stuff for the LaTeX preamble.

    * appendices: Documents to append as an appendix to all manuals.

    * show_pagerefs: If true, show page references after internal links.

    * domain_indices: If false, no module index is generated.

    * toplevel_sectioning: This value determines the topmost sectioning unit.

    To get more infomations consult `Options for LaTeX output
    <http://www.sphinx-doc.org/en/stable/config.html#options-for-latex-output>`_

    The following example shows, that the traditional *global* ``latex_*``
    settings are used as defaults on the *per-document* basis.

    .. code-block:: python

        # conf.py

        # set default values
        latex_paper_size = "a4paper"
        latex_font_size  = "12pt"

        xelatex_documents = [

            # A book with default DIN A4 and 12pt
            dict(docname         = "my_book"
                 , targetname    = "my_book-a4"
                 , documentclass = "manual")

            # An alternativ format: US-letter and 10pt
            , dict(docname         = "my_book"
                   , targetname    = "my_book-letter"
                   , documentclass = "manual"
                   , paper_size    = "letter"
                   , font_size     = "10pt" )]
    """
    cfg_name  = "xelatex_documents"
    req_names = ["documentclass", ]

    # TODO: (currently) not supported:
    #
    # * latex_docclass = ({}, None) : no need for
    #
    # * latex_additional_files: not supported on a per-document basis / no need
    #   for ?

    def __init__(self, *args, **kwargs):
        super(XeLatexDocSet, self).__init__(*args, **kwargs)
        self.additional_files = self.app.config.latex_additional_files
        self.logo             = self.app.config.latex_logo

        self.loadDocData()

    def replacePendingRefsInTree(self, tree):

        # resolve :ref:s to distant tex files -- we can't add a cross-reference,
        # but append the document name

        for pendingnode in tree.traverse(addnodes.pending_xref):
            docname  = pendingnode['refdocname']
            sectname = pendingnode['refsectname']
            newnodes = [nodes.emphasis(sectname, sectname)]
            for subdir, title in self.titles:
                if docname.startswith(subdir):
                    newnodes.append(nodes.Text(_(' (in '), _(' (in ')))
                    newnodes.append(nodes.emphasis(title, title))
                    newnodes.append(nodes.Text(')', ')'))
                    break
            pendingnode.replace_self(newnodes)

    def loadDocData(self):
        super(XeLatexDocSet, self).__init__(
            paper_size            = self.app.config.latex_paper_size
            , font_size           = self.app.config.latex_font_size
            , use_parts           = self.app.config.latex_use_parts
            , show_urls           = self.app.config.latex_show_urls
            , appendices          = self.app.config.latex_appendices
            , show_pagerefs       = self.app.config.latex_show_pagerefs
            , domain_indices      = self.app.config.latex_domain_indices
            , toplevel_sectioning = self.app.config.latex_toplevel_sectioning
            , toctree_only        = False

            # TODO: in which use-cases is a title required and not taken
            # from the startdoc?
            , title = None

            # TODO: I'am not happy with the latex_elements, it is very specific
            # and does not fit well to the xelatex workflow, so I ignore it. May
            # be aktivated later, but preamble should be enough.
            # , elements = self.app.config.latex_elements
            , preamble   = self.app.config.latex_preamble
        )
