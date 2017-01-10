.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_fb_cma_helper.c

.. _`drm_fb_cma_create_with_funcs`:

drm_fb_cma_create_with_funcs
============================

.. c:function:: struct drm_framebuffer *drm_fb_cma_create_with_funcs(struct drm_device *dev, struct drm_file *file_priv, const struct drm_mode_fb_cmd2 *mode_cmd, const struct drm_framebuffer_funcs *funcs)

    helper function for the \ :c:type:`struct drm_mode_config_funcs <drm_mode_config_funcs>`\  ->fb_create callback function

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

    :param const struct drm_mode_fb_cmd2 \*mode_cmd:
        metadata from the userspace fb creation request

    :param const struct drm_framebuffer_funcs \*funcs:
        vtable to be used for the new framebuffer object

.. _`drm_fb_cma_create_with_funcs.description`:

Description
-----------

This can be used to set \ :c:type:`struct drm_framebuffer_funcs <drm_framebuffer_funcs>`\  for drivers that need the
\ :c:func:`dirty`\  callback. Use \ :c:func:`drm_fb_cma_create`\  if you don't need to change
\ :c:type:`struct drm_framebuffer_funcs <drm_framebuffer_funcs>`\ .

.. _`drm_fb_cma_create`:

drm_fb_cma_create
=================

.. c:function:: struct drm_framebuffer *drm_fb_cma_create(struct drm_device *dev, struct drm_file *file_priv, const struct drm_mode_fb_cmd2 *mode_cmd)

    &drm_mode_config_funcs ->fb_create callback function

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

    :param const struct drm_mode_fb_cmd2 \*mode_cmd:
        metadata from the userspace fb creation request

.. _`drm_fb_cma_create.description`:

Description
-----------

If your hardware has special alignment or pitch requirements these should be
checked before calling this function. Use \ :c:func:`drm_fb_cma_create_with_funcs`\  if
you need to set \ :c:type:`struct drm_framebuffer_funcs <drm_framebuffer_funcs>`\  ->dirty.

.. _`drm_fb_cma_get_gem_obj`:

drm_fb_cma_get_gem_obj
======================

.. c:function:: struct drm_gem_cma_object *drm_fb_cma_get_gem_obj(struct drm_framebuffer *fb, unsigned int plane)

    Get CMA GEM object for framebuffer

    :param struct drm_framebuffer \*fb:
        The framebuffer

    :param unsigned int plane:
        Which plane

.. _`drm_fb_cma_get_gem_obj.description`:

Description
-----------

Return the CMA GEM object for given framebuffer.

This function will usually be called from the CRTC callback functions.

.. _`drm_fb_cma_prepare_fb`:

drm_fb_cma_prepare_fb
=====================

.. c:function:: int drm_fb_cma_prepare_fb(struct drm_plane *plane, struct drm_plane_state *state)

    Prepare CMA framebuffer

    :param struct drm_plane \*plane:
        Which plane

    :param struct drm_plane_state \*state:
        Plane state attach fence to

.. _`drm_fb_cma_prepare_fb.description`:

Description
-----------

This should be put into prepare_fb hook of struct \ :c:type:`struct drm_plane_helper_funcs <drm_plane_helper_funcs>`\  .

This function checks if the plane FB has an dma-buf attached, extracts
the exclusive fence and attaches it to plane state for the atomic helper
to wait on.

There is no need for cleanup_fb for CMA based framebuffer drivers.

.. _`drm_fb_cma_debugfs_show`:

drm_fb_cma_debugfs_show
=======================

.. c:function:: int drm_fb_cma_debugfs_show(struct seq_file *m, void *arg)

    Helper to list CMA framebuffer objects in debugfs.

    :param struct seq_file \*m:
        output file

    :param void \*arg:
        private data for the callback

.. _`drm_fbdev_cma_init_with_funcs`:

drm_fbdev_cma_init_with_funcs
=============================

.. c:function:: struct drm_fbdev_cma *drm_fbdev_cma_init_with_funcs(struct drm_device *dev, unsigned int preferred_bpp, unsigned int num_crtc, unsigned int max_conn_count, const struct drm_fb_helper_funcs *funcs)

    Allocate and initializes a drm_fbdev_cma struct

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int preferred_bpp:
        Preferred bits per pixel for the device

    :param unsigned int num_crtc:
        Number of CRTCs

    :param unsigned int max_conn_count:
        Maximum number of connectors

    :param const struct drm_fb_helper_funcs \*funcs:
        fb helper functions, in particular \ :c:func:`fb_probe`\ 

.. _`drm_fbdev_cma_init_with_funcs.description`:

Description
-----------

Returns a newly allocated drm_fbdev_cma struct or a ERR_PTR.

.. _`drm_fbdev_cma_init`:

drm_fbdev_cma_init
==================

.. c:function:: struct drm_fbdev_cma *drm_fbdev_cma_init(struct drm_device *dev, unsigned int preferred_bpp, unsigned int num_crtc, unsigned int max_conn_count)

    Allocate and initializes a drm_fbdev_cma struct

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int preferred_bpp:
        Preferred bits per pixel for the device

    :param unsigned int num_crtc:
        Number of CRTCs

    :param unsigned int max_conn_count:
        Maximum number of connectors

.. _`drm_fbdev_cma_init.description`:

Description
-----------

Returns a newly allocated drm_fbdev_cma struct or a ERR_PTR.

.. _`drm_fbdev_cma_fini`:

drm_fbdev_cma_fini
==================

.. c:function:: void drm_fbdev_cma_fini(struct drm_fbdev_cma *fbdev_cma)

    Free drm_fbdev_cma struct

    :param struct drm_fbdev_cma \*fbdev_cma:
        The drm_fbdev_cma struct

.. _`drm_fbdev_cma_restore_mode`:

drm_fbdev_cma_restore_mode
==========================

.. c:function:: void drm_fbdev_cma_restore_mode(struct drm_fbdev_cma *fbdev_cma)

    Restores initial framebuffer mode

    :param struct drm_fbdev_cma \*fbdev_cma:
        The drm_fbdev_cma struct, may be NULL

.. _`drm_fbdev_cma_restore_mode.description`:

Description
-----------

This function is usually called from the DRM drivers lastclose callback.

.. _`drm_fbdev_cma_hotplug_event`:

drm_fbdev_cma_hotplug_event
===========================

.. c:function:: void drm_fbdev_cma_hotplug_event(struct drm_fbdev_cma *fbdev_cma)

    Poll for hotpulug events

    :param struct drm_fbdev_cma \*fbdev_cma:
        The drm_fbdev_cma struct, may be NULL

.. _`drm_fbdev_cma_hotplug_event.description`:

Description
-----------

This function is usually called from the DRM drivers output_poll_changed
callback.

.. _`drm_fbdev_cma_set_suspend`:

drm_fbdev_cma_set_suspend
=========================

.. c:function:: void drm_fbdev_cma_set_suspend(struct drm_fbdev_cma *fbdev_cma, int state)

    wrapper around drm_fb_helper_set_suspend

    :param struct drm_fbdev_cma \*fbdev_cma:
        The drm_fbdev_cma struct, may be NULL

    :param int state:
        desired state, zero to resume, non-zero to suspend

.. _`drm_fbdev_cma_set_suspend.description`:

Description
-----------

Calls drm_fb_helper_set_suspend, which is a wrapper around
fb_set_suspend implemented by fbdev core.

.. This file was automatic generated / don't edit.

