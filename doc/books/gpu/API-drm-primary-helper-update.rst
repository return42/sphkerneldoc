
.. _API-drm-primary-helper-update:

=========================
drm_primary_helper_update
=========================

*man drm_primary_helper_update(9)*

*4.6.0-rc1*

Helper for primary plane update


Synopsis
========

.. c:function:: int drm_primary_helper_update( struct drm_plane * plane, struct drm_crtc * crtc, struct drm_framebuffer * fb, int crtc_x, int crtc_y, unsigned int crtc_w, unsigned int crtc_h, uint32_t src_x, uint32_t src_y, uint32_t src_w, uint32_t src_h )

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

Provides a default plane update handler for primary planes. This is handler is called in response to a userspace SetPlane operation on the plane with a non-NULL framebuffer. We
call the driver's modeset handler to update the framebuffer.

``SetPlane`` on a primary plane of a disabled CRTC is not supported, and will return an error.

Note that we make some assumptions about hardware limitations that may not be true for all hardware -- 1) Primary plane cannot be repositioned. 2) Primary plane cannot be scaled.
3) Primary plane must cover the entire CRTC. 4) Subpixel positioning is not supported. Drivers for hardware that don't have these restrictions can provide their own implementation
rather than using this helper.


RETURNS
=======

Zero on success, error code on failure
