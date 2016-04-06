
.. _API-drm-fb-helper-blank:

===================
drm_fb_helper_blank
===================

*man drm_fb_helper_blank(9)*

*4.6.0-rc1*

implementation for ->fb_blank


Synopsis
========

.. c:function:: int drm_fb_helper_blank( int blank, struct fb_info * info )

Arguments
=========

``blank``
    desired blanking state

``info``
    fbdev registered by the helper
