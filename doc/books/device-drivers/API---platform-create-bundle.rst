
.. _API---platform-create-bundle:

========================
__platform_create_bundle
========================

*man __platform_create_bundle(9)*

*4.6.0-rc1*

register driver and create corresponding device


Synopsis
========

.. c:function:: struct platform_device ⋆ __platform_create_bundle( struct platform_driver * driver, int (*probe) struct platform_device *, struct resource * res, unsigned int n_res, const void * data, size_t size, struct module * module )

Arguments
=========

``driver``
    platform driver structure

``probe``
    the driver probe routine, probably from an __init section

``res``
    set of resources that needs to be allocated for the device

``n_res``
    number of resources

``data``
    platform specific data for this platform device

``size``
    size of platform specific data

``module``
    module which will be the owner of the driver


Description
===========

Use this in legacy-style modules that probe hardware directly and register a single platform device and corresponding platform driver.

Returns ``struct platform_device`` pointer on success, or ``ERR_PTR`` on error.
