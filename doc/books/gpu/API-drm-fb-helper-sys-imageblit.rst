.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-sys-imageblit:

===========================
drm_fb_helper_sys_imageblit
===========================

*man drm_fb_helper_sys_imageblit(9)*

*4.6.0-rc5*

wrapper around sys_imageblit


Synopsis
========

.. c:function:: void drm_fb_helper_sys_imageblit( struct fb_info * info, const struct fb_image * image )

Arguments
=========

``info``
    fbdev registered by the helper

``image``
    info about image to blit


Description
===========

A wrapper around sys_imageblit implemented by fbdev core


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
