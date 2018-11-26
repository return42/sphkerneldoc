.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dio/dio-driver.c

.. _`dio_match_device`:

dio_match_device
================

.. c:function:: const struct dio_device_id *dio_match_device(const struct dio_device_id *ids, const struct dio_dev *d)

    Tell if a DIO device structure has a matching DIO device id structure

    :param ids:
        array of DIO device id structures to search in
    :type ids: const struct dio_device_id \*

    :param d:
        the DIO device structure to match against
    :type d: const struct dio_dev \*

.. _`dio_match_device.description`:

Description
-----------

Used by a driver to check whether a DIO device present in the
system is in its list of supported devices. Returns the matching
dio_device_id structure or \ ``NULL``\  if there is no match.

.. _`dio_register_driver`:

dio_register_driver
===================

.. c:function:: int dio_register_driver(struct dio_driver *drv)

    register a new DIO driver

    :param drv:
        the driver structure to register
    :type drv: struct dio_driver \*

.. _`dio_register_driver.description`:

Description
-----------

Adds the driver structure to the list of registered drivers
Returns zero or a negative error value.

.. _`dio_unregister_driver`:

dio_unregister_driver
=====================

.. c:function:: void dio_unregister_driver(struct dio_driver *drv)

    unregister a DIO driver

    :param drv:
        the driver structure to unregister
    :type drv: struct dio_driver \*

.. _`dio_unregister_driver.description`:

Description
-----------

Deletes the driver structure from the list of registered DIO drivers,
gives it a chance to clean up by calling its \ :c:func:`remove`\  function for
each device it was responsible for, and marks those devices as
driverless.

.. _`dio_bus_match`:

dio_bus_match
=============

.. c:function:: int dio_bus_match(struct device *dev, struct device_driver *drv)

    Tell if a DIO device structure has a matching DIO device id structure

    :param dev:
        the DIO device structure to match against
    :type dev: struct device \*

    :param drv:
        the \ :c:type:`struct device_driver <device_driver>`\  that points to the array of DIO device id structures to search
    :type drv: struct device_driver \*

.. _`dio_bus_match.description`:

Description
-----------

Used by a driver to check whether a DIO device present in the
system is in its list of supported devices. Returns the matching
dio_device_id structure or \ ``NULL``\  if there is no match.

.. This file was automatic generated / don't edit.

