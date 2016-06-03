.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _reST-kernel-doc-mode:

====================
reST kernel-doc mode
====================

To get in use of the fully reST_ add the following comment (e.g.) at the top of
your source code file (or at any line reST content starts).::

    /* parse-markup: reST */

In reST mode the kernel-doc parser pass through all text / markups unchanged to
the reST toolchain including any whitespace.  To toggle back to
:ref:`vintage-kernel-doc-mode` type the following line::

    /* parse-markup: kernel-doc */

Within reST mode, most of the *vintage* kernel-doc markup -- as described in
:ref:`kernel-doc-syntax` -- stays unchanged, except the vintage-highlighting
markup and the treatment of whitespaces in description blocks. The *vintage
highlighting* markup is not supported in reST mode, because it conflicts with
the reST markup syntax.

The reST syntax brings it's own markup to refer and highlight function,
structs or whatever definition e.g.:

* functions ...

  .. code-block:: rst

     :c:func:`foo_func`

* structs ...

  .. code-block:: rst

     :c:type:`stuct foo_struct`

If you are familiar with the vintage style, first this might be a cons-change
for you, but take in account, that you get a expressive ASCII markup on the
pro-side.


reST section structure
======================

Since a section title in reST mode needs a line break after the colon, the colon
handling is less ugly (:ref:`vintage-mode-quirks`).  E.g.::

    prints out: hello world

is rendered as expected in one line. If non text follows the colon, a section
is inserted. To avoid sectioning in any case, place a space in front of the column.::

   lorem list :

   * lorem
   * ipsum

On the opposite, super-short sections like::

    Return: sum of a and b

are no longer supported, you have to enter at least one line break::

    Return:
    sum of a and b

Beside these *sectioning* of the kernel-doc syntax, reST has it's own chapter,
section etc. markup (e.g. see `Sections
<http://www.sphinx-doc.org/en/stable/rest.html#sections>`_). Normally, there are
no heading levels assigned to certain characters as the structure is determined
from the succession of headings. However, there is a common convention, which is
used by the kernel-doc parser also:

* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=`` for sections
* ``-`` for subsections
* ``^`` for subsubsections
* ``"`` for paragraphs

Within kernel-doc comments you should use this sectioning with care. A
kernel-doc section like the "Return" section above is translated into a reST
section with the following markup.

.. code-block:: rst

    Return
    ------

    sum of a and b

As you see, a kernel-doc section is at reST *subsection* level. This means, you
can only use the following *sub-levels* within a kernel-doc section.

* ``^`` for subsubsections
* ``"`` for paragraphs


further references
==================

Here are some handy links about reST_  and the `Sphinx markup constructs`_:

* reST_ primer, `reST (quickref)`_, `reST (spec)`_
* `Sphinx markup constructs`_
* `sphinx domains`_
* `sphinx cross refences`_
* `intersphinx`_, `sphinx.ext.intersphinx`_
* `sphinx-doc`_, `sphinx-doc FAQ`_
* `docutils`_, `docutils FAQ`_

In absence of a more detailed C style guide for documentation, the `Python's
Style Guide for documentating
<https://docs.python.org/devguide/documenting.html#style-guide>`_ provides a
good orientation.
