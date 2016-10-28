.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/tegra/clk-tegra124.c

.. _`tegra124_clock_apply_init_table`:

tegra124_clock_apply_init_table
===============================

.. c:function:: void tegra124_clock_apply_init_table( void)

    initialize clocks on Tegra124 SoCs

    :param  void:
        no arguments

.. _`tegra124_clock_apply_init_table.description`:

Description
-----------

Program an initial clock rate and enable or disable clocks needed
by the rest of the kernel, for Tegra124 SoCs.  It is intended to be
called by assigning a pointer to it to tegra_clk_apply_init_table -
this will be called as an arch_initcall.  No return value.

.. _`tegra124_car_barrier`:

tegra124_car_barrier
====================

.. c:function:: void tegra124_car_barrier( void)

    wait for pending writes to the CAR to complete

    :param  void:
        no arguments

.. _`tegra124_car_barrier.description`:

Description
-----------

Wait for any outstanding writes to the CAR MMIO space from this CPU
to complete before continuing execution.  No return value.

.. _`tegra124_clock_assert_dfll_dvco_reset`:

tegra124_clock_assert_dfll_dvco_reset
=====================================

.. c:function:: void tegra124_clock_assert_dfll_dvco_reset( void)

    assert the DFLL's DVCO reset

    :param  void:
        no arguments

.. _`tegra124_clock_assert_dfll_dvco_reset.description`:

Description
-----------

Assert the reset line of the DFLL's DVCO.  No return value.

.. _`tegra124_clock_deassert_dfll_dvco_reset`:

tegra124_clock_deassert_dfll_dvco_reset
=======================================

.. c:function:: void tegra124_clock_deassert_dfll_dvco_reset( void)

    deassert the DFLL's DVCO reset

    :param  void:
        no arguments

.. _`tegra124_clock_deassert_dfll_dvco_reset.description`:

Description
-----------

Deassert the reset line of the DFLL's DVCO, allowing the DVCO to
operate.  No return value.

.. _`tegra132_clock_apply_init_table`:

tegra132_clock_apply_init_table
===============================

.. c:function:: void tegra132_clock_apply_init_table( void)

    initialize clocks on Tegra132 SoCs

    :param  void:
        no arguments

.. _`tegra132_clock_apply_init_table.description`:

Description
-----------

Program an initial clock rate and enable or disable clocks needed
by the rest of the kernel, for Tegra132 SoCs.  It is intended to be
called by assigning a pointer to it to tegra_clk_apply_init_table -
this will be called as an arch_initcall.  No return value.

.. _`tegra124_132_clock_init_pre`:

tegra124_132_clock_init_pre
===========================

.. c:function:: void tegra124_132_clock_init_pre(struct device_node *np)

    clock initialization preamble for T124/T132

    :param struct device_node \*np:
        struct device_node \* of the DT node for the SoC CAR IP block

.. _`tegra124_132_clock_init_pre.description`:

Description
-----------

Register most of the clocks controlled by the CAR IP block, along
with a few clocks controlled by the PMC IP block.  Everything in
this function should be common to Tegra124 and Tegra132.  XXX The
PMC clock initialization should probably be moved to PMC-specific
driver code.  No return value.

.. _`tegra124_132_clock_init_post`:

tegra124_132_clock_init_post
============================

.. c:function:: void tegra124_132_clock_init_post(struct device_node *np)

    clock initialization postamble for T124/T132

    :param struct device_node \*np:
        struct device_node \* of the DT node for the SoC CAR IP block

.. _`tegra124_132_clock_init_post.description`:

Description
-----------

Register most of the along with a few clocks controlled by the PMC
IP block.  Everything in this function should be common to Tegra124
and Tegra132.  This function must be called after
\ :c:func:`tegra124_132_clock_init_pre`\ , otherwise clk_base and pmc_base will
not be set.  No return value.

.. _`tegra124_clock_init`:

tegra124_clock_init
===================

.. c:function:: void tegra124_clock_init(struct device_node *np)

    Tegra124-specific clock initialization

    :param struct device_node \*np:
        struct device_node \* of the DT node for the SoC CAR IP block

.. _`tegra124_clock_init.description`:

Description
-----------

Register most SoC clocks for the Tegra124 system-on-chip.  Most of
this code is shared between the Tegra124 and Tegra132 SoCs,
although some of the initial clock settings and CPU clocks differ.
Intended to be called by the OF init code when a DT node with the
"nvidia,tegra124-car" string is encountered, and declared with
CLK_OF_DECLARE.  No return value.

.. _`tegra132_clock_init`:

tegra132_clock_init
===================

.. c:function:: void tegra132_clock_init(struct device_node *np)

    Tegra132-specific clock initialization

    :param struct device_node \*np:
        struct device_node \* of the DT node for the SoC CAR IP block

.. _`tegra132_clock_init.description`:

Description
-----------

Register most SoC clocks for the Tegra132 system-on-chip.  Most of
this code is shared between the Tegra124 and Tegra132 SoCs,
although some of the initial clock settings and CPU clocks differ.
Intended to be called by the OF init code when a DT node with the
"nvidia,tegra132-car" string is encountered, and declared with
CLK_OF_DECLARE.  No return value.

.. This file was automatic generated / don't edit.

