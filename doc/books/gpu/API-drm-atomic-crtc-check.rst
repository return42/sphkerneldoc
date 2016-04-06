
.. _API-drm-atomic-crtc-check:

=====================
drm_atomic_crtc_check
=====================

*man drm_atomic_crtc_check(9)*

*4.6.0-rc1*

check crtc state


Synopsis
========

.. c:function:: int drm_atomic_crtc_check( struct drm_crtc * crtc, struct drm_crtc_state * state )

Arguments
=========

``crtc``
    crtc to check

``state``
    crtc state to check


Description
===========

Provides core sanity checks for crtc state.


RETURNS
=======

Zero on success, error code on failure
