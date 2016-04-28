.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-write-config-16:

===================
rio_write_config_16
===================

*man rio_write_config_16(9)*

*4.6.0-rc5*

Write 16 bits to configuration space


Synopsis
========

.. c:function:: int rio_write_config_16( struct rio_dev * rdev, u32 offset, u16 data )

Arguments
=========

``rdev``
    RIO device

``offset``
    Offset into device configuration space

``data``
    Data to be written


Description
===========

Writes 16 bits of data to the specified offset within the RIO device's
configuration space.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
