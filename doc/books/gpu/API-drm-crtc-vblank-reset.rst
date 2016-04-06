
.. _API-drm-crtc-vblank-reset:

=====================
drm_crtc_vblank_reset
=====================

*man drm_crtc_vblank_reset(9)*

*4.6.0-rc1*

reset vblank state to off on a CRTC


Synopsis
========

.. c:function:: void drm_crtc_vblank_reset( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    CRTC in question


Description
===========

Drivers can use this function to reset the vblank state to off at load time. Drivers should use this together with the ``drm_crtc_vblank_off`` and ``drm_crtc_vblank_on`` functions.
The difference compared to ``drm_crtc_vblank_off`` is that this function doesn't save the vblank counter and hence doesn't need to call any driver hooks.
