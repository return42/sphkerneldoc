
.. _API-eventfd-ctx-read:

================
eventfd_ctx_read
================

*man eventfd_ctx_read(9)*

*4.6.0-rc1*

Reads the eventfd counter or wait if it is zero.


Synopsis
========

.. c:function:: ssize_t eventfd_ctx_read( struct eventfd_ctx * ctx, int no_wait, __u64 * cnt )

Arguments
=========

``ctx``
    [in] Pointer to eventfd context.

``no_wait``
    [in] Different from zero if the operation should not block.

``cnt``
    [out] Pointer to the 64-bit counter value.


Description
===========

Returns ``0`` if successful, or the following error codes:

-EAGAIN : The operation would have blocked but ``no_wait`` was non-zero. -ERESTARTSYS : A signal interrupted the wait operation.

If ``no_wait`` is zero, the function might sleep until the eventfd internal counter becomes greater than zero.
