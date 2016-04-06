
.. _API-drm-format-plane-cpp:

====================
drm_format_plane_cpp
====================

*man drm_format_plane_cpp(9)*

*4.6.0-rc1*

determine the bytes per pixel value


Synopsis
========

.. c:function:: int drm_format_plane_cpp( uint32_t format, int plane )

Arguments
=========

``format``
    pixel format (DRM_FORMAT_⋆)

``plane``
    plane index


Returns
=======

The bytes per pixel value for the specified plane.
