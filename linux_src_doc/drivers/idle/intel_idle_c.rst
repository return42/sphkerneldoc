.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/idle/intel_idle.c

.. _`intel_idle`:

intel_idle
==========

.. c:function:: __cpuidle int intel_idle(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    :param struct cpuidle_device \*dev:
        cpuidle_device

    :param struct cpuidle_driver \*drv:
        cpuidle driver

    :param int index:
        index of cpuidle state

.. _`intel_idle.description`:

Description
-----------

Must be called under \ :c:func:`local_irq_disable`\ .

.. _`intel_idle_freeze`:

intel_idle_freeze
=================

.. c:function:: void intel_idle_freeze(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    simplified "enter" callback routine for suspend-to-idle

    :param struct cpuidle_device \*dev:
        cpuidle_device

    :param struct cpuidle_driver \*drv:
        cpuidle driver

    :param int index:
        state index

.. This file was automatic generated / don't edit.

