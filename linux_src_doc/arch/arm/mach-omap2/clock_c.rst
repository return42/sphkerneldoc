.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/clock.c

.. _`omap2_clk_setup_ll_ops`:

omap2_clk_setup_ll_ops
======================

.. c:function:: int omap2_clk_setup_ll_ops( void)

    setup clock driver low-level ops

    :param  void:
        no arguments

.. _`omap2_clk_setup_ll_ops.description`:

Description
-----------

Sets up clock driver low-level platform ops. These are needed
for register accesses and various other misc platform operations.
Returns 0 on success, -EBUSY if low level ops have been registered
already.

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

.. _`omap2_clk_print_new_rates`:

omap2_clk_print_new_rates
=========================

.. c:function:: void omap2_clk_print_new_rates(const char *hfclkin_ck_name, const char *core_ck_name, const char *mpu_ck_name)

    print summary of current clock tree rates

    :param const char \*hfclkin_ck_name:
        clk name for the off-chip HF oscillator

    :param const char \*core_ck_name:
        clk name for the on-chip CORE_CLK

    :param const char \*mpu_ck_name:
        clk name for the ARM MPU clock

.. _`omap2_clk_print_new_rates.description`:

Description
-----------

Prints a short message to the console with the HFCLKIN oscillator
rate, the rate of the CORE clock, and the rate of the ARM MPU clock.
Called by the boot-time MPU rate switching code.   XXX This is intended
to be handled by the OPP layer code in the near future and should be
removed from the clock code.  No return value.

.. _`ti_clk_init_features`:

ti_clk_init_features
====================

.. c:function:: void ti_clk_init_features( void)

    init clock features struct for the SoC

    :param  void:
        no arguments

.. _`ti_clk_init_features.description`:

Description
-----------

Initializes the clock features struct based on the SoC type.

.. This file was automatic generated / don't edit.

