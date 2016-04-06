
.. _API-drm-crtc-vblank-on:

==================
drm_crtc_vblank_on
==================

*man drm_crtc_vblank_on(9)*

*4.6.0-rc1*

enable vblank events on a CRTC


Synopsis
========

.. c:function:: void drm_crtc_vblank_on( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    CRTC in question


Description
===========

This functions restores the vblank interrupt state captured with ``drm_vblank_off`` again. Note that calls to ``drm_vblank_on`` and ``drm_vblank_off`` can be unbalanced and so can
also be unconditionally called in driver load code to reflect the current hardware state of the crtc.

This is the native kms version of ``drm_vblank_on``.
