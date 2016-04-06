
.. _API-drm-modeset-lock-crtc:

=====================
drm_modeset_lock_crtc
=====================

*man drm_modeset_lock_crtc(9)*

*4.6.0-rc1*

lock crtc with hidden acquire ctx for a plane update


Synopsis
========

.. c:function:: void drm_modeset_lock_crtc( struct drm_crtc * crtc, struct drm_plane * plane )

Arguments
=========

``crtc``
    DRM CRTC

``plane``
    DRM plane to be updated on ``crtc``


Description
===========

This function locks the given crtc and plane (which should be either the primary or cursor plane) using a hidden acquire context. This is necessary so that drivers internally using
the atomic interfaces can grab further locks with the lock acquire context.

Note that ``plane`` can be NULL, e.g. when the cursor support hasn't yet been converted to universal planes yet.
