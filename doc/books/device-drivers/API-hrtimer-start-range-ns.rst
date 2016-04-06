
.. _API-hrtimer-start-range-ns:

======================
hrtimer_start_range_ns
======================

*man hrtimer_start_range_ns(9)*

*4.6.0-rc1*

(re)start an hrtimer on the current CPU


Synopsis
========

.. c:function:: void hrtimer_start_range_ns( struct hrtimer * timer, ktime_t tim, u64 delta_ns, const enum hrtimer_mode mode )

Arguments
=========

``timer``
    the timer to be added

``tim``
    expiry time

``delta_ns``
    "slack" range for the timer

``mode``
    expiry mode: absolute (HRTIMER_MODE_ABS) or relative (HRTIMER_MODE_REL)
