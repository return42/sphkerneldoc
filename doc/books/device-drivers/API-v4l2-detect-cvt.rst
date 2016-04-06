
.. _API-v4l2-detect-cvt:

===============
v4l2_detect_cvt
===============

*man v4l2_detect_cvt(9)*

*4.6.0-rc1*

detect if the given timings follow the CVT standard


Synopsis
========

.. c:function:: bool v4l2_detect_cvt( unsigned frame_height, unsigned hfreq, unsigned vsync, unsigned active_width, u32 polarities, bool interlaced, struct v4l2_dv_timings * fmt )

Arguments
=========

``frame_height``
    the total height of the frame (including blanking) in lines.

``hfreq``
    the horizontal frequency in Hz.

``vsync``
    the height of the vertical sync in lines.

``active_width``
    active width of image (does not include blanking). This information is needed only in case of version 2 of reduced blanking. In other cases, this parameter does not have any
    effect on timings.

``polarities``
    the horizontal and vertical polarities (same as struct v4l2_bt_timings polarities).

``interlaced``
    if this flag is true, it indicates interlaced format

``fmt``
    the resulting timings.


Description
===========

This function will attempt to detect if the given values correspond to a valid CVT format. If so, then it will return true, and fmt will be filled in with the found CVT timings.
