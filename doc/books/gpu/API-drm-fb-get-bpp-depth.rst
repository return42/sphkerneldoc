
.. _API-drm-fb-get-bpp-depth:

====================
drm_fb_get_bpp_depth
====================

*man drm_fb_get_bpp_depth(9)*

*4.6.0-rc1*

get the bpp/depth values for format


Synopsis
========

.. c:function:: void drm_fb_get_bpp_depth( uint32_t format, unsigned int * depth, int * bpp )

Arguments
=========

``format``
    pixel format (DRM_FORMAT_⋆)

``depth``
    storage for the depth value

``bpp``
    storage for the bpp value


Description
===========

This only supports RGB formats here for compat with code that doesn't use pixel formats directly yet.
