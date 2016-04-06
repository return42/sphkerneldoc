
.. _API-i2c-smbus-read-block-data:

=========================
i2c_smbus_read_block_data
=========================

*man i2c_smbus_read_block_data(9)*

*4.6.0-rc1*

SMBus “block read” protocol


Synopsis
========

.. c:function:: s32 i2c_smbus_read_block_data( const struct i2c_client * client, u8 command, u8 * values )

Arguments
=========

``client``
    Handle to slave device

``command``
    Byte interpreted by slave

``values``
    Byte array into which data will be read; big enough to hold the data returned by the slave. SMBus allows at most 32 bytes.


Description
===========

This executes the SMBus “block read” protocol, returning negative errno else the number of data bytes in the slave's response.

Note that using this function requires that the client's adapter support the I2C_FUNC_SMBUS_READ_BLOCK_DATA functionality. Not all adapter drivers support this; its emulation
through I2C messaging relies on a specific mechanism (I2C_M_RECV_LEN) which may not be implemented.
