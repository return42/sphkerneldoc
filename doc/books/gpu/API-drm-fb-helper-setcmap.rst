
.. _API-drm-fb-helper-setcmap:

=====================
drm_fb_helper_setcmap
=====================

*man drm_fb_helper_setcmap(9)*

*4.6.0-rc1*

implementation for ->fb_setcmap


Synopsis
========

.. c:function:: int drm_fb_helper_setcmap( struct fb_cmap * cmap, struct fb_info * info )

Arguments
=========

``cmap``
    cmap to set

``info``
    fbdev registered by the helper
