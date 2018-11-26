.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/core/fbsysfs.c

.. _`framebuffer_alloc`:

framebuffer_alloc
=================

.. c:function:: struct fb_info *framebuffer_alloc(size_t size, struct device *dev)

    creates a new frame buffer info structure

    :param size:
        size of driver private data, can be zero
    :type size: size_t

    :param dev:
        pointer to the device for this fb, this can be NULL
    :type dev: struct device \*

.. _`framebuffer_alloc.description`:

Description
-----------

Creates a new frame buffer info structure. Also reserves \ ``size``\  bytes
for driver private data (info->par). info->par (if any) will be
aligned to sizeof(long).

Returns the new structure, or NULL if an error occurred.

.. _`framebuffer_release`:

framebuffer_release
===================

.. c:function:: void framebuffer_release(struct fb_info *info)

    marks the structure available for freeing

    :param info:
        frame buffer info structure
    :type info: struct fb_info \*

.. _`framebuffer_release.description`:

Description
-----------

Drop the reference count of the device embedded in the
framebuffer info structure.

.. This file was automatic generated / don't edit.

