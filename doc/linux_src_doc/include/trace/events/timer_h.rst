.. -*- coding: utf-8; mode: rst -*-

=======
timer.h
=======


.. _`trace_timer_init`:

trace_timer_init
================

.. c:function:: void trace_timer_init (struct timer_list *timer)

    called when the timer is initialized

    :param struct timer_list \*timer:
        pointer to struct timer_list



.. _`trace_timer_start`:

trace_timer_start
=================

.. c:function:: void trace_timer_start (struct timer_list *timer, unsigned long expires, unsigned int flags)

    called when the timer is started

    :param struct timer_list \*timer:
        pointer to struct timer_list

    :param unsigned long expires:
        the timers expiry time

    :param unsigned int flags:

        *undescribed*



.. _`trace_timer_expire_entry`:

trace_timer_expire_entry
========================

.. c:function:: void trace_timer_expire_entry (struct timer_list *timer)

    called immediately before the timer callback

    :param struct timer_list \*timer:
        pointer to struct timer_list



.. _`trace_timer_expire_entry.description`:

Description
-----------

Allows to determine the timer latency.



.. _`trace_timer_expire_exit`:

trace_timer_expire_exit
=======================

.. c:function:: void trace_timer_expire_exit (struct timer_list *timer)

    called immediately after the timer callback returns

    :param struct timer_list \*timer:
        pointer to struct timer_list



.. _`trace_timer_expire_exit.description`:

Description
-----------

When used in combination with the timer_expire_entry tracepoint we can
determine the runtime of the timer callback function.



.. _`trace_timer_expire_exit.note`:

NOTE
----

Do NOT derefernce timer in TP_fast_assign. The pointer might
be invalid. We solely track the pointer.



.. _`trace_timer_cancel`:

trace_timer_cancel
==================

.. c:function:: void trace_timer_cancel (struct timer_list *timer)

    called when the timer is canceled

    :param struct timer_list \*timer:
        pointer to struct timer_list



.. _`trace_hrtimer_init`:

trace_hrtimer_init
==================

.. c:function:: void trace_hrtimer_init (struct hrtimer *hrtimer, clockid_t clockid, enum hrtimer_mode mode)

    called when the hrtimer is initialized

    :param struct hrtimer \*hrtimer:
        pointer to struct hrtimer

    :param clockid_t clockid:
        the hrtimers clock

    :param enum hrtimer_mode mode:
        the hrtimers mode



.. _`trace_hrtimer_start`:

trace_hrtimer_start
===================

.. c:function:: void trace_hrtimer_start (struct hrtimer *hrtimer)

    called when the hrtimer is started

    :param struct hrtimer \*hrtimer:
        pointer to struct hrtimer



.. _`trace_hrtimer_expire_entry`:

trace_hrtimer_expire_entry
==========================

.. c:function:: void trace_hrtimer_expire_entry (struct hrtimer *hrtimer, ktime_t *now)

    called immediately before the hrtimer callback

    :param struct hrtimer \*hrtimer:
        pointer to struct hrtimer

    :param ktime_t \*now:
        pointer to variable which contains current time of the
        timers base.



.. _`trace_hrtimer_expire_entry.description`:

Description
-----------

Allows to determine the timer latency.



.. _`trace_hrtimer_expire_exit`:

trace_hrtimer_expire_exit
=========================

.. c:function:: void trace_hrtimer_expire_exit (struct hrtimer *hrtimer)

    called immediately after the hrtimer callback returns

    :param struct hrtimer \*hrtimer:
        pointer to struct hrtimer



.. _`trace_hrtimer_expire_exit.description`:

Description
-----------

When used in combination with the hrtimer_expire_entry tracepoint we can
determine the runtime of the callback function.



.. _`trace_hrtimer_cancel`:

trace_hrtimer_cancel
====================

.. c:function:: void trace_hrtimer_cancel (struct hrtimer *hrtimer)

    called when the hrtimer is canceled

    :param struct hrtimer \*hrtimer:
        pointer to struct hrtimer



.. _`trace_itimer_state`:

trace_itimer_state
==================

.. c:function:: void trace_itimer_state (int which, const struct itimerval *const value, cputime_t expires)

    called when itimer is started or canceled

    :param int which:
        name of the interval timer

    :param const struct itimerval \*const value:
        the itimers value, itimer is canceled if value->it_value is
        zero, otherwise it is started

    :param cputime_t expires:
        the itimers expiry time



.. _`trace_itimer_expire`:

trace_itimer_expire
===================

.. c:function:: void trace_itimer_expire (int which, struct pid *pid, cputime_t now)

    called when itimer expires

    :param int which:
        type of the interval timer

    :param struct pid \*pid:
        pid of the process which owns the timer

    :param cputime_t now:
        current time, used to calculate the latency of itimer

