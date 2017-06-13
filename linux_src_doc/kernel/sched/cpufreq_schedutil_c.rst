.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/cpufreq_schedutil.c

.. _`get_next_freq`:

get_next_freq
=============

.. c:function:: unsigned int get_next_freq(struct sugov_policy *sg_policy, unsigned long util, unsigned long max)

    Compute a new frequency for a given cpufreq policy.

    :param struct sugov_policy \*sg_policy:
        schedutil policy object to compute the new frequency for.

    :param unsigned long util:
        Current CPU utilization.

    :param unsigned long max:
        CPU capacity.

.. _`get_next_freq.description`:

Description
-----------

If the utilization is frequency-invariant, choose the new frequency to be
proportional to it, that is

next_freq = C \* max_freq \* util / max

Otherwise, approximate the would-be frequency-invariant utilization by
util_raw \* (curr_freq / max_freq) which leads to

next_freq = C \* curr_freq \* util_raw / max

Take C = 1.25 for the frequency tipping point at (util / max) = 0.8.

The lowest driver-supported frequency which is equal or greater than the raw
next_freq (as calculated above) is returned, subject to policy min/max and
cpufreq driver limitations.

.. This file was automatic generated / don't edit.

