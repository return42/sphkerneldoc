.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/framebuffer.c

.. _`psb_framebuffer_init`:

psb_framebuffer_init
====================

.. c:function:: int psb_framebuffer_init(struct drm_device *dev, struct psb_framebuffer *fb, const struct drm_mode_fb_cmd2 *mode_cmd, struct gtt_range *gt)

    initialize a framebuffer

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

    :param fb:
        framebuffer to set up
    :type fb: struct psb_framebuffer \*

    :param mode_cmd:
        mode description
    :type mode_cmd: const struct drm_mode_fb_cmd2 \*

    :param gt:
        backing object
    :type gt: struct gtt_range \*

.. _`psb_framebuffer_init.description`:

Description
-----------

Configure and fill in the boilerplate for our frame buffer. Return
0 on success or an error code if we fail.

.. _`psb_framebuffer_create`:

psb_framebuffer_create
======================

.. c:function:: struct drm_framebuffer *psb_framebuffer_create(struct drm_device *dev, const struct drm_mode_fb_cmd2 *mode_cmd, struct gtt_range *gt)

    create a framebuffer backed by gt

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

    :param mode_cmd:
        the description of the requested mode
    :type mode_cmd: const struct drm_mode_fb_cmd2 \*

    :param gt:
        the backing object
    :type gt: struct gtt_range \*

.. _`psb_framebuffer_create.description`:

Description
-----------

Create a framebuffer object backed by the gt, and fill in the
boilerplate required

.. _`psb_framebuffer_create.todo`:

TODO
----

review object references

.. _`psbfb_alloc`:

psbfb_alloc
===========

.. c:function:: struct gtt_range *psbfb_alloc(struct drm_device *dev, int aligned_size)

    allocate frame buffer memory

    :param dev:
        the DRM device
    :type dev: struct drm_device \*

    :param aligned_size:
        space needed
    :type aligned_size: int

.. _`psbfb_alloc.description`:

Description
-----------

Allocate the frame buffer. In the usual case we get a GTT range that
is stolen memory backed and life is simple. If there isn't sufficient
we fail as we don't have the virtual mapping space to really vmap it
and the kernel console code can't handle non linear framebuffers.

Re-address this as and if the framebuffer layer grows this ability.

.. _`psbfb_create`:

psbfb_create
============

.. c:function:: int psbfb_create(struct psb_fbdev *fbdev, struct drm_fb_helper_surface_size *sizes)

    create a framebuffer

    :param fbdev:
        the framebuffer device
    :type fbdev: struct psb_fbdev \*

    :param sizes:
        specification of the layout
    :type sizes: struct drm_fb_helper_surface_size \*

.. _`psbfb_create.description`:

Description
-----------

Create a framebuffer to the specifications provided

.. _`psb_user_framebuffer_create`:

psb_user_framebuffer_create
===========================

.. c:function:: struct drm_framebuffer *psb_user_framebuffer_create(struct drm_device *dev, struct drm_file *filp, const struct drm_mode_fb_cmd2 *cmd)

    create framebuffer

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

    :param filp:
        client file
    :type filp: struct drm_file \*

    :param cmd:
        mode request
    :type cmd: const struct drm_mode_fb_cmd2 \*

.. _`psb_user_framebuffer_create.description`:

Description
-----------

Create a new framebuffer backed by a userspace GEM object

.. This file was automatic generated / don't edit.

