
.. _API---drm-atomic-helper-plane-duplicate-state:

=========================================
__drm_atomic_helper_plane_duplicate_state
=========================================

*man __drm_atomic_helper_plane_duplicate_state(9)*

*4.6.0-rc1*

copy atomic plane state


Synopsis
========

.. c:function:: void __drm_atomic_helper_plane_duplicate_state( struct drm_plane * plane, struct drm_plane_state * state )

Arguments
=========

``plane``
    plane object

``state``
    atomic plane state


Description
===========

Copies atomic state from a plane's current state. This is useful for drivers that subclass the plane state.
