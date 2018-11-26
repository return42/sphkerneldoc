.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/psi.c

.. _`psi_memstall_enter`:

psi_memstall_enter
==================

.. c:function:: void psi_memstall_enter(unsigned long *flags)

    mark the beginning of a memory stall section

    :param flags:
        flags to handle nested sections
    :type flags: unsigned long \*

.. _`psi_memstall_enter.description`:

Description
-----------

Marks the calling task as being stalled due to a lack of memory,
such as waiting for a refault or performing reclaim.

.. _`psi_memstall_leave`:

psi_memstall_leave
==================

.. c:function:: void psi_memstall_leave(unsigned long *flags)

    mark the end of an memory stall section

    :param flags:
        flags to handle nested memdelay sections
    :type flags: unsigned long \*

.. _`psi_memstall_leave.description`:

Description
-----------

Marks the calling task as no longer stalled due to lack of memory.

.. _`cgroup_move_task`:

cgroup_move_task
================

.. c:function:: void cgroup_move_task(struct task_struct *task, struct css_set *to)

    move task to a different cgroup

    :param task:
        the task
    :type task: struct task_struct \*

    :param to:
        the target css_set
    :type to: struct css_set \*

.. _`cgroup_move_task.description`:

Description
-----------

Move task to a new cgroup and safely migrate its associated stall
state between the different groups.

This function acquires the task's rq lock to lock out concurrent
changes to the task's scheduling state and - in case the task is
running - concurrent changes to its stall state.

.. This file was automatic generated / don't edit.

