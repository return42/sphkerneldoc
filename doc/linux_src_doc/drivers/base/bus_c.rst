.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/bus.c

.. _`bus_for_each_dev`:

bus_for_each_dev
================

.. c:function:: int bus_for_each_dev(struct bus_type *bus, struct device *start, void *data, int (*fn)(struct device *, void *))

    device iterator.

    :param struct bus_type \*bus:
        bus type.

    :param struct device \*start:
        device to start iterating from.

    :param void \*data:
        data for the callback.

    :param int (\*fn)(struct device \*, void \*):
        function to be called for each device.

.. _`bus_for_each_dev.description`:

Description
-----------

Iterate over \ ``bus``\ 's list of devices, and call \ ``fn``\  for each,
passing it \ ``data``\ . If \ ``start``\  is not NULL, we use that device to
begin iterating from.

We check the return of \ ``fn``\  each time. If it returns anything
other than 0, we break out and return that value.

.. _`bus_for_each_dev.note`:

NOTE
----

The device that returns a non-zero value is not retained
in any way, nor is its refcount incremented. If the caller needs
to retain this data, it should do so, and increment the reference
count in the supplied callback.

.. _`bus_find_device`:

bus_find_device
===============

.. c:function:: struct device *bus_find_device(struct bus_type *bus, struct device *start, void *data, int (*match)(struct device *dev, void *data))

    device iterator for locating a particular device.

    :param struct bus_type \*bus:
        bus type

    :param struct device \*start:
        Device to begin with

    :param void \*data:
        Data to pass to match function

    :param int (\*match)(struct device \*dev, void \*data):
        Callback function to check device

.. _`bus_find_device.description`:

Description
-----------

This is similar to the \ :c:func:`bus_for_each_dev`\  function above, but it
returns a reference to a device that is 'found' for later use, as
determined by the \ ``match``\  callback.

The callback should return 0 if the device doesn't match and non-zero
if it does.  If the callback returns non-zero, this function will
return to the caller and not iterate over any more devices.

.. _`bus_find_device_by_name`:

bus_find_device_by_name
=======================

.. c:function:: struct device *bus_find_device_by_name(struct bus_type *bus, struct device *start, const char *name)

    device iterator for locating a particular device of a specific name

    :param struct bus_type \*bus:
        bus type

    :param struct device \*start:
        Device to begin with

    :param const char \*name:
        name of the device to match

.. _`bus_find_device_by_name.description`:

Description
-----------

This is similar to the \ :c:func:`bus_find_device`\  function above, but it handles
searching by a name automatically, no need to write another strcmp matching
function.

.. _`subsys_find_device_by_id`:

subsys_find_device_by_id
========================

.. c:function:: struct device *subsys_find_device_by_id(struct bus_type *subsys, unsigned int id, struct device *hint)

    find a device with a specific enumeration number

    :param struct bus_type \*subsys:
        subsystem

    :param unsigned int id:
        index 'id' in struct device

    :param struct device \*hint:
        device to check first

.. _`subsys_find_device_by_id.description`:

Description
-----------

Check the hint's next object and if it is a match return it directly,
otherwise, fall back to a full list search. Either way a reference for
the returned object is taken.

.. _`bus_for_each_drv`:

bus_for_each_drv
================

.. c:function:: int bus_for_each_drv(struct bus_type *bus, struct device_driver *start, void *data, int (*fn)(struct device_driver *, void *))

    driver iterator

    :param struct bus_type \*bus:
        bus we're dealing with.

    :param struct device_driver \*start:
        driver to start iterating on.

    :param void \*data:
        data to pass to the callback.

    :param int (\*fn)(struct device_driver \*, void \*):
        function to call for each driver.

.. _`bus_for_each_drv.description`:

Description
-----------

This is nearly identical to the device iterator above.
We iterate over each driver that belongs to \ ``bus``\ , and call
\ ``fn``\  for each. If \ ``fn``\  returns anything but 0, we break out
and return it. If \ ``start``\  is not NULL, we use it as the head
of the list.

.. _`bus_for_each_drv.note`:

NOTE
----

we don't return the driver that returns a non-zero
value, nor do we leave the reference count incremented for that
driver. If the caller needs to know that info, it must set it
in the callback. It must also be sure to increment the refcount
so it doesn't disappear before returning to the caller.

.. _`bus_add_device`:

bus_add_device
==============

.. c:function:: int bus_add_device(struct device *dev)

    add device to bus

    :param struct device \*dev:
        device being added

.. _`bus_add_device.description`:

Description
-----------

- Add device's bus attributes.
- Create links to device's bus.
- Add the device to its bus's list of devices.

.. _`bus_probe_device`:

bus_probe_device
================

.. c:function:: void bus_probe_device(struct device *dev)

    probe drivers for a new device

    :param struct device \*dev:
        device to probe

.. _`bus_probe_device.description`:

Description
-----------

- Automatically probe for a driver if the bus allows it.

.. _`bus_remove_device`:

bus_remove_device
=================

.. c:function:: void bus_remove_device(struct device *dev)

    remove device from bus

    :param struct device \*dev:
        device to be removed

.. _`bus_remove_device.description`:

Description
-----------

- Remove device from all interfaces.
- Remove symlink from bus' directory.
- Delete device from bus's list.
- Detach from its driver.
- Drop reference taken in \ :c:func:`bus_add_device`\ .

.. _`bus_add_driver`:

bus_add_driver
==============

.. c:function:: int bus_add_driver(struct device_driver *drv)

    Add a driver to the bus.

    :param struct device_driver \*drv:
        driver.

.. _`bus_remove_driver`:

bus_remove_driver
=================

.. c:function:: void bus_remove_driver(struct device_driver *drv)

    delete driver from bus's knowledge.

    :param struct device_driver \*drv:
        driver.

.. _`bus_remove_driver.description`:

Description
-----------

Detach the driver from the devices it controls, and remove
it from its bus's list of drivers. Finally, we drop the reference
to the bus we took in \ :c:func:`bus_add_driver`\ .

.. _`bus_rescan_devices`:

bus_rescan_devices
==================

.. c:function:: int bus_rescan_devices(struct bus_type *bus)

    rescan devices on the bus for possible drivers

    :param struct bus_type \*bus:
        the bus to scan.

.. _`bus_rescan_devices.description`:

Description
-----------

This function will look for devices on the bus with no driver
attached and rescan it against existing drivers to see if it matches
any by calling \ :c:func:`device_attach`\  for the unbound devices.

.. _`device_reprobe`:

device_reprobe
==============

.. c:function:: int device_reprobe(struct device *dev)

    remove driver for a device and probe for a new driver

    :param struct device \*dev:
        the device to reprobe

.. _`device_reprobe.description`:

Description
-----------

This function detaches the attached driver (if any) for the given
device and restarts the driver probing process.  It is intended
to use if probing criteria changed during a devices lifetime and
driver attachment should change accordingly.

.. _`find_bus`:

find_bus
========

.. c:function:: struct bus_type *find_bus(char *name)

    locate bus by name.

    :param char \*name:
        name of bus.

.. _`find_bus.description`:

Description
-----------

Call \ :c:func:`kset_find_obj`\  to iterate over list of buses to
find a bus by name. Return bus if found.

Note that kset_find_obj increments bus' reference count.

.. _`bus_register`:

bus_register
============

.. c:function:: int bus_register(struct bus_type *bus)

    register a driver-core subsystem

    :param struct bus_type \*bus:
        bus to register

.. _`bus_register.description`:

Description
-----------

Once we have that, we register the bus with the kobject
infrastructure, then register the children subsystems it has:
the devices and drivers that belong to the subsystem.

.. _`bus_unregister`:

bus_unregister
==============

.. c:function:: void bus_unregister(struct bus_type *bus)

    remove a bus from the system

    :param struct bus_type \*bus:
        bus.

.. _`bus_unregister.description`:

Description
-----------

Unregister the child subsystems and the bus itself.
Finally, we call \ :c:func:`bus_put`\  to release the refcount

.. _`subsys_dev_iter_init`:

subsys_dev_iter_init
====================

.. c:function:: void subsys_dev_iter_init(struct subsys_dev_iter *iter, struct bus_type *subsys, struct device *start, const struct device_type *type)

    initialize subsys device iterator

    :param struct subsys_dev_iter \*iter:
        subsys iterator to initialize

    :param struct bus_type \*subsys:
        the subsys we wanna iterate over

    :param struct device \*start:
        the device to start iterating from, if any

    :param const struct device_type \*type:
        device_type of the devices to iterate over, NULL for all

.. _`subsys_dev_iter_init.description`:

Description
-----------

Initialize subsys iterator \ ``iter``\  such that it iterates over devices
of \ ``subsys``\ .  If \ ``start``\  is set, the list iteration will start there,
otherwise if it is NULL, the iteration starts at the beginning of
the list.

.. _`subsys_dev_iter_next`:

subsys_dev_iter_next
====================

.. c:function:: struct device *subsys_dev_iter_next(struct subsys_dev_iter *iter)

    iterate to the next device

    :param struct subsys_dev_iter \*iter:
        subsys iterator to proceed

.. _`subsys_dev_iter_next.description`:

Description
-----------

Proceed \ ``iter``\  to the next device and return it.  Returns NULL if
iteration is complete.

The returned device is referenced and won't be released till
iterator is proceed to the next device or exited.  The caller is
free to do whatever it wants to do with the device including
calling back into subsys code.

.. _`subsys_dev_iter_exit`:

subsys_dev_iter_exit
====================

.. c:function:: void subsys_dev_iter_exit(struct subsys_dev_iter *iter)

    finish iteration

    :param struct subsys_dev_iter \*iter:
        subsys iterator to finish

.. _`subsys_dev_iter_exit.description`:

Description
-----------

Finish an iteration.  Always call this function after iteration is
complete whether the iteration ran till the end or not.

.. _`subsys_system_register`:

subsys_system_register
======================

.. c:function:: int subsys_system_register(struct bus_type *subsys, const struct attribute_group **groups)

    register a subsystem at /sys/devices/system/

    :param struct bus_type \*subsys:
        system subsystem

    :param const struct attribute_group \*\*groups:
        default attributes for the root device

.. _`subsys_system_register.description`:

Description
-----------

All 'system' subsystems have a /sys/devices/system/<name> root device
with the name of the subsystem. The root device can carry subsystem-
wide attributes. All registered devices are below this single root
device and are named after the subsystem with a simple enumeration
number appended. The registered devices are not explicitly named;
only 'id' in the device needs to be set.

Do not use this interface for anything new, it exists for compatibility
with bad ideas only. New subsystems should use plain subsystems; and
add the subsystem-wide attributes should be added to the subsystem
directory itself and not some create fake root-device placed in
/sys/devices/system/<name>.

.. _`subsys_virtual_register`:

subsys_virtual_register
=======================

.. c:function:: int subsys_virtual_register(struct bus_type *subsys, const struct attribute_group **groups)

    register a subsystem at /sys/devices/virtual/

    :param struct bus_type \*subsys:
        virtual subsystem

    :param const struct attribute_group \*\*groups:
        default attributes for the root device

.. _`subsys_virtual_register.description`:

Description
-----------

All 'virtual' subsystems have a /sys/devices/system/<name> root device
with the name of the subystem.  The root device can carry subsystem-wide
attributes.  All registered devices are below this single root device.
There's no restriction on device naming.  This is for kernel software
constructs which need sysfs interface.

.. This file was automatic generated / don't edit.

