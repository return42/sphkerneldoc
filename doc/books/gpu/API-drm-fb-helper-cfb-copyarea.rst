
.. _API-drm-fb-helper-cfb-copyarea:

==========================
drm_fb_helper_cfb_copyarea
==========================

*man drm_fb_helper_cfb_copyarea(9)*

*4.6.0-rc1*

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
