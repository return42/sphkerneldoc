
.. _API---hrtimer-get-remaining:

=======================
__hrtimer_get_remaining
=======================

*man __hrtimer_get_remaining(9)*

*4.6.0-rc1*

get remaining time for the timer


Synopsis
========

.. c:function:: ktime_t __hrtimer_get_remaining( const struct hrtimer * timer, bool adjust )

Arguments
=========

``timer``
    the timer to read

``adjust``
    adjust relative timers when CONFIG_TIME_LOW_RES=y
