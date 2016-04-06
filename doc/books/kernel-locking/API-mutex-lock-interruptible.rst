
.. _API-mutex-lock-interruptible:

========================
mutex_lock_interruptible
========================

*man mutex_lock_interruptible(9)*

*4.6.0-rc1*

acquire the mutex, interruptible


Synopsis
========

.. c:function:: int __sched mutex_lock_interruptible( struct mutex * lock )

Arguments
=========

``lock``
    the mutex to be acquired


Description
===========

Lock the mutex like ``mutex_lock``, and return 0 if the mutex has been acquired or sleep until the mutex becomes available. If a signal arrives while waiting for the lock then this
function returns -EINTR.

This function is similar to (but not equivalent to) ``down_interruptible``.
