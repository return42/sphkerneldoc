.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-smbus-read-word-data:

========================
i2c_smbus_read_word_data
========================

*man i2c_smbus_read_word_data(9)*

*4.6.0-rc5*

SMBus “read word” protocol


Synopsis
========

.. c:function:: s32 i2c_smbus_read_word_data( const struct i2c_client * client, u8 command )

Arguments
=========

``client``
    Handle to slave device

``command``
    Byte interpreted by slave


Description
===========

This executes the SMBus “read word” protocol, returning negative errno
else a 16-bit unsigned “word” received from the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
