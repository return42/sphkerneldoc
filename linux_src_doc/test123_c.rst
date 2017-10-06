.. -*- coding: utf-8; mode: rst -*-
.. src-file: test123.c

.. _`foo`:

enum foo
========

.. c:type:: enum foo

    foo

.. _`foo.definition`:

Definition
----------

.. code-block:: c

    enum foo {
        F1,
        F2
    };

.. _`foo.constants`:

Constants
---------

F1
    f1

F2
    f2

.. _`something`:

struct something
================

.. c:type:: struct something

    Lorem ipsum dolor sit amet.

.. _`something.definition`:

Definition
----------

.. code-block:: c

    struct something {
        union {
            struct dmx_ts_feed ts;
            struct dmx_section_feed sec;
        } feed;
        union {
            dmx_ts_cb ts;
            dmx_section_cb sec;
        } cb;
        struct foo foofoo;
        struct bar barbar;
    }

.. _`something.members`:

Members
-------

feed
    xyz

cb
    xxxxx yyyy zzz

foofoo
    lorem

barbar
    ipsum

.. This file was automatic generated / don't edit.

