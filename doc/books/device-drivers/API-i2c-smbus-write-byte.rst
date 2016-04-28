.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-smbus-write-byte:

====================
i2c_smbus_write_byte
====================

*man i2c_smbus_write_byte(9)*

*4.6.0-rc5*

SMBus “send byte” protocol


Synopsis
========

.. c:function:: s32 i2c_smbus_write_byte( const struct i2c_client * client, u8 value )

Arguments
=========

``client``
    Handle to slave device

``value``
    Byte to be sent


Description
===========

This executes the SMBus “send byte” protocol, returning negative errno
else zero on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
