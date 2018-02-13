.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-dv-timings.h

.. _`v4l2_check_dv_timings_fnc`:

v4l2_check_dv_timings_fnc
=========================

.. c:function:: bool v4l2_check_dv_timings_fnc(const struct v4l2_dv_timings *t, void *handle)

    timings check callback

    :param const struct v4l2_dv_timings \*t:
        the v4l2_dv_timings struct.

    :param void \*handle:
        a handle from the driver.

.. _`v4l2_check_dv_timings_fnc.description`:

Description
-----------

Returns true if the given timings are valid.

.. _`v4l2_valid_dv_timings`:

v4l2_valid_dv_timings
=====================

.. c:function:: bool v4l2_valid_dv_timings(const struct v4l2_dv_timings *t, const struct v4l2_dv_timings_cap *cap, v4l2_check_dv_timings_fnc fnc, void *fnc_handle)

    are these timings valid?

    :param const struct v4l2_dv_timings \*t:
        the v4l2_dv_timings struct.

    :param const struct v4l2_dv_timings_cap \*cap:
        the v4l2_dv_timings_cap capabilities.

    :param v4l2_check_dv_timings_fnc fnc:
        callback to check if this timing is OK. May be NULL.

    :param void \*fnc_handle:
        a handle that is passed on to \ ``fnc``\ .

.. _`v4l2_valid_dv_timings.description`:

Description
-----------

Returns true if the given dv_timings struct is supported by the
hardware capabilities and the callback function (if non-NULL), returns
false otherwise.

.. _`v4l2_enum_dv_timings_cap`:

v4l2_enum_dv_timings_cap
========================

.. c:function:: int v4l2_enum_dv_timings_cap(struct v4l2_enum_dv_timings *t, const struct v4l2_dv_timings_cap *cap, v4l2_check_dv_timings_fnc fnc, void *fnc_handle)

    Helper function to enumerate possible DV timings based on capabilities

    :param struct v4l2_enum_dv_timings \*t:
        the v4l2_enum_dv_timings struct.

    :param const struct v4l2_dv_timings_cap \*cap:
        the v4l2_dv_timings_cap capabilities.

    :param v4l2_check_dv_timings_fnc fnc:
        callback to check if this timing is OK. May be NULL.

    :param void \*fnc_handle:
        a handle that is passed on to \ ``fnc``\ .

.. _`v4l2_enum_dv_timings_cap.description`:

Description
-----------

This enumerates dv_timings using the full list of possible CEA-861 and DMT
timings, filtering out any timings that are not supported based on the
hardware capabilities and the callback function (if non-NULL).

If a valid timing for the given index is found, it will fill in \ ``t``\  and
return 0, otherwise it returns -EINVAL.

.. _`v4l2_find_dv_timings_cap`:

v4l2_find_dv_timings_cap
========================

.. c:function:: bool v4l2_find_dv_timings_cap(struct v4l2_dv_timings *t, const struct v4l2_dv_timings_cap *cap, unsigned pclock_delta, v4l2_check_dv_timings_fnc fnc, void *fnc_handle)

    Find the closest timings struct

    :param struct v4l2_dv_timings \*t:
        the v4l2_enum_dv_timings struct.

    :param const struct v4l2_dv_timings_cap \*cap:
        the v4l2_dv_timings_cap capabilities.

    :param unsigned pclock_delta:
        maximum delta between t->pixelclock and the timing struct
        under consideration.

    :param v4l2_check_dv_timings_fnc fnc:
        callback to check if a given timings struct is OK. May be NULL.

    :param void \*fnc_handle:
        a handle that is passed on to \ ``fnc``\ .

.. _`v4l2_find_dv_timings_cap.description`:

Description
-----------

This function tries to map the given timings to an entry in the
full list of possible CEA-861 and DMT timings, filtering out any timings
that are not supported based on the hardware capabilities and the callback
function (if non-NULL).

On success it will fill in \ ``t``\  with the found timings and it returns true.
On failure it will return false.

.. _`v4l2_find_dv_timings_cea861_vic`:

v4l2_find_dv_timings_cea861_vic
===============================

.. c:function:: bool v4l2_find_dv_timings_cea861_vic(struct v4l2_dv_timings *t, u8 vic)

    find timings based on CEA-861 VIC

    :param struct v4l2_dv_timings \*t:
        the timings data.

    :param u8 vic:
        CEA-861 VIC code

.. _`v4l2_find_dv_timings_cea861_vic.description`:

Description
-----------

On success it will fill in \ ``t``\  with the found timings and it returns true.
On failure it will return false.

.. _`v4l2_match_dv_timings`:

v4l2_match_dv_timings
=====================

.. c:function:: bool v4l2_match_dv_timings(const struct v4l2_dv_timings *measured, const struct v4l2_dv_timings *standard, unsigned pclock_delta, bool match_reduced_fps)

    do two timings match?

    :param const struct v4l2_dv_timings \*measured:
        the measured timings data.

    :param const struct v4l2_dv_timings \*standard:
        the timings according to the standard.

    :param unsigned pclock_delta:
        maximum delta in Hz between standard->pixelclock and
        the measured timings.

    :param bool match_reduced_fps:
        if true, then fail if V4L2_DV_FL_REDUCED_FPS does not
        match.

.. _`v4l2_match_dv_timings.description`:

Description
-----------

Returns true if the two timings match, returns false otherwise.

.. _`v4l2_print_dv_timings`:

v4l2_print_dv_timings
=====================

.. c:function:: void v4l2_print_dv_timings(const char *dev_prefix, const char *prefix, const struct v4l2_dv_timings *t, bool detailed)

    log the contents of a dv_timings struct

    :param const char \*dev_prefix:
        device prefix for each log line.

    :param const char \*prefix:
        additional prefix for each log line, may be NULL.

    :param const struct v4l2_dv_timings \*t:
        the timings data.

    :param bool detailed:
        if true, give a detailed log.

.. _`v4l2_detect_cvt`:

v4l2_detect_cvt
===============

.. c:function:: bool v4l2_detect_cvt(unsigned frame_height, unsigned hfreq, unsigned vsync, unsigned active_width, u32 polarities, bool interlaced, struct v4l2_dv_timings *fmt)

    detect if the given timings follow the CVT standard

    :param unsigned frame_height:
        the total height of the frame (including blanking) in lines.

    :param unsigned hfreq:
        the horizontal frequency in Hz.

    :param unsigned vsync:
        the height of the vertical sync in lines.

    :param unsigned active_width:
        active width of image (does not include blanking). This
        information is needed only in case of version 2 of reduced blanking.
        In other cases, this parameter does not have any effect on timings.

    :param u32 polarities:
        the horizontal and vertical polarities (same as struct
        v4l2_bt_timings polarities).

    :param bool interlaced:
        if this flag is true, it indicates interlaced format

    :param struct v4l2_dv_timings \*fmt:
        the resulting timings.

.. _`v4l2_detect_cvt.description`:

Description
-----------

This function will attempt to detect if the given values correspond to a
valid CVT format. If so, then it will return true, and fmt will be filled
in with the found CVT timings.

.. _`v4l2_detect_gtf`:

v4l2_detect_gtf
===============

.. c:function:: bool v4l2_detect_gtf(unsigned frame_height, unsigned hfreq, unsigned vsync, u32 polarities, bool interlaced, struct v4l2_fract aspect, struct v4l2_dv_timings *fmt)

    detect if the given timings follow the GTF standard

    :param unsigned frame_height:
        the total height of the frame (including blanking) in lines.

    :param unsigned hfreq:
        the horizontal frequency in Hz.

    :param unsigned vsync:
        the height of the vertical sync in lines.

    :param u32 polarities:
        the horizontal and vertical polarities (same as struct
        v4l2_bt_timings polarities).

    :param bool interlaced:
        if this flag is true, it indicates interlaced format

    :param struct v4l2_fract aspect:
        preferred aspect ratio. GTF has no method of determining the
        aspect ratio in order to derive the image width from the
        image height, so it has to be passed explicitly. Usually
        the native screen aspect ratio is used for this. If it
        is not filled in correctly, then 16:9 will be assumed.

    :param struct v4l2_dv_timings \*fmt:
        the resulting timings.

.. _`v4l2_detect_gtf.description`:

Description
-----------

This function will attempt to detect if the given values correspond to a
valid GTF format. If so, then it will return true, and fmt will be filled
in with the found GTF timings.

.. _`v4l2_calc_aspect_ratio`:

v4l2_calc_aspect_ratio
======================

.. c:function:: struct v4l2_fract v4l2_calc_aspect_ratio(u8 hor_landscape, u8 vert_portrait)

    calculate the aspect ratio based on bytes 0x15 and 0x16 from the EDID.

    :param u8 hor_landscape:
        byte 0x15 from the EDID.

    :param u8 vert_portrait:
        byte 0x16 from the EDID.

.. _`v4l2_calc_aspect_ratio.description`:

Description
-----------

Determines the aspect ratio from the EDID.
See VESA Enhanced EDID standard, release A, rev 2, section 3.6.2:
"Horizontal and Vertical Screen Size or Aspect Ratio"

.. _`v4l2_dv_timings_aspect_ratio`:

v4l2_dv_timings_aspect_ratio
============================

.. c:function:: struct v4l2_fract v4l2_dv_timings_aspect_ratio(const struct v4l2_dv_timings *t)

    calculate the aspect ratio based on the v4l2_dv_timings information.

    :param const struct v4l2_dv_timings \*t:
        the timings data.

.. _`can_reduce_fps`:

can_reduce_fps
==============

.. c:function:: bool can_reduce_fps(struct v4l2_bt_timings *bt)

    check if conditions for reduced fps are true.

    :param struct v4l2_bt_timings \*bt:
        v4l2 timing structure

.. _`can_reduce_fps.description`:

Description
-----------

For different timings reduced fps is allowed if the following conditions

.. _`can_reduce_fps.are-met`:

are met
-------


  - For CVT timings: if reduced blanking v2 (vsync == 8) is true.
  - For CEA861 timings: if \ ``V4L2_DV_FL_CAN_REDUCE_FPS``\  flag is true.

.. This file was automatic generated / don't edit.

