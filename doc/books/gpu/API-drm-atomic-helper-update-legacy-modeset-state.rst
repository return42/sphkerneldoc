.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-update-legacy-modeset-state:

=============================================
drm_atomic_helper_update_legacy_modeset_state
=============================================

*man drm_atomic_helper_update_legacy_modeset_state(9)*

*4.6.0-rc5*

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

This function updates all the various legacy modeset state pointers in
connectors, encoders and crtcs. It also updates the timestamping
constants used for precise vblank timestamps by calling
``drm_calc_timestamping_constants``.

Drivers can use this for building their own atomic commit if they don't
have a pure helper-based modeset implementation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
