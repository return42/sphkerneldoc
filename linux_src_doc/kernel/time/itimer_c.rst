.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/itimer.c

.. _`itimer_get_remtime`:

itimer_get_remtime
==================

.. c:function:: struct timeval itimer_get_remtime(struct hrtimer *timer)

    get remaining time for the timer

    :param struct hrtimer \*timer:
        the timer to read

.. _`itimer_get_remtime.description`:

Description
-----------

Returns the delta between the expiry time and now, which can be
less than zero or 1usec for an pending expired timer

.. _`alarm_setitimer`:

alarm_setitimer
===============

.. c:function:: unsigned int alarm_setitimer(unsigned int seconds)

    set alarm in seconds

    :param unsigned int seconds:
        number of seconds until alarm
        0 disables the alarm

.. _`alarm_setitimer.description`:

Description
-----------

Returns the remaining time in seconds of a pending timer or 0 when
the timer is not active.

On 32 bit machines the seconds value is limited to (INT_MAX/2) to avoid
negative timeval settings which would cause immediate expiry.

.. This file was automatic generated / don't edit.

