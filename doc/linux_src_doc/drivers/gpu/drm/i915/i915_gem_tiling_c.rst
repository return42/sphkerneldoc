.. -*- coding: utf-8; mode: rst -*-

=================
i915_gem_tiling.c
=================

.. _`buffer-object-tiling`:

buffer object tiling
====================

:c:func:`i915_gem_set_tiling` and :c:func:`i915_gem_get_tiling` is the userspace interface to
declare fence register requirements.

In principle GEM doesn't care at all about the internal data layout of an
object, and hence it also doesn't care about tiling or swizzling. There's two
exceptions:

- For X and Y tiling the hardware provides detilers for CPU access, so called
  fences. Since there's only a limited amount of them the kernel must manage
  these, and therefore userspace must tell the kernel the object tiling if it
  wants to use fences for detiling.

- On gen3 and gen4 platforms have a swizzling pattern for tiled objects which
  depends upon the physical page frame number. When swapping such objects the
  page frame number might change and the kernel must be able to fix this up
  and hence now the tiling. Note that on a subset of platforms with
  asymmetric memory channel population the swizzling pattern changes in an
  unknown way, and for those the kernel simply forbids swapping completely.

Since neither of this applies for new tiling layouts on modern platforms like
W, Ys and Yf tiling GEM only allows object tiling to be set to X or Y tiled.
Anything else can be handled in userspace entirely without the kernel's
invovlement.


.. _`i915_gem_set_tiling`:

i915_gem_set_tiling
===================

.. c:function:: int i915_gem_set_tiling (struct drm_device *dev, void *data, struct drm_file *file)

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

Returns:
Zero on success, negative errno on failure.


.. _`i915_gem_get_tiling`:

i915_gem_get_tiling
===================

.. c:function:: int i915_gem_get_tiling (struct drm_device *dev, void *data, struct drm_file *file)

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

Returns:
Zero on success, negative errno on failure.

