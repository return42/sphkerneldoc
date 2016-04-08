
.. _API-rio-set-device-id:

=================
rio_set_device_id
=================

*man rio_set_device_id(9)*

*4.6.0-rc1*

Set the base/extended device id for a device


Synopsis
========

.. c:function:: void rio_set_device_id( struct rio_mport * port, u16 destid, u8 hopcount, u16 did )

Arguments
=========

``port``
    RIO master port

``destid``
    Destination ID of device

``hopcount``
    Hopcount to device

``did``
    Device ID value to be written


Description
===========

Writes the base/extended device id from a device.
