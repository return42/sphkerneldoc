
.. _API-RIO-OP-READ:

===========
RIO_OP_READ
===========

*man RIO_OP_READ(9)*

*4.6.0-rc1*

Generate rio_mport_read_config_⋆ functions


Synopsis
========

.. c:function:: RIO_OP_READ( size, type, len )

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

Generates rio_mport_read_config_⋆ functions used to access configuration space registers on the local device.
