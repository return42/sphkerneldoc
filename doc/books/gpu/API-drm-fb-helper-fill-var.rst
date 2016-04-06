
.. _API-drm-fb-helper-fill-var:

======================
drm_fb_helper_fill_var
======================

*man drm_fb_helper_fill_var(9)*

*4.6.0-rc1*

initalizes variable fbdev information


Synopsis
========

.. c:function:: void drm_fb_helper_fill_var( struct fb_info * info, struct drm_fb_helper * fb_helper, uint32_t fb_width, uint32_t fb_height )

Arguments
=========

``info``
    fbdev instance to set up

``fb_helper``
    fb helper instance to use as template

``fb_width``
    desired fb width

``fb_height``
    desired fb height


Description
===========

Sets up the variable fbdev metainformation from the given fb helper instance and the drm framebuffer allocated in fb_helper->fb.

Drivers should call this (or their equivalent setup code) from their ->fb_probe callback after having allocated the fbdev backing storage framebuffer.
