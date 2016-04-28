.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-device-add-properties:

==============================
platform_device_add_properties
==============================

*man platform_device_add_properties(9)*

*4.6.0-rc5*

add built-in properties to a platform device


Synopsis
========

.. c:function:: int platform_device_add_properties( struct platform_device * pdev, const struct property_set * pset )

Arguments
=========

``pdev``
    platform device to add properties to

``pset``
    properties to add


Description
===========

The function will take deep copy of the properties in ``pset`` and
attach the copy to the platform device. The memory associated with
properties will be freed when the platform device is released.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
