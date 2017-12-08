.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_fb_cma_helper.c

.. _`framebuffer-cma-helper-functions`:

framebuffer cma helper functions
================================

Provides helper functions for creating a cma (contiguous memory allocator)
backed framebuffer.

\ :c:func:`drm_gem_fb_create`\  is used in the \ :c:type:`drm_mode_config_funcs.fb_create <drm_mode_config_funcs>`\ 
callback function to create a cma backed framebuffer.

An fbdev framebuffer backed by cma is also available by calling
\ :c:func:`drm_fbdev_cma_init`\ . \ :c:func:`drm_fbdev_cma_fini`\  tears it down.
If the \ :c:type:`drm_framebuffer_funcs.dirty <drm_framebuffer_funcs>`\  callback is set, fb_deferred_io will be
set up automatically. \ :c:type:`drm_framebuffer_funcs.dirty <drm_framebuffer_funcs>`\  is called by
\ :c:func:`drm_fb_helper_deferred_io`\  in process context (&struct delayed_work).

Example fbdev deferred io code::

    static int driver_fb_dirty(struct drm_framebuffer *fb,
                               struct drm_file *file_priv,
                               unsigned flags, unsigned color,
                               struct drm_clip_rect *clips,
                               unsigned num_clips)
    {
        struct drm_gem_cma_object *cma = drm_fb_cma_get_gem_obj(fb, 0);
        ... push changes ...
        return 0;
    }

    static struct drm_framebuffer_funcs driver_fb_funcs = {
        .destroy       = drm_gem_fb_destroy,
        .create_handle = drm_gem_fb_create_handle,
        .dirty         = driver_fb_dirty,
    };

Initialize::

    fbdev = drm_fbdev_cma_init_with_funcs(dev, 16,
                                          dev->mode_config.num_crtc,
                                          dev->mode_config.num_connector,
                                          \ :c:type:`struct driver_fb_funcs <driver_fb_funcs>`\ );

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

.. _`drm_fb_cma_get_gem_addr`:

drm_fb_cma_get_gem_addr
=======================

.. c:function:: dma_addr_t drm_fb_cma_get_gem_addr(struct drm_framebuffer *fb, struct drm_plane_state *state, unsigned int plane)

    Get physical address for framebuffer

    :param struct drm_framebuffer \*fb:
        The framebuffer

    :param struct drm_plane_state \*state:
        Which state of drm plane

    :param unsigned int plane:
        Which plane
        Return the CMA GEM address for given framebuffer.

.. _`drm_fb_cma_get_gem_addr.description`:

Description
-----------

This function will usually be called from the PLANE callback functions.

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

.. c:function:: struct drm_fbdev_cma *drm_fbdev_cma_init_with_funcs(struct drm_device *dev, unsigned int preferred_bpp, unsigned int max_conn_count, const struct drm_framebuffer_funcs *funcs)

    Allocate and initializes a drm_fbdev_cma struct

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int preferred_bpp:
        Preferred bits per pixel for the device

    :param unsigned int max_conn_count:
        Maximum number of connectors

    :param const struct drm_framebuffer_funcs \*funcs:
        fb helper functions, in particular a custom \ :c:func:`dirty`\  callback

.. _`drm_fbdev_cma_init_with_funcs.description`:

Description
-----------

Returns a newly allocated drm_fbdev_cma struct or a ERR_PTR.

.. _`drm_fbdev_cma_init`:

drm_fbdev_cma_init
==================

.. c:function:: struct drm_fbdev_cma *drm_fbdev_cma_init(struct drm_device *dev, unsigned int preferred_bpp, unsigned int max_conn_count)

    Allocate and initializes a drm_fbdev_cma struct

    :param struct drm_device \*dev:
        DRM device

    :param unsigned int preferred_bpp:
        Preferred bits per pixel for the device

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

This function is usually called from the \ :c:type:`drm_driver.lastclose <drm_driver>`\  callback.

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

This function is usually called from the \ :c:type:`drm_mode_config.output_poll_changed <drm_mode_config>`\ 
callback.

.. _`drm_fbdev_cma_set_suspend`:

drm_fbdev_cma_set_suspend
=========================

.. c:function:: void drm_fbdev_cma_set_suspend(struct drm_fbdev_cma *fbdev_cma, bool state)

    wrapper around drm_fb_helper_set_suspend

    :param struct drm_fbdev_cma \*fbdev_cma:
        The drm_fbdev_cma struct, may be NULL

    :param bool state:
        desired state, zero to resume, non-zero to suspend

.. _`drm_fbdev_cma_set_suspend.description`:

Description
-----------

Calls drm_fb_helper_set_suspend, which is a wrapper around
fb_set_suspend implemented by fbdev core.

.. _`drm_fbdev_cma_set_suspend_unlocked`:

drm_fbdev_cma_set_suspend_unlocked
==================================

.. c:function:: void drm_fbdev_cma_set_suspend_unlocked(struct drm_fbdev_cma *fbdev_cma, bool state)

    wrapper around drm_fb_helper_set_suspend_unlocked

    :param struct drm_fbdev_cma \*fbdev_cma:
        The drm_fbdev_cma struct, may be NULL

    :param bool state:
        desired state, zero to resume, non-zero to suspend

.. _`drm_fbdev_cma_set_suspend_unlocked.description`:

Description
-----------

Calls drm_fb_helper_set_suspend, which is a wrapper around
fb_set_suspend implemented by fbdev core.

.. This file was automatic generated / don't edit.

