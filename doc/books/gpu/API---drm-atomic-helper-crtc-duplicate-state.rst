
.. _API---drm-atomic-helper-crtc-duplicate-state:

========================================
__drm_atomic_helper_crtc_duplicate_state
========================================

*man __drm_atomic_helper_crtc_duplicate_state(9)*

*4.6.0-rc1*

copy atomic CRTC state


Synopsis
========

.. c:function:: void __drm_atomic_helper_crtc_duplicate_state( struct drm_crtc * crtc, struct drm_crtc_state * state )

Arguments
=========

``crtc``
    CRTC object

``state``
    atomic CRTC state


Description
===========

Copies atomic state from a CRTC's current state and resets inferred values. This is useful for drivers that subclass the CRTC state.
