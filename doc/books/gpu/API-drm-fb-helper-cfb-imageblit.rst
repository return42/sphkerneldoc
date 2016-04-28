.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-cfb-imageblit:

===========================
drm_fb_helper_cfb_imageblit
===========================

*man drm_fb_helper_cfb_imageblit(9)*

*4.6.0-rc5*

wrapper around cfb_imageblit


Synopsis
========

.. c:function:: void drm_fb_helper_cfb_imageblit( struct fb_info * info, const struct fb_image * image )

Arguments
=========

``info``
    fbdev registered by the helper

``image``
    info about image to blit


Description
===========

A wrapper around cfb_imageblit implemented by fbdev core


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
