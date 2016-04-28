.. -*- coding: utf-8; mode: rst -*-

.. _API-flush-scheduled-work:

====================
flush_scheduled_work
====================

*man flush_scheduled_work(9)*

*4.6.0-rc5*

ensure that any scheduled work has run to completion.


Synopsis
========

.. c:function:: void flush_scheduled_work( void )

Arguments
=========

``void``
    no arguments


Description
===========

Forces execution of the kernel-global workqueue and blocks until its
completion.

Think twice before calling this function! It's very easy to get into
trouble if you don't take great care. Either of the following situations


will lead to deadlock
=====================

One of the work items currently on the workqueue needs to acquire a lock
held by your code or its caller.

Your code is running in the context of a work routine.

They will be detected by lockdep when they occur, but the first might
not occur very often. It depends on what work items are on the workqueue
and what locks they need, which you have no control over.

In most situations flushing the entire workqueue is overkill; you merely
need to know that a particular work item isn't queued and isn't running.
In such cases you should use ``cancel_delayed_work_sync`` or
``cancel_work_sync`` instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
