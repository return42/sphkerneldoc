.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-vblank-count-and-time:

==============================
drm_crtc_vblank_count_and_time
==============================

*man drm_crtc_vblank_count_and_time(9)*

*4.6.0-rc5*

retrieve “cooked” vblank counter value and the system timestamp
corresponding to that vblank counter value


Synopsis
========

.. c:function:: u32 drm_crtc_vblank_count_and_time( struct drm_crtc * crtc, struct timeval * vblanktime )

Arguments
=========

``crtc``
    which counter to retrieve

``vblanktime``
    Pointer to struct timeval to receive the vblank timestamp.


Description
===========

Fetches the “cooked” vblank count value that represents the number of
vblank events since the system was booted, including lost events due to
modesetting activity. Returns corresponding system timestamp of the time
of the vblank interval that corresponds to the current vblank counter
value.

This is the native KMS version of ``drm_vblank_count_and_time``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
