.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-arm-vblank-event:

=========================
drm_crtc_arm_vblank_event
=========================

*man drm_crtc_arm_vblank_event(9)*

*4.6.0-rc5*

arm vblank event after pageflip


Synopsis
========

.. c:function:: void drm_crtc_arm_vblank_event( struct drm_crtc * crtc, struct drm_pending_vblank_event * e )

Arguments
=========

``crtc``
    the source CRTC of the vblank event

``e``
    the event to send


Description
===========

A lot of drivers need to generate vblank events for the very next vblank
interrupt. For example when the page flip interrupt happens when the
page flip gets armed, but not when it actually executes within the next
vblank period. This helper function implements exactly the required
vblank arming behaviour.

Caller must hold event lock. Caller must also hold a vblank reference
for the event ``e``, which will be dropped when the next vblank arrives.

This is the native KMS version of ``drm_arm_vblank_event``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
