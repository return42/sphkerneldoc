.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-print-dv-timings:

=====================
v4l2_print_dv_timings
=====================

*man v4l2_print_dv_timings(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
