
.. _API-v4l2-valid-dv-timings:

=====================
v4l2_valid_dv_timings
=====================

*man v4l2_valid_dv_timings(9)*

*4.6.0-rc1*

are these timings valid?


Synopsis
========

.. c:function:: bool v4l2_valid_dv_timings( const struct v4l2_dv_timings * t, const struct v4l2_dv_timings_cap * cap, v4l2_check_dv_timings_fnc fnc, void * fnc_handle )

Arguments
=========

``t``
    the v4l2_dv_timings struct.

``cap``
    the v4l2_dv_timings_cap capabilities.

``fnc``
    callback to check if this timing is OK. May be NULL.

``fnc_handle``
    a handle that is passed on to ``fnc``.


Description
===========

Returns true if the given dv_timings struct is supported by the hardware capabilities and the callback function (if non-NULL), returns false otherwise.
