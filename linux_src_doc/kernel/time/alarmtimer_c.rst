.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/alarmtimer.c

.. _`alarmtimer_get_rtcdev`:

alarmtimer_get_rtcdev
=====================

.. c:function:: struct rtc_device *alarmtimer_get_rtcdev( void)

    Return selected rtcdevice

    :param void:
        no arguments
    :type void: 

.. _`alarmtimer_get_rtcdev.description`:

Description
-----------

This function returns the rtc device to use for wakealarms.
If one has not already been chosen, it checks to see if a
functional rtc device is available.

.. _`alarmtimer_enqueue`:

alarmtimer_enqueue
==================

.. c:function:: void alarmtimer_enqueue(struct alarm_base *base, struct alarm *alarm)

    Adds an alarm timer to an alarm_base timerqueue

    :param base:
        pointer to the base where the timer is being run
    :type base: struct alarm_base \*

    :param alarm:
        pointer to alarm being enqueued.
    :type alarm: struct alarm \*

.. _`alarmtimer_enqueue.description`:

Description
-----------

Adds alarm to a alarm_base timerqueue

Must hold base->lock when calling.

.. _`alarmtimer_dequeue`:

alarmtimer_dequeue
==================

.. c:function:: void alarmtimer_dequeue(struct alarm_base *base, struct alarm *alarm)

    Removes an alarm timer from an alarm_base timerqueue

    :param base:
        pointer to the base where the timer is running
    :type base: struct alarm_base \*

    :param alarm:
        pointer to alarm being removed
    :type alarm: struct alarm \*

.. _`alarmtimer_dequeue.description`:

Description
-----------

Removes alarm to a alarm_base timerqueue

Must hold base->lock when calling.

.. _`alarmtimer_fired`:

alarmtimer_fired
================

.. c:function:: enum hrtimer_restart alarmtimer_fired(struct hrtimer *timer)

    Handles alarm hrtimer being fired.

    :param timer:
        pointer to hrtimer being run
    :type timer: struct hrtimer \*

.. _`alarmtimer_fired.description`:

Description
-----------

When a alarm timer fires, this runs through the timerqueue to
see which alarms expired, and runs those. If there are more alarm
timers queued for the future, we set the hrtimer to fire when
when the next future alarm timer expires.

.. _`alarmtimer_suspend`:

alarmtimer_suspend
==================

.. c:function:: int alarmtimer_suspend(struct device *dev)

    Suspend time callback

    :param dev:
        unused
    :type dev: struct device \*

.. _`alarmtimer_suspend.description`:

Description
-----------

When we are going into suspend, we look through the bases
to see which is the soonest timer to expire. We then
set an rtc timer to fire that far into the future, which
will wake us from suspend.

.. _`alarm_init`:

alarm_init
==========

.. c:function:: void alarm_init(struct alarm *alarm, enum alarmtimer_type type, enum alarmtimer_restart (*function)(struct alarm *, ktime_t))

    Initialize an alarm structure

    :param alarm:
        ptr to alarm to be initialized
    :type alarm: struct alarm \*

    :param type:
        the type of the alarm
    :type type: enum alarmtimer_type

    :param enum alarmtimer_restart (\*function)(struct alarm \*, ktime_t):
        callback that is run when the alarm fires

.. _`alarm_start`:

alarm_start
===========

.. c:function:: void alarm_start(struct alarm *alarm, ktime_t start)

    Sets an absolute alarm to fire

    :param alarm:
        ptr to alarm to set
    :type alarm: struct alarm \*

    :param start:
        time to run the alarm
    :type start: ktime_t

.. _`alarm_start_relative`:

alarm_start_relative
====================

.. c:function:: void alarm_start_relative(struct alarm *alarm, ktime_t start)

    Sets a relative alarm to fire

    :param alarm:
        ptr to alarm to set
    :type alarm: struct alarm \*

    :param start:
        time relative to now to run the alarm
    :type start: ktime_t

.. _`alarm_try_to_cancel`:

alarm_try_to_cancel
===================

.. c:function:: int alarm_try_to_cancel(struct alarm *alarm)

    Tries to cancel an alarm timer

    :param alarm:
        ptr to alarm to be canceled
    :type alarm: struct alarm \*

.. _`alarm_try_to_cancel.description`:

Description
-----------

Returns 1 if the timer was canceled, 0 if it was not running,
and -1 if the callback was running

.. _`alarm_cancel`:

alarm_cancel
============

.. c:function:: int alarm_cancel(struct alarm *alarm)

    Spins trying to cancel an alarm timer until it is done

    :param alarm:
        ptr to alarm to be canceled
    :type alarm: struct alarm \*

.. _`alarm_cancel.description`:

Description
-----------

Returns 1 if the timer was canceled, 0 if it was not active.

.. _`clock2alarm`:

clock2alarm
===========

.. c:function:: enum alarmtimer_type clock2alarm(clockid_t clockid)

    helper that converts from clockid to alarmtypes

    :param clockid:
        clockid.
    :type clockid: clockid_t

.. _`alarm_handle_timer`:

alarm_handle_timer
==================

.. c:function:: enum alarmtimer_restart alarm_handle_timer(struct alarm *alarm, ktime_t now)

    Callback for posix timers

    :param alarm:
        alarm that fired
    :type alarm: struct alarm \*

    :param now:
        *undescribed*
    :type now: ktime_t

.. _`alarm_handle_timer.description`:

Description
-----------

Posix timer callback for expired alarm timers.

.. _`alarm_timer_rearm`:

alarm_timer_rearm
=================

.. c:function:: void alarm_timer_rearm(struct k_itimer *timr)

    Posix timer callback for rearming timer

    :param timr:
        Pointer to the posixtimer data struct
    :type timr: struct k_itimer \*

.. _`alarm_timer_forward`:

alarm_timer_forward
===================

.. c:function:: s64 alarm_timer_forward(struct k_itimer *timr, ktime_t now)

    Posix timer callback for forwarding timer

    :param timr:
        Pointer to the posixtimer data struct
    :type timr: struct k_itimer \*

    :param now:
        Current time to forward the timer against
    :type now: ktime_t

.. _`alarm_timer_remaining`:

alarm_timer_remaining
=====================

.. c:function:: ktime_t alarm_timer_remaining(struct k_itimer *timr, ktime_t now)

    Posix timer callback to retrieve remaining time

    :param timr:
        Pointer to the posixtimer data struct
    :type timr: struct k_itimer \*

    :param now:
        Current time to calculate against
    :type now: ktime_t

.. _`alarm_timer_try_to_cancel`:

alarm_timer_try_to_cancel
=========================

.. c:function:: int alarm_timer_try_to_cancel(struct k_itimer *timr)

    Posix timer callback to cancel a timer

    :param timr:
        Pointer to the posixtimer data struct
    :type timr: struct k_itimer \*

.. _`alarm_timer_arm`:

alarm_timer_arm
===============

.. c:function:: void alarm_timer_arm(struct k_itimer *timr, ktime_t expires, bool absolute, bool sigev_none)

    Posix timer callback to arm a timer

    :param timr:
        Pointer to the posixtimer data struct
    :type timr: struct k_itimer \*

    :param expires:
        The new expiry time
    :type expires: ktime_t

    :param absolute:
        Expiry value is absolute time
    :type absolute: bool

    :param sigev_none:
        Posix timer does not deliver signals
    :type sigev_none: bool

.. _`alarm_clock_getres`:

alarm_clock_getres
==================

.. c:function:: int alarm_clock_getres(const clockid_t which_clock, struct timespec64 *tp)

    posix getres interface

    :param which_clock:
        clockid
    :type which_clock: const clockid_t

    :param tp:
        timespec to fill
    :type tp: struct timespec64 \*

.. _`alarm_clock_getres.description`:

Description
-----------

Returns the granularity of underlying alarm base clock

.. _`alarm_clock_get`:

alarm_clock_get
===============

.. c:function:: int alarm_clock_get(clockid_t which_clock, struct timespec64 *tp)

    posix clock_get interface

    :param which_clock:
        clockid
    :type which_clock: clockid_t

    :param tp:
        timespec to fill.
    :type tp: struct timespec64 \*

.. _`alarm_clock_get.description`:

Description
-----------

Provides the underlying alarm base time.

.. _`alarm_timer_create`:

alarm_timer_create
==================

.. c:function:: int alarm_timer_create(struct k_itimer *new_timer)

    posix timer_create interface

    :param new_timer:
        k_itimer pointer to manage
    :type new_timer: struct k_itimer \*

.. _`alarm_timer_create.description`:

Description
-----------

Initializes the k_itimer structure.

.. _`alarmtimer_nsleep_wakeup`:

alarmtimer_nsleep_wakeup
========================

.. c:function:: enum alarmtimer_restart alarmtimer_nsleep_wakeup(struct alarm *alarm, ktime_t now)

    Wakeup function for alarm_timer_nsleep

    :param alarm:
        ptr to alarm that fired
    :type alarm: struct alarm \*

    :param now:
        *undescribed*
    :type now: ktime_t

.. _`alarmtimer_nsleep_wakeup.description`:

Description
-----------

Wakes up the task that set the alarmtimer

.. _`alarmtimer_do_nsleep`:

alarmtimer_do_nsleep
====================

.. c:function:: int alarmtimer_do_nsleep(struct alarm *alarm, ktime_t absexp, enum alarmtimer_type type)

    Internal alarmtimer nsleep implementation

    :param alarm:
        ptr to alarmtimer
    :type alarm: struct alarm \*

    :param absexp:
        absolute expiration time
    :type absexp: ktime_t

    :param type:
        *undescribed*
    :type type: enum alarmtimer_type

.. _`alarmtimer_do_nsleep.description`:

Description
-----------

Sets the alarm timer and sleeps until it is fired or interrupted.

.. _`alarm_timer_nsleep_restart`:

alarm_timer_nsleep_restart
==========================

.. c:function:: long __sched alarm_timer_nsleep_restart(struct restart_block *restart)

    restartblock alarmtimer nsleep

    :param restart:
        ptr to restart block
    :type restart: struct restart_block \*

.. _`alarm_timer_nsleep_restart.description`:

Description
-----------

Handles restarted clock_nanosleep calls

.. _`alarm_timer_nsleep`:

alarm_timer_nsleep
==================

.. c:function:: int alarm_timer_nsleep(const clockid_t which_clock, int flags, const struct timespec64 *tsreq)

    alarmtimer nanosleep

    :param which_clock:
        clockid
    :type which_clock: const clockid_t

    :param flags:
        determins abstime or relative
    :type flags: int

    :param tsreq:
        requested sleep time (abs or rel)
    :type tsreq: const struct timespec64 \*

.. _`alarm_timer_nsleep.description`:

Description
-----------

Handles clock_nanosleep calls against \_ALARM clockids

.. _`alarmtimer_init`:

alarmtimer_init
===============

.. c:function:: int alarmtimer_init( void)

    Initialize alarm timer code

    :param void:
        no arguments
    :type void: 

.. _`alarmtimer_init.description`:

Description
-----------

This function initializes the alarm bases and registers
the posix clock ids.

.. This file was automatic generated / don't edit.

