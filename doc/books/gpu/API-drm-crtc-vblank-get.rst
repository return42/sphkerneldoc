
.. _API-drm-crtc-vblank-get:

===================
drm_crtc_vblank_get
===================

*man drm_crtc_vblank_get(9)*

*4.6.0-rc1*

get a reference count on vblank events


Synopsis
========

.. c:function:: int drm_crtc_vblank_get( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    which CRTC to own


Description
===========

Acquire a reference count on vblank events to avoid having them disabled while in use.

This is the native kms version of ``drm_vblank_get``.


Returns
=======

Zero on success or a negative error code on failure.
