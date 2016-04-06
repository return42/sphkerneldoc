
.. _API-i2c-smbus-read-i2c-block-data-or-emulated:

=========================================
i2c_smbus_read_i2c_block_data_or_emulated
=========================================

*man i2c_smbus_read_i2c_block_data_or_emulated(9)*

*4.6.0-rc1*

read block or emulate


Synopsis
========

.. c:function:: s32 i2c_smbus_read_i2c_block_data_or_emulated( const struct i2c_client * client, u8 command, u8 length, u8 * values )

Arguments
=========

``client``
    Handle to slave device

``command``
    Byte interpreted by slave

``length``
    Size of data block; SMBus allows at most I2C_SMBUS_BLOCK_MAX bytes

``values``
    Byte array into which data will be read; big enough to hold the data returned by the slave. SMBus allows at most I2C_SMBUS_BLOCK_MAX bytes.


Description
===========

This executes the SMBus “block read” protocol if supported by the adapter. If block read is not supported, it emulates it using either word or byte read protocols depending on
availability.

The addresses of the I2C slave device that are accessed with this function must be mapped to a linear region, so that a block read will have the same effect as a byte read. Before
using this function you must double-check if the I2C slave does support exchanging a block transfer with a byte transfer.
