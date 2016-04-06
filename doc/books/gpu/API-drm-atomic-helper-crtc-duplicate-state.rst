
.. _API-drm-atomic-helper-crtc-duplicate-state:

======================================
drm_atomic_helper_crtc_duplicate_state
======================================

*man drm_atomic_helper_crtc_duplicate_state(9)*

*4.6.0-rc1*

default state duplicate hook


Synopsis
========

.. c:function:: struct drm_crtc_state ⋆ drm_atomic_helper_crtc_duplicate_state( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    drm CRTC


Description
===========

Default CRTC state duplicate hook for drivers which don't have their own subclassed CRTC state structure.
