.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_dumb_buffers.c

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

