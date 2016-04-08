
.. _API-rio-local-read-config-32:

========================
rio_local_read_config_32
========================

*man rio_local_read_config_32(9)*

*4.6.0-rc1*

Read 32 bits from local configuration space


Synopsis
========

.. c:function:: int rio_local_read_config_32( struct rio_mport * port, u32 offset, u32 * data )

Arguments
=========

``port``
    Master port

``offset``
    Offset into local configuration space

``data``
    Pointer to read data into


Description
===========

Reads 32 bits of data from the specified offset within the local device's configuration space.
