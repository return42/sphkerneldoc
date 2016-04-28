.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-get-device-id:

=================
rio_get_device_id
=================

*man rio_get_device_id(9)*

*4.6.0-rc5*

Get the base/extended device id for a device


Synopsis
========

.. c:function:: u16 rio_get_device_id( struct rio_mport * port, u16 destid, u8 hopcount )

Arguments
=========

``port``
    RIO master port

``destid``
    Destination ID of device

``hopcount``
    Hopcount to device


Description
===========

Reads the base/extended device id from a device. Returns the 8/16-bit
device ID.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
