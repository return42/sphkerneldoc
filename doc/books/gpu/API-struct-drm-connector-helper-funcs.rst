.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-connector-helper-funcs:

=================================
struct drm_connector_helper_funcs
=================================

*man struct drm_connector_helper_funcs(9)*

*4.6.0-rc5*

helper operations for connectors


Synopsis
========

.. code-block:: c

    struct drm_connector_helper_funcs {
      int (* get_modes) (struct drm_connector *connector);
      enum drm_mode_status (* mode_valid) (struct drm_connector *connector,struct drm_display_mode *mode);
      struct drm_encoder *(* best_encoder) (struct drm_connector *connector);
      struct drm_encoder *(* atomic_best_encoder) (struct drm_connector *connector,struct drm_connector_state *connector_state);
    };


Members
=======

get_modes
    This function should fill in all modes currently valid for the sink
    into the connector->probed_modes list. It should also update the
    EDID property by calling
    ``drm_mode_connector_update_edid_property``.

    The usual way to implement this is to cache the EDID retrieved in
    the probe callback somewhere in the driver-private connector
    structure. In this function drivers then parse the modes in the EDID
    and add them by calling ``drm_add_edid_modes``. But connectors that
    driver a fixed panel can also manually add specific modes using
    ``drm_mode_probed_add``. Drivers which manually add modes should
    also make sure that the ``display_info``, ``width_mm`` and
    ``height_mm`` fields of the struct #drm_connector are filled in.

    Virtual drivers that just want some standard VESA mode with a given
    resolution can call ``drm_add_modes_noedid``, and mark the preferred
    one using ``drm_set_preferred_mode``.

    Finally drivers that support audio probably want to update the ELD
    data, too, using ``drm_edid_to_eld``.

    This function is only called after the ->``detect`` hook has
    indicated that a sink is connected and when the EDID isn't
    overridden through sysfs or the kernel commandline.

    This callback is used by the probe helpers in e.g.
    ``drm_helper_probe_single_connector_modes``.

    RETURNS:

    The number of modes added by calling ``drm_mode_probed_add``.

mode_valid
    Callback to validate a mode for a connector, irrespective of the
    specific display configuration.

    This callback is used by the probe helpers to filter the mode list
    (which is usually derived from the EDID data block from the sink).
    See e.g. ``drm_helper_probe_single_connector_modes``.

    NOTE:

    This only filters the mode list supplied to userspace in the
    GETCONNECOTR IOCTL. Userspace is free to create modes of its own and
    ask the kernel to use them. It this case the atomic helpers or
    legacy CRTC helpers will not call this function. Drivers therefore
    must still fully validate any mode passed in in a modeset request.

    RETURNS:

    Either MODE_OK or one of the failure reasons in enum
    ``drm_mode_status``.

best_encoder
    This function should select the best encoder for the given
    connector.

    This function is used by both the atomic helpers (in the
    ``drm_atomic_helper_check_modeset`` function) and in the legacy CRTC
    helpers.

    NOTE:

    In atomic drivers this function is called in the check phase of an
    atomic update. The driver is not allowed to change or inspect
    anything outside of arguments passed-in. Atomic drivers which need
    to inspect dynamic configuration state should instead use
    ``atomic_best_encoder``.

    RETURNS:

    Encoder that should be used for the given connector and connector
    state, or NULL if no suitable encoder exists. Note that the helpers
    will ensure that encoders aren't used twice, drivers should not
    check for this.

atomic_best_encoder
    This is the atomic version of ``best_encoder`` for atomic drivers
    which need to select the best encoder depending upon the desired
    configuration and can't select it statically.

    This function is used by ``drm_atomic_helper_check_modeset`` and
    either this or ``best_encoder`` is required.

    NOTE:

    This function is called in the check phase of an atomic update. The
    driver is not allowed to change anything outside of the
    free-standing state objects passed-in or assembled in the overall
    ``drm_atomic_state`` update tracking structure.

    RETURNS:

    Encoder that should be used for the given connector and connector
    state, or NULL if no suitable encoder exists. Note that the helpers
    will ensure that encoders aren't used twice, drivers should not
    check for this.


Description
===========

These functions are used by the atomic and legacy modeset helpers and by
the probe helpers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
