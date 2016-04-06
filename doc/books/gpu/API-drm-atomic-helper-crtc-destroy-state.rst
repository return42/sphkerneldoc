
.. _API-drm-atomic-helper-crtc-destroy-state:

====================================
drm_atomic_helper_crtc_destroy_state
====================================

*man drm_atomic_helper_crtc_destroy_state(9)*

*4.6.0-rc1*

default state destroy hook


Synopsis
========

.. c:function:: void drm_atomic_helper_crtc_destroy_state( struct drm_crtc * crtc, struct drm_crtc_state * state )

Arguments
=========

``crtc``
    drm CRTC

``state``
    CRTC state object to release


Description
===========

Default CRTC state destroy hook for drivers which don't have their own subclassed CRTC state structure.
