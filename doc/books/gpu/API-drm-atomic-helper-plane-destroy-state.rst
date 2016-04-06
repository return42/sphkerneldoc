
.. _API-drm-atomic-helper-plane-destroy-state:

=====================================
drm_atomic_helper_plane_destroy_state
=====================================

*man drm_atomic_helper_plane_destroy_state(9)*

*4.6.0-rc1*

default state destroy hook


Synopsis
========

.. c:function:: void drm_atomic_helper_plane_destroy_state( struct drm_plane * plane, struct drm_plane_state * state )

Arguments
=========

``plane``
    drm plane

``state``
    plane state object to release


Description
===========

Default plane state destroy hook for drivers which don't have their own subclassed plane state structure.
