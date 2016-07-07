.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/keystone/pll.c

.. _`clk_pll_data`:

struct clk_pll_data
===================

.. c:type:: struct clk_pll_data

    pll data structure

.. _`clk_pll_data.definition`:

Definition
----------

.. code-block:: c

    struct clk_pll_data {
        bool has_pllctrl;
        u32 phy_pllm;
        u32 phy_pll_ctl0;
        void __iomem *pllm;
        void __iomem *pllod;
        void __iomem *pll_ctl0;
        u32 pllm_lower_mask;
        u32 pllm_upper_mask;
        u32 pllm_upper_shift;
        u32 plld_mask;
        u32 clkod_mask;
        u32 clkod_shift;
        u32 postdiv;
    }

.. _`clk_pll_data.members`:

Members
-------

has_pllctrl
    If set to non zero, lower 6 bits of multiplier is in pllm
    register of pll controller, else it is in the pll_ctrl0((bit 11-6)

phy_pllm
    Physical address of PLLM in pll controller. Used when
    has_pllctrl is non zero.

phy_pll_ctl0
    Physical address of PLL ctrl0. This could be that of
    Main PLL or any other PLLs in the device such as ARM PLL, DDR PLL
    or PA PLL available on keystone2. These PLLs are controlled by
    this register. Main PLL is controlled by a PLL controller.

pllm
    PLL register map address for multiplier bits

pllod
    PLL register map address for post divider bits

pll_ctl0
    PLL controller map address

pllm_lower_mask
    multiplier lower mask

pllm_upper_mask
    multiplier upper mask

pllm_upper_shift
    multiplier upper shift

plld_mask
    divider mask

clkod_mask
    output divider mask

clkod_shift
    output divider shift

postdiv
    Fixed post divider

.. _`clk_pll`:

struct clk_pll
==============

.. c:type:: struct clk_pll

    Main pll clock

.. _`clk_pll.definition`:

Definition
----------

.. code-block:: c

    struct clk_pll {
        struct clk_hw hw;
        struct clk_pll_data *pll_data;
    }

.. _`clk_pll.members`:

Members
-------

hw
    clk_hw for the pll

pll_data
    PLL driver specific data

.. _`_of_pll_clk_init`:

_of_pll_clk_init
================

.. c:function:: void _of_pll_clk_init(struct device_node *node, bool pllctrl)

    PLL initialisation via DT

    :param struct device_node \*node:
        device tree node for this clock

    :param bool pllctrl:
        If true, lower 6 bits of multiplier is in pllm register of
        pll controller, else it is in the control register0(bit 11-6)

.. _`of_keystone_pll_clk_init`:

of_keystone_pll_clk_init
========================

.. c:function:: void of_keystone_pll_clk_init(struct device_node *node)

    PLL initialisation DT wrapper

    :param struct device_node \*node:
        device tree node for this clock

.. _`of_keystone_main_pll_clk_init`:

of_keystone_main_pll_clk_init
=============================

.. c:function:: void of_keystone_main_pll_clk_init(struct device_node *node)

    Main PLL initialisation DT wrapper

    :param struct device_node \*node:
        device tree node for this clock

.. _`of_pll_div_clk_init`:

of_pll_div_clk_init
===================

.. c:function:: void of_pll_div_clk_init(struct device_node *node)

    PLL divider setup function

    :param struct device_node \*node:
        device tree node for this clock

.. _`of_pll_mux_clk_init`:

of_pll_mux_clk_init
===================

.. c:function:: void of_pll_mux_clk_init(struct device_node *node)

    PLL mux setup function

    :param struct device_node \*node:
        device tree node for this clock

.. This file was automatic generated / don't edit.

