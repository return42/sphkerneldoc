.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vblank-cleanup:

==================
drm_vblank_cleanup
==================

*man drm_vblank_cleanup(9)*

*4.6.0-rc5*

cleanup vblank support


Synopsis
========

.. c:function:: void drm_vblank_cleanup( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

This function cleans up any resources allocated in drm_vblank_init.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
