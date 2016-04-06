
.. _API-drm-vblank-count:

================
drm_vblank_count
================

*man drm_vblank_count(9)*

*4.6.0-rc1*

retrieve “cooked” vblank counter value


Synopsis
========

.. c:function:: u32 drm_vblank_count( struct drm_device * dev, unsigned int pipe )

Arguments
=========

``dev``
    DRM device

``pipe``
    index of CRTC for which to retrieve the counter


Description
===========

Fetches the “cooked” vblank count value that represents the number of vblank events since the system was booted, including lost events due to modesetting activity.

This is the legacy version of ``drm_crtc_vblank_count``.


Returns
=======

The software vblank counter.
