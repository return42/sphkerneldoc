.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/process.c

.. _`set_thread_tidr`:

set_thread_tidr
===============

.. c:function:: int set_thread_tidr(struct task_struct *t)

    structure. For now, we only support setting TIDR for 'current' task.

    :param t:
        the task to set the thread ID for
    :type t: struct task_struct \*

.. _`set_thread_tidr.description`:

Description
-----------

Since the TID value is a truncated form of it PID, it is possible
(but unlikely) for 2 threads to have the same TID. In the unlikely event
that 2 threads share the same TID and are waiting, one of the following

.. _`set_thread_tidr.cases-will-happen`:

cases will happen
-----------------


1. The correct thread is running, the wrong thread is not
In this situation, the correct thread is woken and proceeds to pass it's
condition check.

2. Neither threads are running
In this situation, neither thread will be woken. When scheduled, the waiting
threads will execute either a wait, which will return immediately, followed
by a condition check, which will pass for the correct thread and fail
for the wrong thread, or they will execute the condition check immediately.

3. The wrong thread is running, the correct thread is not
The wrong thread will be woken, but will fail it's condition check and
re-execute wait. The correct thread, when scheduled, will execute either
it's condition check (which will pass), or wait, which returns immediately
when called the first time after the thread is scheduled, followed by it's
condition check (which will pass).

4. Both threads are running
Both threads will be woken. The wrong thread will fail it's condition check
and execute another wait, while the correct thread will pass it's condition
check.

.. This file was automatic generated / don't edit.

