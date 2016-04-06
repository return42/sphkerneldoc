
.. _API-mutex-trylock:

=============
mutex_trylock
=============

*man mutex_trylock(9)*

*4.6.0-rc1*

try to acquire the mutex, without waiting


Synopsis
========

.. c:function:: int __sched mutex_trylock( struct mutex * lock )

Arguments
=========

``lock``
    the mutex to be acquired


Description
===========

Try to acquire the mutex atomically. Returns 1 if the mutex has been acquired successfully, and 0 on contention.


NOTE
====

this function follows the ``spin_trylock`` convention, so it is negated from the ``down_trylock`` return values! Be careful about this when converting semaphore users to mutexes.

This function must not be used in interrupt context. The mutex must be released by the same task that acquired it.
