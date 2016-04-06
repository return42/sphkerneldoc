
.. _API-drm-crtc-vblank-put:

===================
drm_crtc_vblank_put
===================

*man drm_crtc_vblank_put(9)*

*4.6.0-rc1*

give up ownership of vblank events


Synopsis
========

.. c:function:: void drm_crtc_vblank_put( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    which counter to give up


Description
===========

Release ownership of a given vblank counter, turning off interrupts if possible. Disable interrupts after drm_vblank_offdelay milliseconds.

This is the native kms version of ``drm_vblank_put``.
