.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/cpuidle-big_little.c

.. _`bl_enter_powerdown`:

bl_enter_powerdown
==================

.. c:function:: int bl_enter_powerdown(struct cpuidle_device *dev, struct cpuidle_driver *drv, int idx)

    Programs CPU to enter the specified state

    :param struct cpuidle_device \*dev:
        cpuidle device

    :param struct cpuidle_driver \*drv:
        The target state to be programmed

    :param int idx:
        state index

.. _`bl_enter_powerdown.description`:

Description
-----------

Called from the CPUidle framework to program the device to the
specified target state selected by the governor.

.. This file was automatic generated / don't edit.

