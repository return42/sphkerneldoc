.. -*- coding: utf-8; mode: rst -*-

.. _xref_faq:

===
FAQ
===

What is reStructuredText?
-------------------------

reStructuredText is a extendable plaintext markup specification. The complete
specification is described at `reST (spec)`_ and there is also a
*Quick-Refence* `reST (quickref)`_.

What is docutils?
-----------------

Docutils is a plaintext (reST) processor which consist of a reader to read
plaintext markup and a writer, to write formats such as HTML, LaTeX,
man-pages, open-document or XML. Docutils and reST are projects of David
Goodger. There is a project documentation `docutils`_ and a `docutils FAQ`_.

What is sphinx-doc?
-------------------

`sphinx-doc`_ is a documentation generator, based on the `docutils`_. Think
about a extension / superset of the reST markup and a extended docutils
processer.  `sphinx-doc`_ is a project from the `pocoo`_ team, precisely Georg
Brandl.  One of these reST extensions is the `sphinx domains`_ to document
source code (e.g. ``C`` / ``C++``). An other extension to name is the concept of
`sphinx cross refences`_ and the `sphinx.ext.intersphinx`_ extension. With this
extension the `sphinx-doc`_ documentation generator genrates links to other
projects documentation. E.g. refer a content in the documentation of the python
project with ``:ref:`built-in types <python:bltin-types>``` (:ref:`built-in
types <python:bltin-types>`). Beside these *built-in* extensions, there are
plenty extensions out in the web. Finally, `sphinx-doc`_ is distributed by all
known package managers.

What does *autodoc* mean
------------------------

The term *autodoc* adresses the automatic creation of reST files from the source
code, it is simular to (based on) the ``kernel-doc`` script. In the section
:ref:`xref_doc_from_source` a modified version of ``kernel-doc`` is introduced,
which creates reST files from kernel's sources.



References
==========

.. _`reST (spec)`: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
.. _`reST (quickref)`: http://docutils.sourceforge.net/docs/user/rst/quickref.html

.. _`docutils`: http://docutils.sourceforge.net/docs/index.html
.. _`docutils FAQ`: http://docutils.sourceforge.net/FAQ.html

.. _`pocoo`: http://www.pocoo.org/
.. _`sphinx-doc`: http://www.sphinx-doc.org/
.. _`sphinx-doc FAQ`: http://www.sphinx-doc.org/en/stable/faq.html
.. _`sphinx domains`: http://www.sphinx-doc.org/en/stable/domains.html
.. _`sphinx cross refences`: http://www.sphinx-doc.org/en/stable/markup/inline.html#cross-referencing-arbitrary-locations
.. _`sphinx.ext.intersphinx`: http://www.sphinx-doc.org/en/stable/ext/intersphinx.html#module-sphinx.ext.intersphinx

* `reST (spec)`_, `reST (quickref)`_
* `docutils`_, `docutils FAQ`_
* `sphinx-doc`_, `sphinx-doc FAQ`_, `pocoo`_
* `sphinx domains`_
* `sphinx cross refences`_, `sphinx.ext.intersphinx`_

