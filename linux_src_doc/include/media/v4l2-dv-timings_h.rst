.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-dv-timings.h

.. _`v4l2_calc_timeperframe`:

v4l2_calc_timeperframe
======================

.. c:function:: struct v4l2_fract v4l2_calc_timeperframe(const struct v4l2_dv_timings *t)

    helper function to calculate timeperframe based v4l2_dv_timings fields.

    :param t:
        Timings for the video mode.
    :type t: const struct v4l2_dv_timings \*

.. _`v4l2_calc_timeperframe.description`:

Description
-----------

Calculates the expected timeperframe using the pixel clock value and
horizontal/vertical measures. This means that v4l2_dv_timings structure
must be correctly and fully filled.

.. _`v4l2_check_dv_timings_fnc`:

v4l2_check_dv_timings_fnc
=========================

.. c:function:: bool v4l2_check_dv_timings_fnc(const struct v4l2_dv_timings *t, void *handle)

    timings check callback

    :param t:
        the v4l2_dv_timings struct.
    :type t: const struct v4l2_dv_timings \*

    :param handle:
        a handle from the driver.
    :type handle: void \*

.. _`v4l2_check_dv_timings_fnc.description`:

Description
-----------

Returns true if the given timings are valid.

.. _`v4l2_valid_dv_timings`:

v4l2_valid_dv_timings
=====================

.. c:function:: bool v4l2_valid_dv_timings(const struct v4l2_dv_timings *t, const struct v4l2_dv_timings_cap *cap, v4l2_check_dv_timings_fnc fnc, void *fnc_handle)

    are these timings valid?

    :param t:
        the v4l2_dv_timings struct.
    :type t: const struct v4l2_dv_timings \*

    :param cap:
        the v4l2_dv_timings_cap capabilities.
    :type cap: const struct v4l2_dv_timings_cap \*

    :param fnc:
        callback to check if this timing is OK. May be NULL.
    :type fnc: v4l2_check_dv_timings_fnc

    :param fnc_handle:
        a handle that is passed on to \ ``fnc``\ .
    :type fnc_handle: void \*

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

    :param t:
        the v4l2_enum_dv_timings struct.
    :type t: struct v4l2_enum_dv_timings \*

    :param cap:
        the v4l2_dv_timings_cap capabilities.
    :type cap: const struct v4l2_dv_timings_cap \*

    :param fnc:
        callback to check if this timing is OK. May be NULL.
    :type fnc: v4l2_check_dv_timings_fnc

    :param fnc_handle:
        a handle that is passed on to \ ``fnc``\ .
    :type fnc_handle: void \*

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

    :param t:
        the v4l2_enum_dv_timings struct.
    :type t: struct v4l2_dv_timings \*

    :param cap:
        the v4l2_dv_timings_cap capabilities.
    :type cap: const struct v4l2_dv_timings_cap \*

    :param pclock_delta:
        maximum delta between t->pixelclock and the timing struct
        under consideration.
    :type pclock_delta: unsigned

    :param fnc:
        callback to check if a given timings struct is OK. May be NULL.
    :type fnc: v4l2_check_dv_timings_fnc

    :param fnc_handle:
        a handle that is passed on to \ ``fnc``\ .
    :type fnc_handle: void \*

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

    :param t:
        the timings data.
    :type t: struct v4l2_dv_timings \*

    :param vic:
        CEA-861 VIC code
    :type vic: u8

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

    :param measured:
        the measured timings data.
    :type measured: const struct v4l2_dv_timings \*

    :param standard:
        the timings according to the standard.
    :type standard: const struct v4l2_dv_timings \*

    :param pclock_delta:
        maximum delta in Hz between standard->pixelclock and
        the measured timings.
    :type pclock_delta: unsigned

    :param match_reduced_fps:
        if true, then fail if V4L2_DV_FL_REDUCED_FPS does not
        match.
    :type match_reduced_fps: bool

.. _`v4l2_match_dv_timings.description`:

Description
-----------

Returns true if the two timings match, returns false otherwise.

.. _`v4l2_print_dv_timings`:

v4l2_print_dv_timings
=====================

.. c:function:: void v4l2_print_dv_timings(const char *dev_prefix, const char *prefix, const struct v4l2_dv_timings *t, bool detailed)

    log the contents of a dv_timings struct

    :param dev_prefix:
        device prefix for each log line.
    :type dev_prefix: const char \*

    :param prefix:
        additional prefix for each log line, may be NULL.
    :type prefix: const char \*

    :param t:
        the timings data.
    :type t: const struct v4l2_dv_timings \*

    :param detailed:
        if true, give a detailed log.
    :type detailed: bool

.. _`v4l2_detect_cvt`:

v4l2_detect_cvt
===============

.. c:function:: bool v4l2_detect_cvt(unsigned frame_height, unsigned hfreq, unsigned vsync, unsigned active_width, u32 polarities, bool interlaced, struct v4l2_dv_timings *fmt)

    detect if the given timings follow the CVT standard

    :param frame_height:
        the total height of the frame (including blanking) in lines.
    :type frame_height: unsigned

    :param hfreq:
        the horizontal frequency in Hz.
    :type hfreq: unsigned

    :param vsync:
        the height of the vertical sync in lines.
    :type vsync: unsigned

    :param active_width:
        active width of image (does not include blanking). This
        information is needed only in case of version 2 of reduced blanking.
        In other cases, this parameter does not have any effect on timings.
    :type active_width: unsigned

    :param polarities:
        the horizontal and vertical polarities (same as struct
        v4l2_bt_timings polarities).
    :type polarities: u32

    :param interlaced:
        if this flag is true, it indicates interlaced format
    :type interlaced: bool

    :param fmt:
        the resulting timings.
    :type fmt: struct v4l2_dv_timings \*

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

    :param frame_height:
        the total height of the frame (including blanking) in lines.
    :type frame_height: unsigned

    :param hfreq:
        the horizontal frequency in Hz.
    :type hfreq: unsigned

    :param vsync:
        the height of the vertical sync in lines.
    :type vsync: unsigned

    :param polarities:
        the horizontal and vertical polarities (same as struct
        v4l2_bt_timings polarities).
    :type polarities: u32

    :param interlaced:
        if this flag is true, it indicates interlaced format
    :type interlaced: bool

    :param aspect:
        preferred aspect ratio. GTF has no method of determining the
        aspect ratio in order to derive the image width from the
        image height, so it has to be passed explicitly. Usually
        the native screen aspect ratio is used for this. If it
        is not filled in correctly, then 16:9 will be assumed.
    :type aspect: struct v4l2_fract

    :param fmt:
        the resulting timings.
    :type fmt: struct v4l2_dv_timings \*

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

    :param hor_landscape:
        byte 0x15 from the EDID.
    :type hor_landscape: u8

    :param vert_portrait:
        byte 0x16 from the EDID.
    :type vert_portrait: u8

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

    :param t:
        the timings data.
    :type t: const struct v4l2_dv_timings \*

.. _`can_reduce_fps`:

can_reduce_fps
==============

.. c:function:: bool can_reduce_fps(struct v4l2_bt_timings *bt)

    check if conditions for reduced fps are true.

    :param bt:
        v4l2 timing structure
    :type bt: struct v4l2_bt_timings \*

.. _`can_reduce_fps.description`:

Description
-----------

For different timings reduced fps is allowed if the following conditions

.. _`can_reduce_fps.are-met`:

are met
-------


  - For CVT timings: if reduced blanking v2 (vsync == 8) is true.
  - For CEA861 timings: if \ ``V4L2_DV_FL_CAN_REDUCE_FPS``\  flag is true.

.. _`v4l2_hdmi_colorimetry`:

struct v4l2_hdmi_colorimetry
============================

.. c:type:: struct v4l2_hdmi_colorimetry

    describes the HDMI colorimetry information

.. _`v4l2_hdmi_colorimetry.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_hdmi_colorimetry {
        enum v4l2_colorspace colorspace;
        enum v4l2_ycbcr_encoding ycbcr_enc;
        enum v4l2_quantization quantization;
        enum v4l2_xfer_func xfer_func;
    }

.. _`v4l2_hdmi_colorimetry.members`:

Members
-------

colorspace
    enum v4l2_colorspace, the colorspace

ycbcr_enc
    enum v4l2_ycbcr_encoding, Y'CbCr encoding

quantization
    enum v4l2_quantization, colorspace quantization

xfer_func
    enum v4l2_xfer_func, colorspace transfer function

.. This file was automatic generated / don't edit.

