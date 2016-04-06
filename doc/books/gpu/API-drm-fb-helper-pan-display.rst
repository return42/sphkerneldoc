
.. _API-drm-fb-helper-pan-display:

=========================
drm_fb_helper_pan_display
=========================

*man drm_fb_helper_pan_display(9)*

*4.6.0-rc1*

implementation for ->fb_pan_display


Synopsis
========

.. c:function:: int drm_fb_helper_pan_display( struct fb_var_screeninfo * var, struct fb_info * info )

Arguments
=========

``var``
    updated screen information

``info``
    fbdev registered by the helper
