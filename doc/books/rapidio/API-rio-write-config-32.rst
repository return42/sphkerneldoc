
.. _API-rio-write-config-32:

===================
rio_write_config_32
===================

*man rio_write_config_32(9)*

*4.6.0-rc1*

Write 32 bits to configuration space


Synopsis
========

.. c:function:: int rio_write_config_32( struct rio_dev * rdev, u32 offset, u32 data )

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

Writes 32 bits of data to the specified offset within the RIO device's configuration space.
