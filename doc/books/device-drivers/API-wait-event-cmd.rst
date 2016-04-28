.. -*- coding: utf-8; mode: rst -*-

.. _API-wait-event-cmd:

==============
wait_event_cmd
==============

*man wait_event_cmd(9)*

*4.6.0-rc5*

sleep until a condition gets true


Synopsis
========

.. c:function:: wait_event_cmd( wq, condition, cmd1, cmd2 )

Arguments
=========

``wq``
    the waitqueue to wait on

``condition``
    a C expression for the event to wait for

``cmd1``
    the command will be executed before sleep

``cmd2``
    the command will be executed after sleep


Description
===========

The process is put to sleep (TASK_UNINTERRUPTIBLE) until the
``condition`` evaluates to true. The ``condition`` is checked each time
the waitqueue ``wq`` is woken up.

``wake_up`` has to be called after changing any variable that could
change the result of the wait condition.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
