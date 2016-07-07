.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/stats.h

.. _`cputimer_running`:

cputimer_running
================

.. c:function:: bool cputimer_running(struct task_struct *tsk)

    return true if cputimer is running

    :param struct task_struct \*tsk:
        Pointer to target task.

.. _`account_group_user_time`:

account_group_user_time
=======================

.. c:function:: void account_group_user_time(struct task_struct *tsk, cputime_t cputime)

    Maintain utime for a thread group.

    :param struct task_struct \*tsk:
        Pointer to task structure.

    :param cputime_t cputime:
        Time value by which to increment the utime field of the
        thread_group_cputime structure.

.. _`account_group_user_time.description`:

Description
-----------

If thread group time is being maintained, get the structure for the
running CPU and update the utime field there.

.. _`account_group_system_time`:

account_group_system_time
=========================

.. c:function:: void account_group_system_time(struct task_struct *tsk, cputime_t cputime)

    Maintain stime for a thread group.

    :param struct task_struct \*tsk:
        Pointer to task structure.

    :param cputime_t cputime:
        Time value by which to increment the stime field of the
        thread_group_cputime structure.

.. _`account_group_system_time.description`:

Description
-----------

If thread group time is being maintained, get the structure for the
running CPU and update the stime field there.

.. _`account_group_exec_runtime`:

account_group_exec_runtime
==========================

.. c:function:: void account_group_exec_runtime(struct task_struct *tsk, unsigned long long ns)

    Maintain exec runtime for a thread group.

    :param struct task_struct \*tsk:
        Pointer to task structure.

    :param unsigned long long ns:
        Time value by which to increment the sum_exec_runtime field
        of the thread_group_cputime structure.

.. _`account_group_exec_runtime.description`:

Description
-----------

If thread group time is being maintained, get the structure for the
running CPU and update the sum_exec_runtime field there.

.. This file was automatic generated / don't edit.

