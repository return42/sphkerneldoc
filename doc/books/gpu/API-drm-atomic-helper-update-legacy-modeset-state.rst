
.. _API-drm-atomic-helper-update-legacy-modeset-state:

=============================================
drm_atomic_helper_update_legacy_modeset_state
=============================================

*man drm_atomic_helper_update_legacy_modeset_state(9)*

*4.6.0-rc1*

update legacy modeset state


Synopsis
========

.. c:function:: void drm_atomic_helper_update_legacy_modeset_state( struct drm_device * dev, struct drm_atomic_state * old_state )

Arguments
=========

``dev``
    DRM device

``old_state``
    atomic state object with old state structures


Description
===========

This function updates all the various legacy modeset state pointers in connectors, encoders and crtcs. It also updates the timestamping constants used for precise vblank timestamps
by calling ``drm_calc_timestamping_constants``.

Drivers can use this for building their own atomic commit if they don't have a pure helper-based modeset implementation.
