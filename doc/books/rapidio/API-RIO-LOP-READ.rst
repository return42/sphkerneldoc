
.. _API-RIO-LOP-READ:

============
RIO_LOP_READ
============

*man RIO_LOP_READ(9)*

*4.6.0-rc1*

Generate rio_local_read_config_⋆ functions


Synopsis
========

.. c:function:: RIO_LOP_READ( size, type, len )

Arguments
=========

``size``
    Size of configuration space read (8, 16, 32 bits)

``type``
    C type of value argument

``len``
    Length of configuration space read (1, 2, 4 bytes)


Description
===========

Generates rio_local_read_config_⋆ functions used to access configuration space registers on the local device.
