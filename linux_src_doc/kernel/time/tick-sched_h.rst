.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/tick-sched.h

.. _`tick_sched`:

struct tick_sched
=================

.. c:type:: struct tick_sched

    sched tick emulation and no idle tick control/stats

.. _`tick_sched.definition`:

Definition
----------

.. code-block:: c

    struct tick_sched {
        struct hrtimer sched_timer;
        unsigned long check_clocks;
        enum tick_nohz_mode nohz_mode;
        unsigned int inidle : 1;
        unsigned int tick_stopped : 1;
        unsigned int idle_active : 1;
        unsigned int do_timer_last : 1;
        unsigned int got_idle_tick : 1;
        ktime_t last_tick;
        ktime_t next_tick;
        unsigned long idle_jiffies;
        unsigned long idle_calls;
        unsigned long idle_sleeps;
        ktime_t idle_entrytime;
        ktime_t idle_waketime;
        ktime_t idle_exittime;
        ktime_t idle_sleeptime;
        ktime_t iowait_sleeptime;
        unsigned long last_jiffies;
        u64 timer_expires;
        u64 timer_expires_base;
        u64 next_timer;
        ktime_t idle_expires;
        atomic_t tick_dep_mask;
    }

.. _`tick_sched.members`:

Members
-------

sched_timer
    hrtimer to schedule the periodic tick in high
    resolution mode

check_clocks
    *undescribed*

nohz_mode
    *undescribed*

inidle
    *undescribed*

tick_stopped
    Indicator that the idle tick has been stopped

idle_active
    *undescribed*

do_timer_last
    *undescribed*

got_idle_tick
    Tick timer function has run with \ ``inidle``\  set

last_tick
    Store the last tick expiry time when the tick
    timer is modified for nohz sleeps. This is necessary
    to resume the tick timer operation in the timeline
    when the CPU returns from nohz sleep.

next_tick
    Next tick to be fired when in dynticks mode.

idle_jiffies
    jiffies at the entry to idle for idle time accounting

idle_calls
    Total number of idle calls

idle_sleeps
    Number of idle calls, where the sched tick was stopped

idle_entrytime
    Time when the idle call was entered

idle_waketime
    Time when the idle was interrupted

idle_exittime
    Time when the idle state was left

idle_sleeptime
    Sum of the time slept in idle with sched tick stopped

iowait_sleeptime
    Sum of the time slept in idle with sched tick stopped, with IO outstanding

last_jiffies
    *undescribed*

timer_expires
    Anticipated timer expiration time (in case sched tick is stopped)

timer_expires_base
    Base time clock monotonic for \ ``timer_expires``\ 

next_timer
    *undescribed*

idle_expires
    *undescribed*

tick_dep_mask
    *undescribed*

.. This file was automatic generated / don't edit.

