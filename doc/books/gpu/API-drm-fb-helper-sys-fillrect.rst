
.. _API-drm-fb-helper-sys-fillrect:

==========================
drm_fb_helper_sys_fillrect
==========================

*man drm_fb_helper_sys_fillrect(9)*

*4.6.0-rc1*

wrapper around sys_fillrect


Synopsis
========

.. c:function:: void drm_fb_helper_sys_fillrect( struct fb_info * info, const struct fb_fillrect * rect )

Arguments
=========

``info``
    fbdev registered by the helper

``rect``
    info about rectangle to fill


Description
===========

A wrapper around sys_fillrect implemented by fbdev core
