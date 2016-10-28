.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/timer_stats.c

.. _`timer_stats_update_stats`:

timer_stats_update_stats
========================

.. c:function:: void timer_stats_update_stats(void *timer, pid_t pid, void *startf, void *timerf, char *comm, u32 tflags)

    Update the statistics for a timer.

    :param void \*timer:
        pointer to either a timer_list or a hrtimer

    :param pid_t pid:
        the pid of the task which set up the timer

    :param void \*startf:
        pointer to the function which did the timer setup

    :param void \*timerf:
        pointer to the timer callback function of the timer

    :param char \*comm:
        name of the process which set up the timer

    :param u32 tflags:
        The flags field of the timer

.. _`timer_stats_update_stats.description`:

Description
-----------

When the timer is already registered, then the event counter is
incremented. Otherwise the timer is registered in a free slot.

.. This file was automatic generated / don't edit.

