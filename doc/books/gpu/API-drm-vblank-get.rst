.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vblank-get:

==============
drm_vblank_get
==============

*man drm_vblank_get(9)*

*4.6.0-rc5*

get a reference count on vblank events


Synopsis
========

.. c:function:: int drm_vblank_get( struct drm_device * dev, unsigned int pipe )

Arguments
=========

``dev``
    DRM device

``pipe``
    index of CRTC to own


Description
===========

Acquire a reference count on vblank events to avoid having them disabled
while in use.

This is the legacy version of ``drm_crtc_vblank_get``.


Returns
=======

Zero on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
