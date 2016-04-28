.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-event-lock-irq-cmd:

=======================
wait_event_lock_irq_cmd
=======================

*man wait_event_lock_irq_cmd(9)*

*4.6.0-rc5*

sleep until a condition gets true. The condition is checked under the
lock. This is expected to be called with the lock taken.


Synopsis
========

.. c:function:: wait_event_lock_irq_cmd( wq, condition, lock, cmd )

Arguments
=========

``wq``
    the waitqueue to wait on

``condition``
    a C expression for the event to wait for

``lock``
    a locked spinlock_t, which will be released before cmd and
    ``schedule`` and reacquired afterwards.

``cmd``
    a command which is invoked outside the critical section before sleep


Description
===========

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
``condition`` evaluates to true. The ``condition`` is checked each time
the waitqueue ``wq`` is woken up.

``wake_up`` has to be called after changing any variable that could
change the result of the wait condition.

This is supposed to be called while holding the lock. The lock is
dropped before invoking the cmd and going to sleep and is reacquired
afterwards.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
