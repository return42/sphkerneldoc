
.. _API-drm-fb-helper-check-var:

=======================
drm_fb_helper_check_var
=======================

*man drm_fb_helper_check_var(9)*

*4.6.0-rc1*

implementation for ->fb_check_var


Synopsis
========

.. c:function:: int drm_fb_helper_check_var( struct fb_var_screeninfo * var, struct fb_info * info )

Arguments
=========

``var``
    screeninfo to check

``info``
    fbdev registered by the helper
