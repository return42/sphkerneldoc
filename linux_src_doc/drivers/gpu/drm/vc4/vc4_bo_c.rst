.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_bo.c

.. _`vc4-gem-bo-management-support`:

VC4 GEM BO management support
=============================

The VC4 GPU architecture (both scanout and rendering) has direct
access to system memory with no MMU in between.  To support it, we
use the GEM CMA helper functions to allocate contiguous ranges of
physical memory for our BOs.

Since the CMA allocator is very slow, we keep a cache of recently
freed BOs around so that the kernel's allocation of objects for 3D
rendering can return quickly.

.. _`vc4_create_object`:

vc4_create_object
=================

.. c:function:: struct drm_gem_object *vc4_create_object(struct drm_device *dev, size_t size)

    Implementation of driver->gem_create_object.

    :param struct drm_device \*dev:
        DRM device

    :param size_t size:
        Size in bytes of the memory the object will reference

.. _`vc4_create_object.description`:

Description
-----------

This lets the CMA helpers allocate object structs for us, and keep
our BO stats correct.

.. _`vc4_set_tiling_ioctl`:

vc4_set_tiling_ioctl
====================

.. c:function:: int vc4_set_tiling_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Sets the tiling modifier for a BO.

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl argument

    :param struct drm_file \*file_priv:
        DRM file for this fd

.. _`vc4_set_tiling_ioctl.description`:

Description
-----------

The tiling state of the BO decides the default modifier of an fb if
no specific modifier was set by userspace, and the return value of
\ :c:func:`vc4_get_tiling_ioctl`\  (so that userspace can treat a BO it
received from dmabuf as the same tiling format as the producer
used).

.. _`vc4_get_tiling_ioctl`:

vc4_get_tiling_ioctl
====================

.. c:function:: int vc4_get_tiling_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Gets the tiling modifier for a BO.

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl argument

    :param struct drm_file \*file_priv:
        DRM file for this fd

.. _`vc4_get_tiling_ioctl.description`:

Description
-----------

Returns the tiling modifier for a BO as set by \ :c:func:`vc4_set_tiling_ioctl`\ .

.. This file was automatic generated / don't edit.

