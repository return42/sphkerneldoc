
.. _API-wait-event-timeout:

==================
wait_event_timeout
==================

*man wait_event_timeout(9)*

*4.6.0-rc1*

sleep until a condition gets true or a timeout elapses


Synopsis
========

.. c:function:: wait_event_timeout( wq, condition, timeout )

Arguments
=========

``wq``
    the waitqueue to wait on

``condition``
    a C expression for the event to wait for

``timeout``
    timeout, in jiffies


Description
===========

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the ``condition`` evaluates to true. The ``condition`` is checked each time the waitqueue ``wq`` is woken up.

``wake_up`` has to be called after changing any variable that could change the result of the wait condition.


Returns
=======

0 if the ``condition`` evaluated to ``false`` after the ``timeout`` elapsed, 1 if the ``condition`` evaluated to ``true`` after the ``timeout`` elapsed, or the remaining jiffies
(at least 1) if the ``condition`` evaluated to ``true`` before the ``timeout`` elapsed.
