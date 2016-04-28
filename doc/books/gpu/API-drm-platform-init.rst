.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-platform-init:

=================
drm_platform_init
=================

*man drm_platform_init(9)*

*4.6.0-rc5*

Register a platform device with the DRM subsystem


Synopsis
========

.. c:function:: int drm_platform_init( struct drm_driver * driver, struct platform_device * platform_device )

Arguments
=========

``driver``
    DRM device driver

``platform_device``
    platform device to register


Description
===========

Registers the specified DRM device driver and platform device with the
DRM subsystem, initializing a drm_device structure and calling the
driver's .\ ``load`` function.


NOTE
====

This function is deprecated, please use ``drm_dev_alloc`` and
``drm_dev_register`` instead and remove your ->``load`` callback.


Return
======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
