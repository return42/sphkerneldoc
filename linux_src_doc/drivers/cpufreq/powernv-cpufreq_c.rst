.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/powernv-cpufreq.c

.. _`global_pstate_info`:

struct global_pstate_info
=========================

.. c:type:: struct global_pstate_info

    Per policy data structure to maintain history of global pstates

.. _`global_pstate_info.definition`:

Definition
----------

.. code-block:: c

    struct global_pstate_info {
        int highest_lpstate;
        unsigned int elapsed_time;
        unsigned int last_sampled_time;
        int last_lpstate;
        int last_gpstate;
        spinlock_t gpstate_lock;
        struct timer_list timer;
    }

.. _`global_pstate_info.members`:

Members
-------

highest_lpstate
    The local pstate from which we are ramping down

elapsed_time
    Time in ms spent in ramping down from
    highest_lpstate

last_sampled_time
    Time from boot in ms when global pstates were
    last set

last_lpstate
    Last set values for local and global pstates

last_gpstate
    *undescribed*

gpstate_lock
    A spinlock to maintain synchronization between
    routines called by the timer handler and
    governer's target_index calls

timer
    Is used for ramping down if cpu goes idle for
    a long time with global pstate held high

.. _`calc_global_pstate`:

calc_global_pstate
==================

.. c:function:: int calc_global_pstate(unsigned int elapsed_time, int highest_lpstate, int local_pstate)

    Calculate global pstate

    :param unsigned int elapsed_time:
        Elapsed time in milliseconds

    :param int highest_lpstate:
        pstate from which its ramping down

    :param int local_pstate:
        New local pstate

.. _`calc_global_pstate.description`:

Description
-----------

Finds the appropriate global pstate based on the pstate from which its
ramping down and the time elapsed in ramping down. It follows a quadratic
equation which ensures that it reaches ramping down to pmin in 5sec.

.. _`gpstate_timer_handler`:

gpstate_timer_handler
=====================

.. c:function:: void gpstate_timer_handler(unsigned long data)

    :param unsigned long data:
        pointer to cpufreq_policy on which timer was queued

.. _`gpstate_timer_handler.description`:

Description
-----------

This handler brings down the global pstate closer to the local pstate
according quadratic equation. Queues a new timer if it is still not equal
to local pstate

.. This file was automatic generated / don't edit.

