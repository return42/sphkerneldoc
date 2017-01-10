.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_crtc.c

.. _`drm_crtc_force_disable`:

drm_crtc_force_disable
======================

.. c:function:: int drm_crtc_force_disable(struct drm_crtc *crtc)

    Forcibly turn off a CRTC

    :param struct drm_crtc \*crtc:
        CRTC to turn off

.. _`drm_crtc_force_disable.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_crtc_force_disable_all`:

drm_crtc_force_disable_all
==========================

.. c:function:: int drm_crtc_force_disable_all(struct drm_device *dev)

    Forcibly turn off all enabled CRTCs

    :param struct drm_device \*dev:
        DRM device whose CRTCs to turn off

.. _`drm_crtc_force_disable_all.description`:

Description
-----------

Drivers may want to call this on unload to ensure that all displays are
unlit and the GPU is in a consistent, low power state. Takes modeset locks.

.. _`drm_crtc_force_disable_all.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_crtc_init_with_planes`:

drm_crtc_init_with_planes
=========================

.. c:function:: int drm_crtc_init_with_planes(struct drm_device *dev, struct drm_crtc *crtc, struct drm_plane *primary, struct drm_plane *cursor, const struct drm_crtc_funcs *funcs, const char *name,  ...)

    Initialise a new CRTC object with specified primary and cursor planes.

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_crtc \*crtc:
        CRTC object to init

    :param struct drm_plane \*primary:
        Primary plane for CRTC

    :param struct drm_plane \*cursor:
        Cursor plane for CRTC

    :param const struct drm_crtc_funcs \*funcs:
        callbacks for the new CRTC

    :param const char \*name:
        printf style format string for the CRTC name, or NULL for default name

    :param ... :
        variable arguments

.. _`drm_crtc_init_with_planes.description`:

Description
-----------

Inits a new object created as base part of a driver crtc object. Drivers
should use this function instead of \ :c:func:`drm_crtc_init`\ , which is only provided
for backwards compatibility with drivers which do not yet support universal
planes). For really simple hardware which has only 1 plane look at
\ :c:func:`drm_simple_display_pipe_init`\  instead.

.. _`drm_crtc_init_with_planes.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_crtc_cleanup`:

drm_crtc_cleanup
================

.. c:function:: void drm_crtc_cleanup(struct drm_crtc *crtc)

    Clean up the core crtc usage

    :param struct drm_crtc \*crtc:
        CRTC to cleanup

.. _`drm_crtc_cleanup.description`:

Description
-----------

This function cleans up \ ``crtc``\  and removes it from the DRM mode setting
core. Note that the function does *not* free the crtc structure itself,
this is the responsibility of the caller.

.. _`drm_mode_getcrtc`:

drm_mode_getcrtc
================

.. c:function:: int drm_mode_getcrtc(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get CRTC configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_getcrtc.description`:

Description
-----------

Construct a CRTC configuration structure to return to the user.

Called by the user via ioctl.

.. _`drm_mode_getcrtc.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_set_config_internal`:

drm_mode_set_config_internal
============================

.. c:function:: int drm_mode_set_config_internal(struct drm_mode_set *set)

    helper to call ->set_config

    :param struct drm_mode_set \*set:
        modeset config to set

.. _`drm_mode_set_config_internal.description`:

Description
-----------

This is a little helper to wrap internal calls to the ->set_config driver
interface. The only thing it adds is correct refcounting dance.

.. _`drm_mode_set_config_internal.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_crtc_get_hv_timing`:

drm_crtc_get_hv_timing
======================

.. c:function:: void drm_crtc_get_hv_timing(const struct drm_display_mode *mode, int *hdisplay, int *vdisplay)

    Fetches hdisplay/vdisplay for given mode

    :param const struct drm_display_mode \*mode:
        mode to query

    :param int \*hdisplay:
        hdisplay value to fill in

    :param int \*vdisplay:
        vdisplay value to fill in

.. _`drm_crtc_get_hv_timing.description`:

Description
-----------

The vdisplay value will be doubled if the specified mode is a stereo mode of
the appropriate layout.

.. _`drm_crtc_check_viewport`:

drm_crtc_check_viewport
=======================

.. c:function:: int drm_crtc_check_viewport(const struct drm_crtc *crtc, int x, int y, const struct drm_display_mode *mode, const struct drm_framebuffer *fb)

    Checks that a framebuffer is big enough for the CRTC viewport

    :param const struct drm_crtc \*crtc:
        CRTC that framebuffer will be displayed on

    :param int x:
        x panning

    :param int y:
        y panning

    :param const struct drm_display_mode \*mode:
        mode that framebuffer will be displayed under

    :param const struct drm_framebuffer \*fb:
        framebuffer to check size of

.. _`drm_mode_setcrtc`:

drm_mode_setcrtc
================

.. c:function:: int drm_mode_setcrtc(struct drm_device *dev, void *data, struct drm_file *file_priv)

    set CRTC configuration

    :param struct drm_device \*dev:
        drm device for the ioctl

    :param void \*data:
        data pointer for the ioctl

    :param struct drm_file \*file_priv:
        drm file for the ioctl call

.. _`drm_mode_setcrtc.description`:

Description
-----------

Build a new CRTC configuration based on user request.

Called by the user via ioctl.

.. _`drm_mode_setcrtc.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

