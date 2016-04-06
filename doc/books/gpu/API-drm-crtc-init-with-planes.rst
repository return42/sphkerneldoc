
.. _API-drm-crtc-init-with-planes:

=========================
drm_crtc_init_with_planes
=========================

*man drm_crtc_init_with_planes(9)*

*4.6.0-rc1*

Initialise a new CRTC object with specified primary and cursor planes.


Synopsis
========

.. c:function:: int drm_crtc_init_with_planes( struct drm_device * dev, struct drm_crtc * crtc, struct drm_plane * primary, struct drm_plane * cursor, const struct drm_crtc_funcs * funcs, const char * name, ... )

Arguments
=========

``dev``
    DRM device

``crtc``
    CRTC object to init

``primary``
    Primary plane for CRTC

``cursor``
    Cursor plane for CRTC

``funcs``
    callbacks for the new CRTC

``name``
    printf style format string for the CRTC name, or NULL for default name

``...``
    variable arguments


Description
===========

Inits a new object created as base part of a driver crtc object.


Returns
=======

Zero on success, error code on failure.
