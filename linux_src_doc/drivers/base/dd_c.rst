.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/dd.c

.. _`driver_deferred_probe_trigger`:

driver_deferred_probe_trigger
=============================

.. c:function:: void driver_deferred_probe_trigger( void)

    Kick off re-probing deferred devices

    :param void:
        no arguments
    :type void: 

.. _`driver_deferred_probe_trigger.description`:

Description
-----------

This functions moves all devices from the pending list to the active
list and schedules the deferred probe workqueue to process them.  It
should be called anytime a driver is successfully bound to a device.

Note, there is a race condition in multi-threaded probe. In the case where
more than one device is probing at the same time, it is possible for one
probe to complete successfully while another is about to defer. If the second
depends on the first, then it will get put on the pending list after the
trigger event has already occurred and will be stuck there.

The atomic 'deferred_trigger_count' is used to determine if a successful
trigger has occurred in the midst of probing a driver. If the trigger count
changes in the midst of a probe, then deferred processing should be triggered
again.

.. _`device_block_probing`:

device_block_probing
====================

.. c:function:: void device_block_probing( void)

    Block/defere device's probes

    :param void:
        no arguments
    :type void: 

.. _`device_block_probing.description`:

Description
-----------

     It will disable probing of devices and defer their probes instead.

.. _`device_unblock_probing`:

device_unblock_probing
======================

.. c:function:: void device_unblock_probing( void)

    Unblock/enable device's probes

    :param void:
        no arguments
    :type void: 

.. _`device_unblock_probing.description`:

Description
-----------

     It will restore normal behavior and trigger re-probing of deferred
devices.

.. _`driver_deferred_probe_check_state`:

driver_deferred_probe_check_state
=================================

.. c:function:: int driver_deferred_probe_check_state(struct device *dev)

    Check deferred probe state

    :param dev:
        device to check
    :type dev: struct device \*

.. _`driver_deferred_probe_check_state.description`:

Description
-----------

Returns -ENODEV if init is done and all built-in drivers have had a chance
to probe (i.e. initcalls are done), -ETIMEDOUT if deferred probe debug
timeout has expired, or -EPROBE_DEFER if none of those conditions are met.

Drivers or subsystems can opt-in to calling this function instead of directly
returning -EPROBE_DEFER.

.. _`deferred_probe_initcall`:

deferred_probe_initcall
=======================

.. c:function:: int deferred_probe_initcall( void)

    Enable probing of deferred devices

    :param void:
        no arguments
    :type void: 

.. _`deferred_probe_initcall.description`:

Description
-----------

We don't want to get in the way when the bulk of drivers are getting probed.
Instead, this initcall makes sure that deferred probing is delayed until
late_initcall time.

.. _`device_is_bound`:

device_is_bound
===============

.. c:function:: bool device_is_bound(struct device *dev)

    Check if device is bound to a driver

    :param dev:
        device to check
    :type dev: struct device \*

.. _`device_is_bound.description`:

Description
-----------

Returns true if passed device has already finished probing successfully
against a driver.

This function must be called with the device lock held.

.. _`device_bind_driver`:

device_bind_driver
==================

.. c:function:: int device_bind_driver(struct device *dev)

    bind a driver to one device.

    :param dev:
        device.
    :type dev: struct device \*

.. _`device_bind_driver.description`:

Description
-----------

Allow manual attachment of a driver to a device.
Caller must have already set \ ``dev->driver``\ .

Note that this does not modify the bus reference count
nor take the bus's rwsem. Please verify those are accounted
for before calling this. (It is ok to call with no other effort
from a driver's \ :c:func:`probe`\  method.)

This function must be called with the device lock held.

.. _`driver_probe_done`:

driver_probe_done
=================

.. c:function:: int driver_probe_done( void)

    Determine if the probe sequence is finished or not.

    :param void:
        no arguments
    :type void: 

.. _`driver_probe_done.description`:

Description
-----------

Should somehow figure out how to use a semaphore, not an atomic variable...

.. _`wait_for_device_probe`:

wait_for_device_probe
=====================

.. c:function:: void wait_for_device_probe( void)

    Wait for device probing to be completed.

    :param void:
        no arguments
    :type void: 

.. _`driver_probe_device`:

driver_probe_device
===================

.. c:function:: int driver_probe_device(struct device_driver *drv, struct device *dev)

    attempt to bind device & driver together

    :param drv:
        driver to bind a device to
    :type drv: struct device_driver \*

    :param dev:
        device to try to bind to the driver
    :type dev: struct device \*

.. _`driver_probe_device.description`:

Description
-----------

This function returns -ENODEV if the device is not registered,
1 if the device is bound successfully and 0 otherwise.

This function must be called with \ ``dev``\  lock held.  When called for a
USB interface, \ ``dev->parent``\  lock must be held as well.

If the device has a parent, runtime-resume the parent before driver probing.

.. _`device_attach`:

device_attach
=============

.. c:function:: int device_attach(struct device *dev)

    try to attach device to a driver.

    :param dev:
        device.
    :type dev: struct device \*

.. _`device_attach.description`:

Description
-----------

Walk the list of drivers that the bus has and call
\ :c:func:`driver_probe_device`\  for each pair. If a compatible
pair is found, break out and return.

Returns 1 if the device was bound to a driver;
0 if no matching driver was found;
-ENODEV if the device is not registered.

When called for a USB interface, \ ``dev->parent``\  lock must be held.

.. _`driver_attach`:

driver_attach
=============

.. c:function:: int driver_attach(struct device_driver *drv)

    try to bind driver to devices.

    :param drv:
        driver.
    :type drv: struct device_driver \*

.. _`driver_attach.description`:

Description
-----------

Walk the list of devices that the bus has on it and try to
match the driver with each one.  If \ :c:func:`driver_probe_device`\ 
returns 0 and the \ ``dev->driver``\  is set, we've found a
compatible pair.

.. _`device_release_driver`:

device_release_driver
=====================

.. c:function:: void device_release_driver(struct device *dev)

    manually detach device from driver.

    :param dev:
        device.
    :type dev: struct device \*

.. _`device_release_driver.description`:

Description
-----------

Manually detach device from driver.
When called for a USB interface, \ ``dev->parent``\  lock must be held.

If this function is to be called with \ ``dev->parent``\  lock held, ensure that
the device's consumers are unbound in advance or that their locks can be
acquired under the \ ``dev->parent``\  lock.

.. _`driver_detach`:

driver_detach
=============

.. c:function:: void driver_detach(struct device_driver *drv)

    detach driver from all devices it controls.

    :param drv:
        driver.
    :type drv: struct device_driver \*

.. This file was automatic generated / don't edit.

