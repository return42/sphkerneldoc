
.. _API-drm-vblank-off:

==============
drm_vblank_off
==============

*man drm_vblank_off(9)*

*4.6.0-rc1*

disable vblank events on a CRTC


Synopsis
========

.. c:function:: void drm_vblank_off( struct drm_device * dev, unsigned int pipe )

Arguments
=========

``dev``
    DRM device

``pipe``
    CRTC index


Description
===========

Drivers can use this function to shut down the vblank interrupt handling when disabling a crtc. This function ensures that the latest vblank frame count is stored so that
``drm_vblank_on`` can restore it again.

Drivers must use this function when the hardware vblank counter can get reset, e.g. when suspending.

This is the legacy version of ``drm_crtc_vblank_off``.
