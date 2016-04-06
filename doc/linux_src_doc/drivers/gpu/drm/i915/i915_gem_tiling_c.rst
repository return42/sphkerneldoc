.. -*- coding: utf-8; mode: rst -*-

=================
i915_gem_tiling.c
=================



.. _xref_i915_gem_set_tiling:

i915_gem_set_tiling
===================

.. c:function:: int i915_gem_set_tiling (struct drm_device * dev, void * data, struct drm_file * file)

    IOCTL handler to set tiling mode

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file:
        DRM file for the ioctl call



Description
-----------

Sets the tiling mode of an object, returning the required swizzling of
bit 6 of addresses in the object.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.




.. _xref_i915_gem_get_tiling:

i915_gem_get_tiling
===================

.. c:function:: int i915_gem_get_tiling (struct drm_device * dev, void * data, struct drm_file * file)

    IOCTL handler to get tiling mode

    :param struct drm_device * dev:
        DRM device

    :param void * data:
        data pointer for the ioctl

    :param struct drm_file * file:
        DRM file for the ioctl call



Description
-----------

Returns the current tiling mode and required bit 6 swizzling for the object.


Called by the user via ioctl.



Returns
-------

Zero on success, negative errno on failure.


