
.. _API-rio-read-config-32:

==================
rio_read_config_32
==================

*man rio_read_config_32(9)*

*4.6.0-rc1*

Read 32 bits from configuration space


Synopsis
========

.. c:function:: int rio_read_config_32( struct rio_dev * rdev, u32 offset, u32 * data )

Arguments
=========

``rdev``
    RIO device

``offset``
    Offset into device configuration space

``data``
    Pointer to read data into


Description
===========

Reads 32 bits of data from the specified offset within the RIO device's configuration space.
