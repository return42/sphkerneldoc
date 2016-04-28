.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-local-write-config-8:

========================
rio_local_write_config_8
========================

*man rio_local_write_config_8(9)*

*4.6.0-rc5*

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

Writes 8 bits of data to the specified offset within the local device's
configuration space.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
