.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-intro:

================
kernel-doc intro
================

In order to provide good documentation of kernel functions and data structures,
please use the following conventions to format your kernel-doc comments in Linux
kernel source.

We also look to provide kernel-doc formatted documentation for functions
externally visible to other kernel files (not marked "static").  We also
recommend providing kernel-doc formatted documentation for private (file
"static") routines, for consistency of kernel source code layout.  But this is
lower priority and at the discretion of the MAINTAINER of that kernel source
file.  Data structures visible in kernel include files should also be documented
using kernel-doc formatted comments.

The opening comment mark ``/**`` is reserved for kernel-doc comments.  Only
comments so marked will be considered by the kernel-doc tools, and any comment
so marked must be in kernel-doc format. The closing comment marker for
kernel-doc comments can be either ``*/`` or ``**/``, but ``*/`` is preferred in
the Linux kernel tree.

.. hint::

  1. Do not use ``/**`` to be begin a comment block unless the comment block
     contains kernel-doc formatted comments.

  2. We definitely need kernel-doc formatted documentation for functions that
     are exported to loadable modules using EXPORT_SYMBOL.

  3. Kernel-doc comments should be placed just before the function or data
     structure being described.


Example kernel-doc function comment:

.. code-block:: c

    /**
     * foobar() - short function description of foobar
     * @arg1:	Describe the first argument to foobar.
     * @arg2:	Describe the second argument to foobar.
     *		One can provide multiple line descriptions
     *		for arguments.
     *
     * A longer description, with more discussion of the function foobar()
     * that might be useful to those using or modifying it.  Begins with
     * empty comment line, and may include additional embedded empty
     * comment lines.
     *
     * The longer description can have multiple paragraphs.
     *
     * Return: Describe the return value of foobar.
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
