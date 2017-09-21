.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_dumb_buffers.c

.. _`overview`:

overview
========

The KMS API doesn't standardize backing storage object creation and leaves it
to driver-specific ioctls. Furthermore actually creating a buffer object even
for GEM-based drivers is done through a driver-specific ioctl - GEM only has
a common userspace interface for sharing and destroying objects. While not an
issue for full-fledged graphics stacks that include device-specific userspace
components (in libdrm for instance), this limit makes DRM-based early boot
graphics unnecessarily complex.

Dumb objects partly alleviate the problem by providing a standard API to
create dumb buffers suitable for scanout, which can then be used to create
KMS frame buffers.

To support dumb objects drivers must implement the \ :c:type:`drm_driver.dumb_create <drm_driver>`\ 
operation. \ :c:type:`drm_driver.dumb_destroy <drm_driver>`\  defaults to \ :c:func:`drm_gem_dumb_destroy`\  if
not set and \ :c:type:`drm_driver.dumb_map_offset <drm_driver>`\  defaults to
\ :c:func:`drm_gem_dumb_map_offset`\ . See the callbacks for further details.

Note that dumb objects may not be used for gpu acceleration, as has been
attempted on some ARM embedded platforms. Such drivers really must have
a hardware-specific ioctl to allocate suitable buffer objects.

.. _`drm_mode_mmap_dumb_ioctl`:

drm_mode_mmap_dumb_ioctl
========================

.. c:function:: int drm_mode_mmap_dumb_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    create an mmap offset for a dumb backing storage buffer

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_mmap_dumb_ioctl.description`:

Description
-----------

Allocate an offset in the drm device node's address space to be able to
memory map a dumb buffer.

Called by the user via ioctl.

.. _`drm_mode_mmap_dumb_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

