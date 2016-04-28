.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-device-register-data:

=============================
platform_device_register_data
=============================

*man platform_device_register_data(9)*

*4.6.0-rc5*

add a platform-level device with platform-specific data


Synopsis
========

.. c:function:: struct platform_device * platform_device_register_data( struct device * parent, const char * name, int id, const void * data, size_t size )

Arguments
=========

``parent``
    parent device for the device we're adding

``name``
    base name of the device we're adding

``id``
    instance id

``data``
    platform specific data for this platform device

``size``
    size of platform specific data


Description
===========

This function creates a simple platform device that requires minimal
resource and memory management. Canned release function freeing memory
allocated for the device allows drivers using such devices to be
unloaded without waiting for the last reference to the device to be
dropped.

Returns ``struct platform_device`` pointer on success, or ``ERR_PTR`` on
error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
