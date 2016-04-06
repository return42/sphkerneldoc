
.. _API-drm-fb-helper-init:

==================
drm_fb_helper_init
==================

*man drm_fb_helper_init(9)*

*4.6.0-rc1*

initialize a drm_fb_helper structure


Synopsis
========

.. c:function:: int drm_fb_helper_init( struct drm_device * dev, struct drm_fb_helper * fb_helper, int crtc_count, int max_conn_count )

Arguments
=========

``dev``
    drm device

``fb_helper``
    driver-allocated fbdev helper structure to initialize

``crtc_count``
    maximum number of crtcs to support in this fbdev emulation

``max_conn_count``
    max connector count


Description
===========

This allocates the structures for the fbdev helper with the given limits. Note that this won't yet touch the hardware (through the driver interfaces) nor register the fbdev. This
is only done in ``drm_fb_helper_initial_config`` to allow driver writes more control over the exact init sequence.

Drivers must call ``drm_fb_helper_prepare`` before calling this function.


RETURNS
=======

Zero if everything went ok, nonzero otherwise.
