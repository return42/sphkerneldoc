.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-event-timeout:

==================
wait_event_timeout
==================

*man wait_event_timeout(9)*

*4.6.0-rc5*

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

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
``condition`` evaluates to true. The ``condition`` is checked each time
the waitqueue ``wq`` is woken up.

``wake_up`` has to be called after changing any variable that could
change the result of the wait condition.


Returns
=======

0 if the ``condition`` evaluated to ``false`` after the ``timeout``
elapsed, 1 if the ``condition`` evaluated to ``true`` after the
``timeout`` elapsed, or the remaining jiffies (at least 1) if the
``condition`` evaluated to ``true`` before the ``timeout`` elapsed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
