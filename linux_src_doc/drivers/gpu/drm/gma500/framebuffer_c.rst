.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/framebuffer.c

.. _`psb_framebuffer_init`:

psb_framebuffer_init
====================

.. c:function:: int psb_framebuffer_init(struct drm_device *dev, struct psb_framebuffer *fb, const struct drm_mode_fb_cmd2 *mode_cmd, struct gtt_range *gt)

    initialize a framebuffer

    :param struct drm_device \*dev:
        our DRM device

    :param struct psb_framebuffer \*fb:
        framebuffer to set up

    :param const struct drm_mode_fb_cmd2 \*mode_cmd:
        mode description

    :param struct gtt_range \*gt:
        backing object

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

    :param struct drm_device \*dev:
        our DRM device

    :param const struct drm_mode_fb_cmd2 \*mode_cmd:
        the description of the requested mode

    :param struct gtt_range \*gt:
        the backing object

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

    :param struct drm_device \*dev:
        the DRM device

    :param int aligned_size:
        space needed

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

    :param struct psb_fbdev \*fbdev:
        the framebuffer device

    :param struct drm_fb_helper_surface_size \*sizes:
        specification of the layout

.. _`psbfb_create.description`:

Description
-----------

Create a framebuffer to the specifications provided

.. _`psb_user_framebuffer_create`:

psb_user_framebuffer_create
===========================

.. c:function:: struct drm_framebuffer *psb_user_framebuffer_create(struct drm_device *dev, struct drm_file *filp, const struct drm_mode_fb_cmd2 *cmd)

    create framebuffer

    :param struct drm_device \*dev:
        our DRM device

    :param struct drm_file \*filp:
        client file

    :param const struct drm_mode_fb_cmd2 \*cmd:
        mode request

.. _`psb_user_framebuffer_create.description`:

Description
-----------

Create a new framebuffer backed by a userspace GEM object

.. _`psb_user_framebuffer_create_handle`:

psb_user_framebuffer_create_handle
==================================

.. c:function:: int psb_user_framebuffer_create_handle(struct drm_framebuffer *fb, struct drm_file *file_priv, unsigned int *handle)

    add hamdle to a framebuffer

    :param struct drm_framebuffer \*fb:
        framebuffer

    :param struct drm_file \*file_priv:
        our DRM file

    :param unsigned int \*handle:
        returned handle

.. _`psb_user_framebuffer_create_handle.description`:

Description
-----------

Our framebuffer object is a GTT range which also contains a GEM
object. We need to turn it into a handle for userspace. GEM will do
the work for us

.. _`psb_user_framebuffer_destroy`:

psb_user_framebuffer_destroy
============================

.. c:function:: void psb_user_framebuffer_destroy(struct drm_framebuffer *fb)

    destruct user created fb

    :param struct drm_framebuffer \*fb:
        framebuffer

.. _`psb_user_framebuffer_destroy.description`:

Description
-----------

User framebuffers are backed by GEM objects so all we have to do is
clean up a bit and drop the reference, GEM will handle the fallout

.. This file was automatic generated / don't edit.

