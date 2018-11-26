.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rapidio/rio-driver.c

.. _`rio_match_device`:

rio_match_device
================

.. c:function:: const struct rio_device_id *rio_match_device(const struct rio_device_id *id, const struct rio_dev *rdev)

    Tell if a RIO device has a matching RIO device id structure

    :param id:
        the RIO device id structure to match against
    :type id: const struct rio_device_id \*

    :param rdev:
        the RIO device structure to match against
    :type rdev: const struct rio_dev \*

.. _`rio_match_device.description`:

Description
-----------

 Used from driver probe and bus matching to check whether a RIO device
 matches a device id structure provided by a RIO driver. Returns the
 matching \ :c:type:`struct rio_device_id <rio_device_id>`\  or \ ``NULL``\  if there is no match.

.. _`rio_dev_get`:

rio_dev_get
===========

.. c:function:: struct rio_dev *rio_dev_get(struct rio_dev *rdev)

    Increments the reference count of the RIO device structure

    :param rdev:
        RIO device being referenced
    :type rdev: struct rio_dev \*

.. _`rio_dev_get.description`:

Description
-----------

Each live reference to a device should be refcounted.

Drivers for RIO devices should normally record such references in
their \ :c:func:`probe`\  methods, when they bind to a device, and release
them by calling \ :c:func:`rio_dev_put`\ , in their \ :c:func:`disconnect`\  methods.

.. _`rio_dev_put`:

rio_dev_put
===========

.. c:function:: void rio_dev_put(struct rio_dev *rdev)

    Release a use of the RIO device structure

    :param rdev:
        RIO device being disconnected
    :type rdev: struct rio_dev \*

.. _`rio_dev_put.description`:

Description
-----------

Must be called when a user of a device is finished with it.
When the last user of the device calls this function, the
memory of the device is freed.

.. _`rio_device_probe`:

rio_device_probe
================

.. c:function:: int rio_device_probe(struct device *dev)

    Tell if a RIO device structure has a matching RIO device id structure

    :param dev:
        the RIO device structure to match against
    :type dev: struct device \*

.. _`rio_device_probe.description`:

Description
-----------

return 0 and set rio_dev->driver when drv claims rio_dev, else error

.. _`rio_device_remove`:

rio_device_remove
=================

.. c:function:: int rio_device_remove(struct device *dev)

    Remove a RIO device from the system

    :param dev:
        the RIO device structure to match against
    :type dev: struct device \*

.. _`rio_device_remove.description`:

Description
-----------

Remove a RIO device from the system. If it has an associated
driver, then run the driver \ :c:func:`remove`\  method.  Then update
the reference count.

.. _`rio_register_driver`:

rio_register_driver
===================

.. c:function:: int rio_register_driver(struct rio_driver *rdrv)

    register a new RIO driver

    :param rdrv:
        the RIO driver structure to register
    :type rdrv: struct rio_driver \*

.. _`rio_register_driver.description`:

Description
-----------

 Adds a \ :c:type:`struct rio_driver <rio_driver>`\  to the list of registered drivers.
 Returns a negative value on error, otherwise 0. If no error
 occurred, the driver remains registered even if no device
 was claimed during registration.

.. _`rio_unregister_driver`:

rio_unregister_driver
=====================

.. c:function:: void rio_unregister_driver(struct rio_driver *rdrv)

    unregister a RIO driver

    :param rdrv:
        the RIO driver structure to unregister
    :type rdrv: struct rio_driver \*

.. _`rio_unregister_driver.description`:

Description
-----------

 Deletes the \ :c:type:`struct rio_driver <rio_driver>`\  from the list of registered RIO
 drivers, gives it a chance to clean up by calling its \ :c:func:`remove`\ 
 function for each device it was responsible for, and marks those
 devices as driverless.

.. _`rio_match_bus`:

rio_match_bus
=============

.. c:function:: int rio_match_bus(struct device *dev, struct device_driver *drv)

    Tell if a RIO device structure has a matching RIO driver device id structure

    :param dev:
        the standard device structure to match against
    :type dev: struct device \*

    :param drv:
        the standard driver structure containing the ids to match against
    :type drv: struct device_driver \*

.. _`rio_match_bus.description`:

Description
-----------

 Used by a driver to check whether a RIO device present in the
 system is in its list of supported devices. Returns 1 if
 there is a matching \ :c:type:`struct rio_device_id <rio_device_id>`\  or 0 if there is
 no match.

.. _`rio_bus_init`:

rio_bus_init
============

.. c:function:: int rio_bus_init( void)

    Register the RapidIO bus with the device model

    :param void:
        no arguments
    :type void: 

.. _`rio_bus_init.description`:

Description
-----------

 Registers the RIO mport device class and RIO bus type with the Linux
 device model.

.. This file was automatic generated / don't edit.

