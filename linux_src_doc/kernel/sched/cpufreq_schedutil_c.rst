.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/cpufreq_schedutil.c

.. _`get_next_freq`:

get_next_freq
=============

.. c:function:: unsigned int get_next_freq(struct sugov_policy *sg_policy, unsigned long util, unsigned long max)

    Compute a new frequency for a given cpufreq policy.

    :param sg_policy:
        schedutil policy object to compute the new frequency for.
    :type sg_policy: struct sugov_policy \*

    :param util:
        Current CPU utilization.
    :type util: unsigned long

    :param max:
        CPU capacity.
    :type max: unsigned long

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

.. _`sugov_iowait_reset`:

sugov_iowait_reset
==================

.. c:function:: bool sugov_iowait_reset(struct sugov_cpu *sg_cpu, u64 time, bool set_iowait_boost)

    Reset the IO boost status of a CPU.

    :param sg_cpu:
        the sugov data for the CPU to boost
    :type sg_cpu: struct sugov_cpu \*

    :param time:
        the update time from the caller
    :type time: u64

    :param set_iowait_boost:
        true if an IO boost has been requested
    :type set_iowait_boost: bool

.. _`sugov_iowait_reset.description`:

Description
-----------

The IO wait boost of a task is disabled after a tick since the last update
of a CPU. If a new IO wait boost is requested after more then a tick, then
we enable the boost starting from the minimum frequency, which improves
energy efficiency by ignoring sporadic wakeups from IO.

.. _`sugov_iowait_boost`:

sugov_iowait_boost
==================

.. c:function:: void sugov_iowait_boost(struct sugov_cpu *sg_cpu, u64 time, unsigned int flags)

    Updates the IO boost status of a CPU.

    :param sg_cpu:
        the sugov data for the CPU to boost
    :type sg_cpu: struct sugov_cpu \*

    :param time:
        the update time from the caller
    :type time: u64

    :param flags:
        SCHED_CPUFREQ_IOWAIT if the task is waking up after an IO wait
    :type flags: unsigned int

.. _`sugov_iowait_boost.description`:

Description
-----------

Each time a task wakes up after an IO operation, the CPU utilization can be
boosted to a certain utilization which doubles at each "frequent and
successive" wakeup from IO, ranging from the utilization of the minimum
OPP to the utilization of the maximum OPP.
To keep doubling, an IO boost has to be requested at least once per tick,
otherwise we restart from the utilization of the minimum OPP.

.. _`sugov_iowait_apply`:

sugov_iowait_apply
==================

.. c:function:: void sugov_iowait_apply(struct sugov_cpu *sg_cpu, u64 time, unsigned long *util, unsigned long *max)

    Apply the IO boost to a CPU.

    :param sg_cpu:
        the sugov data for the cpu to boost
    :type sg_cpu: struct sugov_cpu \*

    :param time:
        the update time from the caller
    :type time: u64

    :param util:
        the utilization to (eventually) boost
    :type util: unsigned long \*

    :param max:
        the maximum value the utilization can be boosted to
    :type max: unsigned long \*

.. _`sugov_iowait_apply.description`:

Description
-----------

A CPU running a task which woken up after an IO operation can have its
utilization boosted to speed up the completion of those IO operations.
The IO boost value is increased each time a task wakes up from IO, in
\ :c:func:`sugov_iowait_apply`\ , and it's instead decreased by this function,
each time an increase has not been requested (!iowait_boost_pending).

A CPU which also appears to have been idle for at least one tick has also
its IO boost utilization reset.

This mechanism is designed to boost high frequently IO waiting tasks, while
being more conservative on tasks which does sporadic IO operations.

.. This file was automatic generated / don't edit.

