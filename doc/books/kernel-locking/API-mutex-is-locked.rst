
.. _API-mutex-is-locked:

===============
mutex_is_locked
===============

*man mutex_is_locked(9)*

*4.6.0-rc1*

is the mutex locked


Synopsis
========

.. c:function:: int mutex_is_locked( struct mutex * lock )

Arguments
=========

``lock``
    the mutex to be queried


Description
===========

Returns 1 if the mutex is locked, 0 if unlocked.
