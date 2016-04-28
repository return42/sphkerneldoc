.. -*- coding: utf-8; mode: rst -*-

.. _API-RIO-OP-WRITE:

============
RIO_OP_WRITE
============

*man RIO_OP_WRITE(9)*

*4.6.0-rc5*

Generate rio_mport_write_config_* functions


Synopsis
========

.. c:function:: RIO_OP_WRITE( size, type, len )

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

Generates rio_mport_write_config_* functions used to access
configuration space registers on the local device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
