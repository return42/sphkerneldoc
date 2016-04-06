
.. _API-i2c-smbus-xfer:

==============
i2c_smbus_xfer
==============

*man i2c_smbus_xfer(9)*

*4.6.0-rc1*

execute SMBus protocol operations


Synopsis
========

.. c:function:: s32 i2c_smbus_xfer( struct i2c_adapter * adapter, u16 addr, unsigned short flags, char read_write, u8 command, int protocol, union i2c_smbus_data * data )

Arguments
=========

``adapter``
    Handle to I2C bus

``addr``
    Address of SMBus slave on that bus

``flags``
    I2C_CLIENT_⋆ flags (usually zero or I2C_CLIENT_PEC)

``read_write``
    I2C_SMBUS_READ or I2C_SMBUS_WRITE

``command``
    Byte interpreted by slave, for protocols which use such bytes

``protocol``
    SMBus protocol operation to execute, such as I2C_SMBUS_PROC_CALL

``data``
    Data to be read or written


Description
===========

This executes an SMBus protocol operation, and returns a negative errno code else zero on success.
