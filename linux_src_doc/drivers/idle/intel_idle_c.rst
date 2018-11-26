.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/idle/intel_idle.c

.. _`intel_idle`:

intel_idle
==========

.. c:function:: __cpuidle int intel_idle(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    :param dev:
        cpuidle_device
    :type dev: struct cpuidle_device \*

    :param drv:
        cpuidle driver
    :type drv: struct cpuidle_driver \*

    :param index:
        index of cpuidle state
    :type index: int

.. _`intel_idle.description`:

Description
-----------

Must be called under \ :c:func:`local_irq_disable`\ .

.. _`intel_idle_s2idle`:

intel_idle_s2idle
=================

.. c:function:: void intel_idle_s2idle(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    simplified "enter" callback routine for suspend-to-idle

    :param dev:
        cpuidle_device
    :type dev: struct cpuidle_device \*

    :param drv:
        cpuidle driver
    :type drv: struct cpuidle_driver \*

    :param index:
        state index
    :type index: int

.. This file was automatic generated / don't edit.

