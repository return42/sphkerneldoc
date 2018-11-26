.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/tinydrm/core/tinydrm-pipe.c

.. _`tinydrm_display_pipe_update`:

tinydrm_display_pipe_update
===========================

.. c:function:: void tinydrm_display_pipe_update(struct drm_simple_display_pipe *pipe, struct drm_plane_state *old_state)

    Display pipe update helper

    :param pipe:
        Simple display pipe
    :type pipe: struct drm_simple_display_pipe \*

    :param old_state:
        Old plane state
    :type old_state: struct drm_plane_state \*

.. _`tinydrm_display_pipe_update.description`:

Description
-----------

This function does a full framebuffer flush if the plane framebuffer
has changed. It also handles vblank events. Drivers can use this as their
\ :c:type:`drm_simple_display_pipe_funcs->update <drm_simple_display_pipe_funcs>`\  callback.

.. _`tinydrm_display_pipe_init`:

tinydrm_display_pipe_init
=========================

.. c:function:: int tinydrm_display_pipe_init(struct tinydrm_device *tdev, const struct drm_simple_display_pipe_funcs *funcs, int connector_type, const uint32_t *formats, unsigned int format_count, const struct drm_display_mode *mode, unsigned int rotation)

    Initialize display pipe

    :param tdev:
        tinydrm device
    :type tdev: struct tinydrm_device \*

    :param funcs:
        Display pipe functions
    :type funcs: const struct drm_simple_display_pipe_funcs \*

    :param connector_type:
        Connector type
    :type connector_type: int

    :param formats:
        Array of supported formats (DRM_FORMAT\_\*)
    :type formats: const uint32_t \*

    :param format_count:
        Number of elements in \ ``formats``\ 
    :type format_count: unsigned int

    :param mode:
        Supported mode
    :type mode: const struct drm_display_mode \*

    :param rotation:
        Initial \ ``mode``\  rotation in degrees Counter Clock Wise
    :type rotation: unsigned int

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

