.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/wait.h

.. _`waitqueue_active`:

waitqueue_active
================

.. c:function:: int waitqueue_active(struct wait_queue_head *wq_head)

    - locklessly test for waiters on the queue

    :param struct wait_queue_head \*wq_head:
        the waitqueue to test for waiters

.. _`waitqueue_active.description`:

Description
-----------

returns true if the wait list is not empty

.. _`waitqueue_active.note`:

NOTE
----

this function is lockless and requires care, incorrect usage _will_
lead to sporadic and non-obvious failure.

Use either while holding wait_queue_head::lock or when used for wakeups
with an extra \ :c:func:`smp_mb`\  like:

     CPU0 - waker                    CPU1 - waiter

                                     for (;;) {
     \ ``cond``\  = true;                     prepare_to_wait(&wq_head, \ :c:type:`struct wait <wait>`\ , state);
     \ :c:func:`smp_mb`\ ;                         // \ :c:func:`smp_mb`\  from \ :c:func:`set_current_state`\ 
     if (waitqueue_active(wq_head))         if (@cond)
       wake_up(wq_head);                      break;
                                       \ :c:func:`schedule`\ ;
                                     }
                                     finish_wait(&wq_head, \ :c:type:`struct wait <wait>`\ );

Because without the explicit \ :c:func:`smp_mb`\  it's possible for the
\ :c:func:`waitqueue_active`\  load to get hoisted over the \ ``cond``\  store such that we'll
observe an empty wait list while the waiter might not observe \ ``cond``\ .

Also note that this 'optimization' trades a \ :c:func:`spin_lock`\  for an \ :c:func:`smp_mb`\ ,
which (when the lock is uncontended) are of roughly equal cost.

.. _`wq_has_sleeper`:

wq_has_sleeper
==============

.. c:function:: bool wq_has_sleeper(struct wait_queue_head *wq_head)

    check if there are any waiting processes

    :param struct wait_queue_head \*wq_head:
        wait queue head

.. _`wq_has_sleeper.description`:

Description
-----------

Returns true if wq_head has waiting processes

Please refer to the comment for waitqueue_active.

.. _`wait_event`:

wait_event
==========

.. c:function::  wait_event( wq_head,  condition)

    sleep until a condition gets true

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event.description`:

Description
-----------

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
\ ``condition``\  evaluates to true. The \ ``condition``\  is checked each time
the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_freezable`:

wait_event_freezable
====================

.. c:function::  wait_event_freezable( wq_head,  condition)

    sleep (or freeze) until a condition gets true

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_freezable.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE -- so as not to contribute
to system load) until the \ ``condition``\  evaluates to true. The
\ ``condition``\  is checked each time the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_timeout`:

wait_event_timeout
==================

.. c:function::  wait_event_timeout( wq_head,  condition,  timeout)

    sleep until a condition gets true or a timeout elapses

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  timeout:
        timeout, in jiffies

.. _`wait_event_timeout.description`:

Description
-----------

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
\ ``condition``\  evaluates to true. The \ ``condition``\  is checked each time
the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_timeout.return`:

Return
------

0 if the \ ``condition``\  evaluated to \ ``false``\  after the \ ``timeout``\  elapsed,
1 if the \ ``condition``\  evaluated to \ ``true``\  after the \ ``timeout``\  elapsed,
or the remaining jiffies (at least 1) if the \ ``condition``\  evaluated
to \ ``true``\  before the \ ``timeout``\  elapsed.

.. _`wait_event_cmd`:

wait_event_cmd
==============

.. c:function::  wait_event_cmd( wq_head,  condition,  cmd1,  cmd2)

    sleep until a condition gets true

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  cmd1:
        the command will be executed before sleep

    :param  cmd2:
        the command will be executed after sleep

.. _`wait_event_cmd.description`:

Description
-----------

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
\ ``condition``\  evaluates to true. The \ ``condition``\  is checked each time
the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_interruptible`:

wait_event_interruptible
========================

.. c:function::  wait_event_interruptible( wq_head,  condition)

    sleep until a condition gets true

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_interruptible.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if \ ``condition``\  evaluated to true.

.. _`wait_event_interruptible_timeout`:

wait_event_interruptible_timeout
================================

.. c:function::  wait_event_interruptible_timeout( wq_head,  condition,  timeout)

    sleep until a condition gets true or a timeout elapses

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  timeout:
        timeout, in jiffies

.. _`wait_event_interruptible_timeout.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_interruptible_timeout.return`:

Return
------

0 if the \ ``condition``\  evaluated to \ ``false``\  after the \ ``timeout``\  elapsed,
1 if the \ ``condition``\  evaluated to \ ``true``\  after the \ ``timeout``\  elapsed,
the remaining jiffies (at least 1) if the \ ``condition``\  evaluated
to \ ``true``\  before the \ ``timeout``\  elapsed, or -%ERESTARTSYS if it was
interrupted by a signal.

.. _`wait_event_hrtimeout`:

wait_event_hrtimeout
====================

.. c:function::  wait_event_hrtimeout( wq_head,  condition,  timeout)

    sleep until a condition gets true or a timeout elapses

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  timeout:
        timeout, as a ktime_t

.. _`wait_event_hrtimeout.description`:

Description
-----------

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

The function returns 0 if \ ``condition``\  became true, or -ETIME if the timeout
elapsed.

.. _`wait_event_interruptible_hrtimeout`:

wait_event_interruptible_hrtimeout
==================================

.. c:function::  wait_event_interruptible_hrtimeout( wq,  condition,  timeout)

    sleep until a condition gets true or a timeout elapses

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  timeout:
        timeout, as a ktime_t

.. _`wait_event_interruptible_hrtimeout.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

The function returns 0 if \ ``condition``\  became true, -ERESTARTSYS if it was
interrupted by a signal, or -ETIME if the timeout elapsed.

.. _`wait_event_idle`:

wait_event_idle
===============

.. c:function::  wait_event_idle( wq_head,  condition)

    wait for a condition without contributing to system load

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_idle.description`:

Description
-----------

The process is put to sleep (TASK_IDLE) until the
\ ``condition``\  evaluates to true.
The \ ``condition``\  is checked each time the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_idle_exclusive`:

wait_event_idle_exclusive
=========================

.. c:function::  wait_event_idle_exclusive( wq_head,  condition)

    wait for a condition with contributing to system load

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_idle_exclusive.description`:

Description
-----------

The process is put to sleep (TASK_IDLE) until the
\ ``condition``\  evaluates to true.
The \ ``condition``\  is checked each time the waitqueue \ ``wq_head``\  is woken up.

The process is put on the wait queue with an WQ_FLAG_EXCLUSIVE flag
set thus if other processes wait on the same list, when this
process is woken further processes are not considered.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_idle_timeout`:

wait_event_idle_timeout
=======================

.. c:function::  wait_event_idle_timeout( wq_head,  condition,  timeout)

    sleep without load until a condition becomes true or a timeout elapses

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  timeout:
        timeout, in jiffies

.. _`wait_event_idle_timeout.description`:

Description
-----------

The process is put to sleep (TASK_IDLE) until the
\ ``condition``\  evaluates to true. The \ ``condition``\  is checked each time
the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_idle_timeout.return`:

Return
------

0 if the \ ``condition``\  evaluated to \ ``false``\  after the \ ``timeout``\  elapsed,
1 if the \ ``condition``\  evaluated to \ ``true``\  after the \ ``timeout``\  elapsed,
or the remaining jiffies (at least 1) if the \ ``condition``\  evaluated
to \ ``true``\  before the \ ``timeout``\  elapsed.

.. _`wait_event_idle_exclusive_timeout`:

wait_event_idle_exclusive_timeout
=================================

.. c:function::  wait_event_idle_exclusive_timeout( wq_head,  condition,  timeout)

    sleep without load until a condition becomes true or a timeout elapses

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  timeout:
        timeout, in jiffies

.. _`wait_event_idle_exclusive_timeout.description`:

Description
-----------

The process is put to sleep (TASK_IDLE) until the
\ ``condition``\  evaluates to true. The \ ``condition``\  is checked each time
the waitqueue \ ``wq_head``\  is woken up.

The process is put on the wait queue with an WQ_FLAG_EXCLUSIVE flag
set thus if other processes wait on the same list, when this
process is woken further processes are not considered.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_idle_exclusive_timeout.return`:

Return
------

0 if the \ ``condition``\  evaluated to \ ``false``\  after the \ ``timeout``\  elapsed,
1 if the \ ``condition``\  evaluated to \ ``true``\  after the \ ``timeout``\  elapsed,
or the remaining jiffies (at least 1) if the \ ``condition``\  evaluated
to \ ``true``\  before the \ ``timeout``\  elapsed.

.. _`wait_event_interruptible_locked`:

wait_event_interruptible_locked
===============================

.. c:function::  wait_event_interruptible_locked( wq,  condition)

    sleep until a condition gets true

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_interruptible_locked.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

It must be called with wq.lock being held.  This spinlock is
unlocked while sleeping but \ ``condition``\  testing is done while lock
is held and when this macro exits the lock is held.

The lock is locked/unlocked using \ :c:func:`spin_lock`\ /spin_unlock()
functions which must match the way they are locked/unlocked outside
of this macro.

\ :c:func:`wake_up_locked`\  has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if \ ``condition``\  evaluated to true.

.. _`wait_event_interruptible_locked_irq`:

wait_event_interruptible_locked_irq
===================================

.. c:function::  wait_event_interruptible_locked_irq( wq,  condition)

    sleep until a condition gets true

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_interruptible_locked_irq.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

It must be called with wq.lock being held.  This spinlock is
unlocked while sleeping but \ ``condition``\  testing is done while lock
is held and when this macro exits the lock is held.

The lock is locked/unlocked using \ :c:func:`spin_lock_irq`\ /spin_unlock_irq()
functions which must match the way they are locked/unlocked outside
of this macro.

\ :c:func:`wake_up_locked`\  has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if \ ``condition``\  evaluated to true.

.. _`wait_event_interruptible_exclusive_locked`:

wait_event_interruptible_exclusive_locked
=========================================

.. c:function::  wait_event_interruptible_exclusive_locked( wq,  condition)

    sleep exclusively until a condition gets true

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_interruptible_exclusive_locked.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

It must be called with wq.lock being held.  This spinlock is
unlocked while sleeping but \ ``condition``\  testing is done while lock
is held and when this macro exits the lock is held.

The lock is locked/unlocked using \ :c:func:`spin_lock`\ /spin_unlock()
functions which must match the way they are locked/unlocked outside
of this macro.

The process is put on the wait queue with an WQ_FLAG_EXCLUSIVE flag
set thus when other process waits process on the list if this
process is awaken further processes are not considered.

\ :c:func:`wake_up_locked`\  has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if \ ``condition``\  evaluated to true.

.. _`wait_event_interruptible_exclusive_locked_irq`:

wait_event_interruptible_exclusive_locked_irq
=============================================

.. c:function::  wait_event_interruptible_exclusive_locked_irq( wq,  condition)

    sleep until a condition gets true

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_interruptible_exclusive_locked_irq.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

It must be called with wq.lock being held.  This spinlock is
unlocked while sleeping but \ ``condition``\  testing is done while lock
is held and when this macro exits the lock is held.

The lock is locked/unlocked using \ :c:func:`spin_lock_irq`\ /spin_unlock_irq()
functions which must match the way they are locked/unlocked outside
of this macro.

The process is put on the wait queue with an WQ_FLAG_EXCLUSIVE flag
set thus when other process waits process on the list if this
process is awaken further processes are not considered.

\ :c:func:`wake_up_locked`\  has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if \ ``condition``\  evaluated to true.

.. _`wait_event_killable`:

wait_event_killable
===================

.. c:function::  wait_event_killable( wq_head,  condition)

    sleep until a condition gets true

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_killable.description`:

Description
-----------

The process is put to sleep (TASK_KILLABLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if \ ``condition``\  evaluated to true.

.. _`wait_event_killable_timeout`:

wait_event_killable_timeout
===========================

.. c:function::  wait_event_killable_timeout( wq_head,  condition,  timeout)

    sleep until a condition gets true or a timeout elapses

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  timeout:
        timeout, in jiffies

.. _`wait_event_killable_timeout.description`:

Description
-----------

The process is put to sleep (TASK_KILLABLE) until the
\ ``condition``\  evaluates to true or a kill signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_killable_timeout.return`:

Return
------

0 if the \ ``condition``\  evaluated to \ ``false``\  after the \ ``timeout``\  elapsed,
1 if the \ ``condition``\  evaluated to \ ``true``\  after the \ ``timeout``\  elapsed,
the remaining jiffies (at least 1) if the \ ``condition``\  evaluated
to \ ``true``\  before the \ ``timeout``\  elapsed, or -%ERESTARTSYS if it was
interrupted by a kill signal.

Only kill signals interrupt this process.

.. _`wait_event_lock_irq_cmd`:

wait_event_lock_irq_cmd
=======================

.. c:function::  wait_event_lock_irq_cmd( wq_head,  condition,  lock,  cmd)

    sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  lock:
        a locked spinlock_t, which will be released before cmd
        and \ :c:func:`schedule`\  and reacquired afterwards.

    :param  cmd:
        a command which is invoked outside the critical section before
        sleep

.. _`wait_event_lock_irq_cmd.description`:

Description
-----------

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
\ ``condition``\  evaluates to true. The \ ``condition``\  is checked each time
the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before invoking the cmd and going to sleep and is reacquired
afterwards.

.. _`wait_event_lock_irq`:

wait_event_lock_irq
===================

.. c:function::  wait_event_lock_irq( wq_head,  condition,  lock)

    sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  lock:
        a locked spinlock_t, which will be released before \ :c:func:`schedule`\ 
        and reacquired afterwards.

.. _`wait_event_lock_irq.description`:

Description
-----------

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
\ ``condition``\  evaluates to true. The \ ``condition``\  is checked each time
the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before going to sleep and is reacquired afterwards.

.. _`wait_event_interruptible_lock_irq_cmd`:

wait_event_interruptible_lock_irq_cmd
=====================================

.. c:function::  wait_event_interruptible_lock_irq_cmd( wq_head,  condition,  lock,  cmd)

    sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  lock:
        a locked spinlock_t, which will be released before cmd and
        \ :c:func:`schedule`\  and reacquired afterwards.

    :param  cmd:
        a command which is invoked outside the critical section before
        sleep

.. _`wait_event_interruptible_lock_irq_cmd.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or a signal is received. The \ ``condition``\  is
checked each time the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before invoking the cmd and going to sleep and is reacquired
afterwards.

The macro will return -ERESTARTSYS if it was interrupted by a signal
and 0 if \ ``condition``\  evaluated to true.

.. _`wait_event_interruptible_lock_irq`:

wait_event_interruptible_lock_irq
=================================

.. c:function::  wait_event_interruptible_lock_irq( wq_head,  condition,  lock)

    sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

    :param  wq_head:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  lock:
        a locked spinlock_t, which will be released before \ :c:func:`schedule`\ 
        and reacquired afterwards.

.. _`wait_event_interruptible_lock_irq.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or signal is received. The \ ``condition``\  is
checked each time the waitqueue \ ``wq_head``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before going to sleep and is reacquired afterwards.

The macro will return -ERESTARTSYS if it was interrupted by a signal
and 0 if \ ``condition``\  evaluated to true.

.. This file was automatic generated / don't edit.

