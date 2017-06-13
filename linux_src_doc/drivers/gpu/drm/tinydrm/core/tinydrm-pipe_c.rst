.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/tinydrm/core/tinydrm-pipe.c

.. _`tinydrm_display_pipe_update`:

tinydrm_display_pipe_update
===========================

.. c:function:: void tinydrm_display_pipe_update(struct drm_simple_display_pipe *pipe, struct drm_plane_state *old_state)

    Display pipe update helper

    :param struct drm_simple_display_pipe \*pipe:
        Simple display pipe

    :param struct drm_plane_state \*old_state:
        Old plane state

.. _`tinydrm_display_pipe_update.description`:

Description
-----------

This function does a full framebuffer flush if the plane framebuffer
has changed. It also handles vblank events. Drivers can use this as their
\ :c:type:`drm_simple_display_pipe_funcs->update <drm_simple_display_pipe_funcs>`\  callback.

.. _`tinydrm_display_pipe_prepare_fb`:

tinydrm_display_pipe_prepare_fb
===============================

.. c:function:: int tinydrm_display_pipe_prepare_fb(struct drm_simple_display_pipe *pipe, struct drm_plane_state *plane_state)

    Display pipe prepare_fb helper

    :param struct drm_simple_display_pipe \*pipe:
        Simple display pipe

    :param struct drm_plane_state \*plane_state:
        Plane state

.. _`tinydrm_display_pipe_prepare_fb.description`:

Description
-----------

This function uses \ :c:func:`drm_fb_cma_prepare_fb`\  to check if the plane FB has an
dma-buf attached, extracts the exclusive fence and attaches it to plane
state for the atomic helper to wait on. Drivers can use this as their
\ :c:type:`drm_simple_display_pipe_funcs->prepare_fb <drm_simple_display_pipe_funcs>`\  callback.

.. _`tinydrm_display_pipe_init`:

tinydrm_display_pipe_init
=========================

.. c:function:: int tinydrm_display_pipe_init(struct tinydrm_device *tdev, const struct drm_simple_display_pipe_funcs *funcs, int connector_type, const uint32_t *formats, unsigned int format_count, const struct drm_display_mode *mode, unsigned int rotation)

    Initialize display pipe

    :param struct tinydrm_device \*tdev:
        tinydrm device

    :param const struct drm_simple_display_pipe_funcs \*funcs:
        Display pipe functions

    :param int connector_type:
        Connector type

    :param const uint32_t \*formats:
        Array of supported formats (DRM_FORMAT\_\*)

    :param unsigned int format_count:
        Number of elements in \ ``formats``\ 

    :param const struct drm_display_mode \*mode:
        Supported mode

    :param unsigned int rotation:
        Initial \ ``mode``\  rotation in degrees Counter Clock Wise

.. _`tinydrm_display_pipe_init.description`:

Description
-----------

This function sets up a \ :c:type:`struct drm_simple_display_pipe <drm_simple_display_pipe>`\  with a \ :c:type:`struct drm_connector <drm_connector>`\  that
has one fixed \ :c:type:`struct drm_display_mode <drm_display_mode>`\  which is rotated according to \ ``rotation``\ .

.. _`tinydrm_display_pipe_init.return`:

Return
------

Zero on success, negative error code on failure.

.. This file was automatic generated / don't edit.

