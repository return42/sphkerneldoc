
.. _API-platform-device-add-data:

========================
platform_device_add_data
========================

*man platform_device_add_data(9)*

*4.6.0-rc1*

add platform-specific data to a platform device


Synopsis
========

.. c:function:: int platform_device_add_data( struct platform_device * pdev, const void * data, size_t size )

Arguments
=========

``pdev``
    platform device allocated by platform_device_alloc to add resources to

``data``
    platform specific data for this platform device

``size``
    size of platform specific data


Description
===========

Add a copy of platform specific data to the platform device's platform_data pointer. The memory associated with the platform data will be freed when the platform device is
released.
