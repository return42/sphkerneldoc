.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-device-unregister:

==========================
platform_device_unregister
==========================

*man platform_device_unregister(9)*

*4.6.0-rc5*

unregister a platform-level device


Synopsis
========

.. c:function:: void platform_device_unregister( struct platform_device * pdev )

Arguments
=========

``pdev``
    platform device we're unregistering


Description
===========

Unregistration is done in 2 steps. First we release all resources and
remove it from the subsystem, then we drop reference count by calling
``platform_device_put``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
