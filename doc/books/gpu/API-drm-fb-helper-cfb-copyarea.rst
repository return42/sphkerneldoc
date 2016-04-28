.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-cfb-copyarea:

==========================
drm_fb_helper_cfb_copyarea
==========================

*man drm_fb_helper_cfb_copyarea(9)*

*4.6.0-rc5*

wrapper around cfb_copyarea


Synopsis
========

.. c:function:: void drm_fb_helper_cfb_copyarea( struct fb_info * info, const struct fb_copyarea * area )

Arguments
=========

``info``
    fbdev registered by the helper

``area``
    info about area to copy


Description
===========

A wrapper around cfb_copyarea implemented by fbdev core


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
