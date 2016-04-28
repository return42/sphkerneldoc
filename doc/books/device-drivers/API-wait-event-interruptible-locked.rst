.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-event-interruptible-locked:

===============================
wait_event_interruptible_locked
===============================

*man wait_event_interruptible_locked(9)*

*4.6.0-rc5*

sleep until a condition gets true


Synopsis
========

.. c:function:: wait_event_interruptible_locked( wq, condition )

Arguments
=========

``wq``
    the waitqueue to wait on

``condition``
    a C expression for the event to wait for


Description
===========

The process is put to sleep (TASK_INTERRUPTIBLE) until the
``condition`` evaluates to true or a signal is received. The
``condition`` is checked each time the waitqueue ``wq`` is woken up.

It must be called with wq.lock being held. This spinlock is unlocked
while sleeping but ``condition`` testing is done while lock is held and
when this macro exits the lock is held.

The lock is locked/unlocked using ``spin_lock``/``spin_unlock``
functions which must match the way they are locked/unlocked outside of
this macro.

``wake_up_locked`` has to be called after changing any variable that
could change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a signal
and 0 if ``condition`` evaluated to true.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
