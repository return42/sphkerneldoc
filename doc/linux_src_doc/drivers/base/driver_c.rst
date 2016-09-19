.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/driver.c

.. _`driver_for_each_device`:

driver_for_each_device
======================

.. c:function:: int driver_for_each_device(struct device_driver *drv, struct device *start, void *data, int (*fn)(struct device *, void *))

    Iterator for devices bound to a driver.

    :param struct device_driver \*drv:
        Driver we're iterating.

    :param struct device \*start:
        Device to begin with

    :param void \*data:
        Data to pass to the callback.

    :param int (\*fn)(struct device \*, void \*):
        Function to call for each device.

.. _`driver_for_each_device.description`:

Description
-----------

Iterate over the \ ``drv``\ 's list of devices calling \ ``fn``\  for each one.

.. _`driver_find_device`:

driver_find_device
==================

.. c:function:: struct device *driver_find_device(struct device_driver *drv, struct device *start, void *data, int (*match)(struct device *dev, void *data))

    device iterator for locating a particular device.

    :param struct device_driver \*drv:
        The device's driver

    :param struct device \*start:
        Device to begin with

    :param void \*data:
        Data to pass to match function

    :param int (\*match)(struct device \*dev, void \*data):
        Callback function to check device

.. _`driver_find_device.description`:

Description
-----------

This is similar to the \ :c:func:`driver_for_each_device`\  function above, but
it returns a reference to a device that is 'found' for later use, as
determined by the \ ``match``\  callback.

The callback should return 0 if the device doesn't match and non-zero
if it does.  If the callback returns non-zero, this function will
return to the caller and not iterate over any more devices.

.. _`driver_create_file`:

driver_create_file
==================

.. c:function:: int driver_create_file(struct device_driver *drv, const struct driver_attribute *attr)

    create sysfs file for driver.

    :param struct device_driver \*drv:
        driver.

    :param const struct driver_attribute \*attr:
        driver attribute descriptor.

.. _`driver_remove_file`:

driver_remove_file
==================

.. c:function:: void driver_remove_file(struct device_driver *drv, const struct driver_attribute *attr)

    remove sysfs file for driver.

    :param struct device_driver \*drv:
        driver.

    :param const struct driver_attribute \*attr:
        driver attribute descriptor.

.. _`driver_register`:

driver_register
===============

.. c:function:: int driver_register(struct device_driver *drv)

    register driver with bus

    :param struct device_driver \*drv:
        driver to register

.. _`driver_register.description`:

Description
-----------

We pass off most of the work to the \ :c:func:`bus_add_driver`\  call,
since most of the things we have to do deal with the bus
structures.

.. _`driver_unregister`:

driver_unregister
=================

.. c:function:: void driver_unregister(struct device_driver *drv)

    remove driver from system.

    :param struct device_driver \*drv:
        driver.

.. _`driver_unregister.description`:

Description
-----------

Again, we pass off most of the work to the bus-level call.

.. _`driver_find`:

driver_find
===========

.. c:function:: struct device_driver *driver_find(const char *name, struct bus_type *bus)

    locate driver on a bus by its name.

    :param const char \*name:
        name of the driver.

    :param struct bus_type \*bus:
        bus to scan for the driver.

.. _`driver_find.description`:

Description
-----------

Call \ :c:func:`kset_find_obj`\  to iterate over list of drivers on
a bus to find driver by name. Return driver if found.

This routine provides no locking to prevent the driver it returns
from being unregistered or unloaded while the caller is using it.
The caller is responsible for preventing this.

.. This file was automatic generated / don't edit.

