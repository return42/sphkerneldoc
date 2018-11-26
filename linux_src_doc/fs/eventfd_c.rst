.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/eventfd.c

.. _`eventfd_signal`:

eventfd_signal
==============

.. c:function:: __u64 eventfd_signal(struct eventfd_ctx *ctx, __u64 n)

    Adds \ ``n``\  to the eventfd counter.

    :param ctx:
        [in] Pointer to the eventfd context.
    :type ctx: struct eventfd_ctx \*

    :param n:
        [in] Value of the counter to be added to the eventfd internal counter.
        The value cannot be negative.
    :type n: __u64

.. _`eventfd_signal.description`:

Description
-----------

This function is supposed to be called by the kernel in paths that do not
allow sleeping. In this function we allow the counter to reach the ULLONG_MAX
value, and we signal this as overflow condition by returning a EPOLLERR
to poll(2).

Returns the amount by which the counter was incremented.  This will be less
than \ ``n``\  if the counter has overflowed.

.. _`eventfd_ctx_put`:

eventfd_ctx_put
===============

.. c:function:: void eventfd_ctx_put(struct eventfd_ctx *ctx)

    Releases a reference to the internal eventfd context.

    :param ctx:
        [in] Pointer to eventfd context.
    :type ctx: struct eventfd_ctx \*

.. _`eventfd_ctx_put.description`:

Description
-----------

The eventfd context reference must have been previously acquired either
with \ :c:func:`eventfd_ctx_fdget`\  or \ :c:func:`eventfd_ctx_fileget`\ .

.. _`eventfd_ctx_remove_wait_queue`:

eventfd_ctx_remove_wait_queue
=============================

.. c:function:: int eventfd_ctx_remove_wait_queue(struct eventfd_ctx *ctx, wait_queue_entry_t *wait, __u64 *cnt)

    Read the current counter and removes wait queue.

    :param ctx:
        [in] Pointer to eventfd context.
    :type ctx: struct eventfd_ctx \*

    :param wait:
        [in] Wait queue to be removed.
    :type wait: wait_queue_entry_t \*

    :param cnt:
        [out] Pointer to the 64-bit counter value.
    :type cnt: __u64 \*

.. _`eventfd_ctx_remove_wait_queue.description`:

Description
-----------

Returns \ ``0``\  if successful, or the following error codes:

-EAGAIN      : The operation would have blocked.

This is used to atomically remove a wait queue entry from the eventfd wait
queue head, and read/reset the counter value.

.. _`eventfd_fget`:

eventfd_fget
============

.. c:function:: struct file *eventfd_fget(int fd)

    Acquire a reference of an eventfd file descriptor.

    :param fd:
        [in] Eventfd file descriptor.
    :type fd: int

.. _`eventfd_fget.description`:

Description
-----------

Returns a pointer to the eventfd file structure in case of success, or the

.. _`eventfd_fget.following-error-pointer`:

following error pointer
-----------------------


-EBADF    : Invalid \ ``fd``\  file descriptor.
-EINVAL   : The \ ``fd``\  file descriptor is not an eventfd file.

.. _`eventfd_ctx_fdget`:

eventfd_ctx_fdget
=================

.. c:function:: struct eventfd_ctx *eventfd_ctx_fdget(int fd)

    Acquires a reference to the internal eventfd context.

    :param fd:
        [in] Eventfd file descriptor.
    :type fd: int

.. _`eventfd_ctx_fdget.description`:

Description
-----------

Returns a pointer to the internal eventfd context, otherwise the error

.. _`eventfd_ctx_fdget.pointers-returned-by-the-following-functions`:

pointers returned by the following functions
--------------------------------------------


eventfd_fget

.. _`eventfd_ctx_fileget`:

eventfd_ctx_fileget
===================

.. c:function:: struct eventfd_ctx *eventfd_ctx_fileget(struct file *file)

    Acquires a reference to the internal eventfd context.

    :param file:
        [in] Eventfd file pointer.
    :type file: struct file \*

.. _`eventfd_ctx_fileget.description`:

Description
-----------

Returns a pointer to the internal eventfd context, otherwise the error

.. _`eventfd_ctx_fileget.pointer`:

pointer
-------


-EINVAL   : The \ ``fd``\  file descriptor is not an eventfd file.

.. This file was automatic generated / don't edit.

