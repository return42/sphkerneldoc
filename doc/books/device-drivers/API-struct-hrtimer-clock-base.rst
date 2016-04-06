
.. _API-struct-hrtimer-clock-base:

=========================
struct hrtimer_clock_base
=========================

*man struct hrtimer_clock_base(9)*

*4.6.0-rc1*

the timer base for a specific clock


Synopsis
========

.. code-block:: c

    struct hrtimer_clock_base {
      struct hrtimer_cpu_base * cpu_base;
      int index;
      clockid_t clockid;
      struct timerqueue_head active;
      ktime_t (* get_time) (void);
      ktime_t offset;
    };


Members
=======

cpu_base
    per cpu clock base

index
    clock type index for per_cpu support when moving a timer to a base on another cpu.

clockid
    clock id for per_cpu support

active
    red black tree root node for the active timers

get_time
    function to retrieve the current time of the clock

offset
    offset of this clock to the monotonic base
