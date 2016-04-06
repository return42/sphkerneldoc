
.. _API-schedule-hrtimeout:

==================
schedule_hrtimeout
==================

*man schedule_hrtimeout(9)*

*4.6.0-rc1*

sleep until timeout


Synopsis
========

.. c:function:: int __sched schedule_hrtimeout( ktime_t * expires, const enum hrtimer_mode mode )

Arguments
=========

``expires``
    timeout value (ktime_t)

``mode``
    timer mode, HRTIMER_MODE_ABS or HRTIMER_MODE_REL


Description
===========

Make the current task sleep until the given expiry time has elapsed. The routine will return immediately unless the current task state has been set (see ``set_current_state``).

You can set the task state as follows -

``TASK_UNINTERRUPTIBLE`` - at least ``timeout`` time is guaranteed to pass before the routine returns.

``TASK_INTERRUPTIBLE`` - the routine may return early if a signal is delivered to the current task.

The current task state is guaranteed to be TASK_RUNNING when this routine returns.

Returns 0 when the timer has expired otherwise -EINTR
