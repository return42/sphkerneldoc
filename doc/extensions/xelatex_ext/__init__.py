# -*- coding: utf-8; mode: python -*-
# pylint: disable=R0912, R0903, C0330

u"""
    xelatex
    ~~~~~~~

    :copyright:  Copyright (C) 2016 Markus Heiser
    :license:    GPL V3.0, see LICENSE for details.

    This modul brings a *native* XeLaTeX builder and writer to the Sphinx
    documentation generator. The XeLaTeX output is suited for processing with
    XeLaTeX (http://tug.org/xetex/).

    There has been a XeLaTeX support in Sphinx (and docutils) already, but this
    inherits from (is based on) LaTeX implementations. XeLaTeX has builtin
    unicode support, uses ``fontspec`` and ``polyglossia``, while LaTeX needs
    ``inputenc``, additional unicode declaration and uses ``babel`` for
    hyphenation. In short, XeLaTeX and ``polyglossia`` are making things much
    simpler. XeLaTeX have similarities, but a XeLatex generator should not
    inherited or based on a LaTeX implementation.

    The XeLaTeX builder (and writer) is a rewrite from scratch which tries to
    keep as many as possible similarities to the to the Sphinx LaTeX and
    docutils XeTeX builder:

    * https://github.com/sphinx-doc/sphinx/tree/master/sphinx

    and the sources of the docutils XeTeX writer:

    * http://docutils.sourceforge.net/docutils/writers/xetex

"""

# ==============================================================================
#  imports ...
# ==============================================================================

from xelatex_ext.builders.xelatex import XeLaTeXBuilder

# ==============================================================================
def setup(app):
# ==============================================================================

    u"""initialize *this* sphinx extension"""

    app.add_builder(XeLaTeXBuilder)
    app.add_config_value("xelatex_documents", [], '')

