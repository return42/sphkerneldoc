
.. _API-rio-read-config-16:

==================
rio_read_config_16
==================

*man rio_read_config_16(9)*

*4.6.0-rc1*

Read 16 bits from configuration space


Synopsis
========

.. c:function:: int rio_read_config_16( struct rio_dev * rdev, u32 offset, u16 * data )

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

Reads 16 bits of data from the specified offset within the RIO device's configuration space.
