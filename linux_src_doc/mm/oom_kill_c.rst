.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/oom_kill.c

.. _`has_intersects_mems_allowed`:

has_intersects_mems_allowed
===========================

.. c:function:: bool has_intersects_mems_allowed(struct task_struct *start, const nodemask_t *mask)

    check task eligiblity for kill

    :param struct task_struct \*start:
        task struct of which task to consider

    :param const nodemask_t \*mask:
        nodemask passed to page allocator for mempolicy ooms

.. _`has_intersects_mems_allowed.description`:

Description
-----------

Task eligibility is determined by whether or not a candidate task, \ ``tsk``\ ,
shares the same mempolicy nodes as current if it is bound by such a policy
and whether or not it has the same set of allowed cpuset nodes.

.. _`oom_badness`:

oom_badness
===========

.. c:function:: unsigned long oom_badness(struct task_struct *p, struct mem_cgroup *memcg, const nodemask_t *nodemask, unsigned long totalpages)

    heuristic function to determine which candidate task to kill

    :param struct task_struct \*p:
        task struct of which task we should calculate

    :param struct mem_cgroup \*memcg:
        *undescribed*

    :param const nodemask_t \*nodemask:
        *undescribed*

    :param unsigned long totalpages:
        total present RAM allowed for page allocation

.. _`oom_badness.description`:

Description
-----------

The heuristic for determining which task to kill is made to be as simple and
predictable as possible.  The goal is to return the highest value for the
task consuming the most memory to avoid subsequent oom failures.

.. _`dump_tasks`:

dump_tasks
==========

.. c:function:: void dump_tasks(struct mem_cgroup *memcg, const nodemask_t *nodemask)

    dump current memory state of all system tasks

    :param struct mem_cgroup \*memcg:
        current's memory controller, if constrained

    :param const nodemask_t \*nodemask:
        nodemask passed to page allocator for mempolicy ooms

.. _`dump_tasks.description`:

Description
-----------

Dumps the current memory state of all eligible tasks.  Tasks not in the same
memcg, not in the same cpuset, or bound to a disjoint set of mempolicy nodes
are not shown.
State information includes task's pid, uid, tgid, vm size, rss, nr_ptes,
swapents, oom_score_adj value, and name.

.. _`mark_oom_victim`:

mark_oom_victim
===============

.. c:function:: void mark_oom_victim(struct task_struct *tsk)

    mark the given task as OOM victim

    :param struct task_struct \*tsk:
        task to mark

.. _`mark_oom_victim.description`:

Description
-----------

Has to be called with oom_lock held and never after
oom has been disabled already.

tsk->mm has to be non NULL and caller has to guarantee it is stable (either
under task_lock or operate on the current).

.. _`exit_oom_victim`:

exit_oom_victim
===============

.. c:function:: void exit_oom_victim( void)

    note the exit of an OOM victim

    :param  void:
        no arguments

.. _`oom_killer_enable`:

oom_killer_enable
=================

.. c:function:: void oom_killer_enable( void)

    enable OOM killer

    :param  void:
        no arguments

.. _`oom_killer_disable`:

oom_killer_disable
==================

.. c:function:: bool oom_killer_disable(signed long timeout)

    disable OOM killer

    :param signed long timeout:
        maximum timeout to wait for oom victims in jiffies

.. _`oom_killer_disable.description`:

Description
-----------

Forces all page allocations to fail rather than trigger OOM killer.
Will block and wait until all OOM victims are killed or the given
timeout expires.

The function cannot be called when there are runnable user tasks because
the userspace would see unexpected allocation failures as a result. Any
new usage of this function should be consulted with MM people.

Returns true if successful and false if the OOM killer cannot be
disabled.

.. _`out_of_memory`:

out_of_memory
=============

.. c:function:: bool out_of_memory(struct oom_control *oc)

    kill the "best" process when we run out of memory

    :param struct oom_control \*oc:
        pointer to struct oom_control

.. _`out_of_memory.description`:

Description
-----------

If we run out of memory, we have the choice between either
killing a random task (bad), letting the system crash (worse)
OR try to be smart about which process to kill. Note that we
don't have to be perfect here, we just have to be good.

.. This file was automatic generated / don't edit.

