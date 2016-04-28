.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vblank-pre-modeset:

======================
drm_vblank_pre_modeset
======================

*man drm_vblank_pre_modeset(9)*

*4.6.0-rc5*

account for vblanks across mode sets


Synopsis
========

.. c:function:: void drm_vblank_pre_modeset( struct drm_device * dev, unsigned int pipe )

Arguments
=========

``dev``
    DRM device

``pipe``
    CRTC index


Description
===========

Account for vblank events across mode setting events, which will likely
reset the hardware frame counter.

This is done by grabbing a temporary vblank reference to ensure that the
vblank interrupt keeps running across the modeset sequence. With this
the software-side vblank frame counting will ensure that there are no
jumps or discontinuities.

Unfortunately this approach is racy and also doesn't work when the
vblank interrupt stops running, e.g. across system suspend resume. It is
therefore highly recommended that drivers use the newer
``drm_vblank_off`` and ``drm_vblank_on`` instead.
``drm_vblank_pre_modeset`` only works correctly when using “cooked”
software vblank frame counters and not relying on any hardware counters.

Drivers must call ``drm_vblank_post_modeset`` when re-enabling the same
crtc again.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
