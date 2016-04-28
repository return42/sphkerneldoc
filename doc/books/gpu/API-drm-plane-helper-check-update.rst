.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-plane-helper-check-update:

=============================
drm_plane_helper_check_update
=============================

*man drm_plane_helper_check_update(9)*

*4.6.0-rc5*

Check plane update for validity


Synopsis
========

.. c:function:: int drm_plane_helper_check_update( struct drm_plane * plane, struct drm_crtc * crtc, struct drm_framebuffer * fb, struct drm_rect * src, struct drm_rect * dest, const struct drm_rect * clip, int min_scale, int max_scale, bool can_position, bool can_update_disabled, bool * visible )

Arguments
=========

``plane``
    plane object to update

``crtc``
    owning CRTC of owning plane

``fb``
    framebuffer to flip onto plane

``src``
    source coordinates in 16.16 fixed point

``dest``
    integer destination coordinates

``clip``
    integer clipping coordinates

``min_scale``
    minimum ``src``:``dest`` scaling factor in 16.16 fixed point

``max_scale``
    maximum ``src``:``dest`` scaling factor in 16.16 fixed point

``can_position``
    is it legal to position the plane such that it doesn't cover the
    entire crtc? This will generally only be false for primary planes.

``can_update_disabled``
    can the plane be updated while the crtc is disabled?

``visible``
    output parameter indicating whether plane is still visible after
    clipping


Description
===========

Checks that a desired plane update is valid. Drivers that provide their
own plane handling rather than helper-provided implementations may still
wish to call this function to avoid duplication of error checking code.


RETURNS
=======

Zero if update appears valid, error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
