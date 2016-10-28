.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/mxs/clk-ref.c

.. _`clk_ref`:

struct clk_ref
==============

.. c:type:: struct clk_ref

    mxs reference clock

.. _`clk_ref.definition`:

Definition
----------

.. code-block:: c

    struct clk_ref {
        struct clk_hw hw;
        void __iomem *reg;
        u8 idx;
    }

.. _`clk_ref.members`:

Members
-------

hw
    clk_hw for the reference clock

reg
    register address

idx
    the index of the reference clock within the same register

.. _`clk_ref.description`:

Description
-----------

The mxs reference clock sources from pll.  Every 4 reference clocks share
one register space, and \ ``idx``\  is used to identify them.  Each reference
clock has a gate control and a fractional \* divider.  The rate is calculated
as pll rate  \* (18 / FRAC), where FRAC = 18 ~ 35.

.. This file was automatic generated / don't edit.

