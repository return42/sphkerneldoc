.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-device-add-resources:

=============================
platform_device_add_resources
=============================

*man platform_device_add_resources(9)*

*4.6.0-rc5*

add resources to a platform device


Synopsis
========

.. c:function:: int platform_device_add_resources( struct platform_device * pdev, const struct resource * res, unsigned int num )

Arguments
=========

``pdev``
    platform device allocated by platform_device_alloc to add
    resources to

``res``
    set of resources that needs to be allocated for the device

``num``
    number of resources


Description
===========

Add a copy of the resources to the platform device. The memory
associated with the resources will be freed when the platform device is
released.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
