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
        struct cpufreq_policy *policy;
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

policy
    *undescribed*

.. _`pstate_idx_revmap_data`:

struct pstate_idx_revmap_data
=============================

.. c:type:: struct pstate_idx_revmap_data

    Entry in the hashmap pstate_revmap indexed by a function of pstate id.

.. _`pstate_idx_revmap_data.definition`:

Definition
----------

.. code-block:: c

    struct pstate_idx_revmap_data {
        u8 pstate_id;
        unsigned int cpufreq_table_idx;
        struct hlist_node hentry;
    }

.. _`pstate_idx_revmap_data.members`:

Members
-------

pstate_id
    pstate id for this entry.

cpufreq_table_idx
    Index into the powernv_freqs
    cpufreq_frequency_table for frequency
    corresponding to pstate_id.

hentry
    hlist_node that hooks this entry into the pstate_revmap
    hashtable

.. _`idx_to_pstate`:

idx_to_pstate
=============

.. c:function:: u8 idx_to_pstate(unsigned int i)

    Returns the pstate id corresponding to the frequency in the cpufreq frequency table powernv_freqs indexed by \ ``i``\ .

    :param unsigned int i:
        *undescribed*

.. _`idx_to_pstate.description`:

Description
-----------

If \ ``i``\  is out of bound, this will return the pstate
corresponding to the nominal frequency.

.. _`pstate_to_idx`:

pstate_to_idx
=============

.. c:function:: unsigned int pstate_to_idx(u8 pstate)

    Returns the index in the cpufreq frequencytable powernv_freqs for the frequency whose corresponding pstate id is \ ``pstate``\ .

    :param u8 pstate:
        *undescribed*

.. _`pstate_to_idx.description`:

Description
-----------

If no frequency corresponding to \ ``pstate``\  is found,
this will return the index of the nominal
frequency.

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

.. c:function:: void gpstate_timer_handler(struct timer_list *t)

    :param struct timer_list \*t:
        *undescribed*

.. _`gpstate_timer_handler.description`:

Description
-----------

This handler brings down the global pstate closer to the local pstate
according quadratic equation. Queues a new timer if it is still not equal
to local pstate

.. This file was automatic generated / don't edit.

