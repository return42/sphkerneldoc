.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-unlink-fbi:

========================
drm_fb_helper_unlink_fbi
========================

*man drm_fb_helper_unlink_fbi(9)*

*4.6.0-rc5*

wrapper around unlink_framebuffer


Synopsis
========

.. c:function:: void drm_fb_helper_unlink_fbi( struct drm_fb_helper * fb_helper )

Arguments
=========

``fb_helper``
    driver-allocated fbdev helper


Description
===========

A wrapper around unlink_framebuffer implemented by fbdev core


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
