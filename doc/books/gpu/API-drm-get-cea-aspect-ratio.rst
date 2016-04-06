
.. _API-drm-get-cea-aspect-ratio:

========================
drm_get_cea_aspect_ratio
========================

*man drm_get_cea_aspect_ratio(9)*

*4.6.0-rc1*

get the picture aspect ratio corresponding to the input VIC from the CEA mode list


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
