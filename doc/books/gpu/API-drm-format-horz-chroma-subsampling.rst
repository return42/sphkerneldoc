.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-format-horz-chroma-subsampling:

==================================
drm_format_horz_chroma_subsampling
==================================

*man drm_format_horz_chroma_subsampling(9)*

*4.6.0-rc5*

get the horizontal chroma subsampling factor


Synopsis
========

.. c:function:: int drm_format_horz_chroma_subsampling( uint32_t format )

Arguments
=========

``format``
    pixel format (DRM_FORMAT_*)


Returns
=======

The horizontal chroma subsampling factor for the specified pixel format.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
