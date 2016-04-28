.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-vblank-waitqueue:

=========================
drm_crtc_vblank_waitqueue
=========================

*man drm_crtc_vblank_waitqueue(9)*

*4.6.0-rc5*

get vblank waitqueue for the CRTC


Synopsis
========

.. c:function:: wait_queue_head_t * drm_crtc_vblank_waitqueue( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    which CRTC's vblank waitqueue to retrieve


Description
===========

This function returns a pointer to the vblank waitqueue for the CRTC.
Drivers can use this to implement vblank waits using ``wait_event`` &
co.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
