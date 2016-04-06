
.. _API-drm-handle-vblank:

=================
drm_handle_vblank
=================

*man drm_handle_vblank(9)*

*4.6.0-rc1*

handle a vblank event


Synopsis
========

.. c:function:: bool drm_handle_vblank( struct drm_device * dev, unsigned int pipe )

Arguments
=========

``dev``
    DRM device

``pipe``
    index of CRTC where this event occurred


Description
===========

Drivers should call this routine in their vblank interrupt handlers to update the vblank counter and send any signals that may be pending.

This is the legacy version of ``drm_crtc_handle_vblank``.
