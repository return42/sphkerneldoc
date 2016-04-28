.. -*- coding: utf-8; mode: rst -*-

.. _API-abort-exclusive-wait:

====================
abort_exclusive_wait
====================

*man abort_exclusive_wait(9)*

*4.6.0-rc5*

abort exclusive waiting in a queue


Synopsis
========

.. c:function:: void abort_exclusive_wait( wait_queue_head_t * q, wait_queue_t * wait, unsigned int mode, void * key )

Arguments
=========

``q``
    waitqueue waited on

``wait``
    wait descriptor

``mode``
    runstate of the waiter to be woken

``key``
    key to identify a wait bit queue or ``NULL``


Description
===========

Sets current thread back to running state and removes the wait
descriptor from the given waitqueue if still queued.

Wakes up the next waiter if the caller is concurrently woken up through
the queue.

This prevents waiter starvation where an exclusive waiter aborts and is
woken up concurrently and no one wakes up the next waiter.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
