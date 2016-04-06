
.. _API-drm-fb-helper-cfb-fillrect:

==========================
drm_fb_helper_cfb_fillrect
==========================

*man drm_fb_helper_cfb_fillrect(9)*

*4.6.0-rc1*

wrapper around cfb_fillrect


Synopsis
========

.. c:function:: void drm_fb_helper_cfb_fillrect( struct fb_info * info, const struct fb_fillrect * rect )

Arguments
=========

``info``
    fbdev registered by the helper

``rect``
    info about rectangle to fill


Description
===========

A wrapper around cfb_imageblit implemented by fbdev core
