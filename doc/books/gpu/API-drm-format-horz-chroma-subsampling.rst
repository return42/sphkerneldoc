
.. _API-drm-format-horz-chroma-subsampling:

==================================
drm_format_horz_chroma_subsampling
==================================

*man drm_format_horz_chroma_subsampling(9)*

*4.6.0-rc1*

get the horizontal chroma subsampling factor


Synopsis
========

.. c:function:: int drm_format_horz_chroma_subsampling( uint32_t format )

Arguments
=========

``format``
    pixel format (DRM_FORMAT_⋆)


Returns
=======

The horizontal chroma subsampling factor for the specified pixel format.
