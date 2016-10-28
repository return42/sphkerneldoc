.. -*- coding: utf-8; mode: rst -*-
.. include:: article_refs.txt

.. _reST-nano-HOWTO:

###############
reST nano HOWTO
###############

:author:    Markus Heiser
:address:   markus.heiser@darmarIT.de

  This article describes, how to write a *loose reST article* and gives hints,
  how to use basic reST markup. To create a *book* see
  ``Documentation/template-book`` :ref:`[ref] <template-book:get-started>`.

A *loose reST article* is just a ordinary text file with reST markup in and a
``.rst`` file extension. All files matching ``Documentaton/*.rst`` are bundled
into one build.

It is recommend to add a mode-line and a include directive on top of these
files:

.. code-block:: rst

   .. -*- coding: utf-8; mode: rst -*-
   .. include:: article_refs.txt

The included ``article_refs.txt`` file contains common used hyperlink target
definitions. You don't have to include this file, but it helps to fix dead or
moved links.

OK, thats all you have to know for the start. You see, a *loose reST article* is
nothing more than a trival text file, but with *batteries included* ;-) ... see
:ref:`kernel-doc-extensions`.

.. _xref_rest_and_sphinx:

===================
reST and sphinx-doc
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

.. _kernel-doc-extensions:

==========================
kernel-doc reST extensions
==========================

The kernel-doc project includes some reST markup extensions:

* the kernel-doc directive :ref:`[ref] <kernel-doc:kernel-doc-directive>`
* the flat-table directive :ref:`[ref] <kernel-doc:rest-flat-table>`
* the kernel-include directive :ref:`[ref] <kernel-include-directive>`

In the following, you will find some usage examples of these extension.

include source code comments
============================

To include kernel-doc comments from your sources use the ``.. kernel-doc::``
directive :ref:`[ref] <kernel-doc:kernel-doc-directive>`:

.. code-block:: rst

    .. kernel-doc:: include/trace/events/signal.h
       :functions:  trace_signal_generate

.. kernel-doc:: include/trace/events/signal.h
   :functions:  trace_signal_deliver


include intermediates
=====================

To include intermediate files from build process, use the
``.. kernel-include::`` directive :ref:`[ref] <kernel-include-directive>`.

.. code-block:: rst

    .. _media_header:

    ****************************
    Media Controller Header File
    ****************************

    .. kernel-include:: $BUILDDIR/media.h.rst



use flat-table
==============

For tables, it is recommend to use the ``.. flat-table::`` directive :ref:`[ref]
<kernel-doc:rest-flat-table>`.  The ``flat-table`` is a *list table* format.
The *list table* formats are double stage list. Compared to the ASCII-art they
migth not be as comfortable for readers of the text-files. Their advantage is,
that they are easy to create/modify and that the diff of a modification is much
more meaningfull,

.. flat-table:: example table
   :fill-cells:

   * - foo
     - bar
     - gizmo

   * - X
     - Y

============
chapter name
============

This is just a chapter example.

second section name
===================

This is just a section example.

sub-section name
----------------

This is just a sub-section example.

.. hint::

    Drop all the content until *here*.


=======
Licence
=======

This documentation is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License version 2 as published by the
Free Software Foundation.

This documentation is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
this documentation; if not, write to the Free Software Foundation, Inc., 59
Temple Place, Suite 330, Boston, MA 02111-1307 USA

For more details see the file COPYING_ in the source distribution of Linux.
