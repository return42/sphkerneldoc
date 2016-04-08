
.. _API-rio-local-set-device-id:

=======================
rio_local_set_device_id
=======================

*man rio_local_set_device_id(9)*

*4.6.0-rc1*

Set the base/extended device id for a port


Synopsis
========

.. c:function:: void rio_local_set_device_id( struct rio_mport * port, u16 did )

Arguments
=========

``port``
    RIO master port

``did``
    Device ID value to be written


Description
===========

Writes the base/extended device id from a device.
