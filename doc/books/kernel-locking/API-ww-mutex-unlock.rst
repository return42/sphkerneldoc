
.. _API-ww-mutex-unlock:

===============
ww_mutex_unlock
===============

*man ww_mutex_unlock(9)*

*4.6.0-rc1*

release the w/w mutex


Synopsis
========

.. c:function:: void __sched ww_mutex_unlock( struct ww_mutex * lock )

Arguments
=========

``lock``
    the mutex to be released


Description
===========

Unlock a mutex that has been locked by this task previously with any of the ww_mutex_lock⋆ functions (with or without an acquire context). It is forbidden to release the locks
after releasing the acquire context.

This function must not be used in interrupt context. Unlocking of a unlocked mutex is not allowed.
