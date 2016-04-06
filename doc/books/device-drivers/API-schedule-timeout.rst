
.. _API-schedule-timeout:

================
schedule_timeout
================

*man schedule_timeout(9)*

*4.6.0-rc1*

sleep until timeout


Synopsis
========

.. c:function:: signed long __sched schedule_timeout( signed long timeout )

Arguments
=========

``timeout``
    timeout value in jiffies


Description
===========

Make the current task sleep until ``timeout`` jiffies have elapsed. The routine will return immediately unless the current task state has been set (see ``set_current_state``).

You can set the task state as follows -

``TASK_UNINTERRUPTIBLE`` - at least ``timeout`` jiffies are guaranteed to pass before the routine returns. The routine will return 0

``TASK_INTERRUPTIBLE`` - the routine may return early if a signal is delivered to the current task. In this case the remaining time in jiffies will be returned, or 0 if the timer
expired in time

The current task state is guaranteed to be TASK_RUNNING when this routine returns.

Specifying a ``timeout`` value of ``MAX_SCHEDULE_TIMEOUT`` will schedule the CPU away without a bound on the timeout. In this case the return value will be
``MAX_SCHEDULE_TIMEOUT``.

In all cases the return value is guaranteed to be non-negative.
