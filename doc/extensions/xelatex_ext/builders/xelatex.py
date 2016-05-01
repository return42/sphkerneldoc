# -*- coding: utf-8; mode: python -*-

"""
    xelatex_ext.builders.xelatex
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    XeLaTeX builder.

    :copyright:  Copyright (C) 2016 Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.

    TODO: document ...

    * XeLaTex does not use sphinx.sty, has it's own "xetex_inputs" folder with an
      other set of files needed for a XeTeX run.

"""

# ==============================================================================
# imports
# ==============================================================================

from six import iteritems
from os import path, listdir

from docutils import nodes
from docutils.io import FileOutput
from docutils.utils import new_document

from sphinx import addnodes
from sphinx.builders import Builder
from sphinx.environment import NoUri
from sphinx.errors import SphinxError
from sphinx.util.console import bold, darkgreen
from sphinx.util.nodes import inline_all_toctrees
from sphinx.util.osutil import copyfile

from xelatex_ext.writers.doccfg import XeLateXDocSet
from xelatex_ext.writers.xelatex import XeLaTeXWriter
#from sphinx.writers.xelatex import XeLaTeXWriter

XETEX_INPUTS_FOLDER = path.abspath(
    path.join(path.dirname(__file__), "xetex_inputs"))

# ==============================================================================
class XeLaTeXBuilder(Builder):
# ==============================================================================

    name        = 'xelatex'
    format      = 'xelatex'
    writerClass = XeLaTeXWriter

    # allow parallel write_doc() calls
    allow_parallel = True

    supported_image_types = [
        'application/pdf'
        , 'application/eps'
        , 'image/png'
        , 'image/gif'
        , 'image/jpeg'
        ]

    def init(self):

        u"""XeLaTeXBuilder specific initialisations.

        Init / set required members.

        :ivar XeLateXDocSet docset:  Extended (Xe)LaTeX *per-document* settings.
        """
        super(XeLaTeXBuilder, self).init()
        self.docset = XeLateXDocSet(self.app)

    def build(self, docnames, summary=None, _method=None):
        u"""Build (Xe)LaTeX documents.

        Builds always all (Xe)LaTeX documents.  Partial (re-) build of (Xe)LaTeX
        output is not yet intended.  (see :py:`meth`get_outdated_docs`)."""
        super(XeLaTeXBuilder, self).build(docnames, summary=summary, method=None)

    def get_outdated_docs(self):
        u"""Allways returns *all documents*

        Partial (re-) build of (Xe)LaTeX output is not intended!  """

        return list(self.docset.docnames)

    def prepare_writing(self, docnames):
        """A place where you can add logic before :meth:`write_doc` is run"""
        pass

    def write_doc(self, docname, doctree):
        """Where you actually write something to the filesystem."""

        # the argument doctree from base implementation can't used any more,
        # because the tree of a LateX document might be different in case of
        # options like toctree_only. These LaTeX aspetcs are covered by the
        # self.assemble_doctree method.

        docCfg = self.docset.getDocCfg(docname)

        self.info("processing " + docCfg.targetname + "... ", nonl=1)
        tree = self.assemble_doctree(docCfg)
        tree.docCfg = docCfg
        self.post_process_images(tree)

        self.info("writing... ", nonl=1)
        outFile = FileOutput(
            destination_path = path.join(self.outdir, docCfg.targetname),
            encoding         = 'utf-8')
        tree.settings = docCfg

        writer = self.writerClass()
        writer.write(tree, outFile)
        self.info("done")

    def assemble_doctree(self, docCfg):

        self.info(darkgreen(docCfg.startdocname))
        tree = self.env.get_doctree(docCfg.startdocname)

        if docCfg.toctree_only:
            # extract toctree nodes from the tree and put them in a
            # fresh document
            new_tree = new_document('<latex output>')
            new_sect = nodes.section()
            new_sect += nodes.title(
                u'<Set title in conf.py>', u'<Set title in conf.py>')
            new_tree += new_sect
            for node in tree.traverse(addnodes.toctree):
                new_sect += node
            tree = new_tree

        tree = inline_all_toctrees(
            self, docCfg.docnames, docCfg.startdocname, tree,
            darkgreen, [docCfg.startdocname])

        tree['docname'] = docCfg.startdocname

        for docname in docCfg.appendices:
            appendix = self.env.get_doctree(docname)
            appendix['docname'] = docname
            tree.append(appendix)

        self.info("resolving references...")
        self.env.resolve_references(tree, docCfg.startdocname, self)
        docCfg.replacePendingRefsInTree(tree)
        docCfg.initFromTree(tree)
        return tree

    def get_target_uri(self, docname, typ=None):
        """Return the target URI for a document name."""
        if docname not in self.docset.docnames:
            raise NoUri
        else:
            return '%' + docname

    def get_relative_uri(self, from_, to, typ=None):
        """Return a relative URI between two source filenames.

        This implementation always ignores the *from* path.  May raise
        environment.NoUri if there's no way to return a sensible URI."""
        return self.get_target_uri(to, typ)

    def finish(self):
        # copy image files
        if self.images:
            self.info(bold('copying images...'), nonl=1)
            for src, dst in iteritems(self.images):
                self.info(' ' + src, nonl=1)
                src = path.join(self.srcdir, src)
                dst = path.join(self.outdir, dst)
                copyfile(src, dst)
            self.info()

        # copy XeTeX support files from texinputs
        self.info(bold('copying XeTeX support files...'))
        for fname in listdir(XETEX_INPUTS_FOLDER):
            if not fname.startswith('.'):
                src = path.join(XETEX_INPUTS_FOLDER, fname)
                dst = path.join(self.outdir, fname)
                copyfile(src, dst)

        # copy additional files
        if self.docset.additional_files:
            self.info(bold('copying additional files...'), nonl=1)
            _copied = []
            for fname in self.docset.additional_files:
                self.info(' ' + fname, nonl=1)
                src = path.join(self.confdir, fname)
                dst = path.join(self.outdir, path.basename(fname))
                if dst in _copied:
                    raise SphinxError(
                        "two *additional* files with same basename `%s`"
                        % path.basename(fname))
                copyfile(src, dst)
            self.info()

        # copy logo
        if self.docset.logo:
            fname = path.basename(self.docset.logo)
            src   = path.join(self.confdir, fname)
            dst   = path.join(self.outdir, fname)
            if not path.isfile(src):
                raise SphinxError('logo file %r does not exist' % src)
            elif not path.isfile(dst):
                copyfile(src, dst)

        # all done
        self.info('done')
