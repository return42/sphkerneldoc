.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-init:

=============
drm_crtc_init
=============

*man drm_crtc_init(9)*

*4.6.0-rc5*

Legacy CRTC initialization function


Synopsis
========

.. c:function:: int drm_crtc_init( struct drm_device * dev, struct drm_crtc * crtc, const struct drm_crtc_funcs * funcs )

Arguments
=========

``dev``
    DRM device

``crtc``
    CRTC object to init

``funcs``
    callbacks for the new CRTC


Description
===========

Initialize a CRTC object with a default helper-provided primary plane
and no cursor plane.


Returns
=======

Zero on success, error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
