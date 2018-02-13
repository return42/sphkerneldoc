.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/clkt2xxx_dpll.c

.. _`_allow_idle`:

\_allow_idle
============

.. c:function:: void _allow_idle(struct clk_hw_omap *clk)

    enable DPLL autoidle bits

    :param struct clk_hw_omap \*clk:
        struct clk \* of the DPLL to operate on

.. _`_allow_idle.description`:

Description
-----------

Enable DPLL automatic idle control.  The DPLL will enter low-power
stop when its downstream clocks are gated.  No return value.

.. _`_allow_idle.revisit`:

REVISIT
-------

DPLL can optionally enter low-power bypass by writing 0x1
instead.  Add some mechanism to optionally enter this mode.

.. _`_deny_idle`:

\_deny_idle
===========

.. c:function:: void _deny_idle(struct clk_hw_omap *clk)

    prevent DPLL from automatically idling

    :param struct clk_hw_omap \*clk:
        struct clk \* of the DPLL to operate on

.. _`_deny_idle.description`:

Description
-----------

Disable DPLL automatic idle control.  No return value.

.. This file was automatic generated / don't edit.

