.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-syntax:

==================
kernel-doc syntax
==================

In the following examples,

* ``(...)?`` signifies optional structure and
* ``(...)*`` signifies 0 or more structure elements

The definition (or DOC) name is the section header. The section header names
must be unique per source file.

.. _kernel-doc-syntax-functions:

functions
=========

The format of the block comment is like this::

    /**
     * function_name(:)? (- short description)?
    (* @parameterx: (description of parameter x)?)*
    (* a blank line)?
     * (Description:)? (Description of function)?
     * (section header: (section description)? )*
     (*)?*/

All *description* text can span multiple lines, although the
``function_name`` & its short description are traditionally on a single line.
Description text may also contain blank lines (i.e., lines that contain only a
"*").

.. ????
.. Avoid putting a spurious blank line after the function name, or else the
.. description will be repeated!
.. ????

So, the trivial example would be:

.. code-block:: c

    /**
     * my_function
     */

If the Description: header tag is omitted, then there must be a blank line
after the last parameter specification.:

.. code-block:: c

    /**
     * my_function - does my stuff
     * @my_arg: its mine damnit
     *
     * Does my stuff explained.
     */

or, could also use:

.. code-block:: c

    /**
     * my_function - does my stuff
     * @my_arg: its mine damnit
     * Description: Does my stuff explained.
     */

You can also add additional sections. When documenting kernel functions you
should document the ``Context:`` of the function, e.g. whether the functions can
be called form interrupts. Unlike other sections you can end it with an empty
line.

A non-void function should have a ``Return:`` section describing the return
value(s).  Example-sections should contain the string ``EXAMPLE`` so that
they are marked appropriately in the output format.

.. kernel-doc::  ./all-in-a-tumble.h
    :snippets:  user_function
    :language:  c
    :linenos:

Rendered example: :ref:`example.user_function`

.. _kernel-doc-syntax-misc-types:

structs, unions, enums and typedefs
===================================

Beside functions you can also write documentation for structs, unions, enums and
typedefs. Instead of the function name you must write the name of the
declaration; the ``struct``, ``union``, ``enum`` or ``typedef`` must always
precede the name. Nesting of declarations is not supported.  Use the
``@argument`` mechanism to document members or constants.

Inside a struct description, you can use the 'private:' and 'public:' comment
tags.  Structure fields that are inside a 'private:' area are not listed in the
generated output documentation.  The 'private:' and 'public:' tags must begin
immediately following a ``/*`` comment marker.  They may optionally include
comments between the ``:`` and the ending ``*/`` marker.

.. kernel-doc::  ./all-in-a-tumble.h
    :snippets:  my_struct
    :language:  c
    :linenos:

Rendered example: :ref:`example.my_struct`

All descriptions can be multiline, except the short function description.
For really longs structs, you can also describe arguments inside the body of
the struct.

.. kernel-doc::  ./all-in-a-tumble.h
    :snippets:  my_long_struct
    :language:  c
    :linenos:

Rendered example: :ref:`example.my_long_struct`

This should be used only for struct and enum members.

.. _kernel-doc-syntax-doc:

ducumentation blocks
====================

To facilitate having source code and comments close together, you can include
kernel-doc documentation blocks that are *free-form* comments instead of being
kernel-doc for functions, structures, unions, enums, or typedefs.  This could be
used for something like a theory of operation for a driver or library code, for
example.

This is done by using a ``DOC:`` section keyword with a section title. A small
example:

.. kernel-doc::  ./all-in-a-tumble.h
    :snippets:  theory-of-operation
    :language:  c
    :linenos:

Rendered example: :ref:`example.theory-of-operation`

.. _kernel-doc-syntax-snippets:

Snippets
========

The kernel-doc Parser supports a comment-markup for snippets out of the source
code. To start a region to snip insert::

  /* parse-SNIP: <snippet-name> */

The snippet region stops with a new snippet region or at the next::

  /* parse-SNAP: */

A small example:

.. code-block:: c

    /* parse-SNIP: hello-world */
    #include<stdio.h>
    int main() {
        printf("Hello World\n");
    return 0;
    }
    /* parse-SNAP: */
