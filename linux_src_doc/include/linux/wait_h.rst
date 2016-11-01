.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/wait.h

.. _`waitqueue_active`:

waitqueue_active
================

.. c:function:: int waitqueue_active(wait_queue_head_t *q)

    - locklessly test for waiters on the queue

    :param wait_queue_head_t \*q:
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

Use either while holding wait_queue_head_t::lock or when used for wakeups
with an extra \ :c:func:`smp_mb`\  like:

     CPU0 - waker                    CPU1 - waiter

                                     for (;;) {
     \ ``cond``\  = true;                     prepare_to_wait(&wq, \ :c:type:`struct wait <wait>`\ , state);
     \ :c:func:`smp_mb`\ ;                         // \ :c:func:`smp_mb`\  from \ :c:func:`set_current_state`\ 
     if (waitqueue_active(wq))         if (@cond)
       wake_up(wq);                      break;
                                       \ :c:func:`schedule`\ ;
                                     }
                                     finish_wait(&wq, \ :c:type:`struct wait <wait>`\ );

Because without the explicit \ :c:func:`smp_mb`\  it's possible for the
\ :c:func:`waitqueue_active`\  load to get hoisted over the \ ``cond``\  store such that we'll
observe an empty wait list while the waiter might not observe \ ``cond``\ .

Also note that this 'optimization' trades a \ :c:func:`spin_lock`\  for an \ :c:func:`smp_mb`\ ,
which (when the lock is uncontended) are of roughly equal cost.

.. _`wq_has_sleeper`:

wq_has_sleeper
==============

.. c:function:: bool wq_has_sleeper(wait_queue_head_t *wq)

    check if there are any waiting processes

    :param wait_queue_head_t \*wq:
        wait queue head

.. _`wq_has_sleeper.description`:

Description
-----------

Returns true if wq has waiting processes

Please refer to the comment for waitqueue_active.

.. _`wait_event`:

wait_event
==========

.. c:function::  wait_event( wq,  condition)

    sleep until a condition gets true

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event.description`:

Description
-----------

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
\ ``condition``\  evaluates to true. The \ ``condition``\  is checked each time
the waitqueue \ ``wq``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_freezable`:

wait_event_freezable
====================

.. c:function::  wait_event_freezable( wq,  condition)

    sleep (or freeze) until a condition gets true

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_freezable.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE -- so as not to contribute
to system load) until the \ ``condition``\  evaluates to true. The
\ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_timeout`:

wait_event_timeout
==================

.. c:function::  wait_event_timeout( wq,  condition,  timeout)

    sleep until a condition gets true or a timeout elapses

    :param  wq:
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
the waitqueue \ ``wq``\  is woken up.

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

.. c:function::  wait_event_cmd( wq,  condition,  cmd1,  cmd2)

    sleep until a condition gets true

    :param  wq:
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
the waitqueue \ ``wq``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

.. _`wait_event_interruptible`:

wait_event_interruptible
========================

.. c:function::  wait_event_interruptible( wq,  condition)

    sleep until a condition gets true

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_interruptible.description`:

Description
-----------

The process is put to sleep (TASK_INTERRUPTIBLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if \ ``condition``\  evaluated to true.

.. _`wait_event_interruptible_timeout`:

wait_event_interruptible_timeout
================================

.. c:function::  wait_event_interruptible_timeout( wq,  condition,  timeout)

    sleep until a condition gets true or a timeout elapses

    :param  wq:
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
The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

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

.. c:function::  wait_event_hrtimeout( wq,  condition,  timeout)

    sleep until a condition gets true or a timeout elapses

    :param  wq:
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
The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

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

.. c:function::  wait_event_killable( wq,  condition)

    sleep until a condition gets true

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`wait_event_killable.description`:

Description
-----------

The process is put to sleep (TASK_KILLABLE) until the
\ ``condition``\  evaluates to true or a signal is received.
The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a
signal and 0 if \ ``condition``\  evaluated to true.

.. _`wait_event_lock_irq_cmd`:

wait_event_lock_irq_cmd
=======================

.. c:function::  wait_event_lock_irq_cmd( wq,  condition,  lock,  cmd)

    sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

    :param  wq:
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
the waitqueue \ ``wq``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before invoking the cmd and going to sleep and is reacquired
afterwards.

.. _`wait_event_lock_irq`:

wait_event_lock_irq
===================

.. c:function::  wait_event_lock_irq( wq,  condition,  lock)

    sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

    :param  wq:
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
the waitqueue \ ``wq``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before going to sleep and is reacquired afterwards.

.. _`wait_event_interruptible_lock_irq_cmd`:

wait_event_interruptible_lock_irq_cmd
=====================================

.. c:function::  wait_event_interruptible_lock_irq_cmd( wq,  condition,  lock,  cmd)

    sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

    :param  wq:
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
checked each time the waitqueue \ ``wq``\  is woken up.

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

.. c:function::  wait_event_interruptible_lock_irq( wq,  condition,  lock)

    sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.

    :param  wq:
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
checked each time the waitqueue \ ``wq``\  is woken up.

\ :c:func:`wake_up`\  has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before going to sleep and is reacquired afterwards.

The macro will return -ERESTARTSYS if it was interrupted by a signal
and 0 if \ ``condition``\  evaluated to true.

.. _`wait_on_bit`:

wait_on_bit
===========

.. c:function:: int wait_on_bit(unsigned long *word, int bit, unsigned mode)

    wait for a bit to be cleared

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit.description`:

Description
-----------

There is a standard hashed waitqueue table for generic use. This
is the part of the hashtable's accessor API that waits on a bit.
For instance, if one were to have waiters on a bitflag, one would
call \ :c:func:`wait_on_bit`\  in threads waiting for the bit to clear.
One uses \ :c:func:`wait_on_bit`\  where one is waiting for the bit to clear,
but has no intention of setting it.
Returned value will be zero if the bit was cleared, or non-zero
if the process received a signal and the mode permitted wakeup
on that signal.

.. _`wait_on_bit_io`:

wait_on_bit_io
==============

.. c:function:: int wait_on_bit_io(unsigned long *word, int bit, unsigned mode)

    wait for a bit to be cleared

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit_io.description`:

Description
-----------

Use the standard hashed waitqueue table to wait for a bit
to be cleared.  This is similar to \ :c:func:`wait_on_bit`\ , but calls
\ :c:func:`io_schedule`\  instead of \ :c:func:`schedule`\  for the actual waiting.

Returned value will be zero if the bit was cleared, or non-zero
if the process received a signal and the mode permitted wakeup
on that signal.

.. _`wait_on_bit_timeout`:

wait_on_bit_timeout
===================

.. c:function:: int wait_on_bit_timeout(unsigned long *word, int bit, unsigned mode, unsigned long timeout)

    wait for a bit to be cleared or a timeout elapses

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param unsigned mode:
        the task state to sleep in

    :param unsigned long timeout:
        timeout, in jiffies

.. _`wait_on_bit_timeout.description`:

Description
-----------

Use the standard hashed waitqueue table to wait for a bit
to be cleared. This is similar to \ :c:func:`wait_on_bit`\ , except also takes a
timeout parameter.

Returned value will be zero if the bit was cleared before the
\ ``timeout``\  elapsed, or non-zero if the \ ``timeout``\  elapsed or process
received a signal and the mode permitted wakeup on that signal.

.. _`wait_on_bit_action`:

wait_on_bit_action
==================

.. c:function:: int wait_on_bit_action(unsigned long *word, int bit, wait_bit_action_f *action, unsigned mode)

    wait for a bit to be cleared

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param wait_bit_action_f \*action:
        the function used to sleep, which may take special actions

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit_action.description`:

Description
-----------

Use the standard hashed waitqueue table to wait for a bit
to be cleared, and allow the waiting action to be specified.
This is like \ :c:func:`wait_on_bit`\  but allows fine control of how the waiting
is done.

Returned value will be zero if the bit was cleared, or non-zero
if the process received a signal and the mode permitted wakeup
on that signal.

.. _`wait_on_bit_lock`:

wait_on_bit_lock
================

.. c:function:: int wait_on_bit_lock(unsigned long *word, int bit, unsigned mode)

    wait for a bit to be cleared, when wanting to set it

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit_lock.description`:

Description
-----------

There is a standard hashed waitqueue table for generic use. This
is the part of the hashtable's accessor API that waits on a bit
when one intends to set it, for instance, trying to lock bitflags.
For instance, if one were to have waiters trying to set bitflag
and waiting for it to clear before setting it, one would call
\ :c:func:`wait_on_bit`\  in threads waiting to be able to set the bit.
One uses \ :c:func:`wait_on_bit_lock`\  where one is waiting for the bit to
clear with the intention of setting it, and when done, clearing it.

Returns zero if the bit was (eventually) found to be clear and was
set.  Returns non-zero if a signal was delivered to the process and
the \ ``mode``\  allows that signal to wake the process.

.. _`wait_on_bit_lock_io`:

wait_on_bit_lock_io
===================

.. c:function:: int wait_on_bit_lock_io(unsigned long *word, int bit, unsigned mode)

    wait for a bit to be cleared, when wanting to set it

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit_lock_io.description`:

Description
-----------

Use the standard hashed waitqueue table to wait for a bit
to be cleared and then to atomically set it.  This is similar
to \ :c:func:`wait_on_bit`\ , but calls \ :c:func:`io_schedule`\  instead of \ :c:func:`schedule`\ 
for the actual waiting.

Returns zero if the bit was (eventually) found to be clear and was
set.  Returns non-zero if a signal was delivered to the process and
the \ ``mode``\  allows that signal to wake the process.

.. _`wait_on_bit_lock_action`:

wait_on_bit_lock_action
=======================

.. c:function:: int wait_on_bit_lock_action(unsigned long *word, int bit, wait_bit_action_f *action, unsigned mode)

    wait for a bit to be cleared, when wanting to set it

    :param unsigned long \*word:
        the word being waited on, a kernel virtual address

    :param int bit:
        the bit of the word being waited on

    :param wait_bit_action_f \*action:
        the function used to sleep, which may take special actions

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_bit_lock_action.description`:

Description
-----------

Use the standard hashed waitqueue table to wait for a bit
to be cleared and then to set it, and allow the waiting action
to be specified.
This is like \ :c:func:`wait_on_bit`\  but allows fine control of how the waiting
is done.

Returns zero if the bit was (eventually) found to be clear and was
set.  Returns non-zero if a signal was delivered to the process and
the \ ``mode``\  allows that signal to wake the process.

.. _`wait_on_atomic_t`:

wait_on_atomic_t
================

.. c:function:: int wait_on_atomic_t(atomic_t *val, int (*action)(atomic_t *), unsigned mode)

    Wait for an atomic_t to become 0

    :param atomic_t \*val:
        The atomic value being waited on, a kernel virtual address

    :param int (\*action)(atomic_t \*):
        the function used to sleep, which may take special actions

    :param unsigned mode:
        the task state to sleep in

.. _`wait_on_atomic_t.description`:

Description
-----------

Wait for an atomic_t to become 0.  We abuse the bit-wait waitqueue table for
the purpose of getting a waitqueue, but we set the key to a bit number
outside of the target 'word'.

.. This file was automatic generated / don't edit.

