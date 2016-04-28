.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-prepare:

=====================
drm_fb_helper_prepare
=====================

*man drm_fb_helper_prepare(9)*

*4.6.0-rc5*

setup a drm_fb_helper structure


Synopsis
========

.. c:function:: void drm_fb_helper_prepare( struct drm_device * dev, struct drm_fb_helper * helper, const struct drm_fb_helper_funcs * funcs )

Arguments
=========

``dev``
    DRM device

``helper``
    driver-allocated fbdev helper structure to set up

``funcs``
    pointer to structure of functions associate with this helper


Description
===========

Sets up the bare minimum to make the framebuffer helper usable. This is
useful to implement race-free initialization of the polling helpers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
