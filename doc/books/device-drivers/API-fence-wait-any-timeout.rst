
.. _API-fence-wait-any-timeout:

======================
fence_wait_any_timeout
======================

*man fence_wait_any_timeout(9)*

*4.6.0-rc1*

sleep until any fence gets signaled or until timeout elapses


Synopsis
========

.. c:function:: signed long fence_wait_any_timeout( struct fence ** fences, uint32_t count, bool intr, signed long timeout )

Arguments
=========

``fences``
    [in] array of fences to wait on

``count``
    [in] number of fences to wait on

``intr``
    [in] if true, do an interruptible wait

``timeout``
    [in] timeout value in jiffies, or MAX_SCHEDULE_TIMEOUT


Description
===========

Returns -EINVAL on custom fence wait implementation, -ERESTARTSYS if interrupted, 0 if the wait timed out, or the remaining timeout in jiffies on success.

Synchronous waits for the first fence in the array to be signaled. The caller needs to hold a reference to all fences in the array, otherwise a fence might be freed before return,
resulting in undefined behavior.
