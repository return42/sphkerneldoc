.. -*- coding: utf-8; mode: rst -*-
.. src-file: nested_foobar.h

.. _`nested_foobar`:

struct nested_foobar
====================

.. c:type:: struct nested_foobar

    a struct with nested unions and structs

.. _`nested_foobar.definition`:

Definition
----------

.. code-block:: c

    struct nested_foobar {
        union {
            struct {
                int arg1;
                int arg2;
            } ;
            struct {
                void *arg3;
                int arg4;
            } ;
        } ;
        union {
            struct {
                int arg1;
                int arg2;
            } st1;
            struct {
                void *arg1;
                int arg2;
            } st2;
        } bar;
    }

.. _`nested_foobar.members`:

Members
-------

{unnamed_union}
    anonymous

{unnamed_struct}
    anonymous

arg1
    - first argument of anonymous union/anonymous struct

arg2
    - second argument of anonymous union/anonymous struct

{unnamed_struct}
    anonymous

arg3
    - third argument of anonymous union/anonymous struct

arg4
    - fourth argument of anonymous union/anonymous struct
    \ ``bar``\ .st1.arg1 - first argument of struct st1 on union bar
    \ ``bar``\ .st1.arg2 - second argument of struct st1 on union bar
    \ ``bar``\ .st2.arg1 - first argument of struct st2 on union bar
    \ ``bar``\ .st2.arg2 - second argument of struct st2 on union bar

bar
    *undescribed*

.. This file was automatic generated / don't edit.

