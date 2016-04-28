.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-vblank-on:

==================
drm_crtc_vblank_on
==================

*man drm_crtc_vblank_on(9)*

*4.6.0-rc5*

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

This functions restores the vblank interrupt state captured with
``drm_vblank_off`` again. Note that calls to ``drm_vblank_on`` and
``drm_vblank_off`` can be unbalanced and so can also be unconditionally
called in driver load code to reflect the current hardware state of the
crtc.

This is the native kms version of ``drm_vblank_on``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
