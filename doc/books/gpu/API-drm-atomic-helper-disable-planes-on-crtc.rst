
.. _API-drm-atomic-helper-disable-planes-on-crtc:

========================================
drm_atomic_helper_disable_planes_on_crtc
========================================

*man drm_atomic_helper_disable_planes_on_crtc(9)*

*4.6.0-rc1*

helper to disable CRTC's planes


Synopsis
========

.. c:function:: void drm_atomic_helper_disable_planes_on_crtc( struct drm_crtc * crtc, bool atomic )

Arguments
=========

``crtc``
    CRTC

``atomic``
    if set, synchronize with CRTC's atomic_begin/flush hooks


Description
===========

Disables all planes associated with the given CRTC. This can be used for instance in the CRTC helper disable callback to disable all planes before shutting down the display
pipeline.

If the atomic-parameter is set the function calls the CRTC's atomic_begin hook before and atomic_flush hook after disabling the planes.

It is a bug to call this function without having implemented the ->``atomic_disable`` plane hook.
