.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-get-cea-aspect-ratio:

========================
drm_get_cea_aspect_ratio
========================

*man drm_get_cea_aspect_ratio(9)*

*4.6.0-rc5*

get the picture aspect ratio corresponding to the input VIC from the CEA
mode list


Synopsis
========

.. c:function:: enum hdmi_picture_aspect drm_get_cea_aspect_ratio( const u8 video_code )

Arguments
=========

``video_code``
    ID given to each of the CEA modes


Description
===========

Returns picture aspect ratio


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
