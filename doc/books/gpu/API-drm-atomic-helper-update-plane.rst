.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-update-plane:

==============================
drm_atomic_helper_update_plane
==============================

*man drm_atomic_helper_update_plane(9)*

*4.6.0-rc5*

Helper for primary plane update using atomic


Synopsis
========

.. c:function:: int drm_atomic_helper_update_plane( struct drm_plane * plane, struct drm_crtc * crtc, struct drm_framebuffer * fb, int crtc_x, int crtc_y, unsigned int crtc_w, unsigned int crtc_h, uint32_t src_x, uint32_t src_y, uint32_t src_w, uint32_t src_h )

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

Provides a default plane update handler using the atomic driver
interface.


RETURNS
=======

Zero on success, error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
