.. -*- coding: utf-8; mode: rst -*-

=======
tiocx.c
=======


.. _`tiocx_match`:

tiocx_match
===========

.. c:function:: int tiocx_match (struct device *dev, struct device_driver *drv)

    Try to match driver id list with device.

    :param struct device \*dev:
        device pointer

    :param struct device_driver \*drv:
        driver pointer



.. _`tiocx_match.description`:

Description
-----------

Returns 1 if match, 0 otherwise.



.. _`cx_device_match`:

cx_device_match
===============

.. c:function:: const struct cx_device_id *cx_device_match (const struct cx_device_id *ids, struct cx_dev *cx_device)

    Find cx_device in the id table.

    :param const struct cx_device_id \*ids:
        id table from driver

    :param struct cx_dev \*cx_device:
        part/mfg id for the device



.. _`cx_device_probe`:

cx_device_probe
===============

.. c:function:: int cx_device_probe (struct device *dev)

    Look for matching device. Call driver probe routine if found.

    :param struct device \*dev:

        *undescribed*



.. _`cx_driver_remove`:

cx_driver_remove
================

.. c:function:: int cx_driver_remove (struct device *dev)

    Remove driver from device struct.

    :param struct device \*dev:
        device



.. _`cx_driver_register`:

cx_driver_register
==================

.. c:function:: int cx_driver_register (struct cx_drv *cx_driver)

    Register the driver.

    :param struct cx_drv \*cx_driver:
        driver table (cx_drv struct) from driver



.. _`cx_driver_register.description`:

Description
-----------

Called from the driver init routine to register a driver.
The cx_drv struct contains the driver name, a pointer to
a table of part/mfg numbers and a pointer to the driver's
probe/attach routine.



.. _`cx_driver_unregister`:

cx_driver_unregister
====================

.. c:function:: int cx_driver_unregister (struct cx_drv *cx_driver)

    Unregister the driver.

    :param struct cx_drv \*cx_driver:
        driver table (cx_drv struct) from driver



.. _`cx_device_register`:

cx_device_register
==================

.. c:function:: int cx_device_register (nasid_t nasid, int part_num, int mfg_num, struct hubdev_info *hubdev, int bt)

    Register a device.

    :param nasid_t nasid:
        device's nasid

    :param int part_num:
        device's part number

    :param int mfg_num:
        device's manufacturer number

    :param struct hubdev_info \*hubdev:
        hub info associated with this device

    :param int bt:
        board type of the device



.. _`cx_device_unregister`:

cx_device_unregister
====================

.. c:function:: int cx_device_unregister (struct cx_dev *cx_dev)

    Unregister a device.

    :param struct cx_dev \*cx_dev:
        part/mfg id for the device



.. _`cx_device_reload`:

cx_device_reload
================

.. c:function:: int cx_device_reload (struct cx_dev *cx_dev)

    Reload the device.

    :param struct cx_dev \*cx_dev:

        *undescribed*



.. _`cx_device_reload.description`:

Description
-----------

Remove the device associated with 'nasid' from device list and then
call device-register with the given part/mfg numbers.

