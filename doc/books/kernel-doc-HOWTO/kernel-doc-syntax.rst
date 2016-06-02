.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-syntax:

==================
kernel-doc syntax
==================

In the following examples,

* ``(...)?`` signifies optional structure and
* ``(...)*`` signifies 0 or more structure elements

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

All *description* text can span multiple lines, although the ``function_name`` &
its short description are traditionally on a single line.  Description text may
also contain blank lines (i.e., lines that contain only a "*").

*section header:* names must be unique per function (or struct, union, typedef,
enum or DOC).

.. ????
.. Avoid putting a spurious blank line after the function name, or else the
.. description will be repeated!
.. ????

So, the trivial example would be::

    /**
     * my_function
     */

If the Description: header tag is omitted, then there must be a blank line
after the last parameter specification.::

    /**
     * my_function - does my stuff
     * @my_arg: its mine damnit
     *
     * Does my stuff explained.
     */

or, could also use::

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
they are marked appropriately in the output format.::

    /**
     * user_function - function that can only be called in user context
     * @a: some argument
     * Context: !in_interrupt()
     *
     * Some description
     *
     * Example:
     *    user_function(22);
     */


structs, unions, enums and typedefs
===================================

Beside functions you can also write documentation for structs, unions, enums and
typedefs. Instead of the function name you must write the name of the
declaration; the ``struct``, ``union``, ``enum`` or ``typedef`` must always
precede the name. Nesting of declarations is not supported.  Use the
``@argument`` mechanism to document members or constants.

Inside a struct description, you can use the ``private:`` and ``public:``
comment tags.  Structure fields that are inside a ``private:`` area are not
listed in the generated output documentation.  The ``private:`` and ``public:``
tags must begin immediately following a ``/* `` comment marker.  They may
optionally include comments between the ``:`` and the ending ``*/`` marker.

Example::

    /**
     * struct my_struct - short description
     * @a: first member
     * @b: second member
     *
     * Longer description
     */
    struct my_struct {
        int a;
        int b;
    /* private: */
        int c;
    };

All descriptions can be multiline, except the short function description.
For really longs structs, you can also describe arguments inside the body of
the struct.::

    /**
     * struct my_struct - short description
     * @a: first member
     * @b: second member
     *
     * Longer description
     */
    struct my_struct {
        int a;
        int b;
        /**
         * @c: This is longer description of C
         *
         * You can use paragraphs to describe arguments
         * using this method.
         */
        int c;
    };

This should be used only for struct and enum members.

To facilitate having source code and comments close together, you can include
kernel-doc documentation blocks that are *free-form* comments instead of being
kernel-doc for functions, structures, unions, enums, or typedefs.  This could be
used for something like a theory of operation for a driver or library code, for
example.

This is done by using a ``DOC:`` section keyword with a section title.  E.g.::

    /**
     * DOC: Theory of Operation
     *
     * The whizbang foobar is a dilly of a gizmo.  It can do whatever you
     * want it to do, at any time.  It reads your mind.  Here's how it works.
     *
     * foo bar splat
     *
     * The only drawback to this gizmo is that is can sometimes damage
     * hardware, software, or its subject(s).
     */

