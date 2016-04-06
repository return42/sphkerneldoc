
.. _API-v4l2-find-dv-timings-cap:

========================
v4l2_find_dv_timings_cap
========================

*man v4l2_find_dv_timings_cap(9)*

*4.6.0-rc1*

Find the closest timings struct


Synopsis
========

.. c:function:: bool v4l2_find_dv_timings_cap( struct v4l2_dv_timings * t, const struct v4l2_dv_timings_cap * cap, unsigned pclock_delta, v4l2_check_dv_timings_fnc fnc, void * fnc_handle )

Arguments
=========

``t``
    the v4l2_enum_dv_timings struct.

``cap``
    the v4l2_dv_timings_cap capabilities.

``pclock_delta``
    maximum delta between t->pixelclock and the timing struct under consideration.

``fnc``
    callback to check if a given timings struct is OK. May be NULL.

``fnc_handle``
    a handle that is passed on to ``fnc``.


Description
===========

This function tries to map the given timings to an entry in the full list of possible CEA-861 and DMT timings, filtering out any timings that are not supported based on the
hardware capabilities and the callback function (if non-NULL).

On success it will fill in ``t`` with the found timings and it returns true. On failure it will return false.
