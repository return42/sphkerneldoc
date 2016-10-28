.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-intro:

================
kernel-doc intro
================

In order to provide embedded, "C" friendly, easy to maintain, but consistent and
extractable overview, function and type documentation, the Linux kernel has
adopted a consistent style for documentation comments. The format for this
documentation is called the **kernel-doc format**.  This style embeds the
documentation within the source files, using a few simple conventions for adding
documentation paragraphs and documenting functions and their parameters,
structures and unions and their members, enumerations, and typedefs.

.. note::

   The kernel-doc format is deceptively similar to Doxygen or javadoc, yet
   distinctively different, for historical reasons. The kernel source contains
   tens of thousands of kernel-doc comments. Please stick to the style described
   here.

The kernel-doc parser is used in the documentation build to extract this
embedded documentation into the reST_ markup format from which sphinx-doc_
generates HTML, PDF, and other format documents.

In order to provide good documentation of kernel functions and data structures,
please use the following conventions to format your kernel-doc comments in the
Linux kernel source.

.. hint::

  1. Do not use ``/**`` to be begin a comment block unless the comment block
     contains kernel-doc formatted comments.

  2. We definitely need kernel-doc formatted documentation for functions that are
     exported to loadable modules using EXPORT_SYMBOL.

  3. We also look to provide kernel-doc formatted documentation for functions
     externally visible to other kernel files (not marked "static").

  4. Data structures visible in kernel include files should also be documented
     using kernel-doc formatted comments.

  5. kernel-doc comments should be placed just before the function or data
     structure being described.


We also recommend providing kernel-doc formatted documentation for private (file
"static") routines, for consistency of kernel source code layout.  But this is
lower priority and at the discretion of the MAINTAINER of that kernel source
file.

The opening comment mark ``/**`` is reserved for kernel-doc comments.  Only
comments so marked will be considered by the kernel-doc tools, and any comment
so marked must be in kernel-doc format.  The closing comment marker for
kernel-doc comments can be either ``*/`` or ``**/``, but ``*/`` is preferred in
the Linux kernel tree.  The lines in between should be prefixed by `` * ``
(space star space).

Example kernel-doc function comment:

.. code-block:: c

    /**
     * foobar() - short function description of foobar
     *
     * @arg1:	Describe the first argument to foobar.
     * @arg2:	Describe the second argument to foobar.
     * One can provide multiple line descriptions
     * for arguments.
     *
     * A longer description, with more discussion of the function foobar()
     * that might be useful to those using or modifying it.  Begins with
     * empty comment line, and may include additional embedded empty
     * comment lines.
     *
     * The longer description can have multiple paragraphs.
     *
     * Return:
     * Describe the return value of foobar.
     */

The short description following the subject can span multiple lines and ends
with an ``@name`` description, an empty line or the end of the comment block.
The kernel-doc function comments describe each parameter to the function, in
order, with the ``@name`` lines.  The ``@name`` descriptions must begin on the
very next line following this opening short function description line, with no
intervening empty comment lines. If a function parameter is ``...`` (varargs),
it should be listed in kernel-doc notation as::

     * @...: description

The return value, if any, should be described in a dedicated section named
``Return``. Beside functions you can also write documentation for structs,
unions, enums and typedefs. Example kernel-doc data structure comment.::

    /**
     * struct blah - the basic blah structure
     * @mem1:	describe the first member of struct blah
     * @mem2:	describe the second member of struct blah,
     *		perhaps with more lines and words.
     *
     * Longer description of this structure.
     */

The kernel-doc data structure comments describe each structure member in the
data structure, with the ``@name`` lines.
