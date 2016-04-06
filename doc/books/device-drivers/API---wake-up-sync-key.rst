
.. _API---wake-up-sync-key:

==================
__wake_up_sync_key
==================

*man __wake_up_sync_key(9)*

*4.6.0-rc1*

wake up threads blocked on a waitqueue.


Synopsis
========

.. c:function:: void __wake_up_sync_key( wait_queue_head_t * q, unsigned int mode, int nr_exclusive, void * key )

Arguments
=========

``q``
    the waitqueue

``mode``
    which threads

``nr_exclusive``
    how many wake-one or wake-many threads to wake up

``key``
    opaque value to be passed to wakeup targets


Description
===========

The sync wakeup differs that the waker knows that it will schedule away soon, so while the target thread will be woken up, it will not be migrated to another CPU - ie. the two
threads are 'synchronized' with each other. This can prevent needless bouncing between CPUs.

On UP it can prevent extra preemption.

It may be assumed that this function implies a write memory barrier before changing the task state if and only if any tasks are woken up.
