.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_gem_framebuffer_helper.c

.. _`overview`:

overview
========

This library provides helpers for drivers that don't subclass
\ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  and use \ :c:type:`struct drm_gem_object <drm_gem_object>`\  for their backing storage.

Drivers without additional needs to validate framebuffers can simply use
\ :c:func:`drm_gem_fb_create`\  and everything is wired up automatically. Other drivers
can use all parts independently.

.. _`drm_gem_fb_get_obj`:

drm_gem_fb_get_obj
==================

.. c:function:: struct drm_gem_object *drm_gem_fb_get_obj(struct drm_framebuffer *fb, unsigned int plane)

    Get GEM object backing the framebuffer

    :param fb:
        Framebuffer
    :type fb: struct drm_framebuffer \*

    :param plane:
        Plane index
    :type plane: unsigned int

.. _`drm_gem_fb_get_obj.description`:

Description
-----------

No additional reference is taken beyond the one that the \ :c:type:`struct drm_frambuffer <drm_frambuffer>`\ 
already holds.

.. _`drm_gem_fb_get_obj.return`:

Return
------

Pointer to \ :c:type:`struct drm_gem_object <drm_gem_object>`\  for the given framebuffer and plane index or NULL
if it does not exist.

.. _`drm_gem_fb_destroy`:

drm_gem_fb_destroy
==================

.. c:function:: void drm_gem_fb_destroy(struct drm_framebuffer *fb)

    Free GEM backed framebuffer

    :param fb:
        Framebuffer
    :type fb: struct drm_framebuffer \*

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

    :param fb:
        Framebuffer
    :type fb: struct drm_framebuffer \*

    :param file:
        DRM file to register the handle for
    :type file: struct drm_file \*

    :param handle:
        Pointer to return the created handle
    :type handle: unsigned int \*

.. _`drm_gem_fb_create_handle.description`:

Description
-----------

This function creates a handle for the GEM object backing the framebuffer.
Drivers can use this as their \ :c:type:`drm_framebuffer_funcs->create_handle <drm_framebuffer_funcs>`\ 
callback. The GETFB IOCTL calls into this callback.

.. _`drm_gem_fb_create_handle.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_gem_fb_create_with_funcs`:

drm_gem_fb_create_with_funcs
============================

.. c:function:: struct drm_framebuffer *drm_gem_fb_create_with_funcs(struct drm_device *dev, struct drm_file *file, const struct drm_mode_fb_cmd2 *mode_cmd, const struct drm_framebuffer_funcs *funcs)

    Helper function for the \ :c:type:`drm_mode_config_funcs.fb_create <drm_mode_config_funcs>`\  callback

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param file:
        DRM file that holds the GEM handle(s) backing the framebuffer
    :type file: struct drm_file \*

    :param mode_cmd:
        Metadata from the userspace framebuffer creation request
    :type mode_cmd: const struct drm_mode_fb_cmd2 \*

    :param funcs:
        vtable to be used for the new framebuffer object
    :type funcs: const struct drm_framebuffer_funcs \*

.. _`drm_gem_fb_create_with_funcs.description`:

Description
-----------

This can be used to set \ :c:type:`struct drm_framebuffer_funcs <drm_framebuffer_funcs>`\  for drivers that need the
\ :c:type:`drm_framebuffer_funcs.dirty <drm_framebuffer_funcs>`\  callback. Use \ :c:func:`drm_gem_fb_create`\  if you don't
need to change \ :c:type:`struct drm_framebuffer_funcs <drm_framebuffer_funcs>`\ .
The function does buffer size validation.

.. _`drm_gem_fb_create_with_funcs.return`:

Return
------

Pointer to a \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  on success or an error pointer on failure.

.. _`drm_gem_fb_create`:

drm_gem_fb_create
=================

.. c:function:: struct drm_framebuffer *drm_gem_fb_create(struct drm_device *dev, struct drm_file *file, const struct drm_mode_fb_cmd2 *mode_cmd)

    Helper function for the \ :c:type:`drm_mode_config_funcs.fb_create <drm_mode_config_funcs>`\  callback

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param file:
        DRM file that holds the GEM handle(s) backing the framebuffer
    :type file: struct drm_file \*

    :param mode_cmd:
        Metadata from the userspace framebuffer creation request
    :type mode_cmd: const struct drm_mode_fb_cmd2 \*

.. _`drm_gem_fb_create.description`:

Description
-----------

This function creates a new framebuffer object described by
\ :c:type:`struct drm_mode_fb_cmd2 <drm_mode_fb_cmd2>`\ . This description includes handles for the buffer(s)
backing the framebuffer.

If your hardware has special alignment or pitch requirements these should be
checked before calling this function. The function does buffer size
validation. Use \ :c:func:`drm_gem_fb_create_with_funcs`\  if you need to set
\ :c:type:`drm_framebuffer_funcs.dirty <drm_framebuffer_funcs>`\ .

Drivers can use this as their \ :c:type:`drm_mode_config_funcs.fb_create <drm_mode_config_funcs>`\  callback.
The ADDFB2 IOCTL calls into this callback.

.. _`drm_gem_fb_create.return`:

Return
------

Pointer to a \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  on success or an error pointer on failure.

.. _`drm_gem_fb_prepare_fb`:

drm_gem_fb_prepare_fb
=====================

.. c:function:: int drm_gem_fb_prepare_fb(struct drm_plane *plane, struct drm_plane_state *state)

    Prepare a GEM backed framebuffer

    :param plane:
        Plane
    :type plane: struct drm_plane \*

    :param state:
        Plane state the fence will be attached to
    :type state: struct drm_plane_state \*

.. _`drm_gem_fb_prepare_fb.description`:

Description
-----------

This function prepares a GEM backed framebuffer for scanout by checking if
the plane framebuffer has a DMA-BUF attached. If it does, it extracts the
exclusive fence and attaches it to the plane state for the atomic helper to
wait on. This function can be used as the \ :c:type:`drm_plane_helper_funcs.prepare_fb <drm_plane_helper_funcs>`\ 
callback.

There is no need for \ :c:type:`drm_plane_helper_funcs.cleanup_fb <drm_plane_helper_funcs>`\  hook for simple
gem based framebuffer drivers which have their buffers always pinned in
memory.

.. _`drm_gem_fb_simple_display_pipe_prepare_fb`:

drm_gem_fb_simple_display_pipe_prepare_fb
=========================================

.. c:function:: int drm_gem_fb_simple_display_pipe_prepare_fb(struct drm_simple_display_pipe *pipe, struct drm_plane_state *plane_state)

    prepare_fb helper for \ :c:type:`struct drm_simple_display_pipe <drm_simple_display_pipe>`\ 

    :param pipe:
        Simple display pipe
    :type pipe: struct drm_simple_display_pipe \*

    :param plane_state:
        Plane state
    :type plane_state: struct drm_plane_state \*

.. _`drm_gem_fb_simple_display_pipe_prepare_fb.description`:

Description
-----------

This function uses \ :c:func:`drm_gem_fb_prepare_fb`\  to check if the plane FB has a
\ :c:type:`struct dma_buf <dma_buf>`\  attached, extracts the exclusive fence and attaches it to plane
state for the atomic helper to wait on. Drivers can use this as their
\ :c:type:`drm_simple_display_pipe_funcs.prepare_fb <drm_simple_display_pipe_funcs>`\  callback.

.. _`drm_gem_fbdev_fb_create`:

drm_gem_fbdev_fb_create
=======================

.. c:function:: struct drm_framebuffer *drm_gem_fbdev_fb_create(struct drm_device *dev, struct drm_fb_helper_surface_size *sizes, unsigned int pitch_align, struct drm_gem_object *obj, const struct drm_framebuffer_funcs *funcs)

    Create a GEM backed \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  for fbdev emulation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param sizes:
        fbdev size description
    :type sizes: struct drm_fb_helper_surface_size \*

    :param pitch_align:
        Optional pitch alignment
    :type pitch_align: unsigned int

    :param obj:
        GEM object backing the framebuffer
    :type obj: struct drm_gem_object \*

    :param funcs:
        Optional vtable to be used for the new framebuffer object when the
        dirty callback is needed.
    :type funcs: const struct drm_framebuffer_funcs \*

.. _`drm_gem_fbdev_fb_create.description`:

Description
-----------

This function creates a framebuffer from a \ :c:type:`struct drm_fb_helper_surface_size <drm_fb_helper_surface_size>`\ 
description for use in the \ :c:type:`drm_fb_helper_funcs.fb_probe <drm_fb_helper_funcs>`\  callback.

.. _`drm_gem_fbdev_fb_create.return`:

Return
------

Pointer to a \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  on success or an error pointer on failure.

.. This file was automatic generated / don't edit.

