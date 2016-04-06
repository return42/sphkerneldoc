
.. _API-drm-fb-helper-set-suspend:

=========================
drm_fb_helper_set_suspend
=========================

*man drm_fb_helper_set_suspend(9)*

*4.6.0-rc1*

wrapper around fb_set_suspend


Synopsis
========

.. c:function:: void drm_fb_helper_set_suspend( struct drm_fb_helper * fb_helper, int state )

Arguments
=========

``fb_helper``
    driver-allocated fbdev helper

``state``
    desired state, zero to resume, non-zero to suspend


Description
===========

A wrapper around fb_set_suspend implemented by fbdev core
