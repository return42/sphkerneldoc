.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/cpuidle34xx.c

.. _`omap3_enter_idle`:

omap3_enter_idle
================

.. c:function:: int omap3_enter_idle(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    Programs OMAP3 to enter the specified state

    :param struct cpuidle_device \*dev:
        cpuidle device

    :param struct cpuidle_driver \*drv:
        cpuidle driver

    :param int index:
        the index of state to be entered

.. _`next_valid_state`:

next_valid_state
================

.. c:function:: int next_valid_state(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    Find next valid C-state

    :param struct cpuidle_device \*dev:
        cpuidle device

    :param struct cpuidle_driver \*drv:
        cpuidle driver

    :param int index:
        Index of currently selected c-state

.. _`next_valid_state.description`:

Description
-----------

If the state corresponding to index is valid, index is returned back
to the caller. Else, this function searches for a lower c-state which is
still valid (as defined in omap3_power_states[]) and returns its index.

A state is valid if the 'valid' field is enabled and
if it satisfies the enable_off_mode condition.

.. _`omap3_enter_idle_bm`:

omap3_enter_idle_bm
===================

.. c:function:: int omap3_enter_idle_bm(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    Checks for any bus activity

    :param struct cpuidle_device \*dev:
        cpuidle device

    :param struct cpuidle_driver \*drv:
        cpuidle driver

    :param int index:
        array index of target state to be programmed

.. _`omap3_enter_idle_bm.description`:

Description
-----------

This function checks for any pending activity and then programs
the device to the specified or a safer state.

.. _`omap3_idle_init`:

omap3_idle_init
===============

.. c:function:: int omap3_idle_init( void)

    Init routine for OMAP3 idle

    :param  void:
        no arguments

.. _`omap3_idle_init.description`:

Description
-----------

Registers the OMAP3 specific cpuidle driver to the cpuidle
framework with the valid set of states.

.. This file was automatic generated / don't edit.

