
.. _API-i915-gem-set-tiling:

===================
i915_gem_set_tiling
===================

*man i915_gem_set_tiling(9)*

*4.6.0-rc1*

IOCTL handler to set tiling mode


Synopsis
========

.. c:function:: int i915_gem_set_tiling( struct drm_device * dev, void * data, struct drm_file * file )

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

Sets the tiling mode of an object, returning the required swizzling of bit 6 of addresses in the object.

Called by the user via ioctl.


Returns
=======

Zero on success, negative errno on failure.
