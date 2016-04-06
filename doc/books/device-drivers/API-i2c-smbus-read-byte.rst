
.. _API-i2c-smbus-read-byte:

===================
i2c_smbus_read_byte
===================

*man i2c_smbus_read_byte(9)*

*4.6.0-rc1*

SMBus “receive byte” protocol


Synopsis
========

.. c:function:: s32 i2c_smbus_read_byte( const struct i2c_client * client )

Arguments
=========

``client``
    Handle to slave device


Description
===========

This executes the SMBus “receive byte” protocol, returning negative errno else the byte received from the device.
