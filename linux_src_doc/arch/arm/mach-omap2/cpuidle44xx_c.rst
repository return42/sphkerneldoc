.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/cpuidle44xx.c

.. _`omap_enter_idle_simple`:

omap_enter_idle_simple
======================

.. c:function:: int omap_enter_idle_simple(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    OMAP4PLUS cpuidle entry functions

    :param dev:
        cpuidle device
    :type dev: struct cpuidle_device \*

    :param drv:
        cpuidle driver
    :type drv: struct cpuidle_driver \*

    :param index:
        the index of state to be entered
    :type index: int

.. _`omap_enter_idle_simple.description`:

Description
-----------

Called from the CPUidle framework to program the device to the
specified low power state selected by the governor.
Returns the amount of time spent in the low power state.

.. _`omap4_idle_init`:

omap4_idle_init
===============

.. c:function:: int omap4_idle_init( void)

    Init routine for OMAP4+ idle

    :param void:
        no arguments
    :type void: 

.. _`omap4_idle_init.description`:

Description
-----------

Registers the OMAP4+ specific cpuidle driver to the cpuidle
framework with the valid set of states.

.. This file was automatic generated / don't edit.

