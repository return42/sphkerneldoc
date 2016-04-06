
.. _API-v4l2-enum-dv-timings-cap:

========================
v4l2_enum_dv_timings_cap
========================

*man v4l2_enum_dv_timings_cap(9)*

*4.6.0-rc1*

Helper function to enumerate possible DV timings based on capabilities


Synopsis
========

.. c:function:: int v4l2_enum_dv_timings_cap( struct v4l2_enum_dv_timings * t, const struct v4l2_dv_timings_cap * cap, v4l2_check_dv_timings_fnc fnc, void * fnc_handle )

Arguments
=========

``t``
    the v4l2_enum_dv_timings struct.

``cap``
    the v4l2_dv_timings_cap capabilities.

``fnc``
    callback to check if this timing is OK. May be NULL.

``fnc_handle``
    a handle that is passed on to ``fnc``.


Description
===========

This enumerates dv_timings using the full list of possible CEA-861 and DMT timings, filtering out any timings that are not supported based on the hardware capabilities and the
callback function (if non-NULL).

If a valid timing for the given index is found, it will fill in ``t`` and return 0, otherwise it returns -EINVAL.
