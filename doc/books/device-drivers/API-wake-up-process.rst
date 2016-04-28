.. -*- coding: utf-8; mode: rst -*-

.. _API-wake-up-process:

===============
wake_up_process
===============

*man wake_up_process(9)*

*4.6.0-rc5*

Wake up a specific process


Synopsis
========

.. c:function:: int wake_up_process( struct task_struct * p )

Arguments
=========

``p``
    The process to be woken up.


Description
===========

Attempt to wake up the nominated process and move it to the set of
runnable processes.


Return
======

1 if the process was woken up, 0 if it was already running.

It may be assumed that this function implies a write memory barrier
before changing the task state if and only if any tasks are woken up.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
