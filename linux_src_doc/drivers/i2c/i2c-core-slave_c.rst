.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/i2c-core-slave.c

.. _`i2c_detect_slave_mode`:

i2c_detect_slave_mode
=====================

.. c:function:: bool i2c_detect_slave_mode(struct device *dev)

    detect operation mode

    :param struct device \*dev:
        The device owning the bus

.. _`i2c_detect_slave_mode.description`:

Description
-----------

This checks the device nodes for an I2C slave by checking the address
used in the reg property. If the address match the I2C_OWN_SLAVE_ADDRESS
flag this means the device is configured to act as a I2C slave and it will
be listening at that address.

Returns true if an I2C own slave address is detected, otherwise returns
false.

.. This file was automatic generated / don't edit.

