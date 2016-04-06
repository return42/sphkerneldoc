
.. _API---wake-up:

=========
__wake_up
=========

*man __wake_up(9)*

*4.6.0-rc1*

wake up threads blocked on a waitqueue.


Synopsis
========

.. c:function:: void __wake_up( wait_queue_head_t * q, unsigned int mode, int nr_exclusive, void * key )

Arguments
=========

``q``
    the waitqueue

``mode``
    which threads

``nr_exclusive``
    how many wake-one or wake-many threads to wake up

``key``
    is directly passed to the wakeup function


Description
===========

It may be assumed that this function implies a write memory barrier before changing the task state if and only if any tasks are woken up.
