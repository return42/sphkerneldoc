.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vblank-on:

=============
drm_vblank_on
=============

*man drm_vblank_on(9)*

*4.6.0-rc5*

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

This functions restores the vblank interrupt state captured with
``drm_vblank_off`` again. Note that calls to ``drm_vblank_on`` and
``drm_vblank_off`` can be unbalanced and so can also be unconditionally
called in driver load code to reflect the current hardware state of the
crtc.

This is the legacy version of ``drm_crtc_vblank_on``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
