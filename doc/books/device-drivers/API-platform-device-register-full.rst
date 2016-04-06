
.. _API-platform-device-register-full:

=============================
platform_device_register_full
=============================

*man platform_device_register_full(9)*

*4.6.0-rc1*

add a platform-level device with resources and platform-specific data


Synopsis
========

.. c:function:: struct platform_device ⋆ platform_device_register_full( const struct platform_device_info * pdevinfo )

Arguments
=========

``pdevinfo``
    data used to create device


Description
===========

Returns ``struct platform_device`` pointer on success, or ``ERR_PTR`` on error.
