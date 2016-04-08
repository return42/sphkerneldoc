
.. _API-rio-write-config-8:

==================
rio_write_config_8
==================

*man rio_write_config_8(9)*

*4.6.0-rc1*

Write 8 bits to configuration space


Synopsis
========

.. c:function:: int rio_write_config_8( struct rio_dev * rdev, u32 offset, u8 data )

Arguments
=========

``rdev``
    RIO device

``offset``
    Offset into device configuration space

``data``
    Data to be written


Description
===========

Writes 8 bits of data to the specified offset within the RIO device's configuration space.
