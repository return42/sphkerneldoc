.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-unregister-fbi:

============================
drm_fb_helper_unregister_fbi
============================

*man drm_fb_helper_unregister_fbi(9)*

*4.6.0-rc5*

unregister fb_info framebuffer device


Synopsis
========

.. c:function:: void drm_fb_helper_unregister_fbi( struct drm_fb_helper * fb_helper )

Arguments
=========

``fb_helper``
    driver-allocated fbdev helper


Description
===========

A wrapper around unregister_framebuffer, to release the fb_info
framebuffer device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
