.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-local-read-config-16:

========================
rio_local_read_config_16
========================

*man rio_local_read_config_16(9)*

*4.6.0-rc5*

Read 16 bits from local configuration space


Synopsis
========

.. c:function:: int rio_local_read_config_16( struct rio_mport * port, u32 offset, u16 * data )

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

Reads 16 bits of data from the specified offset within the local
device's configuration space.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
