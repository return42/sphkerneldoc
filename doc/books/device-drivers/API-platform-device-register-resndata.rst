
.. _API-platform-device-register-resndata:

=================================
platform_device_register_resndata
=================================

*man platform_device_register_resndata(9)*

*4.6.0-rc1*

add a platform-level device with resources and platform-specific data


Synopsis
========

.. c:function:: struct platform_device ⋆ platform_device_register_resndata( struct device * parent, const char * name, int id, const struct resource * res, unsigned int num, const void * data, size_t size )

Arguments
=========

``parent``
    parent device for the device we're adding

``name``
    base name of the device we're adding

``id``
    instance id

``res``
    set of resources that needs to be allocated for the device

``num``
    number of resources

``data``
    platform specific data for this platform device

``size``
    size of platform specific data


Description
===========

Returns ``struct platform_device`` pointer on success, or ``ERR_PTR`` on error.
