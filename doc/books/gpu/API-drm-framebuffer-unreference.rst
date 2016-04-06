
.. _API-drm-framebuffer-unreference:

===========================
drm_framebuffer_unreference
===========================

*man drm_framebuffer_unreference(9)*

*4.6.0-rc1*

unref a framebuffer


Synopsis
========

.. c:function:: void drm_framebuffer_unreference( struct drm_framebuffer * fb )

Arguments
=========

``fb``
    framebuffer to unref


Description
===========

This functions decrements the fb's refcount and frees it if it drops to zero.
