
.. _API---drm-atomic-helper-plane-destroy-state:

=======================================
__drm_atomic_helper_plane_destroy_state
=======================================

*man __drm_atomic_helper_plane_destroy_state(9)*

*4.6.0-rc1*

release plane state


Synopsis
========

.. c:function:: void __drm_atomic_helper_plane_destroy_state( struct drm_plane * plane, struct drm_plane_state * state )

Arguments
=========

``plane``
    plane object

``state``
    plane state object to release


Description
===========

Releases all resources stored in the plane state without actually freeing the memory of the plane state. This is useful for drivers that subclass the plane state.
