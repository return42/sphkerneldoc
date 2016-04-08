
.. _API-rio-local-read-config-8:

=======================
rio_local_read_config_8
=======================

*man rio_local_read_config_8(9)*

*4.6.0-rc1*

Read 8 bits from local configuration space


Synopsis
========

.. c:function:: int rio_local_read_config_8( struct rio_mport * port, u32 offset, u8 * data )

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

Reads 8 bits of data from the specified offset within the local device's configuration space.
