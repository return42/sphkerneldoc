.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/cpuidle-big_little.c

.. _`bl_enter_powerdown`:

bl_enter_powerdown
==================

.. c:function:: int bl_enter_powerdown(struct cpuidle_device *dev, struct cpuidle_driver *drv, int idx)

    Programs CPU to enter the specified state

    :param dev:
        cpuidle device
    :type dev: struct cpuidle_device \*

    :param drv:
        The target state to be programmed
    :type drv: struct cpuidle_driver \*

    :param idx:
        state index
    :type idx: int

.. _`bl_enter_powerdown.description`:

Description
-----------

Called from the CPUidle framework to program the device to the
specified target state selected by the governor.

.. This file was automatic generated / don't edit.

