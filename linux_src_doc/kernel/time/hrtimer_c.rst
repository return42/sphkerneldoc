.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/hrtimer.c

.. _`hrtimer_forward`:

hrtimer_forward
===============

.. c:function:: u64 hrtimer_forward(struct hrtimer *timer, ktime_t now, ktime_t interval)

    forward the timer expiry

    :param struct hrtimer \*timer:
        hrtimer to forward

    :param ktime_t now:
        forward past this time

    :param ktime_t interval:
        the interval to forward

.. _`hrtimer_forward.description`:

Description
-----------

Forward the timer expiry so it will expire in the future.
Returns the number of overruns.

Can be safely called from the callback function of \ ``timer``\ . If
called from other contexts \ ``timer``\  must neither be enqueued nor
running the callback and the caller needs to take care of
serialization.

.. _`hrtimer_forward.note`:

Note
----

This only updates the timer expiry value and does not requeue
the timer.

.. _`hrtimer_start_range_ns`:

hrtimer_start_range_ns
======================

.. c:function:: void hrtimer_start_range_ns(struct hrtimer *timer, ktime_t tim, u64 delta_ns, const enum hrtimer_mode mode)

    (re)start an hrtimer on the current CPU

    :param struct hrtimer \*timer:
        the timer to be added

    :param ktime_t tim:
        expiry time

    :param u64 delta_ns:
        "slack" range for the timer

    :param const enum hrtimer_mode mode:
        expiry mode: absolute (HRTIMER_MODE_ABS) or
        relative (HRTIMER_MODE_REL)

.. _`hrtimer_try_to_cancel`:

hrtimer_try_to_cancel
=====================

.. c:function:: int hrtimer_try_to_cancel(struct hrtimer *timer)

    try to deactivate a timer

    :param struct hrtimer \*timer:
        hrtimer to stop

.. _`hrtimer_try_to_cancel.return`:

Return
------

 0 when the timer was not active
 1 when the timer was active
-1 when the timer is currently excuting the callback function and
   cannot be stopped

.. _`hrtimer_cancel`:

hrtimer_cancel
==============

.. c:function:: int hrtimer_cancel(struct hrtimer *timer)

    cancel a timer and wait for the handler to finish.

    :param struct hrtimer \*timer:
        the timer to be cancelled

.. _`hrtimer_cancel.return`:

Return
------

 0 when the timer was not active
 1 when the timer was active

.. _`__hrtimer_get_remaining`:

__hrtimer_get_remaining
=======================

.. c:function:: ktime_t __hrtimer_get_remaining(const struct hrtimer *timer, bool adjust)

    get remaining time for the timer

    :param const struct hrtimer \*timer:
        the timer to read

    :param bool adjust:
        adjust relative timers when CONFIG_TIME_LOW_RES=y

.. _`hrtimer_get_next_event`:

hrtimer_get_next_event
======================

.. c:function:: u64 hrtimer_get_next_event( void)

    get the time until next expiry event

    :param  void:
        no arguments

.. _`hrtimer_get_next_event.description`:

Description
-----------

Returns the next expiry time or KTIME_MAX if no timer is pending.

.. _`hrtimer_init`:

hrtimer_init
============

.. c:function:: void hrtimer_init(struct hrtimer *timer, clockid_t clock_id, enum hrtimer_mode mode)

    initialize a timer to the given clock

    :param struct hrtimer \*timer:
        the timer to be initialized

    :param clockid_t clock_id:
        the clock to be used

    :param enum hrtimer_mode mode:
        timer mode abs/rel

.. _`schedule_hrtimeout_range_clock`:

schedule_hrtimeout_range_clock
==============================

.. c:function:: int __sched schedule_hrtimeout_range_clock(ktime_t *expires, u64 delta, const enum hrtimer_mode mode, int clock)

    sleep until timeout

    :param ktime_t \*expires:
        timeout value (ktime_t)

    :param u64 delta:
        slack in expires timeout (ktime_t)

    :param const enum hrtimer_mode mode:
        timer mode, HRTIMER_MODE_ABS or HRTIMER_MODE_REL

    :param int clock:
        timer clock, CLOCK_MONOTONIC or CLOCK_REALTIME

.. _`schedule_hrtimeout_range`:

schedule_hrtimeout_range
========================

.. c:function:: int __sched schedule_hrtimeout_range(ktime_t *expires, u64 delta, const enum hrtimer_mode mode)

    sleep until timeout

    :param ktime_t \*expires:
        timeout value (ktime_t)

    :param u64 delta:
        slack in expires timeout (ktime_t)

    :param const enum hrtimer_mode mode:
        timer mode, HRTIMER_MODE_ABS or HRTIMER_MODE_REL

.. _`schedule_hrtimeout_range.description`:

Description
-----------

Make the current task sleep until the given expiry time has
elapsed. The routine will return immediately unless
the current task state has been set (see \ :c:func:`set_current_state`\ ).

The \ ``delta``\  argument gives the kernel the freedom to schedule the
actual wakeup to a time that is both power and performance friendly.
The kernel give the normal best effort behavior for "@expires+@delta",
but may decide to fire the timer earlier, but no earlier than \ ``expires``\ .

You can set the task state as follows -

\ ``TASK_UNINTERRUPTIBLE``\  - at least \ ``timeout``\  time is guaranteed to
pass before the routine returns unless the current task is explicitly
woken up, (e.g. by \ :c:func:`wake_up_process`\ ).

\ ``TASK_INTERRUPTIBLE``\  - the routine may return early if a signal is
delivered to the current task or the current task is explicitly woken
up.

The current task state is guaranteed to be TASK_RUNNING when this
routine returns.

Returns 0 when the timer has expired. If the task was woken before the
timer expired by a signal (only possible in state TASK_INTERRUPTIBLE) or
by an explicit wakeup, it returns -EINTR.

.. _`schedule_hrtimeout`:

schedule_hrtimeout
==================

.. c:function:: int __sched schedule_hrtimeout(ktime_t *expires, const enum hrtimer_mode mode)

    sleep until timeout

    :param ktime_t \*expires:
        timeout value (ktime_t)

    :param const enum hrtimer_mode mode:
        timer mode, HRTIMER_MODE_ABS or HRTIMER_MODE_REL

.. _`schedule_hrtimeout.description`:

Description
-----------

Make the current task sleep until the given expiry time has
elapsed. The routine will return immediately unless
the current task state has been set (see \ :c:func:`set_current_state`\ ).

You can set the task state as follows -

\ ``TASK_UNINTERRUPTIBLE``\  - at least \ ``timeout``\  time is guaranteed to
pass before the routine returns unless the current task is explicitly
woken up, (e.g. by \ :c:func:`wake_up_process`\ ).

\ ``TASK_INTERRUPTIBLE``\  - the routine may return early if a signal is
delivered to the current task or the current task is explicitly woken
up.

The current task state is guaranteed to be TASK_RUNNING when this
routine returns.

Returns 0 when the timer has expired. If the task was woken before the
timer expired by a signal (only possible in state TASK_INTERRUPTIBLE) or
by an explicit wakeup, it returns -EINTR.

.. This file was automatic generated / don't edit.

