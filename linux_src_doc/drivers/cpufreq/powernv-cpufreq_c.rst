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
        int highest_lpstate_idx;
        unsigned int elapsed_time;
        unsigned int last_sampled_time;
        int last_lpstate_idx;
        int last_gpstate_idx;
        spinlock_t gpstate_lock;
        struct timer_list timer;
    }

.. _`global_pstate_info.members`:

Members
-------

highest_lpstate_idx
    The local pstate index from which we are
    ramping down

elapsed_time
    Time in ms spent in ramping down from
    highest_lpstate_idx

last_sampled_time
    Time from boot in ms when global pstates were
    last set
    \ ``last_lpstate_idx``\ ,           Last set value of local pstate and global
    last_gpstate_idx             pstate in terms of cpufreq table index

last_lpstate_idx
    *undescribed*

last_gpstate_idx
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

.. c:function:: int calc_global_pstate(unsigned int elapsed_time, int highest_lpstate_idx, int local_pstate_idx)

    Calculate global pstate

    :param unsigned int elapsed_time:
        Elapsed time in milliseconds

    :param int highest_lpstate_idx:
        pstate from which its ramping down

    :param int local_pstate_idx:
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

