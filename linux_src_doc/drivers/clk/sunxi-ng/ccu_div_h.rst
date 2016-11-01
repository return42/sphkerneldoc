.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/sunxi-ng/ccu_div.h

.. _`_ccu_div`:

struct \_ccu_div
================

.. c:type:: struct _ccu_div

    Internal divider description

.. _`_ccu_div.definition`:

Definition
----------

.. code-block:: c

    struct _ccu_div {
        u8 shift;
        u8 width;
        u32 max;
        u32 flags;
        struct clk_div_table *table;
    }

.. _`_ccu_div.members`:

Members
-------

shift
    Bit offset of the divider in its register

width
    Width of the divider field in its register

max
    Maximum value allowed for that divider. This is the
    arithmetic value, not the maximum value to be set in the
    register.

flags
    clk_divider flags to apply on this divider

table
    Divider table pointer (if applicable)

.. _`_ccu_div.description`:

Description
-----------

That structure represents a single divider, and is meant to be
embedded in other structures representing the various clock
classes.

It is basically a wrapper around the clk_divider functions
arguments.

.. This file was automatic generated / don't edit.

