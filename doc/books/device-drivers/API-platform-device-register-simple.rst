
.. _API-platform-device-register-simple:

===============================
platform_device_register_simple
===============================

*man platform_device_register_simple(9)*

*4.6.0-rc1*

add a platform-level device and its resources


Synopsis
========

.. c:function:: struct platform_device ⋆ platform_device_register_simple( const char * name, int id, const struct resource * res, unsigned int num )

Arguments
=========

``name``
    base name of the device we're adding

``id``
    instance id

``res``
    set of resources that needs to be allocated for the device

``num``
    number of resources


Description
===========

This function creates a simple platform device that requires minimal resource and memory management. Canned release function freeing memory allocated for the device allows drivers
using such devices to be unloaded without waiting for the last reference to the device to be dropped.

This interface is primarily intended for use with legacy drivers which probe hardware directly. Because such drivers create sysfs device nodes themselves, rather than letting
system infrastructure handle such device enumeration tasks, they don't fully conform to the Linux driver model. In particular, when such drivers are built as modules, they can't be
“hotplugged”.

Returns ``struct platform_device`` pointer on success, or ``ERR_PTR`` on error.
