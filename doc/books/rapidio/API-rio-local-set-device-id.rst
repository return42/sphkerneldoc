.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-local-set-device-id:

=======================
rio_local_set_device_id
=======================

*man rio_local_set_device_id(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
