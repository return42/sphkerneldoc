.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_tiling.c

.. _`i915_gem_set_tiling`:

i915_gem_set_tiling
===================

.. c:function:: int i915_gem_set_tiling(struct drm_device *dev, void *data, struct drm_file *file)

    IOCTL handler to set tiling mode

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file:
        DRM file for the ioctl call

.. _`i915_gem_set_tiling.description`:

Description
-----------

Sets the tiling mode of an object, returning the required swizzling of
bit 6 of addresses in the object.

Called by the user via ioctl.

.. _`i915_gem_set_tiling.return`:

Return
------

Zero on success, negative errno on failure.

.. _`i915_gem_get_tiling`:

i915_gem_get_tiling
===================

.. c:function:: int i915_gem_get_tiling(struct drm_device *dev, void *data, struct drm_file *file)

    IOCTL handler to get tiling mode

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file:
        DRM file for the ioctl call

.. _`i915_gem_get_tiling.description`:

Description
-----------

Returns the current tiling mode and required bit 6 swizzling for the object.

Called by the user via ioctl.

.. _`i915_gem_get_tiling.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

