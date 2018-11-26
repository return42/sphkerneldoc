.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/i2c-core-acpi.c

.. _`i2c_acpi_register_devices`:

i2c_acpi_register_devices
=========================

.. c:function:: void i2c_acpi_register_devices(struct i2c_adapter *adap)

    enumerate I2C slave devices behind adapter

    :param adap:
        pointer to adapter
    :type adap: struct i2c_adapter \*

.. _`i2c_acpi_register_devices.description`:

Description
-----------

Enumerate all I2C slave devices behind this adapter by walking the ACPI
namespace. When a device is found it will be added to the Linux device
model and bound to the corresponding ACPI handle.

.. _`i2c_acpi_find_bus_speed`:

i2c_acpi_find_bus_speed
=======================

.. c:function:: u32 i2c_acpi_find_bus_speed(struct device *dev)

    find I2C bus speed from ACPI

    :param dev:
        The device owning the bus
    :type dev: struct device \*

.. _`i2c_acpi_find_bus_speed.description`:

Description
-----------

Find the I2C bus speed by walking the ACPI namespace for all I2C slaves
devices connected to this bus and use the speed of slowest device.

Returns the speed in Hz or zero

.. _`i2c_acpi_new_device`:

i2c_acpi_new_device
===================

.. c:function:: struct i2c_client *i2c_acpi_new_device(struct device *dev, int index, struct i2c_board_info *info)

    Create i2c-client for the Nth I2cSerialBus resource

    :param dev:
        Device owning the ACPI resources to get the client from
    :type dev: struct device \*

    :param index:
        Index of ACPI resource to get
    :type index: int

    :param info:
        describes the I2C device; note this is modified (addr gets set)
    :type info: struct i2c_board_info \*

.. _`i2c_acpi_new_device.context`:

Context
-------

can sleep

.. _`i2c_acpi_new_device.description`:

Description
-----------

By default the i2c subsys creates an i2c-client for the first I2cSerialBus
resource of an acpi_device, but some acpi_devices have multiple I2cSerialBus
resources, in that case this function can be used to create an i2c-client
for other I2cSerialBus resources in the Current Resource Settings table.

Also see i2c_new_device, which this function calls to create the i2c-client.

Returns a pointer to the new i2c-client, or NULL if the adapter is not found.

.. This file was automatic generated / don't edit.

