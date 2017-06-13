.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _xref_rest_and_sphinx:

===================
reST and Sphinx-doc
===================

Here are some handy links about reST_  and the `Sphinx markup constructs`_:

* reST_ primer, `reST (quickref)`_, `reST (spec)`_
* `Sphinx markup constructs`_
* `sphinx domains`_
* `sphinx cross references`_
* `intersphinx`_, `sphinx.ext.intersphinx`_
* `sphinx-doc`_, `sphinx-doc FAQ`_
* `docutils`_, `docutils FAQ`_

In absence of a more detailed C style guide for documentation, the `Python's
Style Guide for documentating
<https://docs.python.org/devguide/documenting.html#style-guide>`_ provides a
good orientation.

What is reStructuredText?
=========================

reStructuredText is a extendable plaintext markup specification. The complete
specification is described at `reST (spec)`_ and there is also a
*Quick-Refence* `reST (quickref)`_.

What is docutils?
=================

Docutils is a plaintext (reST) processor which consist of a reader to read
plaintext markup and a writer, to write formats such as HTML, LaTeX,
man-pages, open-document or XML. Docutils and reST are projects of David
Goodger. There is a project documentation `docutils`_ and a `docutils FAQ`_.

What is sphinx-doc?
===================

`sphinx-doc`_ is a documentation generator, based on the `docutils`_. Think
about a extension / superset of the reST markup and a extended docutils
processer.  `sphinx-doc`_ is a project from the `pocoo`_ team, precisely Georg
Brandl.  One of these reST extensions is the `sphinx domains`_ to document
source code (e.g. ``C`` / ``C++``). An other extension to name is the concept of
`sphinx cross references`_ and the `intersphinx`_ extension. With this
extension the `sphinx-doc`_ documentation generator genrates links to other
projects documentation. E.g. refer a content in the documentation of the linux
source tree with ``:ref:`dtv_get_frontend <linux:dtv_get_frontend>```
(:ref:`dtv_get_frontend <linux:dtv_get_frontend>` ). Beside these *built-in*
extensions, there are plenty extensions out in the web. Finally, `sphinx-doc`_
is distributed by all known package managers.

What is required?
=================

Beside sphinx-doc_ a kernel-doc reST customization is required (see below).  The
customization includes a kernel-doc parser module and an integration into sphinx
(:ref:`LinuxDoc project <linuxdoc:linuxdoc>`).



