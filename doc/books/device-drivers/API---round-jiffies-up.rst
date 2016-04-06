
.. _API---round-jiffies-up:

==================
__round_jiffies_up
==================

*man __round_jiffies_up(9)*

*4.6.0-rc1*

function to round jiffies up to a full second


Synopsis
========

.. c:function:: unsigned long __round_jiffies_up( unsigned long j, int cpu )

Arguments
=========

``j``
    the time in (absolute) jiffies that should be rounded

``cpu``
    the processor number on which the timeout will happen


Description
===========

This is the same as ``__round_jiffies`` except that it will never round down. This is useful for timeouts for which the exact time of firing does not matter too much, as long as
they don't fire too early.
