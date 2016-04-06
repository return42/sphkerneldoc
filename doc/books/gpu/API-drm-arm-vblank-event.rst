
.. _API-drm-arm-vblank-event:

====================
drm_arm_vblank_event
====================

*man drm_arm_vblank_event(9)*

*4.6.0-rc1*

arm vblank event after pageflip


Synopsis
========

.. c:function:: void drm_arm_vblank_event( struct drm_device * dev, unsigned int pipe, struct drm_pending_vblank_event * e )

Arguments
=========

``dev``
    DRM device

``pipe``
    CRTC index

``e``
    the event to prepare to send


Description
===========

A lot of drivers need to generate vblank events for the very next vblank interrupt. For example when the page flip interrupt happens when the page flip gets armed, but not when it
actually executes within the next vblank period. This helper function implements exactly the required vblank arming behaviour.

Caller must hold event lock. Caller must also hold a vblank reference for the event ``e``, which will be dropped when the next vblank arrives.

This is the legacy version of ``drm_crtc_arm_vblank_event``.
