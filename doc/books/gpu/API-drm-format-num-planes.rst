.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-format-num-planes:

=====================
drm_format_num_planes
=====================

*man drm_format_num_planes(9)*

*4.6.0-rc5*

get the number of planes for format


Synopsis
========

.. c:function:: int drm_format_num_planes( uint32_t format )

Arguments
=========

``format``
    pixel format (DRM_FORMAT_*)


Returns
=======

The number of planes used by the specified pixel format.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
