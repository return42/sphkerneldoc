
.. _API-i2c-smbus-write-block-data:

==========================
i2c_smbus_write_block_data
==========================

*man i2c_smbus_write_block_data(9)*

*4.6.0-rc1*

SMBus “block write” protocol


Synopsis
========

.. c:function:: s32 i2c_smbus_write_block_data( const struct i2c_client * client, u8 command, u8 length, const u8 * values )

Arguments
=========

``client``
    Handle to slave device

``command``
    Byte interpreted by slave

``length``
    Size of data block; SMBus allows at most 32 bytes

``values``
    Byte array which will be written.


Description
===========

This executes the SMBus “block write” protocol, returning negative errno else zero on success.
