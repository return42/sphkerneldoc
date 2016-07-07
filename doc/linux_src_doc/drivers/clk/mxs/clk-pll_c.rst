.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/mxs/clk-pll.c

.. _`clk_pll`:

struct clk_pll
==============

.. c:type:: struct clk_pll

    mxs pll clock

.. _`clk_pll.definition`:

Definition
----------

.. code-block:: c

    struct clk_pll {
        struct clk_hw hw;
        void __iomem *base;
        u8 power;
        unsigned long rate;
    }

.. _`clk_pll.members`:

Members
-------

hw
    clk_hw for the pll

base
    base address of the pll

power
    the shift of power bit

rate
    the clock rate of the pll

.. _`clk_pll.description`:

Description
-----------

The mxs pll is a fixed rate clock with power and gate control,
and the shift of gate bit is always 31.

.. This file was automatic generated / don't edit.

