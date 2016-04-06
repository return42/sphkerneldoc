
.. _API-v4l2-print-dv-timings:

=====================
v4l2_print_dv_timings
=====================

*man v4l2_print_dv_timings(9)*

*4.6.0-rc1*

log the contents of a dv_timings struct


Synopsis
========

.. c:function:: void v4l2_print_dv_timings( const char * dev_prefix, const char * prefix, const struct v4l2_dv_timings * t, bool detailed )

Arguments
=========

``dev_prefix``
    device prefix for each log line.

``prefix``
    additional prefix for each log line, may be NULL.

``t``
    the timings data.

``detailed``
    if true, give a detailed log.
