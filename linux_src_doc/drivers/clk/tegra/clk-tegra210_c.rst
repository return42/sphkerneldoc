.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/tegra/clk-tegra210.c

.. _`tegra210_clock_apply_init_table`:

tegra210_clock_apply_init_table
===============================

.. c:function:: void tegra210_clock_apply_init_table( void)

    initialize clocks on Tegra210 SoCs

    :param  void:
        no arguments

.. _`tegra210_clock_apply_init_table.description`:

Description
-----------

Program an initial clock rate and enable or disable clocks needed
by the rest of the kernel, for Tegra210 SoCs.  It is intended to be
called by assigning a pointer to it to tegra_clk_apply_init_table -
this will be called as an arch_initcall.  No return value.

.. _`tegra210_car_barrier`:

tegra210_car_barrier
====================

.. c:function:: void tegra210_car_barrier( void)

    wait for pending writes to the CAR to complete

    :param  void:
        no arguments

.. _`tegra210_car_barrier.description`:

Description
-----------

Wait for any outstanding writes to the CAR MMIO space from this CPU
to complete before continuing execution.  No return value.

.. _`tegra210_clock_assert_dfll_dvco_reset`:

tegra210_clock_assert_dfll_dvco_reset
=====================================

.. c:function:: void tegra210_clock_assert_dfll_dvco_reset( void)

    assert the DFLL's DVCO reset

    :param  void:
        no arguments

.. _`tegra210_clock_assert_dfll_dvco_reset.description`:

Description
-----------

Assert the reset line of the DFLL's DVCO.  No return value.

.. _`tegra210_clock_deassert_dfll_dvco_reset`:

tegra210_clock_deassert_dfll_dvco_reset
=======================================

.. c:function:: void tegra210_clock_deassert_dfll_dvco_reset( void)

    deassert the DFLL's DVCO reset

    :param  void:
        no arguments

.. _`tegra210_clock_deassert_dfll_dvco_reset.description`:

Description
-----------

Deassert the reset line of the DFLL's DVCO, allowing the DVCO to
operate.  No return value.

.. _`tegra210_clock_init`:

tegra210_clock_init
===================

.. c:function:: void tegra210_clock_init(struct device_node *np)

    Tegra210-specific clock initialization

    :param struct device_node \*np:
        struct device_node \* of the DT node for the SoC CAR IP block

.. _`tegra210_clock_init.description`:

Description
-----------

Register most SoC clocks for the Tegra210 system-on-chip.  Intended
to be called by the OF init code when a DT node with the
"nvidia,tegra210-car" string is encountered, and declared with
CLK_OF_DECLARE.  No return value.

.. This file was automatic generated / don't edit.

