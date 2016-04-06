
.. _API-drm-vblank-init:

===============
drm_vblank_init
===============

*man drm_vblank_init(9)*

*4.6.0-rc1*

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

This function initializes vblank support for ``num_crtcs`` display pipelines.


Returns
=======

Zero on success or a negative error code on failure.
