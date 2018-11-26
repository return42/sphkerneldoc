.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/tinydrm/tinydrm.h

.. _`tinydrm_device`:

struct tinydrm_device
=====================

.. c:type:: struct tinydrm_device

    tinydrm device

.. _`tinydrm_device.definition`:

Definition
----------

.. code-block:: c

    struct tinydrm_device {
        struct drm_device *drm;
        struct drm_simple_display_pipe pipe;
        struct mutex dirty_lock;
        const struct drm_framebuffer_funcs *fb_funcs;
        int (*fb_dirty)(struct drm_framebuffer *framebuffer,struct drm_file *file_priv, unsigned flags,unsigned color, struct drm_clip_rect *clips, unsigned num_clips);
    }

.. _`tinydrm_device.members`:

Members
-------

drm
    DRM device

pipe
    Display pipe structure

dirty_lock
    Serializes framebuffer flushing

fb_funcs
    Framebuffer functions used when creating framebuffers

fb_dirty
    Framebuffer dirty callback

.. _`tinydrm_gem_driver_ops`:

TINYDRM_GEM_DRIVER_OPS
======================

.. c:function::  TINYDRM_GEM_DRIVER_OPS()

    default tinydrm gem operations

.. _`tinydrm_gem_driver_ops.description`:

Description
-----------

This macro provides a shortcut for setting the tinydrm GEM operations in
the \ :c:type:`struct drm_driver <drm_driver>`\  structure.

.. _`tinydrm_mode`:

TINYDRM_MODE
============

.. c:function::  TINYDRM_MODE( hd,  vd,  hd_mm,  vd_mm)

    tinydrm display mode

    :param hd:
        Horizontal resolution, width
    :type hd: 

    :param vd:
        Vertical resolution, height
    :type vd: 

    :param hd_mm:
        Display width in millimeters
    :type hd_mm: 

    :param vd_mm:
        Display height in millimeters
    :type vd_mm: 

.. _`tinydrm_mode.description`:

Description
-----------

This macro creates a \ :c:type:`struct drm_display_mode <drm_display_mode>`\  for use with tinydrm.

.. This file was automatic generated / don't edit.

