.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_simple_kms_helper.c

.. _`overview`:

overview
========

This helper library provides helpers for drivers for simple display
hardware.

\ :c:func:`drm_simple_display_pipe_init`\  initializes a simple display pipeline
which has only one full-screen scanout buffer feeding one output. The
pipeline is represented by \ :c:type:`struct drm_simple_display_pipe <drm_simple_display_pipe>`\  and binds
together \ :c:type:`struct drm_plane <drm_plane>`\ , \ :c:type:`struct drm_crtc <drm_crtc>`\  and \ :c:type:`struct drm_encoder <drm_encoder>`\  structures into one fixed
entity. Some flexibility for code reuse is provided through a separately
allocated \ :c:type:`struct drm_connector <drm_connector>`\  object and supporting optional \ :c:type:`struct drm_bridge <drm_bridge>`\ 
encoder drivers.

.. _`drm_simple_display_pipe_attach_bridge`:

drm_simple_display_pipe_attach_bridge
=====================================

.. c:function:: int drm_simple_display_pipe_attach_bridge(struct drm_simple_display_pipe *pipe, struct drm_bridge *bridge)

    Attach a bridge to the display pipe

    :param pipe:
        simple display pipe object
    :type pipe: struct drm_simple_display_pipe \*

    :param bridge:
        bridge to attach
    :type bridge: struct drm_bridge \*

.. _`drm_simple_display_pipe_attach_bridge.description`:

Description
-----------

Makes it possible to still use the drm_simple_display_pipe helpers when
a DRM bridge has to be used.

Note that you probably want to initialize the pipe by passing a NULL
connector to \ :c:func:`drm_simple_display_pipe_init`\ .

.. _`drm_simple_display_pipe_attach_bridge.return`:

Return
------

Zero on success, negative error code on failure.

.. _`drm_simple_display_pipe_init`:

drm_simple_display_pipe_init
============================

.. c:function:: int drm_simple_display_pipe_init(struct drm_device *dev, struct drm_simple_display_pipe *pipe, const struct drm_simple_display_pipe_funcs *funcs, const uint32_t *formats, unsigned int format_count, const uint64_t *format_modifiers, struct drm_connector *connector)

    Initialize a simple display pipeline

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param pipe:
        simple display pipe object to initialize
    :type pipe: struct drm_simple_display_pipe \*

    :param funcs:
        callbacks for the display pipe (optional)
    :type funcs: const struct drm_simple_display_pipe_funcs \*

    :param formats:
        array of supported formats (DRM_FORMAT\_\*)
    :type formats: const uint32_t \*

    :param format_count:
        number of elements in \ ``formats``\ 
    :type format_count: unsigned int

    :param format_modifiers:
        array of formats modifiers
    :type format_modifiers: const uint64_t \*

    :param connector:
        connector to attach and register (optional)
    :type connector: struct drm_connector \*

.. _`drm_simple_display_pipe_init.description`:

Description
-----------

Sets up a display pipeline which consist of a really simple
plane-crtc-encoder pipe.

If a connector is supplied, the pipe will be coupled with the provided
connector. You may supply a NULL connector when using drm bridges, that
handle connectors themselves (see \ :c:func:`drm_simple_display_pipe_attach_bridge`\ ).

Teardown of a simple display pipe is all handled automatically by the drm
core through calling \ :c:func:`drm_mode_config_cleanup`\ . Drivers afterwards need to
release the memory for the structure themselves.

.. _`drm_simple_display_pipe_init.return`:

Return
------

Zero on success, negative error code on failure.

.. This file was automatic generated / don't edit.

