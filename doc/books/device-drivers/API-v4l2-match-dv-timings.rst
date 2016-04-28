.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-match-dv-timings:

=====================
v4l2_match_dv_timings
=====================

*man v4l2_match_dv_timings(9)*

*4.6.0-rc5*

do two timings match?


Synopsis
========

.. c:function:: bool v4l2_match_dv_timings( const struct v4l2_dv_timings * measured, const struct v4l2_dv_timings * standard, unsigned pclock_delta, bool match_reduced_fps )

Arguments
=========

``measured``
    the measured timings data.

``standard``
    the timings according to the standard.

``pclock_delta``
    maximum delta in Hz between standard->pixelclock and the measured
    timings.

``match_reduced_fps``
    if true, then fail if V4L2_DV_FL_REDUCED_FPS does not match.


Description
===========

Returns true if the two timings match, returns false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
