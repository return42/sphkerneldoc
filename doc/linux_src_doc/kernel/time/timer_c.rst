.. -*- coding: utf-8; mode: rst -*-

=======
timer.c
=======

.. _`__round_jiffies`:

__round_jiffies
===============

.. c:function:: unsigned long __round_jiffies (unsigned long j, int cpu)

    function to round jiffies to a full second

    :param unsigned long j:
        the time in (absolute) jiffies that should be rounded

    :param int cpu:
        the processor number on which the timeout will happen


.. _`__round_jiffies.description`:

Description
-----------

:c:func:`__round_jiffies` rounds an absolute time in the future (in jiffies)
up or down to (approximately) full seconds. This is useful for timers
for which the exact time they fire does not matter too much, as long as
they fire approximately every X seconds.

By rounding these timers to whole seconds, all such timers will fire
at the same time, rather than at various times spread out. The goal
of this is to have the CPU wake up less, which saves power.

The exact rounding is skewed for each processor to avoid all
processors firing at the exact same time, which could lead
to lock contention or spurious cache line bouncing.

The return value is the rounded version of the ``j`` parameter.


.. _`__round_jiffies_relative`:

__round_jiffies_relative
========================

.. c:function:: unsigned long __round_jiffies_relative (unsigned long j, int cpu)

    function to round jiffies to a full second

    :param unsigned long j:
        the time in (relative) jiffies that should be rounded

    :param int cpu:
        the processor number on which the timeout will happen


.. _`__round_jiffies_relative.description`:

Description
-----------

:c:func:`__round_jiffies_relative` rounds a time delta  in the future (in jiffies)
up or down to (approximately) full seconds. This is useful for timers
for which the exact time they fire does not matter too much, as long as
they fire approximately every X seconds.

By rounding these timers to whole seconds, all such timers will fire
at the same time, rather than at various times spread out. The goal
of this is to have the CPU wake up less, which saves power.

The exact rounding is skewed for each processor to avoid all
processors firing at the exact same time, which could lead
to lock contention or spurious cache line bouncing.

The return value is the rounded version of the ``j`` parameter.


.. _`round_jiffies`:

round_jiffies
=============

.. c:function:: unsigned long round_jiffies (unsigned long j)

    function to round jiffies to a full second

    :param unsigned long j:
        the time in (absolute) jiffies that should be rounded


.. _`round_jiffies.description`:

Description
-----------

:c:func:`round_jiffies` rounds an absolute time in the future (in jiffies)
up or down to (approximately) full seconds. This is useful for timers
for which the exact time they fire does not matter too much, as long as
they fire approximately every X seconds.

By rounding these timers to whole seconds, all such timers will fire
at the same time, rather than at various times spread out. The goal
of this is to have the CPU wake up less, which saves power.

The return value is the rounded version of the ``j`` parameter.


.. _`round_jiffies_relative`:

round_jiffies_relative
======================

.. c:function:: unsigned long round_jiffies_relative (unsigned long j)

    function to round jiffies to a full second

    :param unsigned long j:
        the time in (relative) jiffies that should be rounded


.. _`round_jiffies_relative.description`:

Description
-----------

:c:func:`round_jiffies_relative` rounds a time delta  in the future (in jiffies)
up or down to (approximately) full seconds. This is useful for timers
for which the exact time they fire does not matter too much, as long as
they fire approximately every X seconds.

By rounding these timers to whole seconds, all such timers will fire
at the same time, rather than at various times spread out. The goal
of this is to have the CPU wake up less, which saves power.

The return value is the rounded version of the ``j`` parameter.


.. _`__round_jiffies_up`:

__round_jiffies_up
==================

.. c:function:: unsigned long __round_jiffies_up (unsigned long j, int cpu)

    function to round jiffies up to a full second

    :param unsigned long j:
        the time in (absolute) jiffies that should be rounded

    :param int cpu:
        the processor number on which the timeout will happen


.. _`__round_jiffies_up.description`:

Description
-----------

This is the same as :c:func:`__round_jiffies` except that it will never
round down.  This is useful for timeouts for which the exact time
of firing does not matter too much, as long as they don't fire too
early.


.. _`__round_jiffies_up_relative`:

__round_jiffies_up_relative
===========================

.. c:function:: unsigned long __round_jiffies_up_relative (unsigned long j, int cpu)

    function to round jiffies up to a full second

    :param unsigned long j:
        the time in (relative) jiffies that should be rounded

    :param int cpu:
        the processor number on which the timeout will happen


.. _`__round_jiffies_up_relative.description`:

Description
-----------

This is the same as :c:func:`__round_jiffies_relative` except that it will never
round down.  This is useful for timeouts for which the exact time
of firing does not matter too much, as long as they don't fire too
early.


.. _`round_jiffies_up`:

round_jiffies_up
================

.. c:function:: unsigned long round_jiffies_up (unsigned long j)

    function to round jiffies up to a full second

    :param unsigned long j:
        the time in (absolute) jiffies that should be rounded


.. _`round_jiffies_up.description`:

Description
-----------

This is the same as :c:func:`round_jiffies` except that it will never
round down.  This is useful for timeouts for which the exact time
of firing does not matter too much, as long as they don't fire too
early.


.. _`round_jiffies_up_relative`:

round_jiffies_up_relative
=========================

.. c:function:: unsigned long round_jiffies_up_relative (unsigned long j)

    function to round jiffies up to a full second

    :param unsigned long j:
        the time in (relative) jiffies that should be rounded


.. _`round_jiffies_up_relative.description`:

Description
-----------

This is the same as :c:func:`round_jiffies_relative` except that it will never
round down.  This is useful for timeouts for which the exact time
of firing does not matter too much, as long as they don't fire too
early.


.. _`set_timer_slack`:

set_timer_slack
===============

.. c:function:: void set_timer_slack (struct timer_list *timer, int slack_hz)

    set the allowed slack for a timer

    :param struct timer_list \*timer:
        the timer to be modified

    :param int slack_hz:
        the amount of time (in jiffies) allowed for rounding


.. _`set_timer_slack.description`:

Description
-----------

Set the amount of time, in jiffies, that a certain timer has
in terms of slack. By setting this value, the timer subsystem
will schedule the actual timer somewhere between
the time :c:func:`mod_timer` asks for, and that time plus the slack.

By setting the slack to -1, a percentage of the delay is used
instead.


.. _`init_timer_key`:

init_timer_key
==============

.. c:function:: void init_timer_key (struct timer_list *timer, unsigned int flags, const char *name, struct lock_class_key *key)

    initialize a timer

    :param struct timer_list \*timer:
        the timer to be initialized

    :param unsigned int flags:
        timer flags

    :param const char \*name:
        name of the timer

    :param struct lock_class_key \*key:
        lockdep class key of the fake lock used for tracking timer
        sync lock dependencies


.. _`init_timer_key.description`:

Description
-----------

:c:func:`init_timer_key` must be done to a timer prior calling \*any\* of the
other timer functions.


.. _`mod_timer_pending`:

mod_timer_pending
=================

.. c:function:: int mod_timer_pending (struct timer_list *timer, unsigned long expires)

    modify a pending timer's timeout

    :param struct timer_list \*timer:
        the pending timer to be modified

    :param unsigned long expires:
        new timeout in jiffies


.. _`mod_timer_pending.description`:

Description
-----------

:c:func:`mod_timer_pending` is the same for pending timers as :c:func:`mod_timer`,
but will not re-activate and modify already deleted timers.

It is useful for unserialized use of timers.


.. _`mod_timer`:

mod_timer
=========

.. c:function:: int mod_timer (struct timer_list *timer, unsigned long expires)

    modify a timer's timeout

    :param struct timer_list \*timer:
        the timer to be modified

    :param unsigned long expires:
        new timeout in jiffies


.. _`mod_timer.description`:

Description
-----------

:c:func:`mod_timer` is a more efficient way to update the expire field of an
active timer (if the timer is inactive it will be activated)

mod_timer(timer, expires) is equivalent to::

    del_timer(timer); timer->expires = expires; add_timer(timer);

Note that if there are multiple unserialized concurrent users of the
same timer, then :c:func:`mod_timer` is the only safe way to modify the timeout,
since :c:func:`add_timer` cannot modify an already running timer.

The function returns whether it has modified a pending timer or not.
(ie. :c:func:`mod_timer` of an inactive timer returns 0, :c:func:`mod_timer` of an
active timer returns 1.)


.. _`mod_timer_pinned`:

mod_timer_pinned
================

.. c:function:: int mod_timer_pinned (struct timer_list *timer, unsigned long expires)

    modify a timer's timeout

    :param struct timer_list \*timer:
        the timer to be modified

    :param unsigned long expires:
        new timeout in jiffies


.. _`mod_timer_pinned.description`:

Description
-----------

:c:func:`mod_timer_pinned` is a way to update the expire field of an
active timer (if the timer is inactive it will be activated)
and to ensure that the timer is scheduled on the current CPU.

Note that this does not prevent the timer from being migrated
when the current CPU goes offline.  If this is a problem for
you, use CPU-hotplug notifiers to handle it correctly, for
example, cancelling the timer when the corresponding CPU goes
offline.

mod_timer_pinned(timer, expires) is equivalent to::

    del_timer(timer); timer->expires = expires; add_timer(timer);


.. _`add_timer`:

add_timer
=========

.. c:function:: void add_timer (struct timer_list *timer)

    start a timer

    :param struct timer_list \*timer:
        the timer to be added


.. _`add_timer.description`:

Description
-----------

The kernel will do a ->function(->data) callback from the
timer interrupt at the ->expires point in the future. The
current time is 'jiffies'.

The timer's ->expires, ->function (and if the handler uses it, ->data)
fields must be set prior calling this function.

Timers with an ->expires field in the past will be executed in the next
timer tick.


.. _`add_timer_on`:

add_timer_on
============

.. c:function:: void add_timer_on (struct timer_list *timer, int cpu)

    start a timer on a particular CPU

    :param struct timer_list \*timer:
        the timer to be added

    :param int cpu:
        the CPU to start it on


.. _`add_timer_on.description`:

Description
-----------

This is not very scalable on SMP. Double adds are not possible.


.. _`del_timer`:

del_timer
=========

.. c:function:: int del_timer (struct timer_list *timer)

    deactive a timer.

    :param struct timer_list \*timer:
        the timer to be deactivated


.. _`del_timer.description`:

Description
-----------

:c:func:`del_timer` deactivates a timer - this works on both active and inactive
timers.

The function returns whether it has deactivated a pending timer or not.
(ie. :c:func:`del_timer` of an inactive timer returns 0, :c:func:`del_timer` of an
active timer returns 1.)


.. _`try_to_del_timer_sync`:

try_to_del_timer_sync
=====================

.. c:function:: int try_to_del_timer_sync (struct timer_list *timer)

    Try to deactivate a timer

    :param struct timer_list \*timer:
        timer do del


.. _`try_to_del_timer_sync.description`:

Description
-----------

This function tries to deactivate a timer. Upon successful (ret >= 0)
exit the timer is not queued and the handler is not running on any CPU.


.. _`del_timer_sync`:

del_timer_sync
==============

.. c:function:: int del_timer_sync (struct timer_list *timer)

    deactivate a timer and wait for the handler to finish.

    :param struct timer_list \*timer:
        the timer to be deactivated


.. _`del_timer_sync.description`:

Description
-----------

This function only differs from :c:func:`del_timer` on SMP: besides deactivating
the timer it also makes sure the handler has finished executing on other
CPUs.

Synchronization rules: Callers must prevent restarting of the timer,
otherwise this function is meaningless. It must not be called from
interrupt contexts unless the timer is an irqsafe one. The caller must
not hold locks which would prevent completion of the timer's
handler. The timer's handler must not call :c:func:`add_timer_on`. Upon exit the
timer is not queued and the handler is not running on any CPU.

Note: For !irqsafe timers, you must not hold locks that are held in
interrupt context while calling this function. Even if the lock has
nothing to do with the timer in question.  Here's why:

CPU0                             CPU1
----                             ----
<SOFTIRQ>
:c:func:`call_timer_fn`;
base->running_timer = mytimer;
spin_lock_irq(somelock);
<IRQ>
spin_lock(somelock);
del_timer_sync(mytimer);
while (base->running_timer == mytimer);

Now :c:func:`del_timer_sync` will never return and never release somelock.
The interrupt on the other CPU is waiting to grab somelock but
it has interrupted the softirq that CPU0 is waiting to finish.

The function returns whether it has deactivated a pending timer or not.


.. _`__run_timers`:

__run_timers
============

.. c:function:: void __run_timers (struct tvec_base *base)

    run all expired timers (if any) on this CPU.

    :param struct tvec_base \*base:
        the timer vector to be processed.


.. _`__run_timers.description`:

Description
-----------

This function cascades all vectors and executes all expired timer
vectors.


.. _`get_next_timer_interrupt`:

get_next_timer_interrupt
========================

.. c:function:: u64 get_next_timer_interrupt (unsigned long basej, u64 basem)

    return the time (clock mono) of the next timer

    :param unsigned long basej:
        base time jiffies

    :param u64 basem:
        base time clock monotonic


.. _`get_next_timer_interrupt.description`:

Description
-----------

Returns the tick aligned clock monotonic time of the next pending
timer or KTIME_MAX if no timer is pending.


.. _`schedule_timeout`:

schedule_timeout
================

.. c:function:: signed long __sched schedule_timeout (signed long timeout)

    sleep until timeout

    :param signed long timeout:
        timeout value in jiffies


.. _`schedule_timeout.description`:

Description
-----------

Make the current task sleep until ``timeout`` jiffies have
elapsed. The routine will return immediately unless
the current task state has been set (see :c:func:`set_current_state`).

You can set the task state as follows -

``TASK_UNINTERRUPTIBLE`` - at least ``timeout`` jiffies are guaranteed to
pass before the routine returns. The routine will return 0

``TASK_INTERRUPTIBLE`` - the routine may return early if a signal is
delivered to the current task. In this case the remaining time
in jiffies will be returned, or 0 if the timer expired in time

The current task state is guaranteed to be TASK_RUNNING when this
routine returns.

Specifying a ``timeout`` value of ``MAX_SCHEDULE_TIMEOUT`` will schedule
the CPU away without a bound on the timeout. In this case the return
value will be ``MAX_SCHEDULE_TIMEOUT``\ .

In all cases the return value is guaranteed to be non-negative.


.. _`msleep`:

msleep
======

.. c:function:: void msleep (unsigned int msecs)

    sleep safely even with waitqueue interruptions

    :param unsigned int msecs:
        Time in milliseconds to sleep for


.. _`msleep_interruptible`:

msleep_interruptible
====================

.. c:function:: unsigned long msleep_interruptible (unsigned int msecs)

    sleep waiting for signals

    :param unsigned int msecs:
        Time in milliseconds to sleep for


.. _`usleep_range`:

usleep_range
============

.. c:function:: void __sched usleep_range (unsigned long min, unsigned long max)

    Drop in replacement for udelay where wakeup is flexible

    :param unsigned long min:
        Minimum time in usecs to sleep

    :param unsigned long max:
        Maximum time in usecs to sleep

