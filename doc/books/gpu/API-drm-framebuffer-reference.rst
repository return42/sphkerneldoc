
.. _API-drm-framebuffer-reference:

=========================
drm_framebuffer_reference
=========================

*man drm_framebuffer_reference(9)*

*4.6.0-rc1*

incr the fb refcnt


Synopsis
========

.. c:function:: void drm_framebuffer_reference( struct drm_framebuffer * fb )

Arguments
=========

``fb``
    framebuffer


Description
===========

This functions increments the fb's refcount.
