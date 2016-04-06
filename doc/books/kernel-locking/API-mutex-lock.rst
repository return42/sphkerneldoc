
.. _API-mutex-lock:

==========
mutex_lock
==========

*man mutex_lock(9)*

*4.6.0-rc1*

acquire the mutex


Synopsis
========

.. c:function:: void __sched mutex_lock( struct mutex * lock )

Arguments
=========

``lock``
    the mutex to be acquired


Description
===========

Lock the mutex exclusively for this task. If the mutex is not available right now, it will sleep until it can get it.

The mutex must later on be released by the same task that acquired it. Recursive locking is not allowed. The task may not exit without first unlocking the mutex. Also, kernel
memory where the mutex resides must not be freed with the mutex still locked. The mutex must first be initialized (or statically defined) before it can be locked. ``memset``-ing
the mutex to 0 is not allowed.

( The CONFIG_DEBUG_MUTEXES .config option turns on debugging checks that will enforce the restrictions and will also do deadlock debugging. )

This function is similar to (but not equivalent to) ``down``.
