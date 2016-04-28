.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-helper-mode-fill-fb-struct:

==============================
drm_helper_mode_fill_fb_struct
==============================

*man drm_helper_mode_fill_fb_struct(9)*

*4.6.0-rc5*

fill out framebuffer metadata


Synopsis
========

.. c:function:: void drm_helper_mode_fill_fb_struct( struct drm_framebuffer * fb, const struct drm_mode_fb_cmd2 * mode_cmd )

Arguments
=========

``fb``
    drm_framebuffer object to fill out

``mode_cmd``
    metadata from the userspace fb creation request


Description
===========

This helper can be used in a drivers fb_create callback to pre-fill the
fb's metadata fields.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
