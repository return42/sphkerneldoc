.. -*- coding: utf-8; mode: rst -*-

.. _API-fence-wait-timeout:

==================
fence_wait_timeout
==================

*man fence_wait_timeout(9)*

*4.6.0-rc5*

sleep until the fence gets signaled or until timeout elapses


Synopsis
========

.. c:function:: signed long fence_wait_timeout( struct fence * fence, bool intr, signed long timeout )

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

Returns -ERESTARTSYS if interrupted, 0 if the wait timed out, or the
remaining timeout in jiffies on success. Other error values may be
returned on custom implementations.

Performs a synchronous wait on this fence. It is assumed the caller
directly or indirectly (buf-mgr between reservation and committing)
holds a reference to the fence, otherwise the fence might be freed
before return, resulting in undefined behavior.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
