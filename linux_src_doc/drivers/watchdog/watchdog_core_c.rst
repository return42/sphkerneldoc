.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/watchdog_core.c

.. _`watchdog_init_timeout`:

watchdog_init_timeout
=====================

.. c:function:: int watchdog_init_timeout(struct watchdog_device *wdd, unsigned int timeout_parm, struct device *dev)

    initialize the timeout field

    :param struct watchdog_device \*wdd:
        *undescribed*

    :param unsigned int timeout_parm:
        timeout module parameter

    :param struct device \*dev:
        Device that stores the timeout-sec property

.. _`watchdog_init_timeout.description`:

Description
-----------

Initialize the timeout field of the watchdog_device struct with either the
timeout module parameter (if it is valid value) or the timeout-sec property
(only if it is a valid value and the timeout_parm is out of bounds).
If none of them are valid then we keep the old value (which should normally
be the default timeout value).

A zero is returned on success and -EINVAL for failure.

.. _`watchdog_set_restart_priority`:

watchdog_set_restart_priority
=============================

.. c:function:: void watchdog_set_restart_priority(struct watchdog_device *wdd, int priority)

    Change priority of restart handler

    :param struct watchdog_device \*wdd:
        watchdog device

    :param int priority:
        priority of the restart handler, should follow these guidelines:
        0:   use watchdog's restart function as last resort, has limited restart
        capabilies

.. _`watchdog_set_restart_priority.128`:

128
---

default restart handler, use if no other handler is expected to be
available and/or if restart is sufficient to restart the entire system

.. _`watchdog_set_restart_priority.255`:

255
---

preempt all other handlers

If a wdd->ops->restart function is provided when watchdog_register_device is
called, it will be registered as a restart handler with the priority given
here.

.. _`watchdog_register_device`:

watchdog_register_device
========================

.. c:function:: int watchdog_register_device(struct watchdog_device *wdd)

    register a watchdog device

    :param struct watchdog_device \*wdd:
        watchdog device

.. _`watchdog_register_device.description`:

Description
-----------

Register a watchdog device with the kernel so that the
watchdog timer can be accessed from userspace.

A zero is returned on success and a negative errno code for
failure.

.. _`watchdog_unregister_device`:

watchdog_unregister_device
==========================

.. c:function:: void watchdog_unregister_device(struct watchdog_device *wdd)

    unregister a watchdog device

    :param struct watchdog_device \*wdd:
        watchdog device to unregister

.. _`watchdog_unregister_device.description`:

Description
-----------

Unregister a watchdog device that was previously successfully
registered with \ :c:func:`watchdog_register_device`\ .

.. _`devm_watchdog_register_device`:

devm_watchdog_register_device
=============================

.. c:function:: int devm_watchdog_register_device(struct device *dev, struct watchdog_device *wdd)

    resource managed \ :c:func:`watchdog_register_device`\ 

    :param struct device \*dev:
        device that is registering this watchdog device

    :param struct watchdog_device \*wdd:
        watchdog device

.. _`devm_watchdog_register_device.description`:

Description
-----------

Managed \ :c:func:`watchdog_register_device`\ . For watchdog device registered by this
function,  \ :c:func:`watchdog_unregister_device`\  is automatically called on driver
detach. See \ :c:func:`watchdog_register_device`\  for more information.

.. This file was automatic generated / don't edit.

