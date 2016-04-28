.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-send-vblank-event:

==========================
drm_crtc_send_vblank_event
==========================

*man drm_crtc_send_vblank_event(9)*

*4.6.0-rc5*

helper to send vblank event after pageflip


Synopsis
========

.. c:function:: void drm_crtc_send_vblank_event( struct drm_crtc * crtc, struct drm_pending_vblank_event * e )

Arguments
=========

``crtc``
    the source CRTC of the vblank event

``e``
    the event to send


Description
===========

Updates sequence # and timestamp on event, and sends it to userspace.
Caller must hold event lock.

This is the native KMS version of ``drm_send_vblank_event``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
