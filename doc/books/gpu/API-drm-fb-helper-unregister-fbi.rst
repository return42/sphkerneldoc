
.. _API-drm-fb-helper-unregister-fbi:

============================
drm_fb_helper_unregister_fbi
============================

*man drm_fb_helper_unregister_fbi(9)*

*4.6.0-rc1*

unregister fb_info framebuffer device


Synopsis
========

.. c:function:: void drm_fb_helper_unregister_fbi( struct drm_fb_helper * fb_helper )

Arguments
=========

``fb_helper``
    driver-allocated fbdev helper


Description
===========

A wrapper around unregister_framebuffer, to release the fb_info framebuffer device
