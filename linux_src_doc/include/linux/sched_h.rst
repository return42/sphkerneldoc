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

.. _`pid_alive`:

pid_alive
=========

.. c:function:: int pid_alive(const struct task_struct *p)

    check that a task structure is not stale

    :param const struct task_struct \*p:
        Task structure to be checked.

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

    :param struct task_struct \*tsk:
        Task structure to be checked.

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

    :param const struct task_struct \*p:
        the task in question.

.. _`task_nice.return`:

Return
------

The nice value [ -20 ... 0 ... 19 ].

.. _`is_idle_task`:

is_idle_task
============

.. c:function:: bool is_idle_task(const struct task_struct *p)

    is the specified task an idle task?

    :param const struct task_struct \*p:
        the task in question.

.. _`is_idle_task.return`:

Return
------

1 if \ ``p``\  is an idle task. 0 otherwise.

.. This file was automatic generated / don't edit.

