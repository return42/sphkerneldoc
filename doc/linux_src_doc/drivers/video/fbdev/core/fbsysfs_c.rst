.. -*- coding: utf-8; mode: rst -*-

=========
fbsysfs.c
=========


.. _`framebuffer_alloc`:

framebuffer_alloc
=================

.. c:function:: struct fb_info *framebuffer_alloc (size_t size, struct device *dev)

    creates a new frame buffer info structure

    :param size_t size:
        size of driver private data, can be zero

    :param struct device \*dev:
        pointer to the device for this fb, this can be NULL



.. _`framebuffer_alloc.description`:

Description
-----------

Creates a new frame buffer info structure. Also reserves ``size`` bytes
for driver private data (info->par). info->par (if any) will be
aligned to sizeof(long).

Returns the new structure, or NULL if an error occurred.



.. _`framebuffer_release`:

framebuffer_release
===================

.. c:function:: void framebuffer_release (struct fb_info *info)

    marks the structure available for freeing

    :param struct fb_info \*info:
        frame buffer info structure



.. _`framebuffer_release.description`:

Description
-----------

Drop the reference count of the device embedded in the
framebuffer info structure.

