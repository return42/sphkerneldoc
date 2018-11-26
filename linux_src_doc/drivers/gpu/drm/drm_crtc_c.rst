.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_crtc.c

.. _`overview`:

overview
========

A CRTC represents the overall display pipeline. It receives pixel data from
\ :c:type:`struct drm_plane <drm_plane>`\  and blends them together. The \ :c:type:`struct drm_display_mode <drm_display_mode>`\  is also attached
to the CRTC, specifying display timings. On the output side the data is fed
to one or more \ :c:type:`struct drm_encoder <drm_encoder>`\ , which are then each connected to one
\ :c:type:`struct drm_connector <drm_connector>`\ .

To create a CRTC, a KMS drivers allocates and zeroes an instances of
\ :c:type:`struct drm_crtc <drm_crtc>`\  (possibly as part of a larger structure) and registers it
with a call to \ :c:func:`drm_crtc_init_with_planes`\ .

The CRTC is also the entry point for legacy modeset operations, see
\ :c:type:`drm_crtc_funcs.set_config <drm_crtc_funcs>`\ , legacy plane operations, see
\ :c:type:`drm_crtc_funcs.page_flip <drm_crtc_funcs>`\  and \ :c:type:`drm_crtc_funcs.cursor_set2 <drm_crtc_funcs>`\ , and other legacy
operations like \ :c:type:`drm_crtc_funcs.gamma_set <drm_crtc_funcs>`\ . For atomic drivers all these
features are controlled through \ :c:type:`struct drm_property <drm_property>`\  and
\ :c:type:`drm_mode_config_funcs.atomic_check <drm_mode_config_funcs>`\  and \ :c:type:`drm_mode_config_funcs.atomic_check <drm_mode_config_funcs>`\ .

.. _`drm_crtc_from_index`:

drm_crtc_from_index
===================

.. c:function:: struct drm_crtc *drm_crtc_from_index(struct drm_device *dev, int idx)

    find the registered CRTC at an index

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param idx:
        index of registered CRTC to find for
    :type idx: int

.. _`drm_crtc_from_index.description`:

Description
-----------

Given a CRTC index, return the registered CRTC from DRM device's
list of CRTCs with matching index. This is the inverse of \ :c:func:`drm_crtc_index`\ .
It's useful in the vblank callbacks (like \ :c:type:`drm_driver.enable_vblank <drm_driver>`\  or
\ :c:type:`drm_driver.disable_vblank <drm_driver>`\ ), since that still deals with indices instead
of pointers to \ :c:type:`struct drm_crtc <drm_crtc>`\ ."

.. _`drm_crtc_force_disable`:

drm_crtc_force_disable
======================

.. c:function:: int drm_crtc_force_disable(struct drm_crtc *crtc)

    Forcibly turn off a CRTC

    :param crtc:
        CRTC to turn off
    :type crtc: struct drm_crtc \*

.. _`drm_crtc_force_disable.note`:

Note
----

This should only be used by non-atomic legacy drivers.

.. _`drm_crtc_force_disable.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_crtc_force_disable_all`:

drm_crtc_force_disable_all
==========================

.. c:function:: int drm_crtc_force_disable_all(struct drm_device *dev)

    Forcibly turn off all enabled CRTCs

    :param dev:
        DRM device whose CRTCs to turn off
    :type dev: struct drm_device \*

.. _`drm_crtc_force_disable_all.description`:

Description
-----------

Drivers may want to call this on unload to ensure that all displays are
unlit and the GPU is in a consistent, low power state. Takes modeset locks.

.. _`drm_crtc_force_disable_all.note`:

Note
----

This should only be used by non-atomic legacy drivers. For an atomic
version look at \ :c:func:`drm_atomic_helper_shutdown`\ .

.. _`drm_crtc_force_disable_all.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_crtc_init_with_planes`:

drm_crtc_init_with_planes
=========================

.. c:function:: int drm_crtc_init_with_planes(struct drm_device *dev, struct drm_crtc *crtc, struct drm_plane *primary, struct drm_plane *cursor, const struct drm_crtc_funcs *funcs, const char *name,  ...)

    Initialise a new CRTC object with specified primary and cursor planes.

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param crtc:
        CRTC object to init
    :type crtc: struct drm_crtc \*

    :param primary:
        Primary plane for CRTC
    :type primary: struct drm_plane \*

    :param cursor:
        Cursor plane for CRTC
    :type cursor: struct drm_plane \*

    :param funcs:
        callbacks for the new CRTC
    :type funcs: const struct drm_crtc_funcs \*

    :param name:
        printf style format string for the CRTC name, or NULL for default name
    :type name: const char \*

    :param ellipsis ellipsis:
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

    :param crtc:
        CRTC to cleanup
    :type crtc: struct drm_crtc \*

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

    :param dev:
        drm device for the ioctl
    :type dev: struct drm_device \*

    :param data:
        data pointer for the ioctl
    :type data: void \*

    :param file_priv:
        drm file for the ioctl call
    :type file_priv: struct drm_file \*

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

    helper to call \ :c:type:`drm_mode_config_funcs.set_config <drm_mode_config_funcs>`\ 

    :param set:
        modeset config to set
    :type set: struct drm_mode_set \*

.. _`drm_mode_set_config_internal.description`:

Description
-----------

This is a little helper to wrap internal calls to the
\ :c:type:`drm_mode_config_funcs.set_config <drm_mode_config_funcs>`\  driver interface. The only thing it adds is
correct refcounting dance.

This should only be used by non-atomic legacy drivers.

.. _`drm_mode_set_config_internal.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_crtc_check_viewport`:

drm_crtc_check_viewport
=======================

.. c:function:: int drm_crtc_check_viewport(const struct drm_crtc *crtc, int x, int y, const struct drm_display_mode *mode, const struct drm_framebuffer *fb)

    Checks that a framebuffer is big enough for the CRTC viewport

    :param crtc:
        CRTC that framebuffer will be displayed on
    :type crtc: const struct drm_crtc \*

    :param x:
        x panning
    :type x: int

    :param y:
        y panning
    :type y: int

    :param mode:
        mode that framebuffer will be displayed under
    :type mode: const struct drm_display_mode \*

    :param fb:
        framebuffer to check size of
    :type fb: const struct drm_framebuffer \*

.. _`drm_mode_setcrtc`:

drm_mode_setcrtc
================

.. c:function:: int drm_mode_setcrtc(struct drm_device *dev, void *data, struct drm_file *file_priv)

    set CRTC configuration

    :param dev:
        drm device for the ioctl
    :type dev: struct drm_device \*

    :param data:
        data pointer for the ioctl
    :type data: void \*

    :param file_priv:
        drm file for the ioctl call
    :type file_priv: struct drm_file \*

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

