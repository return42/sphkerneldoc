
.. _API-drm-vblank-count-and-time:

=========================
drm_vblank_count_and_time
=========================

*man drm_vblank_count_and_time(9)*

*4.6.0-rc1*

retrieve “cooked” vblank counter value and the system timestamp corresponding to that vblank counter value.


Synopsis
========

.. c:function:: u32 drm_vblank_count_and_time( struct drm_device * dev, unsigned int pipe, struct timeval * vblanktime )

Arguments
=========

``dev``
    DRM device

``pipe``
    index of CRTC whose counter to retrieve

``vblanktime``
    Pointer to struct timeval to receive the vblank timestamp.


Description
===========

Fetches the “cooked” vblank count value that represents the number of vblank events since the system was booted, including lost events due to modesetting activity. Returns
corresponding system timestamp of the time of the vblank interval that corresponds to the current vblank counter value.

This is the legacy version of ``drm_crtc_vblank_count_and_time``.
