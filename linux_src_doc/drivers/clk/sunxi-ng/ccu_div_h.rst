.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/sunxi-ng/ccu_div.h

.. _`ccu_div_internal`:

struct ccu_div_internal
=======================

.. c:type:: struct ccu_div_internal

    Internal divider description

.. _`ccu_div_internal.definition`:

Definition
----------

.. code-block:: c

    struct ccu_div_internal {
        u8 shift;
        u8 width;
        u32 max;
        u32 flags;
        struct clk_div_table *table;
    }

.. _`ccu_div_internal.members`:

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

.. _`ccu_div_internal.description`:

Description
-----------

That structure represents a single divider, and is meant to be
embedded in other structures representing the various clock
classes.

It is basically a wrapper around the clk_divider functions
arguments.

.. This file was automatic generated / don't edit.

