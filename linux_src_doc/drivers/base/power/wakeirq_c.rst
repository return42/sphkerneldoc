.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/wakeirq.c

.. _`dev_pm_attach_wake_irq`:

dev_pm_attach_wake_irq
======================

.. c:function:: int dev_pm_attach_wake_irq(struct device *dev, int irq, struct wake_irq *wirq)

    Attach device interrupt as a wake IRQ

    :param dev:
        Device entry
    :type dev: struct device \*

    :param irq:
        Device wake-up capable interrupt
    :type irq: int

    :param wirq:
        Wake irq specific data
    :type wirq: struct wake_irq \*

.. _`dev_pm_attach_wake_irq.description`:

Description
-----------

Internal function to attach either a device IO interrupt or a
dedicated wake-up interrupt as a wake IRQ.

.. _`dev_pm_set_wake_irq`:

dev_pm_set_wake_irq
===================

.. c:function:: int dev_pm_set_wake_irq(struct device *dev, int irq)

    Attach device IO interrupt as wake IRQ

    :param dev:
        Device entry
    :type dev: struct device \*

    :param irq:
        Device IO interrupt
    :type irq: int

.. _`dev_pm_set_wake_irq.description`:

Description
-----------

Attach a device IO interrupt as a wake IRQ. The wake IRQ gets
automatically configured for wake-up from suspend  based
on the device specific sysfs wakeup entry. Typically called
during driver probe after calling \ :c:func:`device_init_wakeup`\ .

.. _`dev_pm_clear_wake_irq`:

dev_pm_clear_wake_irq
=====================

.. c:function:: void dev_pm_clear_wake_irq(struct device *dev)

    Detach a device IO interrupt wake IRQ

    :param dev:
        Device entry
    :type dev: struct device \*

.. _`dev_pm_clear_wake_irq.description`:

Description
-----------

Detach a device wake IRQ and free resources.

Note that it's OK for drivers to call this without calling
\ :c:func:`dev_pm_set_wake_irq`\  as all the driver instances may not have
a wake IRQ configured. This avoid adding wake IRQ specific
checks into the drivers.

.. _`handle_threaded_wake_irq`:

handle_threaded_wake_irq
========================

.. c:function:: irqreturn_t handle_threaded_wake_irq(int irq, void *_wirq)

    Handler for dedicated wake-up interrupts

    :param irq:
        Device specific dedicated wake-up interrupt
    :type irq: int

    :param _wirq:
        Wake IRQ data
    :type _wirq: void \*

.. _`handle_threaded_wake_irq.description`:

Description
-----------

Some devices have a separate wake-up interrupt in addition to the
device IO interrupt. The wake-up interrupt signals that a device
should be woken up from it's idle state. This handler uses device
specific pm_runtime functions to wake the device, and then it's
up to the device to do whatever it needs to. Note that as the
device may need to restore context and start up regulators, we
use a threaded IRQ.

Also note that we are not resending the lost device interrupts.
We assume that the wake-up interrupt just needs to wake-up the
device, and then device's \ :c:func:`pm_runtime_resume`\  can deal with the
situation.

.. _`dev_pm_set_dedicated_wake_irq`:

dev_pm_set_dedicated_wake_irq
=============================

.. c:function:: int dev_pm_set_dedicated_wake_irq(struct device *dev, int irq)

    Request a dedicated wake-up interrupt

    :param dev:
        Device entry
    :type dev: struct device \*

    :param irq:
        Device wake-up interrupt
    :type irq: int

.. _`dev_pm_set_dedicated_wake_irq.description`:

Description
-----------

Unless your hardware has separate wake-up interrupts in addition
to the device IO interrupts, you don't need this.

Sets up a threaded interrupt handler for a device that has
a dedicated wake-up interrupt in addition to the device IO
interrupt.

The interrupt starts disabled, and needs to be managed for
the device by the bus code or the device driver using
\ :c:func:`dev_pm_enable_wake_irq`\  and \ :c:func:`dev_pm_disable_wake_irq`\ 
functions.

.. _`dev_pm_enable_wake_irq`:

dev_pm_enable_wake_irq
======================

.. c:function:: void dev_pm_enable_wake_irq(struct device *dev)

    Enable device wake-up interrupt

    :param dev:
        Device
    :type dev: struct device \*

.. _`dev_pm_enable_wake_irq.description`:

Description
-----------

Optionally called from the bus code or the device driver for
\ :c:func:`runtime_resume`\  to override the PM runtime core managed wake-up
interrupt handling to enable the wake-up interrupt.

Note that for \ :c:func:`runtime_suspend`\ ) the wake-up interrupts
should be unconditionally enabled unlike for \ :c:func:`suspend`\ 
that is conditional.

.. _`dev_pm_disable_wake_irq`:

dev_pm_disable_wake_irq
=======================

.. c:function:: void dev_pm_disable_wake_irq(struct device *dev)

    Disable device wake-up interrupt

    :param dev:
        Device
    :type dev: struct device \*

.. _`dev_pm_disable_wake_irq.description`:

Description
-----------

Optionally called from the bus code or the device driver for
\ :c:func:`runtime_suspend`\  to override the PM runtime core managed wake-up
interrupt handling to disable the wake-up interrupt.

.. _`dev_pm_enable_wake_irq_check`:

dev_pm_enable_wake_irq_check
============================

.. c:function:: void dev_pm_enable_wake_irq_check(struct device *dev, bool can_change_status)

    Checks and enables wake-up interrupt

    :param dev:
        Device
    :type dev: struct device \*

    :param can_change_status:
        Can change wake-up interrupt status
    :type can_change_status: bool

.. _`dev_pm_enable_wake_irq_check.description`:

Description
-----------

Enables wakeirq conditionally. We need to enable wake-up interrupt
lazily on the first \ :c:func:`rpm_suspend`\ . This is needed as the consumer device
starts in RPM_SUSPENDED state, and the the first \ :c:func:`pm_runtime_get`\  would
otherwise try to disable already disabled wakeirq. The wake-up interrupt
starts disabled with IRQ_NOAUTOEN set.

Should be only called from \ :c:func:`rpm_suspend`\  and \ :c:func:`rpm_resume`\  path.
Caller must hold \ :c:type:`dev->power <dev>`\ .lock to change wirq->status

.. _`dev_pm_disable_wake_irq_check`:

dev_pm_disable_wake_irq_check
=============================

.. c:function:: void dev_pm_disable_wake_irq_check(struct device *dev)

    Checks and disables wake-up interrupt

    :param dev:
        Device
    :type dev: struct device \*

.. _`dev_pm_disable_wake_irq_check.description`:

Description
-----------

Disables wake-up interrupt conditionally based on status.
Should be only called from \ :c:func:`rpm_suspend`\  and \ :c:func:`rpm_resume`\  path.

.. _`dev_pm_arm_wake_irq`:

dev_pm_arm_wake_irq
===================

.. c:function:: void dev_pm_arm_wake_irq(struct wake_irq *wirq)

    Arm device wake-up

    :param wirq:
        Device wake-up interrupt
    :type wirq: struct wake_irq \*

.. _`dev_pm_arm_wake_irq.description`:

Description
-----------

Sets up the wake-up event conditionally based on the
\ :c:func:`device_may_wake`\ .

.. _`dev_pm_disarm_wake_irq`:

dev_pm_disarm_wake_irq
======================

.. c:function:: void dev_pm_disarm_wake_irq(struct wake_irq *wirq)

    Disarm device wake-up

    :param wirq:
        Device wake-up interrupt
    :type wirq: struct wake_irq \*

.. _`dev_pm_disarm_wake_irq.description`:

Description
-----------

Clears up the wake-up event conditionally based on the
\ :c:func:`device_may_wake`\ .

.. This file was automatic generated / don't edit.

