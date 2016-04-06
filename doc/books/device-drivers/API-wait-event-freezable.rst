
.. _API-wait-event-freezable:

====================
wait_event_freezable
====================

*man wait_event_freezable(9)*

*4.6.0-rc1*

sleep (or freeze) until a condition gets true


Synopsis
========

.. c:function:: wait_event_freezable( wq, condition )

Arguments
=========

``wq``
    the waitqueue to wait on

``condition``
    a C expression for the event to wait for


Description
===========

The process is put to sleep (TASK_INTERRUPTIBLE -- so as not to contribute to system load) until the ``condition`` evaluates to true. The ``condition`` is checked each time the
waitqueue ``wq`` is woken up.

``wake_up`` has to be called after changing any variable that could change the result of the wait condition.
