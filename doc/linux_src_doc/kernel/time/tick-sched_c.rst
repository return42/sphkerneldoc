.. -*- coding: utf-8; mode: rst -*-

============
tick-sched.c
============


.. _`tick_nohz_update_jiffies`:

tick_nohz_update_jiffies
========================

.. c:function:: void tick_nohz_update_jiffies (ktime_t now)

    update jiffies when idle was interrupted

    :param ktime_t now:

        *undescribed*



.. _`tick_nohz_update_jiffies.description`:

Description
-----------


Called from interrupt entry when the CPU was idle

In case the sched_tick was stopped on this CPU, we have to check if jiffies
must be updated. Otherwise an interrupt handler could use a stale jiffy
value. We do this unconditionally on any cpu, as we don't know whether the
cpu, which has the update task assigned is in a long sleep.



.. _`get_cpu_idle_time_us`:

get_cpu_idle_time_us
====================

.. c:function:: u64 get_cpu_idle_time_us (int cpu, u64 *last_update_time)

    get the total idle time of a cpu

    :param int cpu:
        CPU number to query

    :param u64 \*last_update_time:
        variable to store update time in. Do not update
        counters if NULL.



.. _`get_cpu_idle_time_us.description`:

Description
-----------

Return the cummulative idle time (since boot) for a given
CPU, in microseconds.

This time is measured via accounting rather than sampling,
and is as accurate as :c:func:`ktime_get` is.

This function returns -1 if NOHZ is not enabled.



.. _`get_cpu_iowait_time_us`:

get_cpu_iowait_time_us
======================

.. c:function:: u64 get_cpu_iowait_time_us (int cpu, u64 *last_update_time)

    get the total iowait time of a cpu

    :param int cpu:
        CPU number to query

    :param u64 \*last_update_time:
        variable to store update time in. Do not update
        counters if NULL.



.. _`get_cpu_iowait_time_us.description`:

Description
-----------

Return the cummulative iowait time (since boot) for a given
CPU, in microseconds.

This time is measured via accounting rather than sampling,
and is as accurate as :c:func:`ktime_get` is.

This function returns -1 if NOHZ is not enabled.



.. _`tick_nohz_idle_enter`:

tick_nohz_idle_enter
====================

.. c:function:: void tick_nohz_idle_enter ( void)

    stop the idle tick from the idle task

    :param void:
        no arguments



.. _`tick_nohz_idle_enter.description`:

Description
-----------


When the next event is more than a tick into the future, stop the idle tick
Called when we start the idle loop.



.. _`tick_nohz_idle_enter.the-arch-is-responsible-of-calling`:

The arch is responsible of calling
----------------------------------


- :c:func:`rcu_idle_enter` after its last use of RCU before the CPU is put

 to sleep.

- :c:func:`rcu_idle_exit` before the first use of RCU after the CPU is woken up.



.. _`tick_nohz_irq_exit`:

tick_nohz_irq_exit
==================

.. c:function:: void tick_nohz_irq_exit ( void)

    update next tick event from interrupt exit

    :param void:
        no arguments



.. _`tick_nohz_irq_exit.description`:

Description
-----------


When an interrupt fires while we are idle and it doesn't cause
a reschedule, it may still add, modify or delete a timer, enqueue
an RCU callback, etc...
So we need to re-calculate and reprogram the next tick event.



.. _`tick_nohz_get_sleep_length`:

tick_nohz_get_sleep_length
==========================

.. c:function:: ktime_t tick_nohz_get_sleep_length ( void)

    return the length of the current sleep

    :param void:
        no arguments



.. _`tick_nohz_get_sleep_length.description`:

Description
-----------


Called from power state control code with interrupts disabled



.. _`tick_nohz_idle_exit`:

tick_nohz_idle_exit
===================

.. c:function:: void tick_nohz_idle_exit ( void)

    restart the idle tick from the idle task

    :param void:
        no arguments



.. _`tick_nohz_idle_exit.description`:

Description
-----------


Restart the idle tick when the CPU is woken up from idle
This also exit the RCU extended quiescent state. The CPU
can use RCU again after this function is called.



.. _`tick_nohz_switch_to_nohz`:

tick_nohz_switch_to_nohz
========================

.. c:function:: void tick_nohz_switch_to_nohz ( void)

    switch to nohz mode

    :param void:
        no arguments



.. _`tick_setup_sched_timer`:

tick_setup_sched_timer
======================

.. c:function:: void tick_setup_sched_timer ( void)

    setup the tick emulation timer

    :param void:
        no arguments



.. _`tick_clock_notify`:

tick_clock_notify
=================

.. c:function:: void tick_clock_notify ( void)

    :param void:
        no arguments



.. _`tick_check_oneshot_change`:

tick_check_oneshot_change
=========================

.. c:function:: int tick_check_oneshot_change (int allow_nohz)

    :param int allow_nohz:

        *undescribed*



.. _`tick_check_oneshot_change.description`:

Description
-----------


Called cyclic from the hrtimer softirq (driven by the timer
softirq) allow_nohz signals, that we can switch into low-res nohz
mode, because high resolution timers are disabled (either compile
or runtime). Called with interrupts disabled.

