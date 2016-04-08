
.. _API-RIO-LOP-WRITE:

=============
RIO_LOP_WRITE
=============

*man RIO_LOP_WRITE(9)*

*4.6.0-rc1*

Generate rio_local_write_config_⋆ functions


Synopsis
========

.. c:function:: RIO_LOP_WRITE( size, type, len )

Arguments
=========

``size``
    Size of configuration space write (8, 16, 32 bits)

``type``
    C type of value argument

``len``
    Length of configuration space write (1, 2, 4 bytes)


Description
===========

Generates rio_local_write_config_⋆ functions used to access configuration space registers on the local device.
