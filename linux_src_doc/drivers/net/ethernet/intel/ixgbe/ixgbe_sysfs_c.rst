.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_sysfs.c

.. _`ixgbe_add_hwmon_attr`:

ixgbe_add_hwmon_attr
====================

.. c:function:: int ixgbe_add_hwmon_attr(struct ixgbe_adapter *adapter, unsigned int offset, int type)

    Create hwmon attr table for a hwmon sysfs file.

    :param adapter:
        pointer to the adapter structure
    :type adapter: struct ixgbe_adapter \*

    :param offset:
        offset in the eeprom sensor data table
    :type offset: unsigned int

    :param type:
        type of sensor data to display
    :type type: int

.. _`ixgbe_add_hwmon_attr.description`:

Description
-----------

For each file we want in hwmon's sysfs interface we need a device_attribute
This is included in our hwmon_attr struct that contains the references to
the data structures we need to get the data to display.

.. This file was automatic generated / don't edit.

