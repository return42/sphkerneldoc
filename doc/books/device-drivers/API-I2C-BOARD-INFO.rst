
.. _API-I2C-BOARD-INFO:

==============
I2C_BOARD_INFO
==============

*man I2C_BOARD_INFO(9)*

*4.6.0-rc1*

macro used to list an i2c device and its address


Synopsis
========

.. c:function:: I2C_BOARD_INFO( dev_type, dev_addr )

Arguments
=========

``dev_type``
    identifies the device type

``dev_addr``
    the device's address on the bus.


Description
===========

This macro initializes essential fields of a struct i2c_board_info, declaring what has been provided on a particular board. Optional fields (such as associated irq, or
device-specific platform_data) are provided using conventional syntax.
