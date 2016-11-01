.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_simple_kms_helper.c

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

.. _`drm_simple_display_pipe_detach_bridge`:

drm_simple_display_pipe_detach_bridge
=====================================

.. c:function:: void drm_simple_display_pipe_detach_bridge(struct drm_simple_display_pipe *pipe)

    Detach the bridge from the display pipe

    :param struct drm_simple_display_pipe \*pipe:
        simple display pipe object

.. _`drm_simple_display_pipe_detach_bridge.description`:

Description
-----------

Detaches the drm bridge previously attached with
\ :c:func:`drm_simple_display_pipe_attach_bridge`\ 

.. _`drm_simple_display_pipe_init`:

drm_simple_display_pipe_init
============================

.. c:function:: int drm_simple_display_pipe_init(struct drm_device *dev, struct drm_simple_display_pipe *pipe, const struct drm_simple_display_pipe_funcs *funcs, const uint32_t *formats, unsigned int format_count, struct drm_connector *connector)

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
