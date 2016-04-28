.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-get-bpp-depth:

====================
drm_fb_get_bpp_depth
====================

*man drm_fb_get_bpp_depth(9)*

*4.6.0-rc5*

get the bpp/depth values for format


Synopsis
========

.. c:function:: void drm_fb_get_bpp_depth( uint32_t format, unsigned int * depth, int * bpp )

Arguments
=========

``format``
    pixel format (DRM_FORMAT_*)

``depth``
    storage for the depth value

``bpp``
    storage for the bpp value


Description
===========

This only supports RGB formats here for compat with code that doesn't
use pixel formats directly yet.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
