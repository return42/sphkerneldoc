.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sched.h

.. _`prev_cputime`:

struct prev_cputime
===================

.. c:type:: struct prev_cputime

    snapshot of system and user cputime

.. _`prev_cputime.definition`:

Definition
----------

.. code-block:: c

    struct prev_cputime {
    #ifndef CONFIG_VIRT_CPU_ACCOUNTING_NATIVE
        u64 utime;
        u64 stime;
        raw_spinlock_t lock;
    #endif
    }

.. _`prev_cputime.members`:

Members
-------

utime
    time spent in user mode

stime
    time spent in system mode

lock
    protects the above two fields

.. _`prev_cputime.description`:

Description
-----------

Stores previous user/system time values such that we can guarantee
monotonicity.

.. _`task_cputime`:

struct task_cputime
===================

.. c:type:: struct task_cputime

    collected CPU time counts

.. _`task_cputime.definition`:

Definition
----------

.. code-block:: c

    struct task_cputime {
        u64 utime;
        u64 stime;
        unsigned long long sum_exec_runtime;
    }

.. _`task_cputime.members`:

Members
-------

utime
    time spent in user mode, in nanoseconds

stime
    time spent in kernel mode, in nanoseconds

sum_exec_runtime
    total time spent on the CPU, in nanoseconds

.. _`task_cputime.description`:

Description
-----------

This structure groups together three kinds of CPU time that are tracked for
threads and thread groups.  Most things considering CPU time want to group
these counts together and treat all three of them in parallel.

.. _`util_est`:

struct util_est
===============

.. c:type:: struct util_est

    Estimation utilization of FAIR tasks

.. _`util_est.definition`:

Definition
----------

.. code-block:: c

    struct util_est {
        unsigned int enqueued;
        unsigned int ewma;
    #define UTIL_EST_WEIGHT_SHIFT 2
    }

.. _`util_est.members`:

Members
-------

enqueued
    instantaneous estimated utilization of a task/cpu

ewma
    the Exponential Weighted Moving Average (EWMA)
    utilization of a task

.. _`util_est.description`:

Description
-----------

Support data structure to track an Exponential Weighted Moving Average
(EWMA) of a FAIR task's utilization. New samples are added to the moving
average each time a task completes an activation. Sample's weight is chosen
so that the EWMA will be relatively insensitive to transient changes to the
task's workload.

.. _`util_est.the-enqueued-attribute-has-a-slightly-different-meaning-for-tasks-and-cpus`:

The enqueued attribute has a slightly different meaning for tasks and cpus
--------------------------------------------------------------------------

- task:   the task's util_avg at last task dequeue time
- cfs_rq: the sum of util_est.enqueued for each RUNNABLE task on that CPU
Thus, the util_est.enqueued of a task represents the contribution on the
estimated utilization of the CPU where that task is currently enqueued.

Only for tasks we track a moving average of the past instantaneous
estimated utilization. This allows to absorb sporadic drops in utilization
of an otherwise almost periodic task.

.. _`pid_alive`:

pid_alive
=========

.. c:function:: int pid_alive(const struct task_struct *p)

    check that a task structure is not stale

    :param p:
        Task structure to be checked.
    :type p: const struct task_struct \*

.. _`pid_alive.description`:

Description
-----------

Test if a process is not yet dead (at most zombie state)
If pid_alive fails, then pointers within the task structure
can be stale and must not be dereferenced.

.. _`pid_alive.return`:

Return
------

1 if the process is alive. 0 otherwise.

.. _`is_global_init`:

is_global_init
==============

.. c:function:: int is_global_init(struct task_struct *tsk)

    check if a task structure is init. Since init is free to have sub-threads we need to check tgid.

    :param tsk:
        Task structure to be checked.
    :type tsk: struct task_struct \*

.. _`is_global_init.description`:

Description
-----------

Check if a task structure is the first user space task the kernel created.

.. _`is_global_init.return`:

Return
------

1 if the task structure is init. 0 otherwise.

.. _`task_nice`:

task_nice
=========

.. c:function:: int task_nice(const struct task_struct *p)

    return the nice value of a given task.

    :param p:
        the task in question.
    :type p: const struct task_struct \*

.. _`task_nice.return`:

Return
------

The nice value [ -20 ... 0 ... 19 ].

.. _`is_idle_task`:

is_idle_task
============

.. c:function:: bool is_idle_task(const struct task_struct *p)

    is the specified task an idle task?

    :param p:
        the task in question.
    :type p: const struct task_struct \*

.. _`is_idle_task.return`:

Return
------

1 if \ ``p``\  is an idle task. 0 otherwise.

.. This file was automatic generated / don't edit.

