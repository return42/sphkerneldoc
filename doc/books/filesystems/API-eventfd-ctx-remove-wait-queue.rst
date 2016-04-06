
.. _API-eventfd-ctx-remove-wait-queue:

=============================
eventfd_ctx_remove_wait_queue
=============================

*man eventfd_ctx_remove_wait_queue(9)*

*4.6.0-rc1*

Read the current counter and removes wait queue.


Synopsis
========

.. c:function:: int eventfd_ctx_remove_wait_queue( struct eventfd_ctx * ctx, wait_queue_t * wait, __u64 * cnt )

Arguments
=========

``ctx``
    [in] Pointer to eventfd context.

``wait``
    [in] Wait queue to be removed.

``cnt``
    [out] Pointer to the 64-bit counter value.


Description
===========

Returns ``0`` if successful, or the following error codes:

-EAGAIN : The operation would have blocked.

This is used to atomically remove a wait queue entry from the eventfd wait queue head, and read/reset the counter value.
