.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_crtc_helper.c

.. _`overview`:

overview
========

The CRTC modeset helper library provides a default set_config implementation
in \ :c:func:`drm_crtc_helper_set_config`\ . Plus a few other convenience functions using
the same callbacks which drivers can use to e.g. restore the modeset
configuration on resume with \ :c:func:`drm_helper_resume_force_mode`\ .

Note that this helper library doesn't track the current power state of CRTCs
and encoders. It can call callbacks like \ :c:type:`drm_encoder_helper_funcs.dpms <drm_encoder_helper_funcs>`\  even
though the hardware is already in the desired state. This deficiency has been
fixed in the atomic helpers.

The driver callbacks are mostly compatible with the atomic modeset helpers,
except for the handling of the primary plane: Atomic helpers require that the
primary plane is implemented as a real standalone plane and not directly tied
to the CRTC state. For easier transition this library provides functions to
implement the old semantics required by the CRTC helpers using the new plane
and atomic helper callbacks.

Drivers are strongly urged to convert to the atomic helpers (by way of first
converting to the plane helpers). New drivers must not use these functions
but need to implement the atomic interface instead, potentially using the
atomic helpers for that.

These legacy modeset helpers use the same function table structures as
all other modesetting helpers. See the documentation for struct
\ :c:type:`struct drm_crtc_helper_funcs <drm_crtc_helper_funcs>`\ , \ :c:type:`struct drm_encoder_helper_funcs <drm_encoder_helper_funcs>`\  and struct
\ :c:type:`struct drm_connector_helper_funcs <drm_connector_helper_funcs>`\ .

.. _`drm_helper_encoder_in_use`:

drm_helper_encoder_in_use
=========================

.. c:function:: bool drm_helper_encoder_in_use(struct drm_encoder *encoder)

    check if a given encoder is in use

    :param encoder:
        encoder to check
    :type encoder: struct drm_encoder \*

.. _`drm_helper_encoder_in_use.description`:

Description
-----------

Checks whether \ ``encoder``\  is with the current mode setting output configuration
in use by any connector. This doesn't mean that it is actually enabled since
the DPMS state is tracked separately.

.. _`drm_helper_encoder_in_use.return`:

Return
------

True if \ ``encoder``\  is used, false otherwise.

.. _`drm_helper_crtc_in_use`:

drm_helper_crtc_in_use
======================

.. c:function:: bool drm_helper_crtc_in_use(struct drm_crtc *crtc)

    check if a given CRTC is in a mode_config

    :param crtc:
        CRTC to check
    :type crtc: struct drm_crtc \*

.. _`drm_helper_crtc_in_use.description`:

Description
-----------

Checks whether \ ``crtc``\  is with the current mode setting output configuration
in use by any connector. This doesn't mean that it is actually enabled since
the DPMS state is tracked separately.

.. _`drm_helper_crtc_in_use.return`:

Return
------

True if \ ``crtc``\  is used, false otherwise.

.. _`drm_helper_disable_unused_functions`:

drm_helper_disable_unused_functions
===================================

.. c:function:: void drm_helper_disable_unused_functions(struct drm_device *dev)

    disable unused objects

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_helper_disable_unused_functions.description`:

Description
-----------

This function walks through the entire mode setting configuration of \ ``dev``\ . It
will remove any CRTC links of unused encoders and encoder links of
disconnected connectors. Then it will disable all unused encoders and CRTCs
either by calling their disable callback if available or by calling their
dpms callback with DRM_MODE_DPMS_OFF.

.. _`drm_helper_disable_unused_functions.note`:

NOTE
----


This function is part of the legacy modeset helper library and will cause
major confusion with atomic drivers. This is because atomic helpers guarantee
to never call ->disable() hooks on a disabled function, or ->enable() hooks
on an enabled functions. \ :c:func:`drm_helper_disable_unused_functions`\  on the other
hand throws such guarantees into the wind and calls disable hooks
unconditionally on unused functions.

.. _`drm_crtc_helper_set_mode`:

drm_crtc_helper_set_mode
========================

.. c:function:: bool drm_crtc_helper_set_mode(struct drm_crtc *crtc, struct drm_display_mode *mode, int x, int y, struct drm_framebuffer *old_fb)

    internal helper to set a mode

    :param crtc:
        CRTC to program
    :type crtc: struct drm_crtc \*

    :param mode:
        mode to use
    :type mode: struct drm_display_mode \*

    :param x:
        horizontal offset into the surface
    :type x: int

    :param y:
        vertical offset into the surface
    :type y: int

    :param old_fb:
        old framebuffer, for cleanup
    :type old_fb: struct drm_framebuffer \*

.. _`drm_crtc_helper_set_mode.description`:

Description
-----------

Try to set \ ``mode``\  on \ ``crtc``\ .  Give \ ``crtc``\  and its associated connectors a chance
to fixup or reject the mode prior to trying to set it. This is an internal
helper that drivers could e.g. use to update properties that require the
entire output pipe to be disabled and re-enabled in a new configuration. For
example for changing whether audio is enabled on a hdmi link or for changing
panel fitter or dither attributes. It is also called by the
\ :c:func:`drm_crtc_helper_set_config`\  helper function to drive the mode setting
sequence.

.. _`drm_crtc_helper_set_mode.return`:

Return
------

True if the mode was set successfully, false otherwise.

.. _`drm_crtc_helper_set_config`:

drm_crtc_helper_set_config
==========================

.. c:function:: int drm_crtc_helper_set_config(struct drm_mode_set *set, struct drm_modeset_acquire_ctx *ctx)

    set a new config from userspace

    :param set:
        mode set configuration
    :type set: struct drm_mode_set \*

    :param ctx:
        lock acquire context, not used here
    :type ctx: struct drm_modeset_acquire_ctx \*

.. _`drm_crtc_helper_set_config.description`:

Description
-----------

The \ :c:func:`drm_crtc_helper_set_config`\  helper function implements the of
\ :c:type:`drm_crtc_funcs.set_config <drm_crtc_funcs>`\  callback for drivers using the legacy CRTC
helpers.

It first tries to locate the best encoder for each connector by calling the
connector \ ``drm_connector_helper_funcs.best_encoder``\  helper operation.

After locating the appropriate encoders, the helper function will call the
mode_fixup encoder and CRTC helper operations to adjust the requested mode,
or reject it completely in which case an error will be returned to the
application. If the new configuration after mode adjustment is identical to
the current configuration the helper function will return without performing
any other operation.

If the adjusted mode is identical to the current mode but changes to the
frame buffer need to be applied, the \ :c:func:`drm_crtc_helper_set_config`\  function
will call the CRTC \ :c:type:`drm_crtc_helper_funcs.mode_set_base <drm_crtc_helper_funcs>`\  helper operation.

If the adjusted mode differs from the current mode, or if the
->mode_set_base() helper operation is not provided, the helper function
performs a full mode set sequence by calling the ->prepare(), ->mode_set()
and ->commit() CRTC and encoder helper operations, in that order.
Alternatively it can also use the dpms and disable helper operations. For
details see \ :c:type:`struct drm_crtc_helper_funcs <drm_crtc_helper_funcs>`\  and struct
\ :c:type:`struct drm_encoder_helper_funcs <drm_encoder_helper_funcs>`\ .

This function is deprecated.  New drivers must implement atomic modeset
support, for which this function is unsuitable. Instead drivers should use
\ :c:func:`drm_atomic_helper_set_config`\ .

.. _`drm_crtc_helper_set_config.return`:

Return
------

Returns 0 on success, negative errno numbers on failure.

.. _`drm_helper_connector_dpms`:

drm_helper_connector_dpms
=========================

.. c:function:: int drm_helper_connector_dpms(struct drm_connector *connector, int mode)

    connector dpms helper implementation

    :param connector:
        affected connector
    :type connector: struct drm_connector \*

    :param mode:
        DPMS mode
    :type mode: int

.. _`drm_helper_connector_dpms.description`:

Description
-----------

The \ :c:func:`drm_helper_connector_dpms`\  helper function implements the
\ :c:type:`drm_connector_funcs.dpms <drm_connector_funcs>`\  callback for drivers using the legacy CRTC
helpers.

This is the main helper function provided by the CRTC helper framework for
implementing the DPMS connector attribute. It computes the new desired DPMS
state for all encoders and CRTCs in the output mesh and calls the
\ :c:type:`drm_crtc_helper_funcs.dpms <drm_crtc_helper_funcs>`\  and \ :c:type:`drm_encoder_helper_funcs.dpms <drm_encoder_helper_funcs>`\  callbacks
provided by the driver.

This function is deprecated.  New drivers must implement atomic modeset
support, where DPMS is handled in the DRM core.

.. _`drm_helper_connector_dpms.return`:

Return
------

Always returns 0.

.. _`drm_helper_resume_force_mode`:

drm_helper_resume_force_mode
============================

.. c:function:: void drm_helper_resume_force_mode(struct drm_device *dev)

    force-restore mode setting configuration

    :param dev:
        drm_device which should be restored
    :type dev: struct drm_device \*

.. _`drm_helper_resume_force_mode.description`:

Description
-----------

Drivers which use the mode setting helpers can use this function to
force-restore the mode setting configuration e.g. on resume or when something
else might have trampled over the hw state (like some overzealous old BIOSen
tended to do).

This helper doesn't provide a error return value since restoring the old
config should never fail due to resource allocation issues since the driver
has successfully set the restored configuration already. Hence this should
boil down to the equivalent of a few dpms on calls, which also don't provide
an error code.

Drivers where simply restoring an old configuration again might fail (e.g.
due to slight differences in allocating shared resources when the
configuration is restored in a different order than when userspace set it up)
need to use their own restore logic.

This function is deprecated. New drivers should implement atomic mode-
setting and use the atomic suspend/resume helpers.

.. _`drm_helper_resume_force_mode.see-also`:

See also
--------

\ :c:func:`drm_atomic_helper_suspend`\ , \ :c:func:`drm_atomic_helper_resume`\ 

.. _`drm_helper_crtc_mode_set`:

drm_helper_crtc_mode_set
========================

.. c:function:: int drm_helper_crtc_mode_set(struct drm_crtc *crtc, struct drm_display_mode *mode, struct drm_display_mode *adjusted_mode, int x, int y, struct drm_framebuffer *old_fb)

    mode_set implementation for atomic plane helpers

    :param crtc:
        DRM CRTC
    :type crtc: struct drm_crtc \*

    :param mode:
        DRM display mode which userspace requested
    :type mode: struct drm_display_mode \*

    :param adjusted_mode:
        DRM display mode adjusted by ->mode_fixup callbacks
    :type adjusted_mode: struct drm_display_mode \*

    :param x:
        x offset of the CRTC scanout area on the underlying framebuffer
    :type x: int

    :param y:
        y offset of the CRTC scanout area on the underlying framebuffer
    :type y: int

    :param old_fb:
        previous framebuffer
    :type old_fb: struct drm_framebuffer \*

.. _`drm_helper_crtc_mode_set.description`:

Description
-----------

This function implements a callback useable as the ->mode_set callback
required by the CRTC helpers. Besides the atomic plane helper functions for
the primary plane the driver must also provide the ->mode_set_nofb callback
to set up the CRTC.

This is a transitional helper useful for converting drivers to the atomic
interfaces.

.. _`drm_helper_crtc_mode_set_base`:

drm_helper_crtc_mode_set_base
=============================

.. c:function:: int drm_helper_crtc_mode_set_base(struct drm_crtc *crtc, int x, int y, struct drm_framebuffer *old_fb)

    mode_set_base implementation for atomic plane helpers

    :param crtc:
        DRM CRTC
    :type crtc: struct drm_crtc \*

    :param x:
        x offset of the CRTC scanout area on the underlying framebuffer
    :type x: int

    :param y:
        y offset of the CRTC scanout area on the underlying framebuffer
    :type y: int

    :param old_fb:
        previous framebuffer
    :type old_fb: struct drm_framebuffer \*

.. _`drm_helper_crtc_mode_set_base.description`:

Description
-----------

This function implements a callback useable as the ->mode_set_base used
required by the CRTC helpers. The driver must provide the atomic plane helper
functions for the primary plane.

This is a transitional helper useful for converting drivers to the atomic
interfaces.

.. This file was automatic generated / don't edit.

