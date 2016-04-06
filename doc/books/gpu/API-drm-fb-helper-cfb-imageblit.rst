
.. _API-drm-fb-helper-cfb-imageblit:

===========================
drm_fb_helper_cfb_imageblit
===========================

*man drm_fb_helper_cfb_imageblit(9)*

*4.6.0-rc1*

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
