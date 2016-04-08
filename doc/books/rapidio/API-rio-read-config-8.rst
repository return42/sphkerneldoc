
.. _API-rio-read-config-8:

=================
rio_read_config_8
=================

*man rio_read_config_8(9)*

*4.6.0-rc1*

Read 8 bits from configuration space


Synopsis
========

.. c:function:: int rio_read_config_8( struct rio_dev * rdev, u32 offset, u8 * data )

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

Reads 8 bits of data from the specified offset within the RIO device's configuration space.
