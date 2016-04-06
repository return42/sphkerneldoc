
.. _API-wait-event-interruptible-hrtimeout:

==================================
wait_event_interruptible_hrtimeout
==================================

*man wait_event_interruptible_hrtimeout(9)*

*4.6.0-rc1*

sleep until a condition gets true or a timeout elapses


Synopsis
========

.. c:function:: wait_event_interruptible_hrtimeout( wq, condition, timeout )

Arguments
=========

``wq``
    the waitqueue to wait on

``condition``
    a C expression for the event to wait for

``timeout``
    timeout, as a ktime_t


Description
===========

The process is put to sleep (TASK_INTERRUPTIBLE) until the ``condition`` evaluates to true or a signal is received. The ``condition`` is checked each time the waitqueue ``wq`` is
woken up.

``wake_up`` has to be called after changing any variable that could change the result of the wait condition.

The function returns 0 if ``condition`` became true, -ERESTARTSYS if it was interrupted by a signal, or -ETIME if the timeout elapsed.
