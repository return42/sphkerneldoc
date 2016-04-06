
.. _API-drm-crtc-vblank-waitqueue:

=========================
drm_crtc_vblank_waitqueue
=========================

*man drm_crtc_vblank_waitqueue(9)*

*4.6.0-rc1*

get vblank waitqueue for the CRTC


Synopsis
========

.. c:function:: wait_queue_head_t ⋆ drm_crtc_vblank_waitqueue( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    which CRTC's vblank waitqueue to retrieve


Description
===========

This function returns a pointer to the vblank waitqueue for the CRTC. Drivers can use this to implement vblank waits using ``wait_event`` & co.
