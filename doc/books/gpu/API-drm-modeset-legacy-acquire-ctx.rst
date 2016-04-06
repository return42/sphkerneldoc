
.. _API-drm-modeset-legacy-acquire-ctx:

==============================
drm_modeset_legacy_acquire_ctx
==============================

*man drm_modeset_legacy_acquire_ctx(9)*

*4.6.0-rc1*

find acquire ctx for legacy ioctls


Synopsis
========

.. c:function:: struct drm_modeset_acquire_ctx ⋆ drm_modeset_legacy_acquire_ctx( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    drm crtc


Description
===========

Legacy ioctl operations like cursor updates or page flips only have per-crtc locking, and store the acquire ctx in the corresponding crtc. All other legacy operations take all
locks and use a global acquire context. This function grabs the right one.
