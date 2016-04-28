.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-sys-copyarea:

==========================
drm_fb_helper_sys_copyarea
==========================

*man drm_fb_helper_sys_copyarea(9)*

*4.6.0-rc5*

wrapper around sys_copyarea


Synopsis
========

.. c:function:: void drm_fb_helper_sys_copyarea( struct fb_info * info, const struct fb_copyarea * area )

Arguments
=========

``info``
    fbdev registered by the helper

``area``
    info about area to copy


Description
===========

A wrapper around sys_copyarea implemented by fbdev core


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
