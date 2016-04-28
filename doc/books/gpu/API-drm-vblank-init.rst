.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vblank-init:

===============
drm_vblank_init
===============

*man drm_vblank_init(9)*

*4.6.0-rc5*

initialize vblank support


Synopsis
========

.. c:function:: int drm_vblank_init( struct drm_device * dev, unsigned int num_crtcs )

Arguments
=========

``dev``
    DRM device

``num_crtcs``
    number of CRTCs supported by ``dev``


Description
===========

This function initializes vblank support for ``num_crtcs`` display
pipelines.


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
