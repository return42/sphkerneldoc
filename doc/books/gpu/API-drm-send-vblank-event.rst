
.. _API-drm-send-vblank-event:

=====================
drm_send_vblank_event
=====================

*man drm_send_vblank_event(9)*

*4.6.0-rc1*

helper to send vblank event after pageflip


Synopsis
========

.. c:function:: void drm_send_vblank_event( struct drm_device * dev, unsigned int pipe, struct drm_pending_vblank_event * e )

Arguments
=========

``dev``
    DRM device

``pipe``
    CRTC index

``e``
    the event to send


Description
===========

Updates sequence # and timestamp on event, and sends it to userspace. Caller must hold event lock.

This is the legacy version of ``drm_crtc_send_vblank_event``.
