.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/clkt2xxx_dpllcore.c

.. _`omap2xxx_clk_get_core_rate`:

omap2xxx_clk_get_core_rate
==========================

.. c:function:: unsigned long omap2xxx_clk_get_core_rate( void)

    return the CORE_CLK rate

    :param void:
        no arguments
    :type void: 

.. _`omap2xxx_clk_get_core_rate.description`:

Description
-----------

Returns the CORE_CLK rate.  CORE_CLK can have one of three rate

.. _`omap2xxx_clk_get_core_rate.sources-on-omap2xxx`:

sources on OMAP2xxx
-------------------

the DPLL CLKOUT rate, DPLL CLKOUTX2, or 32KHz
(the latter is unusual).  This currently should be called with
struct clk \*dpll_ck, which is a composite clock of dpll_ck and
core_ck.

.. _`omap2xxx_clkt_dpllcore_init`:

omap2xxx_clkt_dpllcore_init
===========================

.. c:function:: void omap2xxx_clkt_dpllcore_init(struct clk_hw *hw)

    clk init function for dpll_ck

    :param hw:
        *undescribed*
    :type hw: struct clk_hw \*

.. _`omap2xxx_clkt_dpllcore_init.description`:

Description
-----------

Store a local copy of \ ``clk``\  in dpll_core_ck so other code can query
the core rate without having to \ :c:func:`clk_get`\ , which can sleep.  Must
only be called once.  No return value.  XXX If the clock
registration process is ever changed such that dpll_ck is no longer
statically defined, this code may need to change to increment some
kind of use count on dpll_ck.

.. This file was automatic generated / don't edit.

