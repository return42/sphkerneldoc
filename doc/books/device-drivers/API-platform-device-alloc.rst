
.. _API-platform-device-alloc:

=====================
platform_device_alloc
=====================

*man platform_device_alloc(9)*

*4.6.0-rc1*

create a platform device


Synopsis
========

.. c:function:: struct platform_device ⋆ platform_device_alloc( const char * name, int id )

Arguments
=========

``name``
    base name of the device we're adding

``id``
    instance id


Description
===========

Create a platform device object which can have other objects attached to it, and which will have attached objects freed when it is released.
