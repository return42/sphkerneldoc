
.. _API-drm-plane-helper-update:

=======================
drm_plane_helper_update
=======================

*man drm_plane_helper_update(9)*

*4.6.0-rc1*

Transitional helper for plane update


Synopsis
========

.. c:function:: int drm_plane_helper_update( struct drm_plane * plane, struct drm_crtc * crtc, struct drm_framebuffer * fb, int crtc_x, int crtc_y, unsigned int crtc_w, unsigned int crtc_h, uint32_t src_x, uint32_t src_y, uint32_t src_w, uint32_t src_h )

Arguments
=========

``plane``
    plane object to update

``crtc``
    owning CRTC of owning plane

``fb``
    framebuffer to flip onto plane

``crtc_x``
    x offset of primary plane on crtc

``crtc_y``
    y offset of primary plane on crtc

``crtc_w``
    width of primary plane rectangle on crtc

``crtc_h``
    height of primary plane rectangle on crtc

``src_x``
    x offset of ``fb`` for panning

``src_y``
    y offset of ``fb`` for panning

``src_w``
    width of source rectangle in ``fb``

``src_h``
    height of source rectangle in ``fb``


Description
===========

Provides a default plane update handler using the atomic plane update functions. It is fully left to the driver to check plane constraints and handle corner-cases like a fully
occluded or otherwise invisible plane.

This is useful for piecewise transitioning of a driver to the atomic helpers.


RETURNS
=======

Zero on success, error code on failure
