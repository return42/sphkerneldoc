
.. _API-wait-event-killable:

===================
wait_event_killable
===================

*man wait_event_killable(9)*

*4.6.0-rc1*

sleep until a condition gets true


Synopsis
========

.. c:function:: wait_event_killable( wq, condition )

Arguments
=========

``wq``
    the waitqueue to wait on

``condition``
    a C expression for the event to wait for


Description
===========

The process is put to sleep (TASK_KILLABLE) until the ``condition`` evaluates to true or a signal is received. The ``condition`` is checked each time the waitqueue ``wq`` is woken
up.

``wake_up`` has to be called after changing any variable that could change the result of the wait condition.

The function will return -ERESTARTSYS if it was interrupted by a signal and 0 if ``condition`` evaluated to true.
