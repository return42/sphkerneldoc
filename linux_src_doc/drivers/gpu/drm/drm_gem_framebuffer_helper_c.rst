.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_gem_framebuffer_helper.c

.. _`overview`:

overview
========

This library provides helpers for drivers that don't subclass
\ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  and and use \ :c:type:`struct drm_gem_object <drm_gem_object>`\  for their backing storage.

Drivers without additional needs to validate framebuffers can simply use
\ :c:func:`drm_gem_fb_create`\  and everything is wired up automatically. But all
parts can be used individually.

.. _`drm_gem_fb_get_obj`:

drm_gem_fb_get_obj
==================

.. c:function:: struct drm_gem_object *drm_gem_fb_get_obj(struct drm_framebuffer *fb, unsigned int plane)

    Get GEM object for framebuffer

    :param struct drm_framebuffer \*fb:
        The framebuffer

    :param unsigned int plane:
        Which plane

.. _`drm_gem_fb_get_obj.description`:

Description
-----------

Returns the GEM object for given framebuffer.

.. _`drm_gem_fb_destroy`:

drm_gem_fb_destroy
==================

.. c:function:: void drm_gem_fb_destroy(struct drm_framebuffer *fb)

    Free GEM backed framebuffer

    :param struct drm_framebuffer \*fb:
        DRM framebuffer

.. _`drm_gem_fb_destroy.description`:

Description
-----------

Frees a GEM backed framebuffer with its backing buffer(s) and the structure
itself. Drivers can use this as their \ :c:type:`drm_framebuffer_funcs->destroy <drm_framebuffer_funcs>`\ 
callback.

.. _`drm_gem_fb_create_handle`:

drm_gem_fb_create_handle
========================

.. c:function:: int drm_gem_fb_create_handle(struct drm_framebuffer *fb, struct drm_file *file, unsigned int *handle)

    Create handle for GEM backed framebuffer

    :param struct drm_framebuffer \*fb:
        DRM framebuffer

    :param struct drm_file \*file:
        drm file

    :param unsigned int \*handle:
        handle created

.. _`drm_gem_fb_create_handle.description`:

Description
-----------

Drivers can use this as their \ :c:type:`drm_framebuffer_funcs->create_handle <drm_framebuffer_funcs>`\ 
callback.

.. _`drm_gem_fb_create_handle.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_gem_fb_create_with_funcs`:

drm_gem_fb_create_with_funcs
============================

.. c:function:: struct drm_framebuffer *drm_gem_fb_create_with_funcs(struct drm_device *dev, struct drm_file *file, const struct drm_mode_fb_cmd2 *mode_cmd, const struct drm_framebuffer_funcs *funcs)

    helper function for the \ :c:type:`drm_mode_config_funcs.fb_create <drm_mode_config_funcs>`\  callback

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*file:
        drm file for the ioctl call

    :param const struct drm_mode_fb_cmd2 \*mode_cmd:
        metadata from the userspace fb creation request

    :param const struct drm_framebuffer_funcs \*funcs:
        vtable to be used for the new framebuffer object

.. _`drm_gem_fb_create_with_funcs.description`:

Description
-----------

This can be used to set \ :c:type:`struct drm_framebuffer_funcs <drm_framebuffer_funcs>`\  for drivers that need the
\ :c:type:`drm_framebuffer_funcs.dirty <drm_framebuffer_funcs>`\  callback. Use \ :c:func:`drm_gem_fb_create`\  if you don't
need to change \ :c:type:`struct drm_framebuffer_funcs <drm_framebuffer_funcs>`\ .
The function does buffer size validation.

.. _`drm_gem_fb_create`:

drm_gem_fb_create
=================

.. c:function:: struct drm_framebuffer *drm_gem_fb_create(struct drm_device *dev, struct drm_file *file, const struct drm_mode_fb_cmd2 *mode_cmd)

    &drm_mode_config_funcs.fb_create callback function

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*file:
        drm file for the ioctl call

    :param const struct drm_mode_fb_cmd2 \*mode_cmd:
        metadata from the userspace fb creation request

.. _`drm_gem_fb_create.description`:

Description
-----------

If your hardware has special alignment or pitch requirements these should be
checked before calling this function. The function does buffer size
validation. Use \ :c:func:`drm_gem_fb_create_with_funcs`\  if you need to set
\ :c:type:`drm_framebuffer_funcs.dirty <drm_framebuffer_funcs>`\ .

.. _`drm_gem_fb_prepare_fb`:

drm_gem_fb_prepare_fb
=====================

.. c:function:: int drm_gem_fb_prepare_fb(struct drm_plane *plane, struct drm_plane_state *state)

    Prepare gem framebuffer

    :param struct drm_plane \*plane:
        Which plane

    :param struct drm_plane_state \*state:
        Plane state attach fence to

.. _`drm_gem_fb_prepare_fb.description`:

Description
-----------

This can be used as the \ :c:type:`drm_plane_helper_funcs.prepare_fb <drm_plane_helper_funcs>`\  hook.

This function checks if the plane FB has an dma-buf attached, extracts
the exclusive fence and attaches it to plane state for the atomic helper
to wait on.

There is no need for \ :c:type:`drm_plane_helper_funcs.cleanup_fb <drm_plane_helper_funcs>`\  hook for simple
gem based framebuffer drivers which have their buffers always pinned in
memory.

.. _`drm_gem_fbdev_fb_create`:

drm_gem_fbdev_fb_create
=======================

.. c:function:: struct drm_framebuffer *drm_gem_fbdev_fb_create(struct drm_device *dev, struct drm_fb_helper_surface_size *sizes, unsigned int pitch_align, struct drm_gem_object *obj, const struct drm_framebuffer_funcs *funcs)

    Create a drm_framebuffer for fbdev emulation

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_fb_helper_surface_size \*sizes:
        fbdev size description

    :param unsigned int pitch_align:
        optional pitch alignment

    :param struct drm_gem_object \*obj:
        GEM object backing the framebuffer

    :param const struct drm_framebuffer_funcs \*funcs:
        vtable to be used for the new framebuffer object

.. _`drm_gem_fbdev_fb_create.description`:

Description
-----------

This function creates a framebuffer for use with fbdev emulation.

.. _`drm_gem_fbdev_fb_create.return`:

Return
------

Pointer to a drm_framebuffer on success or an error pointer on failure.

.. This file was automatic generated / don't edit.

