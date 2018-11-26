.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/hrtimer.c

.. _`hrtimer_forward`:

hrtimer_forward
===============

.. c:function:: u64 hrtimer_forward(struct hrtimer *timer, ktime_t now, ktime_t interval)

    forward the timer expiry

    :param timer:
        hrtimer to forward
    :type timer: struct hrtimer \*

    :param now:
        forward past this time
    :type now: ktime_t

    :param interval:
        the interval to forward
    :type interval: ktime_t

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

    (re)start an hrtimer

    :param timer:
        the timer to be added
    :type timer: struct hrtimer \*

    :param tim:
        expiry time
    :type tim: ktime_t

    :param delta_ns:
        "slack" range for the timer
    :type delta_ns: u64

    :param mode:
        timer mode: absolute (HRTIMER_MODE_ABS) or
        relative (HRTIMER_MODE_REL), and pinned (HRTIMER_MODE_PINNED);
        softirq based mode is considered for debug purpose only!
    :type mode: const enum hrtimer_mode

.. _`hrtimer_try_to_cancel`:

hrtimer_try_to_cancel
=====================

.. c:function:: int hrtimer_try_to_cancel(struct hrtimer *timer)

    try to deactivate a timer

    :param timer:
        hrtimer to stop
    :type timer: struct hrtimer \*

.. _`hrtimer_try_to_cancel.return`:

Return
------

 0 when the timer was not active
 1 when the timer was active
-1 when the timer is currently executing the callback function and
   cannot be stopped

.. _`hrtimer_cancel`:

hrtimer_cancel
==============

.. c:function:: int hrtimer_cancel(struct hrtimer *timer)

    cancel a timer and wait for the handler to finish.

    :param timer:
        the timer to be cancelled
    :type timer: struct hrtimer \*

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

    :param timer:
        the timer to read
    :type timer: const struct hrtimer \*

    :param adjust:
        adjust relative timers when CONFIG_TIME_LOW_RES=y
    :type adjust: bool

.. _`hrtimer_get_next_event`:

hrtimer_get_next_event
======================

.. c:function:: u64 hrtimer_get_next_event( void)

    get the time until next expiry event

    :param void:
        no arguments
    :type void: 

.. _`hrtimer_get_next_event.description`:

Description
-----------

Returns the next expiry time or KTIME_MAX if no timer is pending.

.. _`hrtimer_next_event_without`:

hrtimer_next_event_without
==========================

.. c:function:: u64 hrtimer_next_event_without(const struct hrtimer *exclude)

    time until next expiry event w/o one timer

    :param exclude:
        timer to exclude
    :type exclude: const struct hrtimer \*

.. _`hrtimer_next_event_without.description`:

Description
-----------

Returns the next expiry time over all timers except for the \ ``exclude``\  one or
KTIME_MAX if none of them is pending.

.. _`hrtimer_init`:

hrtimer_init
============

.. c:function:: void hrtimer_init(struct hrtimer *timer, clockid_t clock_id, enum hrtimer_mode mode)

    initialize a timer to the given clock

    :param timer:
        the timer to be initialized
    :type timer: struct hrtimer \*

    :param clock_id:
        the clock to be used
    :type clock_id: clockid_t

    :param mode:
        The modes which are relevant for intitialization:
        HRTIMER_MODE_ABS, HRTIMER_MODE_REL, HRTIMER_MODE_ABS_SOFT,
        HRTIMER_MODE_REL_SOFT
    :type mode: enum hrtimer_mode

.. _`hrtimer_init.description`:

Description
-----------

             The PINNED variants of the above can be handed in,
             but the PINNED bit is ignored as pinning happens
             when the hrtimer is started

.. _`schedule_hrtimeout_range_clock`:

schedule_hrtimeout_range_clock
==============================

.. c:function:: int __sched schedule_hrtimeout_range_clock(ktime_t *expires, u64 delta, const enum hrtimer_mode mode, clockid_t clock_id)

    sleep until timeout

    :param expires:
        timeout value (ktime_t)
    :type expires: ktime_t \*

    :param delta:
        slack in expires timeout (ktime_t)
    :type delta: u64

    :param mode:
        timer mode
    :type mode: const enum hrtimer_mode

    :param clock_id:
        timer clock to be used
    :type clock_id: clockid_t

.. _`schedule_hrtimeout_range`:

schedule_hrtimeout_range
========================

.. c:function:: int __sched schedule_hrtimeout_range(ktime_t *expires, u64 delta, const enum hrtimer_mode mode)

    sleep until timeout

    :param expires:
        timeout value (ktime_t)
    :type expires: ktime_t \*

    :param delta:
        slack in expires timeout (ktime_t)
    :type delta: u64

    :param mode:
        timer mode
    :type mode: const enum hrtimer_mode

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

    :param expires:
        timeout value (ktime_t)
    :type expires: ktime_t \*

    :param mode:
        timer mode
    :type mode: const enum hrtimer_mode

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

