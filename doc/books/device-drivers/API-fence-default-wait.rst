
.. _API-fence-default-wait:

==================
fence_default_wait
==================

*man fence_default_wait(9)*

*4.6.0-rc1*

default sleep until the fence gets signaled or until timeout elapses


Synopsis
========

.. c:function:: signed long fence_default_wait( struct fence * fence, bool intr, signed long timeout )

Arguments
=========

``fence``
    [in] the fence to wait on

``intr``
    [in] if true, do an interruptible wait

``timeout``
    [in] timeout value in jiffies, or MAX_SCHEDULE_TIMEOUT


Description
===========

Returns -ERESTARTSYS if interrupted, 0 if the wait timed out, or the remaining timeout in jiffies on success.
