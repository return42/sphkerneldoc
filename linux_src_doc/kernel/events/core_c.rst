.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/events/core.c

.. _`task_function_call`:

task_function_call
==================

.. c:function:: int task_function_call(struct task_struct *p, remote_function_f func, void *info)

    call a function on the cpu on which a task runs

    :param struct task_struct \*p:
        the task to evaluate

    :param remote_function_f func:
        the function to be called

    :param void \*info:
        the function call argument

.. _`task_function_call.description`:

Description
-----------

Calls the function \ ``func``\  when the task is currently running. This might
be on the current CPU, which just calls the function directly

.. _`task_function_call.return`:

Return
------

\ ``func``\  return value, or
-ESRCH  - when the process isn't running
-EAGAIN - when the process moved away

.. _`cpu_function_call`:

cpu_function_call
=================

.. c:function:: int cpu_function_call(int cpu, remote_function_f func, void *info)

    call a function on the cpu

    :param int cpu:
        *undescribed*

    :param remote_function_f func:
        the function to be called

    :param void \*info:
        the function call argument

.. _`cpu_function_call.description`:

Description
-----------

Calls the function \ ``func``\  on the remote cpu.

.. _`cpu_function_call.return`:

Return
------

\ ``func``\  return value or -ENXIO when the cpu is offline

.. _`sys_perf_event_open`:

sys_perf_event_open
===================

.. c:function:: long sys_perf_event_open(struct perf_event_attr __user *attr_uptr, pid_t pid, int cpu, int group_fd, unsigned long flags)

    open a performance event, associate it to a task/cpu

    :param struct perf_event_attr __user \*attr_uptr:
        event_id type attributes for monitoring/sampling

    :param pid_t pid:
        target pid

    :param int cpu:
        target cpu

    :param int group_fd:
        group leader event fd

    :param unsigned long flags:
        *undescribed*

.. _`perf_event_create_kernel_counter`:

perf_event_create_kernel_counter
================================

.. c:function:: struct perf_event *perf_event_create_kernel_counter(struct perf_event_attr *attr, int cpu, struct task_struct *task, perf_overflow_handler_t overflow_handler, void *context)

    :param struct perf_event_attr \*attr:
        attributes of the counter to create

    :param int cpu:
        cpu in which the counter is bound

    :param struct task_struct \*task:
        task to profile (NULL for percpu)

    :param perf_overflow_handler_t overflow_handler:
        *undescribed*

    :param void \*context:
        *undescribed*

.. This file was automatic generated / don't edit.

