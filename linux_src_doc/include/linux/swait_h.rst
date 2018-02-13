.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/swait.h

.. _`swait_active`:

swait_active
============

.. c:function:: int swait_active(struct swait_queue_head *wq)

    - locklessly test for waiters on the queue

    :param struct swait_queue_head \*wq:
        the waitqueue to test for waiters

.. _`swait_active.description`:

Description
-----------

returns true if the wait list is not empty

.. _`swait_active.note`:

NOTE
----

this function is lockless and requires care, incorrect usage \_will_
lead to sporadic and non-obvious failure.

.. _`swait_active.note2`:

NOTE2
-----

this function has the same above implications as regular waitqueues.

Use either while holding swait_queue_head::lock or when used for wakeups
with an extra \ :c:func:`smp_mb`\  like:

CPU0 - waker                    CPU1 - waiter

for (;;) {
\ ``cond``\  = true;                     prepare_to_swait(&wq_head, \ :c:type:`struct wait <wait>`\ , state);
\ :c:func:`smp_mb`\ ;                         // \ :c:func:`smp_mb`\  from \ :c:func:`set_current_state`\ 
if (swait_active(wq_head))        if (@cond)
wake_up(wq_head);                      break;
\ :c:func:`schedule`\ ;
}
finish_swait(&wq_head, \ :c:type:`struct wait <wait>`\ );

Because without the explicit \ :c:func:`smp_mb`\  it's possible for the
\ :c:func:`swait_active`\  load to get hoisted over the \ ``cond``\  store such that we'll
observe an empty wait list while the waiter might not observe \ ``cond``\ .
This, in turn, can trigger missing wakeups.

Also note that this 'optimization' trades a \ :c:func:`spin_lock`\  for an \ :c:func:`smp_mb`\ ,
which (when the lock is uncontended) are of roughly equal cost.

.. _`swq_has_sleeper`:

swq_has_sleeper
===============

.. c:function:: bool swq_has_sleeper(struct swait_queue_head *wq)

    check if there are any waiting processes

    :param struct swait_queue_head \*wq:
        the waitqueue to test for waiters

.. _`swq_has_sleeper.description`:

Description
-----------

Returns true if \ ``wq``\  has waiting processes

Please refer to the comment for swait_active.

.. _`swait_event_idle`:

swait_event_idle
================

.. c:function::  swait_event_idle( wq,  condition)

    wait without system load contribution

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`swait_event_idle.description`:

Description
-----------

The process is put to sleep (TASK_IDLE) until the \ ``condition``\  evaluates to
true. The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

This function is mostly used when a kthread or workqueue waits for some
condition and doesn't want to contribute to system load. Signals are
ignored.

.. _`swait_event_idle_timeout`:

swait_event_idle_timeout
========================

.. c:function::  swait_event_idle_timeout( wq,  condition,  timeout)

    wait up to timeout without load contribution

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  timeout:
        timeout at which we'll give up in jiffies

.. _`swait_event_idle_timeout.description`:

Description
-----------

The process is put to sleep (TASK_IDLE) until the \ ``condition``\  evaluates to
true. The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

This function is mostly used when a kthread or workqueue waits for some
condition and doesn't want to contribute to system load. Signals are
ignored.

.. _`swait_event_idle_timeout.return`:

Return
------

0 if the \ ``condition``\  evaluated to \ ``false``\  after the \ ``timeout``\  elapsed,
1 if the \ ``condition``\  evaluated to \ ``true``\  after the \ ``timeout``\  elapsed,
or the remaining jiffies (at least 1) if the \ ``condition``\  evaluated
to \ ``true``\  before the \ ``timeout``\  elapsed.

.. This file was automatic generated / don't edit.

