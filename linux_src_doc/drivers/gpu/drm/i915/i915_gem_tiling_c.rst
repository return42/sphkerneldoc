.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_tiling.c

.. _`i915_gem_fence_size`:

i915_gem_fence_size
===================

.. c:function:: u32 i915_gem_fence_size(struct drm_i915_private *i915, u32 size, unsigned int tiling, unsigned int stride)

    required global GTT size for a fence

    :param struct drm_i915_private \*i915:
        i915 device

    :param u32 size:
        object size

    :param unsigned int tiling:
        tiling mode

    :param unsigned int stride:
        tiling stride

.. _`i915_gem_fence_size.description`:

Description
-----------

Return the required global GTT size for a fence (view of a tiled object),
taking into account potential fence register mapping.

.. _`i915_gem_fence_alignment`:

i915_gem_fence_alignment
========================

.. c:function:: u32 i915_gem_fence_alignment(struct drm_i915_private *i915, u32 size, unsigned int tiling, unsigned int stride)

    required global GTT alignment for a fence

    :param struct drm_i915_private \*i915:
        i915 device

    :param u32 size:
        object size

    :param unsigned int tiling:
        tiling mode

    :param unsigned int stride:
        tiling stride

.. _`i915_gem_fence_alignment.description`:

Description
-----------

Return the required global GTT alignment for a fence (a view of a tiled
object), taking into account potential fence register mapping.

.. _`i915_gem_set_tiling_ioctl`:

i915_gem_set_tiling_ioctl
=========================

.. c:function:: int i915_gem_set_tiling_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    IOCTL handler to set tiling mode

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file:
        DRM file for the ioctl call

.. _`i915_gem_set_tiling_ioctl.description`:

Description
-----------

Sets the tiling mode of an object, returning the required swizzling of
bit 6 of addresses in the object.

Called by the user via ioctl.

.. _`i915_gem_set_tiling_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`i915_gem_get_tiling_ioctl`:

i915_gem_get_tiling_ioctl
=========================

.. c:function:: int i915_gem_get_tiling_ioctl(struct drm_device *dev, void *data, struct drm_file *file)

    IOCTL handler to get tiling mode

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file:
        DRM file for the ioctl call

.. _`i915_gem_get_tiling_ioctl.description`:

Description
-----------

Returns the current tiling mode and required bit 6 swizzling for the object.

Called by the user via ioctl.

.. _`i915_gem_get_tiling_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

