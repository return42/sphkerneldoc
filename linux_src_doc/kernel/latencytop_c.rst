.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/latencytop.c

.. _`__account_scheduler_latency`:

\__account_scheduler_latency
============================

.. c:function:: void __sched __account_scheduler_latency(struct task_struct *tsk, int usecs, int inter)

    record an occurred latency \ ``tsk``\  - the task struct of the task hitting the latency \ ``usecs``\  - the duration of the latency in microseconds \ ``inter``\  - 1 if the sleep was interruptible, 0 if uninterruptible

    :param struct task_struct \*tsk:
        *undescribed*

    :param int usecs:
        *undescribed*

    :param int inter:
        *undescribed*

.. _`__account_scheduler_latency.description`:

Description
-----------

This function is the main entry point for recording latency entries
as called by the scheduler.

This function has a few special cases to deal with normal 'non-latency'

.. _`__account_scheduler_latency.sleeps`:

sleeps
------

specifically, interruptible sleep longer than 5 msec is skipped
since this usually is caused by waiting for events via \ :c:func:`select`\  and co.

Negative latencies (caused by time going backwards) are also explicitly
skipped.

.. This file was automatic generated / don't edit.

