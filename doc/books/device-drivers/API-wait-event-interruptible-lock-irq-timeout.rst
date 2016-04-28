.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-event-interruptible-lock-irq-timeout:

=========================================
wait_event_interruptible_lock_irq_timeout
=========================================

*man wait_event_interruptible_lock_irq_timeout(9)*

*4.6.0-rc5*

sleep until a condition gets true or a timeout elapses. The condition is
checked under the lock. This is expected to be called with the lock
taken.


Synopsis
========

.. c:function:: wait_event_interruptible_lock_irq_timeout( wq, condition, lock, timeout )

Arguments
=========

``wq``
    the waitqueue to wait on

``condition``
    a C expression for the event to wait for

``lock``
    a locked spinlock_t, which will be released before ``schedule`` and
    reacquired afterwards.

``timeout``
    timeout, in jiffies


Description
===========

The process is put to sleep (TASK_INTERRUPTIBLE) until the
``condition`` evaluates to true or signal is received. The ``condition``
is checked each time the waitqueue ``wq`` is woken up.

``wake_up`` has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before going to sleep and is reacquired afterwards.

The function returns 0 if the ``timeout`` elapsed, -ERESTARTSYS if it
was interrupted by a signal, and the remaining jiffies otherwise if the
condition evaluated to true before the timeout elapsed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
