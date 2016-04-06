
.. _API-drm-vblank-on:

=============
drm_vblank_on
=============

*man drm_vblank_on(9)*

*4.6.0-rc1*

enable vblank events on a CRTC


Synopsis
========

.. c:function:: void drm_vblank_on( struct drm_device * dev, unsigned int pipe )

Arguments
=========

``dev``
    DRM device

``pipe``
    CRTC index


Description
===========

This functions restores the vblank interrupt state captured with ``drm_vblank_off`` again. Note that calls to ``drm_vblank_on`` and ``drm_vblank_off`` can be unbalanced and so can
also be unconditionally called in driver load code to reflect the current hardware state of the crtc.

This is the legacy version of ``drm_crtc_vblank_on``.
