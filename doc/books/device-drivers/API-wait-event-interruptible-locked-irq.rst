
.. _API-wait-event-interruptible-locked-irq:

===================================
wait_event_interruptible_locked_irq
===================================

*man wait_event_interruptible_locked_irq(9)*

*4.6.0-rc1*

sleep until a condition gets true


Synopsis
========

.. c:function:: wait_event_interruptible_locked_irq( wq, condition )

Arguments
=========

``wq``
    the waitqueue to wait on

``condition``
    a C expression for the event to wait for


Description
===========

The process is put to sleep (TASK_INTERRUPTIBLE) until the ``condition`` evaluates to true or a signal is received. The ``condition`` is checked each time the waitqueue ``wq`` is
woken up.

It must be called with wq.lock being held. This spinlock is unlocked while sleeping but ``condition`` testing is done while lock is held and when this macro exits the lock is held.

The lock is locked/unlocked using ``spin_lock_irq``/``spin_unlock_irq`` functions which must match the way they are locked/unlocked outside of this macro.

``wake_up_locked`` has to be called after changing any variable that could change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a signal and 0 if ``condition`` evaluated to true.
