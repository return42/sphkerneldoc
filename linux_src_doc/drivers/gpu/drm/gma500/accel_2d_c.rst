.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/accel_2d.c

.. _`psb_spank`:

psb_spank
=========

.. c:function:: void psb_spank(struct drm_psb_private *dev_priv)

    reset the 2D engine

    :param dev_priv:
        our PSB DRM device
    :type dev_priv: struct drm_psb_private \*

.. _`psb_spank.description`:

Description
-----------

Soft reset the graphics engine and then reload the necessary registers.
We use this at initialisation time but it will become relevant for
accelerated X later

.. _`psb_2d_wait_available`:

psb_2d_wait_available
=====================

.. c:function:: int psb_2d_wait_available(struct drm_psb_private *dev_priv, unsigned size)

    wait for FIFO room

    :param dev_priv:
        our DRM device
    :type dev_priv: struct drm_psb_private \*

    :param size:
        size (in dwords) of the command we want to issue
    :type size: unsigned

.. _`psb_2d_wait_available.description`:

Description
-----------

Wait until there is room to load the FIFO with our data. If the
device is not responding then reset it

.. _`psbfb_2d_submit`:

psbfb_2d_submit
===============

.. c:function:: int psbfb_2d_submit(struct drm_psb_private *dev_priv, uint32_t *cmdbuf, unsigned size)

    submit a 2D command

    :param dev_priv:
        our DRM device
    :type dev_priv: struct drm_psb_private \*

    :param cmdbuf:
        command to issue
    :type cmdbuf: uint32_t \*

    :param size:
        length (in dwords)
    :type size: unsigned

.. _`psbfb_2d_submit.description`:

Description
-----------

Issue one or more 2D commands to the accelerator. This needs to be
serialized later when we add the GEM interfaces for acceleration

.. _`psb_accel_2d_copy_direction`:

psb_accel_2d_copy_direction
===========================

.. c:function:: u32 psb_accel_2d_copy_direction(int xdir, int ydir)

    compute blit order

    :param xdir:
        X direction of move
    :type xdir: int

    :param ydir:
        Y direction of move
    :type ydir: int

.. _`psb_accel_2d_copy_direction.description`:

Description
-----------

Compute the correct order setings to ensure that an overlapping blit
correctly copies all the pixels.

.. _`psb_accel_2d_copy`:

psb_accel_2d_copy
=================

.. c:function:: int psb_accel_2d_copy(struct drm_psb_private *dev_priv, uint32_t src_offset, uint32_t src_stride, uint32_t src_format, uint32_t dst_offset, uint32_t dst_stride, uint32_t dst_format, uint16_t src_x, uint16_t src_y, uint16_t dst_x, uint16_t dst_y, uint16_t size_x, uint16_t size_y)

    accelerated 2D copy

    :param dev_priv:
        our DRM device
        \ ``src_offset``\  in bytes
        \ ``src_stride``\  in bytes
        \ ``src_format``\  psb 2D format defines
        \ ``dst_offset``\  in bytes
        \ ``dst_stride``\  in bytes
        \ ``dst_format``\  psb 2D format defines
        \ ``src_x``\  offset in pixels
        \ ``src_y``\  offset in pixels
        \ ``dst_x``\  offset in pixels
        \ ``dst_y``\  offset in pixels
        \ ``size_x``\  of the copied area
        \ ``size_y``\  of the copied area
    :type dev_priv: struct drm_psb_private \*

    :param src_offset:
        *undescribed*
    :type src_offset: uint32_t

    :param src_stride:
        *undescribed*
    :type src_stride: uint32_t

    :param src_format:
        *undescribed*
    :type src_format: uint32_t

    :param dst_offset:
        *undescribed*
    :type dst_offset: uint32_t

    :param dst_stride:
        *undescribed*
    :type dst_stride: uint32_t

    :param dst_format:
        *undescribed*
    :type dst_format: uint32_t

    :param src_x:
        *undescribed*
    :type src_x: uint16_t

    :param src_y:
        *undescribed*
    :type src_y: uint16_t

    :param dst_x:
        *undescribed*
    :type dst_x: uint16_t

    :param dst_y:
        *undescribed*
    :type dst_y: uint16_t

    :param size_x:
        *undescribed*
    :type size_x: uint16_t

    :param size_y:
        *undescribed*
    :type size_y: uint16_t

.. _`psb_accel_2d_copy.description`:

Description
-----------

Format and issue a 2D accelerated copy command.

.. _`psbfb_copyarea_accel`:

psbfb_copyarea_accel
====================

.. c:function:: void psbfb_copyarea_accel(struct fb_info *info, const struct fb_copyarea *a)

    copyarea acceleration for /dev/fb

    :param info:
        our framebuffer
    :type info: struct fb_info \*

    :param a:
        copyarea parameters from the framebuffer core
    :type a: const struct fb_copyarea \*

.. _`psbfb_copyarea_accel.description`:

Description
-----------

Perform a 2D copy via the accelerator

.. _`psbfb_copyarea`:

psbfb_copyarea
==============

.. c:function:: void psbfb_copyarea(struct fb_info *info, const struct fb_copyarea *region)

    2D copy interface

    :param info:
        our framebuffer
    :type info: struct fb_info \*

    :param region:
        region to copy
    :type region: const struct fb_copyarea \*

.. _`psbfb_copyarea.description`:

Description
-----------

Copy an area of the framebuffer console either by the accelerator
or directly using the cfb helpers according to the request

.. _`psbfb_sync`:

psbfb_sync
==========

.. c:function:: int psbfb_sync(struct fb_info *info)

    synchronize 2D

    :param info:
        our framebuffer
    :type info: struct fb_info \*

.. _`psbfb_sync.description`:

Description
-----------

Wait for the 2D engine to quiesce so that we can do CPU
access to the framebuffer again

.. This file was automatic generated / don't edit.

