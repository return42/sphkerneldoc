.. -*- coding: utf-8; mode: rst -*-

.. _API-device-destroy:

==============
device_destroy
==============

*man device_destroy(9)*

*4.6.0-rc5*

removes a device that was created with ``device_create``


Synopsis
========

.. c:function:: void device_destroy( struct class * class, dev_t devt )

Arguments
=========

``class``
    pointer to the struct class that this device was registered with

``devt``
    the dev_t of the device that was previously registered


Description
===========

This call unregisters and cleans up a device that was created with a
call to ``device_create``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
