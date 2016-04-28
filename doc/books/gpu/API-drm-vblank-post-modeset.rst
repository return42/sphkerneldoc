.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vblank-post-modeset:

=======================
drm_vblank_post_modeset
=======================

*man drm_vblank_post_modeset(9)*

*4.6.0-rc5*

undo drm_vblank_pre_modeset changes


Synopsis
========

.. c:function:: void drm_vblank_post_modeset( struct drm_device * dev, unsigned int pipe )

Arguments
=========

``dev``
    DRM device

``pipe``
    CRTC index


Description
===========

This function again drops the temporary vblank reference acquired in
drm_vblank_pre_modeset.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
