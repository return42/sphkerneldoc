.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-device-alloc:

=====================
platform_device_alloc
=====================

*man platform_device_alloc(9)*

*4.6.0-rc5*

create a platform device


Synopsis
========

.. c:function:: struct platform_device * platform_device_alloc( const char * name, int id )

Arguments
=========

``name``
    base name of the device we're adding

``id``
    instance id


Description
===========

Create a platform device object which can have other objects attached to
it, and which will have attached objects freed when it is released.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
