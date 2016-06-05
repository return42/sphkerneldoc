.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _why_rest:

========================
Reason to change to reST
========================

The basic idea of this (proof of) concept is to choose reST as **the** base
authoring format, regardless if you are writing comments in source code or even
writing entire books. With sphinx-doc_ and a :ref:`modified kernel-doc parser
<kernel-doc:kernel-doc-howto>` complex documentation could be composed while
various output formats are available.  Including: HTML, LaTeX (for printable PDF
versions), ePub, Texinfo, manual pages, plain text etc.

Reasons to migrate from DocBook
===============================

* The linux-doc is based on DocBook 4.1 which is incompatible to 5.x. The 4.x
  toolchains are old and less maintained.

* XML markup is hard to integrate in source-code comments.

* XML markup is horrible for authoring and the DocBook markup is to excessive
  for beginners.

Reasons to migrate to reST + Sphinx-Doc
=======================================

* `sphinx-doc`_ is widely used and the tools are well maintained. `sphinx-doc`_
  is less academical and has down-to-earth answers where DocBook and it's
  toolchains often fails. E.g. sphinx has *built-in* search-page, automatic
  indices, a code highlighter an solution for :ref:`cross_references` and much
  more.

* ASCII markup is already in the source-code comments. reST markup extends the
  existing markup ability while existing toolchains can be further used. The
  ``kernel-doc`` parser needs a reissue which takes the :ref:`modified
  kernel-doc parser <kernel-doc:kernel-doc-howto>` as specification (see
  :ref:`xref_kernel-doc`).

* ASCII markups are easy for authoring. reST has a clear syntax definition and
  is the most expressive and expandable ASCII markup.

The Sphinx-Doc generator's approach is complete different to XML applications,
while the reST syntax definition is simple and unambiguously. Coders (the
kernel-doc authors) who gets familiar with reST will love the markup. The
readers appreciate the presentation, build by `sphinx-doc`_ . But, compare it by
yourself: DocBook authoring/rendering versus a reST markup with a `sphinx-doc`_
toolchain ...

* authoring: origin `DocBook XML books`_ and `reST books`_
* rendering: origin `HTML DocBook books`_ and :ref:`HTML reST books <xref_migrated_docbock>`.

