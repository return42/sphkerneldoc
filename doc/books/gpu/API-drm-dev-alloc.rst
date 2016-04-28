.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dev-alloc:

=============
drm_dev_alloc
=============

*man drm_dev_alloc(9)*

*4.6.0-rc5*

Allocate new DRM device


Synopsis
========

.. c:function:: struct drm_device * drm_dev_alloc( struct drm_driver * driver, struct device * parent )

Arguments
=========

``driver``
    DRM driver to allocate device for

``parent``
    Parent device object


Description
===========

Allocate and initialize a new DRM device. No device registration is
done. Call ``drm_dev_register`` to advertice the device to user space
and register it with other core subsystems. This should be done last in
the device initialization sequence to make sure userspace can't access
an inconsistent state.

The initial ref-count of the object is 1. Use ``drm_dev_ref`` and
``drm_dev_unref`` to take and drop further ref-counts.

Note that for purely virtual devices ``parent`` can be NULL.


RETURNS
=======

Pointer to new DRM device, or NULL if out of memory.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
