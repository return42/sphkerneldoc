.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ti/clockdomain.c

.. _`omap2_clkops_enable_clkdm`:

omap2_clkops_enable_clkdm
=========================

.. c:function:: int omap2_clkops_enable_clkdm(struct clk_hw *hw)

    increment usecount on clkdm of \ ``hw``\ 

    :param struct clk_hw \*hw:
        struct clk_hw \* of the clock being enabled

.. _`omap2_clkops_enable_clkdm.description`:

Description
-----------

Increment the usecount of the clockdomain of the clock pointed to
by \ ``hw``\ ; if the usecount is 1, the clockdomain will be "enabled."
Only needed for clocks that don't use \ :c:func:`omap2_dflt_clk_enable`\  as
their enable function pointer.  Passes along the return value of
\ :c:func:`clkdm_clk_enable`\ , -EINVAL if \ ``hw``\  is not associated with a
clockdomain, or 0 if clock framework-based clockdomain control is
not implemented.

.. _`omap2_clkops_disable_clkdm`:

omap2_clkops_disable_clkdm
==========================

.. c:function:: void omap2_clkops_disable_clkdm(struct clk_hw *hw)

    decrement usecount on clkdm of \ ``hw``\ 

    :param struct clk_hw \*hw:
        struct clk_hw \* of the clock being disabled

.. _`omap2_clkops_disable_clkdm.description`:

Description
-----------

Decrement the usecount of the clockdomain of the clock pointed to
by \ ``hw``\ ; if the usecount is 0, the clockdomain will be "disabled."
Only needed for clocks that don't use \ :c:func:`omap2_dflt_clk_disable`\  as their
disable function pointer.  No return value.

.. _`omap2_init_clk_clkdm`:

omap2_init_clk_clkdm
====================

.. c:function:: void omap2_init_clk_clkdm(struct clk_hw *hw)

    look up a clockdomain name, store pointer in clk

    :param struct clk_hw \*hw:
        *undescribed*

.. _`omap2_init_clk_clkdm.description`:

Description
-----------

Convert a clockdomain name stored in a struct clk 'clk' into a
clockdomain pointer, and save it into the struct clk.  Intended to be
called during \ :c:func:`clk_register`\ .  No return value.

.. _`ti_dt_clockdomains_setup`:

ti_dt_clockdomains_setup
========================

.. c:function:: void ti_dt_clockdomains_setup( void)

    setup device tree clockdomains

    :param  void:
        no arguments

.. _`ti_dt_clockdomains_setup.description`:

Description
-----------

Initializes clockdomain nodes for a SoC. This parses through all the
nodes with compatible = "ti,clockdomain", and add the clockdomain
info for all the clocks listed under these. This function shall be
called after rest of the DT clock init has completed and all
clock nodes have been registered.

.. This file was automatic generated / don't edit.

