.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/trace/events/timer.h

.. _`trace_timer_init`:

trace_timer_init
================

.. c:function:: void trace_timer_init(struct timer_list *timer)

    called when the timer is initialized

    :param timer:
        pointer to struct timer_list
    :type timer: struct timer_list \*

.. _`trace_timer_start`:

trace_timer_start
=================

.. c:function:: void trace_timer_start(struct timer_list *timer, unsigned long expires, unsigned int flags)

    called when the timer is started

    :param timer:
        pointer to struct timer_list
    :type timer: struct timer_list \*

    :param expires:
        the timers expiry time
    :type expires: unsigned long

    :param flags:
        *undescribed*
    :type flags: unsigned int

.. _`trace_timer_expire_entry`:

trace_timer_expire_entry
========================

.. c:function:: void trace_timer_expire_entry(struct timer_list *timer)

    called immediately before the timer callback

    :param timer:
        pointer to struct timer_list
    :type timer: struct timer_list \*

.. _`trace_timer_expire_entry.description`:

Description
-----------

Allows to determine the timer latency.

.. _`trace_timer_expire_exit`:

trace_timer_expire_exit
=======================

.. c:function:: void trace_timer_expire_exit(struct timer_list *timer)

    called immediately after the timer callback returns

    :param timer:
        pointer to struct timer_list
    :type timer: struct timer_list \*

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

.. c:function:: void trace_timer_cancel(struct timer_list *timer)

    called when the timer is canceled

    :param timer:
        pointer to struct timer_list
    :type timer: struct timer_list \*

.. _`trace_hrtimer_init`:

trace_hrtimer_init
==================

.. c:function:: void trace_hrtimer_init(struct hrtimer *hrtimer, clockid_t clockid, enum hrtimer_mode mode)

    called when the hrtimer is initialized

    :param hrtimer:
        pointer to struct hrtimer
    :type hrtimer: struct hrtimer \*

    :param clockid:
        the hrtimers clock
    :type clockid: clockid_t

    :param mode:
        the hrtimers mode
    :type mode: enum hrtimer_mode

.. _`trace_hrtimer_start`:

trace_hrtimer_start
===================

.. c:function:: void trace_hrtimer_start(struct hrtimer *hrtimer, enum hrtimer_mode mode)

    called when the hrtimer is started

    :param hrtimer:
        pointer to struct hrtimer
    :type hrtimer: struct hrtimer \*

    :param mode:
        *undescribed*
    :type mode: enum hrtimer_mode

.. _`trace_hrtimer_expire_entry`:

trace_hrtimer_expire_entry
==========================

.. c:function:: void trace_hrtimer_expire_entry(struct hrtimer *hrtimer, ktime_t *now)

    called immediately before the hrtimer callback

    :param hrtimer:
        pointer to struct hrtimer
    :type hrtimer: struct hrtimer \*

    :param now:
        pointer to variable which contains current time of the
        timers base.
    :type now: ktime_t \*

.. _`trace_hrtimer_expire_entry.description`:

Description
-----------

Allows to determine the timer latency.

.. _`trace_hrtimer_expire_exit`:

trace_hrtimer_expire_exit
=========================

.. c:function:: void trace_hrtimer_expire_exit(struct hrtimer *hrtimer)

    called immediately after the hrtimer callback returns

    :param hrtimer:
        pointer to struct hrtimer
    :type hrtimer: struct hrtimer \*

.. _`trace_hrtimer_expire_exit.description`:

Description
-----------

When used in combination with the hrtimer_expire_entry tracepoint we can
determine the runtime of the callback function.

.. _`trace_hrtimer_cancel`:

trace_hrtimer_cancel
====================

.. c:function:: void trace_hrtimer_cancel(struct hrtimer *hrtimer)

    called when the hrtimer is canceled

    :param hrtimer:
        pointer to struct hrtimer
    :type hrtimer: struct hrtimer \*

.. _`trace_itimer_state`:

trace_itimer_state
==================

.. c:function:: void trace_itimer_state(int which, const struct itimerval *const value, unsigned long long expires)

    called when itimer is started or canceled

    :param which:
        name of the interval timer
    :type which: int

    :param value:
        the itimers value, itimer is canceled if value->it_value is
        zero, otherwise it is started
    :type value: const struct itimerval \*const

    :param expires:
        the itimers expiry time
    :type expires: unsigned long long

.. _`trace_itimer_expire`:

trace_itimer_expire
===================

.. c:function:: void trace_itimer_expire(int which, struct pid *pid, unsigned long long now)

    called when itimer expires

    :param which:
        type of the interval timer
    :type which: int

    :param pid:
        pid of the process which owns the timer
    :type pid: struct pid \*

    :param now:
        current time, used to calculate the latency of itimer
    :type now: unsigned long long

.. This file was automatic generated / don't edit.

