
.. _API-drm-fb-helper-fill-fix:

======================
drm_fb_helper_fill_fix
======================

*man drm_fb_helper_fill_fix(9)*

*4.6.0-rc1*

initializes fixed fbdev information


Synopsis
========

.. c:function:: void drm_fb_helper_fill_fix( struct fb_info * info, uint32_t pitch, uint32_t depth )

Arguments
=========

``info``
    fbdev registered by the helper

``pitch``
    desired pitch

``depth``
    desired depth


Description
===========

Helper to fill in the fixed fbdev information useful for a non-accelerated fbdev emulations. Drivers which support acceleration methods which impose additional constraints need to
set up their own limits.

Drivers should call this (or their equivalent setup code) from their ->fb_probe callback.
