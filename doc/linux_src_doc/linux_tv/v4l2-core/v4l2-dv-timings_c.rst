.. -*- coding: utf-8; mode: rst -*-

=================
v4l2-dv-timings.c
=================



.. _xref_v4l2_match_dv_timings:

v4l2_match_dv_timings
=====================

.. c:function:: bool v4l2_match_dv_timings (const struct v4l2_dv_timings * t1, const struct v4l2_dv_timings * t2, unsigned pclock_delta, bool match_reduced_fps)

    check if two timings match @t1 - compare this v4l2_dv_timings struct... @t2 - with this struct. @pclock_delta - the allowed pixelclock deviation. @match_reduced_fps - if true, then fail if V4L2_DV_FL_REDUCED_FPS does not match.

    :param const struct v4l2_dv_timings * t1:

        _undescribed_

    :param const struct v4l2_dv_timings * t2:

        _undescribed_

    :param unsigned pclock_delta:

        _undescribed_

    :param bool match_reduced_fps:

        _undescribed_



Description
-----------



Compare t1 with t2 with a given margin of error for the pixelclock.


