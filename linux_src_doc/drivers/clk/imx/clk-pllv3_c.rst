.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/imx/clk-pllv3.c

.. _`clk_pllv3`:

struct clk_pllv3
================

.. c:type:: struct clk_pllv3

    IMX PLL clock version 3

.. _`clk_pllv3.definition`:

Definition
----------

.. code-block:: c

    struct clk_pllv3 {
        struct clk_hw hw;
        void __iomem *base;
        u32 power_bit;
        bool powerup_set;
        u32 div_mask;
        u32 div_shift;
        unsigned long ref_clock;
    }

.. _`clk_pllv3.members`:

Members
-------

hw
    *undescribed*

base
    base address of PLL registers

power_bit
    pll power bit mask

powerup_set
    set power_bit to power up the PLL

div_mask
    mask of divider bits

div_shift
    shift of divider bits

ref_clock
    *undescribed*

.. _`clk_pllv3.description`:

Description
-----------

IMX PLL clock version 3, found on i.MX6 series.  Divider for pllv3
is actually a multiplier, and always sits at bit 0.

.. This file was automatic generated / don't edit.

