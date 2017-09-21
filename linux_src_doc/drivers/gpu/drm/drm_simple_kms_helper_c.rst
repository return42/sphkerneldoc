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

    :param struct drm_simple_display_pipe \*pipe:
        simple display pipe object

    :param struct drm_bridge \*bridge:
        bridge to attach

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

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_simple_display_pipe \*pipe:
        simple display pipe object to initialize

    :param const struct drm_simple_display_pipe_funcs \*funcs:
        callbacks for the display pipe (optional)

    :param const uint32_t \*formats:
        array of supported formats (DRM_FORMAT\_\*)

    :param unsigned int format_count:
        number of elements in \ ``formats``\ 

    :param const uint64_t \*format_modifiers:
        array of formats modifiers

    :param struct drm_connector \*connector:
        connector to attach and register (optional)

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

