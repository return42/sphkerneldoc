
.. _API-drm-vblank-put:

==============
drm_vblank_put
==============

*man drm_vblank_put(9)*

*4.6.0-rc1*

release ownership of vblank events


Synopsis
========

.. c:function:: void drm_vblank_put( struct drm_device * dev, unsigned int pipe )

Arguments
=========

``dev``
    DRM device

``pipe``
    index of CRTC to release


Description
===========

Release ownership of a given vblank counter, turning off interrupts if possible. Disable interrupts after drm_vblank_offdelay milliseconds.

This is the legacy version of ``drm_crtc_vblank_put``.
