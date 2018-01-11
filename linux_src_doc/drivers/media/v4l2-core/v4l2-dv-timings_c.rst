.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/v4l2-dv-timings.c

.. _`v4l2_match_dv_timings`:

v4l2_match_dv_timings
=====================

.. c:function:: bool v4l2_match_dv_timings(const struct v4l2_dv_timings *t1, const struct v4l2_dv_timings *t2, unsigned pclock_delta, bool match_reduced_fps)

    check if two timings match

    :param const struct v4l2_dv_timings \*t1:
        compare this v4l2_dv_timings struct...

    :param const struct v4l2_dv_timings \*t2:
        with this struct.

    :param unsigned pclock_delta:
        the allowed pixelclock deviation.

    :param bool match_reduced_fps:
        if true, then fail if V4L2_DV_FL_REDUCED_FPS does not
        match.

.. _`v4l2_match_dv_timings.description`:

Description
-----------

Compare t1 with t2 with a given margin of error for the pixelclock.

.. This file was automatic generated / don't edit.

