
.. _API-rio-local-get-device-id:

=======================
rio_local_get_device_id
=======================

*man rio_local_get_device_id(9)*

*4.6.0-rc1*

Get the base/extended device id for a port


Synopsis
========

.. c:function:: u16 rio_local_get_device_id( struct rio_mport * port )

Arguments
=========

``port``
    RIO master port from which to get the deviceid


Description
===========

Reads the base/extended device id from the local device implementing the master port. Returns the 8/16-bit device id.
