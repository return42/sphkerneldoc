
.. _API-drm-fb-helper-set-par:

=====================
drm_fb_helper_set_par
=====================

*man drm_fb_helper_set_par(9)*

*4.6.0-rc1*

implementation for ->fb_set_par


Synopsis
========

.. c:function:: int drm_fb_helper_set_par( struct fb_info * info )

Arguments
=========

``info``
    fbdev registered by the helper


Description
===========

This will let fbcon do the mode init and is called at initialization time by the fbdev core when registering the driver, and later on through the hotplug callback.
