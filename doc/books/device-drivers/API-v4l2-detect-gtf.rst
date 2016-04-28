.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-detect-gtf:

===============
v4l2_detect_gtf
===============

*man v4l2_detect_gtf(9)*

*4.6.0-rc5*

detect if the given timings follow the GTF standard


Synopsis
========

.. c:function:: bool v4l2_detect_gtf( unsigned frame_height, unsigned hfreq, unsigned vsync, u32 polarities, bool interlaced, struct v4l2_fract aspect, struct v4l2_dv_timings * fmt )

Arguments
=========

``frame_height``
    the total height of the frame (including blanking) in lines.

``hfreq``
    the horizontal frequency in Hz.

``vsync``
    the height of the vertical sync in lines.

``polarities``
    the horizontal and vertical polarities (same as struct
    v4l2_bt_timings polarities).

``interlaced``
    if this flag is true, it indicates interlaced format

``aspect``
    preferred aspect ratio. GTF has no method of determining the aspect
    ratio in order to derive the image width from the image height, so
    it has to be passed explicitly. Usually the native screen aspect
    ratio is used for this. If it is not filled in correctly, then 16:9
    will be assumed.

``fmt``
    the resulting timings.


Description
===========

This function will attempt to detect if the given values correspond to a
valid GTF format. If so, then it will return true, and fmt will be
filled in with the found GTF timings.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
