
.. _API-rio-get-device-id:

=================
rio_get_device_id
=================

*man rio_get_device_id(9)*

*4.6.0-rc1*

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

Reads the base/extended device id from a device. Returns the 8/16-bit device ID.
