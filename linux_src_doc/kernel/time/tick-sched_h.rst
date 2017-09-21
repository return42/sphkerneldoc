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
        ktime_t last_tick;
        ktime_t next_tick;
        int inidle;
        int tick_stopped;
        unsigned long idle_jiffies;
        unsigned long idle_calls;
        unsigned long idle_sleeps;
        int idle_active;
        ktime_t idle_entrytime;
        ktime_t idle_waketime;
        ktime_t idle_exittime;
        ktime_t idle_sleeptime;
        ktime_t iowait_sleeptime;
        ktime_t sleep_length;
        unsigned long last_jiffies;
        u64 next_timer;
        ktime_t idle_expires;
        int do_timer_last;
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

last_tick
    Store the last tick expiry time when the tick
    timer is modified for nohz sleeps. This is necessary
    to resume the tick timer operation in the timeline
    when the CPU returns from nohz sleep.

next_tick
    Next tick to be fired when in dynticks mode.

inidle
    *undescribed*

tick_stopped
    Indicator that the idle tick has been stopped

idle_jiffies
    jiffies at the entry to idle for idle time accounting

idle_calls
    Total number of idle calls

idle_sleeps
    Number of idle calls, where the sched tick was stopped

idle_active
    *undescribed*

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

sleep_length
    Duration of the current idle sleep

last_jiffies
    *undescribed*

next_timer
    *undescribed*

idle_expires
    *undescribed*

do_timer_last
    *undescribed*

tick_dep_mask
    *undescribed*

.. This file was automatic generated / don't edit.

