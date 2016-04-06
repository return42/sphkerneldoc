
.. _API---round-jiffies-relative:

========================
__round_jiffies_relative
========================

*man __round_jiffies_relative(9)*

*4.6.0-rc1*

function to round jiffies to a full second


Synopsis
========

.. c:function:: unsigned long __round_jiffies_relative( unsigned long j, int cpu )

Arguments
=========

``j``
    the time in (relative) jiffies that should be rounded

``cpu``
    the processor number on which the timeout will happen


Description
===========

``__round_jiffies_relative`` rounds a time delta in the future (in jiffies) up or down to (approximately) full seconds. This is useful for timers for which the exact time they fire
does not matter too much, as long as they fire approximately every X seconds.

By rounding these timers to whole seconds, all such timers will fire at the same time, rather than at various times spread out. The goal of this is to have the CPU wake up less,
which saves power.

The exact rounding is skewed for each processor to avoid all processors firing at the exact same time, which could lead to lock contention or spurious cache line bouncing.

The return value is the rounded version of the ``j`` parameter.
