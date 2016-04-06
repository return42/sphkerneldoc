
.. _API-struct-drm-crtc-state:

=====================
struct drm_crtc_state
=====================

*man struct drm_crtc_state(9)*

*4.6.0-rc1*

mutable CRTC state


Synopsis
========

.. code-block:: c

    struct drm_crtc_state {
      struct drm_crtc * crtc;
      bool enable;
      bool active;
      bool planes_changed:1;
      bool mode_changed:1;
      bool active_changed:1;
      bool connectors_changed:1;
      bool color_mgmt_changed:1;
      u32 plane_mask;
      u32 connector_mask;
      u32 encoder_mask;
      u32 last_vblank_count;
      struct drm_display_mode adjusted_mode;
      struct drm_display_mode mode;
      struct drm_property_blob * degamma_lut;
      struct drm_property_blob * ctm;
      struct drm_property_blob * gamma_lut;
      struct drm_pending_vblank_event * event;
      struct drm_atomic_state * state;
    };


Members
=======

crtc
    backpointer to the CRTC

enable
    whether the CRTC should be enabled, gates all other state

active
    whether the CRTC is actively displaying (used for DPMS)

planes_changed
    planes on this crtc are updated

mode_changed
    crtc_state->mode or crtc_state->enable has been changed

active_changed
    crtc_state->active has been toggled.

connectors_changed
    connectors to this crtc have been updated

color_mgmt_changed
    color management properties have changed (degamma or gamma LUT or CSC matrix)

plane_mask
    bitmask of (1 << drm_plane_index(plane)) of attached planes

connector_mask
    bitmask of (1 << drm_connector_index(connector)) of attached connectors

encoder_mask
    bitmask of (1 << drm_encoder_index(encoder)) of attached encoders

last_vblank_count
    for helpers and drivers to capture the vblank of the update to ensure framebuffer cleanup isn't done too early

adjusted_mode
    for use by helpers and drivers to compute adjusted mode timings

mode
    current mode timings

degamma_lut
    Lookup table for converting framebuffer pixel data before apply the conversion matrix

ctm
    Transformation matrix

gamma_lut
    Lookup table for converting pixel data after the conversion matrix

event
    optional pointer to a DRM event to signal upon completion of the state update

state
    backpointer to global drm_atomic_state


Description
===========

Note that the distinction between ``enable`` and ``active`` is rather subtile: Flipping ``active`` while ``enable`` is set without changing anything else may never return in a
failure from the ->atomic_check callback. Userspace assumes that a DPMS On will always succeed. In other words: ``enable`` controls resource assignment, ``active`` controls the
actual hardware state.
