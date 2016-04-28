.. -*- coding: utf-8; mode: rst -*-

.. _API-waitqueue-active:

================
waitqueue_active
================

*man waitqueue_active(9)*

*4.6.0-rc5*

- locklessly test for waiters on the queue


Synopsis
========

.. c:function:: int waitqueue_active( wait_queue_head_t * q )

Arguments
=========

``q``
    the waitqueue to test for waiters


Description
===========

returns true if the wait list is not empty


NOTE
====

this function is lockless and requires care, incorrect usage _will_
lead to sporadic and non-obvious failure.


Use either while holding wait_queue_head_t
==========================================

:lock or when used for wakeups with an extra ``smp_mb`` like:

CPU0 - waker CPU1 - waiter

for (;;) { ``cond`` = true; prepare_to_wait( ``wq``, ``wait``,
state); ``smp_mb``; // ``smp_mb`` from ``set_current_state`` if
(waitqueue_active(wq)) if (``cond``) wake_up(wq); break; ``schedule``;
} finish_wait( ``wq``, ``wait``);

Because without the explicit ``smp_mb`` it's possible for the
``waitqueue_active`` load to get hoisted over the ``cond`` store such
that we'll observe an empty wait list while the waiter might not observe
``cond``.

Also note that this 'optimization' trades a ``spin_lock`` for an
``smp_mb``, which (when the lock is uncontended) are of roughly equal
cost.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
