.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-smbus-read-byte:

===================
i2c_smbus_read_byte
===================

*man i2c_smbus_read_byte(9)*

*4.6.0-rc5*

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

This executes the SMBus “receive byte” protocol, returning negative
errno else the byte received from the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
