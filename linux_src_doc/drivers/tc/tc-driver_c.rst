.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tc/tc-driver.c

.. _`tc_register_driver`:

tc_register_driver
==================

.. c:function:: int tc_register_driver(struct tc_driver *tdrv)

    register a new TC driver

    :param tdrv:
        *undescribed*
    :type tdrv: struct tc_driver \*

.. _`tc_register_driver.description`:

Description
-----------

Adds the driver structure to the list of registered drivers
Returns a negative value on error, otherwise 0.
If no error occurred, the driver remains registered even if
no device was claimed during registration.

.. _`tc_unregister_driver`:

tc_unregister_driver
====================

.. c:function:: void tc_unregister_driver(struct tc_driver *tdrv)

    unregister a TC driver

    :param tdrv:
        *undescribed*
    :type tdrv: struct tc_driver \*

.. _`tc_unregister_driver.description`:

Description
-----------

Deletes the driver structure from the list of registered TC drivers,
gives it a chance to clean up by calling its \ :c:func:`remove`\  function for
each device it was responsible for, and marks those devices as
driverless.

.. _`tc_match_device`:

tc_match_device
===============

.. c:function:: const struct tc_device_id *tc_match_device(struct tc_driver *tdrv, struct tc_dev *tdev)

    tell if a TC device structure has a matching TC device ID structure

    :param tdrv:
        the TC driver to earch for matching TC device ID strings
    :type tdrv: struct tc_driver \*

    :param tdev:
        the TC device structure to match against
    :type tdev: struct tc_dev \*

.. _`tc_match_device.description`:

Description
-----------

Used by a driver to check whether a TC device present in the
system is in its list of supported devices.  Returns the matching
tc_device_id structure or \ ``NULL``\  if there is no match.

.. _`tc_bus_match`:

tc_bus_match
============

.. c:function:: int tc_bus_match(struct device *dev, struct device_driver *drv)

    Tell if a device structure has a matching TC device ID structure

    :param dev:
        the device structure to match against
    :type dev: struct device \*

    :param drv:
        the device driver to search for matching TC device ID strings
    :type drv: struct device_driver \*

.. _`tc_bus_match.description`:

Description
-----------

Used by a driver to check whether a TC device present in the
system is in its list of supported devices.  Returns 1 if there
is a match or 0 otherwise.

.. This file was automatic generated / don't edit.

