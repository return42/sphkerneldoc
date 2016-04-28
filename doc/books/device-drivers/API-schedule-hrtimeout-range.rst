.. -*- coding: utf-8; mode: rst -*-

.. _API-schedule-hrtimeout-range:

========================
schedule_hrtimeout_range
========================

*man schedule_hrtimeout_range(9)*

*4.6.0-rc5*

sleep until timeout


Synopsis
========

.. c:function:: int __sched schedule_hrtimeout_range( ktime_t * expires, u64 delta, const enum hrtimer_mode mode )

Arguments
=========

``expires``
    timeout value (ktime_t)

``delta``
    slack in expires timeout (ktime_t)

``mode``
    timer mode, HRTIMER_MODE_ABS or HRTIMER_MODE_REL


Description
===========

Make the current task sleep until the given expiry time has elapsed. The
routine will return immediately unless the current task state has been
set (see ``set_current_state``).

The ``delta`` argument gives the kernel the freedom to schedule the
actual wakeup to a time that is both power and performance friendly. The
kernel give the normal best effort behavior for
“``expires``\ +\ ``delta``”, but may decide to fire the timer earlier,
but no earlier than ``expires``.

You can set the task state as follows -

``TASK_UNINTERRUPTIBLE`` - at least ``timeout`` time is guaranteed to
pass before the routine returns.

``TASK_INTERRUPTIBLE`` - the routine may return early if a signal is
delivered to the current task.

The current task state is guaranteed to be TASK_RUNNING when this
routine returns.

Returns 0 when the timer has expired otherwise -EINTR


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
