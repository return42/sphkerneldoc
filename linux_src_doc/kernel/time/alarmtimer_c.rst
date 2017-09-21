.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/alarmtimer.c

.. _`alarmtimer_get_rtcdev`:

alarmtimer_get_rtcdev
=====================

.. c:function:: struct rtc_device *alarmtimer_get_rtcdev( void)

    Return selected rtcdevice

    :param  void:
        no arguments

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

    :param struct alarm_base \*base:
        pointer to the base where the timer is being run

    :param struct alarm \*alarm:
        pointer to alarm being enqueued.

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

    :param struct alarm_base \*base:
        pointer to the base where the timer is running

    :param struct alarm \*alarm:
        pointer to alarm being removed

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

    :param struct hrtimer \*timer:
        pointer to hrtimer being run

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

    :param struct device \*dev:
        unused

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

    :param struct alarm \*alarm:
        ptr to alarm to be initialized

    :param enum alarmtimer_type type:
        the type of the alarm

    :param enum alarmtimer_restart (\*function)(struct alarm \*, ktime_t):
        callback that is run when the alarm fires

.. _`alarm_start`:

alarm_start
===========

.. c:function:: void alarm_start(struct alarm *alarm, ktime_t start)

    Sets an absolute alarm to fire

    :param struct alarm \*alarm:
        ptr to alarm to set

    :param ktime_t start:
        time to run the alarm

.. _`alarm_start_relative`:

alarm_start_relative
====================

.. c:function:: void alarm_start_relative(struct alarm *alarm, ktime_t start)

    Sets a relative alarm to fire

    :param struct alarm \*alarm:
        ptr to alarm to set

    :param ktime_t start:
        time relative to now to run the alarm

.. _`alarm_try_to_cancel`:

alarm_try_to_cancel
===================

.. c:function:: int alarm_try_to_cancel(struct alarm *alarm)

    Tries to cancel an alarm timer

    :param struct alarm \*alarm:
        ptr to alarm to be canceled

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

    :param struct alarm \*alarm:
        ptr to alarm to be canceled

.. _`alarm_cancel.description`:

Description
-----------

Returns 1 if the timer was canceled, 0 if it was not active.

.. _`clock2alarm`:

clock2alarm
===========

.. c:function:: enum alarmtimer_type clock2alarm(clockid_t clockid)

    helper that converts from clockid to alarmtypes

    :param clockid_t clockid:
        clockid.

.. _`alarm_handle_timer`:

alarm_handle_timer
==================

.. c:function:: enum alarmtimer_restart alarm_handle_timer(struct alarm *alarm, ktime_t now)

    Callback for posix timers

    :param struct alarm \*alarm:
        alarm that fired

    :param ktime_t now:
        *undescribed*

.. _`alarm_handle_timer.description`:

Description
-----------

Posix timer callback for expired alarm timers.

.. _`alarm_timer_rearm`:

alarm_timer_rearm
=================

.. c:function:: void alarm_timer_rearm(struct k_itimer *timr)

    Posix timer callback for rearming timer

    :param struct k_itimer \*timr:
        Pointer to the posixtimer data struct

.. _`alarm_timer_forward`:

alarm_timer_forward
===================

.. c:function:: int alarm_timer_forward(struct k_itimer *timr, ktime_t now)

    Posix timer callback for forwarding timer

    :param struct k_itimer \*timr:
        Pointer to the posixtimer data struct

    :param ktime_t now:
        Current time to forward the timer against

.. _`alarm_timer_remaining`:

alarm_timer_remaining
=====================

.. c:function:: ktime_t alarm_timer_remaining(struct k_itimer *timr, ktime_t now)

    Posix timer callback to retrieve remaining time

    :param struct k_itimer \*timr:
        Pointer to the posixtimer data struct

    :param ktime_t now:
        Current time to calculate against

.. _`alarm_timer_try_to_cancel`:

alarm_timer_try_to_cancel
=========================

.. c:function:: int alarm_timer_try_to_cancel(struct k_itimer *timr)

    Posix timer callback to cancel a timer

    :param struct k_itimer \*timr:
        Pointer to the posixtimer data struct

.. _`alarm_timer_arm`:

alarm_timer_arm
===============

.. c:function:: void alarm_timer_arm(struct k_itimer *timr, ktime_t expires, bool absolute, bool sigev_none)

    Posix timer callback to arm a timer

    :param struct k_itimer \*timr:
        Pointer to the posixtimer data struct

    :param ktime_t expires:
        The new expiry time

    :param bool absolute:
        Expiry value is absolute time

    :param bool sigev_none:
        Posix timer does not deliver signals

.. _`alarm_clock_getres`:

alarm_clock_getres
==================

.. c:function:: int alarm_clock_getres(const clockid_t which_clock, struct timespec64 *tp)

    posix getres interface

    :param const clockid_t which_clock:
        clockid

    :param struct timespec64 \*tp:
        timespec to fill

.. _`alarm_clock_getres.description`:

Description
-----------

Returns the granularity of underlying alarm base clock

.. _`alarm_clock_get`:

alarm_clock_get
===============

.. c:function:: int alarm_clock_get(clockid_t which_clock, struct timespec64 *tp)

    posix clock_get interface

    :param clockid_t which_clock:
        clockid

    :param struct timespec64 \*tp:
        timespec to fill.

.. _`alarm_clock_get.description`:

Description
-----------

Provides the underlying alarm base time.

.. _`alarm_timer_create`:

alarm_timer_create
==================

.. c:function:: int alarm_timer_create(struct k_itimer *new_timer)

    posix timer_create interface

    :param struct k_itimer \*new_timer:
        k_itimer pointer to manage

.. _`alarm_timer_create.description`:

Description
-----------

Initializes the k_itimer structure.

.. _`alarmtimer_nsleep_wakeup`:

alarmtimer_nsleep_wakeup
========================

.. c:function:: enum alarmtimer_restart alarmtimer_nsleep_wakeup(struct alarm *alarm, ktime_t now)

    Wakeup function for alarm_timer_nsleep

    :param struct alarm \*alarm:
        ptr to alarm that fired

    :param ktime_t now:
        *undescribed*

.. _`alarmtimer_nsleep_wakeup.description`:

Description
-----------

Wakes up the task that set the alarmtimer

.. _`alarmtimer_do_nsleep`:

alarmtimer_do_nsleep
====================

.. c:function:: int alarmtimer_do_nsleep(struct alarm *alarm, ktime_t absexp, enum alarmtimer_type type)

    Internal alarmtimer nsleep implementation

    :param struct alarm \*alarm:
        ptr to alarmtimer

    :param ktime_t absexp:
        absolute expiration time

    :param enum alarmtimer_type type:
        *undescribed*

.. _`alarmtimer_do_nsleep.description`:

Description
-----------

Sets the alarm timer and sleeps until it is fired or interrupted.

.. _`alarm_timer_nsleep_restart`:

alarm_timer_nsleep_restart
==========================

.. c:function:: long __sched alarm_timer_nsleep_restart(struct restart_block *restart)

    restartblock alarmtimer nsleep

    :param struct restart_block \*restart:
        ptr to restart block

.. _`alarm_timer_nsleep_restart.description`:

Description
-----------

Handles restarted clock_nanosleep calls

.. _`alarm_timer_nsleep`:

alarm_timer_nsleep
==================

.. c:function:: int alarm_timer_nsleep(const clockid_t which_clock, int flags, const struct timespec64 *tsreq)

    alarmtimer nanosleep

    :param const clockid_t which_clock:
        clockid

    :param int flags:
        determins abstime or relative

    :param const struct timespec64 \*tsreq:
        requested sleep time (abs or rel)

.. _`alarm_timer_nsleep.description`:

Description
-----------

Handles clock_nanosleep calls against \_ALARM clockids

.. _`alarmtimer_init`:

alarmtimer_init
===============

.. c:function:: int alarmtimer_init( void)

    Initialize alarm timer code

    :param  void:
        no arguments

.. _`alarmtimer_init.description`:

Description
-----------

This function initializes the alarm bases and registers
the posix clock ids.

.. This file was automatic generated / don't edit.

