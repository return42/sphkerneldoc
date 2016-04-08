
.. _API-rio-local-write-config-8:

========================
rio_local_write_config_8
========================

*man rio_local_write_config_8(9)*

*4.6.0-rc1*

Write 8 bits to local configuration space


Synopsis
========

.. c:function:: int rio_local_write_config_8( struct rio_mport * port, u32 offset, u8 data )

Arguments
=========

``port``
    Master port

``offset``
    Offset into local configuration space

``data``
    Data to be written


Description
===========

Writes 8 bits of data to the specified offset within the local device's configuration space.
