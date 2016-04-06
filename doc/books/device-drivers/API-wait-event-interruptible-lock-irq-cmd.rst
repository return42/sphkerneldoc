
.. _API-wait-event-interruptible-lock-irq-cmd:

=====================================
wait_event_interruptible_lock_irq_cmd
=====================================

*man wait_event_interruptible_lock_irq_cmd(9)*

*4.6.0-rc1*

sleep until a condition gets true. The condition is checked under the lock. This is expected to be called with the lock taken.


Synopsis
========

.. c:function:: wait_event_interruptible_lock_irq_cmd( wq, condition, lock, cmd )

Arguments
=========

``wq``
    the waitqueue to wait on

``condition``
    a C expression for the event to wait for

``lock``
    a locked spinlock_t, which will be released before cmd and ``schedule`` and reacquired afterwards.

``cmd``
    a command which is invoked outside the critical section before sleep


Description
===========

The process is put to sleep (TASK_INTERRUPTIBLE) until the ``condition`` evaluates to true or a signal is received. The ``condition`` is checked each time the waitqueue ``wq`` is
woken up.

``wake_up`` has to be called after changing any variable that could change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is dropped before invoking the cmd and going to sleep and is reacquired afterwards.

The macro will return -ERESTARTSYS if it was interrupted by a signal and 0 if ``condition`` evaluated to true.
