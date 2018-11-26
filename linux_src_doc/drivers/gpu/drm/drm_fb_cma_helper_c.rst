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
\ :c:func:`drm_fb_cma_fbdev_init`\ . \ :c:func:`drm_fb_cma_fbdev_fini`\  tears it down.

.. _`drm_fb_cma_get_gem_obj`:

drm_fb_cma_get_gem_obj
======================

.. c:function:: struct drm_gem_cma_object *drm_fb_cma_get_gem_obj(struct drm_framebuffer *fb, unsigned int plane)

    Get CMA GEM object for framebuffer

    :param fb:
        The framebuffer
    :type fb: struct drm_framebuffer \*

    :param plane:
        Which plane
    :type plane: unsigned int

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

    :param fb:
        The framebuffer
    :type fb: struct drm_framebuffer \*

    :param state:
        Which state of drm plane
    :type state: struct drm_plane_state \*

    :param plane:
        Which plane
        Return the CMA GEM address for given framebuffer.
    :type plane: unsigned int

.. _`drm_fb_cma_get_gem_addr.description`:

Description
-----------

This function will usually be called from the PLANE callback functions.

.. _`drm_fb_cma_fbdev_init`:

drm_fb_cma_fbdev_init
=====================

.. c:function:: int drm_fb_cma_fbdev_init(struct drm_device *dev, unsigned int preferred_bpp, unsigned int max_conn_count)

    Allocate and initialize fbdev emulation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param preferred_bpp:
        Preferred bits per pixel for the device.
        \ ``dev->mode_config.preferred_depth``\  is used if this is zero.
    :type preferred_bpp: unsigned int

    :param max_conn_count:
        Maximum number of connectors.
        \ ``dev->mode_config.num_connector``\  is used if this is zero.
    :type max_conn_count: unsigned int

.. _`drm_fb_cma_fbdev_init.return`:

Return
------

Zero on success or negative error code on failure.

.. _`drm_fb_cma_fbdev_fini`:

drm_fb_cma_fbdev_fini
=====================

.. c:function:: void drm_fb_cma_fbdev_fini(struct drm_device *dev)

    Teardown fbdev emulation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_fbdev_cma_init`:

drm_fbdev_cma_init
==================

.. c:function:: struct drm_fbdev_cma *drm_fbdev_cma_init(struct drm_device *dev, unsigned int preferred_bpp, unsigned int max_conn_count)

    Allocate and initializes a drm_fbdev_cma struct

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param preferred_bpp:
        Preferred bits per pixel for the device
    :type preferred_bpp: unsigned int

    :param max_conn_count:
        Maximum number of connectors
    :type max_conn_count: unsigned int

.. _`drm_fbdev_cma_init.description`:

Description
-----------

Returns a newly allocated drm_fbdev_cma struct or a ERR_PTR.

.. _`drm_fbdev_cma_fini`:

drm_fbdev_cma_fini
==================

.. c:function:: void drm_fbdev_cma_fini(struct drm_fbdev_cma *fbdev_cma)

    Free drm_fbdev_cma struct

    :param fbdev_cma:
        The drm_fbdev_cma struct
    :type fbdev_cma: struct drm_fbdev_cma \*

.. _`drm_fbdev_cma_restore_mode`:

drm_fbdev_cma_restore_mode
==========================

.. c:function:: void drm_fbdev_cma_restore_mode(struct drm_fbdev_cma *fbdev_cma)

    Restores initial framebuffer mode

    :param fbdev_cma:
        The drm_fbdev_cma struct, may be NULL
    :type fbdev_cma: struct drm_fbdev_cma \*

.. _`drm_fbdev_cma_restore_mode.description`:

Description
-----------

This function is usually called from the \ :c:type:`drm_driver.lastclose <drm_driver>`\  callback.

.. _`drm_fbdev_cma_hotplug_event`:

drm_fbdev_cma_hotplug_event
===========================

.. c:function:: void drm_fbdev_cma_hotplug_event(struct drm_fbdev_cma *fbdev_cma)

    Poll for hotpulug events

    :param fbdev_cma:
        The drm_fbdev_cma struct, may be NULL
    :type fbdev_cma: struct drm_fbdev_cma \*

.. _`drm_fbdev_cma_hotplug_event.description`:

Description
-----------

This function is usually called from the \ :c:type:`drm_mode_config.output_poll_changed <drm_mode_config>`\ 
callback.

.. _`drm_fbdev_cma_set_suspend_unlocked`:

drm_fbdev_cma_set_suspend_unlocked
==================================

.. c:function:: void drm_fbdev_cma_set_suspend_unlocked(struct drm_fbdev_cma *fbdev_cma, bool state)

    wrapper around drm_fb_helper_set_suspend_unlocked

    :param fbdev_cma:
        The drm_fbdev_cma struct, may be NULL
    :type fbdev_cma: struct drm_fbdev_cma \*

    :param state:
        desired state, zero to resume, non-zero to suspend
    :type state: bool

.. _`drm_fbdev_cma_set_suspend_unlocked.description`:

Description
-----------

Calls drm_fb_helper_set_suspend, which is a wrapper around
fb_set_suspend implemented by fbdev core.

.. This file was automatic generated / don't edit.

