
.. _API-drm-format-vert-chroma-subsampling:

==================================
drm_format_vert_chroma_subsampling
==================================

*man drm_format_vert_chroma_subsampling(9)*

*4.6.0-rc1*

get the vertical chroma subsampling factor


Synopsis
========

.. c:function:: int drm_format_vert_chroma_subsampling( uint32_t format )

Arguments
=========

``format``
    pixel format (DRM_FORMAT_⋆)


Returns
=======

The vertical chroma subsampling factor for the specified pixel format.
