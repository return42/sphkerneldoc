.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-get-tiling:

===================
i915_gem_get_tiling
===================

*man i915_gem_get_tiling(9)*

*4.6.0-rc5*

IOCTL handler to get tiling mode


Synopsis
========

.. c:function:: int i915_gem_get_tiling( struct drm_device * dev, void * data, struct drm_file * file )

Arguments
=========

``dev``
    DRM device

``data``
    data pointer for the ioctl

``file``
    DRM file for the ioctl call


Description
===========

Returns the current tiling mode and required bit 6 swizzling for the
object.

Called by the user via ioctl.


Returns
=======

Zero on success, negative errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
