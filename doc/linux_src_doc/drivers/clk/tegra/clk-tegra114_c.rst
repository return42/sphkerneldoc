.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/tegra/clk-tegra114.c

.. _`tegra114_car_barrier`:

tegra114_car_barrier
====================

.. c:function:: void tegra114_car_barrier( void)

    wait for pending writes to the CAR to complete

    :param  void:
        no arguments

.. _`tegra114_car_barrier.description`:

Description
-----------

Wait for any outstanding writes to the CAR MMIO space from this CPU
to complete before continuing execution.  No return value.

.. _`tegra114_clock_tune_cpu_trimmers_high`:

tegra114_clock_tune_cpu_trimmers_high
=====================================

.. c:function:: void tegra114_clock_tune_cpu_trimmers_high( void)

    use high-voltage propagation delays

    :param  void:
        no arguments

.. _`tegra114_clock_tune_cpu_trimmers_high.description`:

Description
-----------

When the CPU rail voltage is in the high-voltage range, use the
built-in hardwired clock propagation delays in the CPU clock
shaper.  No return value.

.. _`tegra114_clock_tune_cpu_trimmers_low`:

tegra114_clock_tune_cpu_trimmers_low
====================================

.. c:function:: void tegra114_clock_tune_cpu_trimmers_low( void)

    use low-voltage propagation delays

    :param  void:
        no arguments

.. _`tegra114_clock_tune_cpu_trimmers_low.description`:

Description
-----------

When the CPU rail voltage is in the low-voltage range, use the
extended clock propagation delays set by
\ :c:func:`tegra114_clock_tune_cpu_trimmers_init`\ .  The intention is to
maintain the input clock duty cycle that the FCPU subsystem
expects.  No return value.

.. _`tegra114_clock_tune_cpu_trimmers_init`:

tegra114_clock_tune_cpu_trimmers_init
=====================================

.. c:function:: void tegra114_clock_tune_cpu_trimmers_init( void)

    set up and enable clk prop delays

    :param  void:
        no arguments

.. _`tegra114_clock_tune_cpu_trimmers_init.description`:

Description
-----------

Program extended clock propagation delays into the FCPU clock
shaper and enable them.  XXX Define the purpose - peak current
reduction?  No return value.

.. _`tegra114_clock_assert_dfll_dvco_reset`:

tegra114_clock_assert_dfll_dvco_reset
=====================================

.. c:function:: void tegra114_clock_assert_dfll_dvco_reset( void)

    assert the DFLL's DVCO reset

    :param  void:
        no arguments

.. _`tegra114_clock_assert_dfll_dvco_reset.description`:

Description
-----------

Assert the reset line of the DFLL's DVCO.  No return value.

.. _`tegra114_clock_deassert_dfll_dvco_reset`:

tegra114_clock_deassert_dfll_dvco_reset
=======================================

.. c:function:: void tegra114_clock_deassert_dfll_dvco_reset( void)

    deassert the DFLL's DVCO reset

    :param  void:
        no arguments

.. _`tegra114_clock_deassert_dfll_dvco_reset.description`:

Description
-----------

Deassert the reset line of the DFLL's DVCO, allowing the DVCO to
operate.  No return value.

.. This file was automatic generated / don't edit.

