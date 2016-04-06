
.. _API-drm-atomic-helper-plane-duplicate-state:

=======================================
drm_atomic_helper_plane_duplicate_state
=======================================

*man drm_atomic_helper_plane_duplicate_state(9)*

*4.6.0-rc1*

default state duplicate hook


Synopsis
========

.. c:function:: struct drm_plane_state ⋆ drm_atomic_helper_plane_duplicate_state( struct drm_plane * plane )

Arguments
=========

``plane``
    drm plane


Description
===========

Default plane state duplicate hook for drivers which don't have their own subclassed plane state structure.
