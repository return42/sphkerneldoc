.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/sched.h

.. _`highest_flag_domain`:

highest_flag_domain
===================

.. c:function:: struct sched_domain *highest_flag_domain(int cpu, int flag)

    Return highest sched_domain containing flag.

    :param int cpu:
        The cpu whose highest level of sched domain is to
        be returned.

    :param int flag:
        The flag to check for the highest sched_domain
        for the given cpu.

.. _`highest_flag_domain.description`:

Description
-----------

Returns the highest sched_domain of a cpu which contains the given flag.

.. _`group_first_cpu`:

group_first_cpu
===============

.. c:function:: unsigned int group_first_cpu(struct sched_group *group)

    Returns the first cpu in the cpumask of a sched_group.

    :param struct sched_group \*group:
        The group whose first cpu is to be returned.

.. _`cpufreq_update_util`:

cpufreq_update_util
===================

.. c:function:: void cpufreq_update_util(struct rq *rq, unsigned int flags)

    Take a note about CPU utilization changes.

    :param struct rq \*rq:
        Runqueue to carry out the update for.

    :param unsigned int flags:
        Update reason flags.

.. _`cpufreq_update_util.description`:

Description
-----------

This function is called by the scheduler on the CPU whose utilization is
being updated.

It can only be called from RCU-sched read-side critical sections.

The way cpufreq is currently arranged requires it to evaluate the CPU
performance state (frequency/voltage) on a regular basis to prevent it from
being stuck in a completely inadequate performance level for too long.
That is not guaranteed to happen if the updates are only triggered from CFS,
though, because they may not be coming in if RT or deadline tasks are active
all the time (or there are RT and DL tasks only).

As a workaround for that issue, this function is called by the RT and DL
sched classes to trigger extra cpufreq updates to prevent it from stalling,
but that really is a band-aid.  Going forward it should be replaced with
solutions targeted more specifically at RT and DL tasks.

.. This file was automatic generated / don't edit.

