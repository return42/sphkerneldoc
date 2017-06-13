.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/eventfd.c

.. _`eventfd_signal`:

eventfd_signal
==============

.. c:function:: __u64 eventfd_signal(struct eventfd_ctx *ctx, __u64 n)

    Adds \ ``n``\  to the eventfd counter.

    :param struct eventfd_ctx \*ctx:
        [in] Pointer to the eventfd context.

    :param __u64 n:
        [in] Value of the counter to be added to the eventfd internal counter.
        The value cannot be negative.

.. _`eventfd_signal.description`:

Description
-----------

This function is supposed to be called by the kernel in paths that do not
allow sleeping. In this function we allow the counter to reach the ULLONG_MAX
value, and we signal this as overflow condition by returning a POLLERR
to poll(2).

Returns the amount by which the counter was incremented.  This will be less
than \ ``n``\  if the counter has overflowed.

.. _`eventfd_ctx_get`:

eventfd_ctx_get
===============

.. c:function:: struct eventfd_ctx *eventfd_ctx_get(struct eventfd_ctx *ctx)

    Acquires a reference to the internal eventfd context.

    :param struct eventfd_ctx \*ctx:
        [in] Pointer to the eventfd context.

.. _`eventfd_ctx_get.return`:

Return
------

In case of success, returns a pointer to the eventfd context.

.. _`eventfd_ctx_put`:

eventfd_ctx_put
===============

.. c:function:: void eventfd_ctx_put(struct eventfd_ctx *ctx)

    Releases a reference to the internal eventfd context.

    :param struct eventfd_ctx \*ctx:
        [in] Pointer to eventfd context.

.. _`eventfd_ctx_put.description`:

Description
-----------

The eventfd context reference must have been previously acquired either
with \ :c:func:`eventfd_ctx_get`\  or \ :c:func:`eventfd_ctx_fdget`\ .

.. _`eventfd_ctx_remove_wait_queue`:

eventfd_ctx_remove_wait_queue
=============================

.. c:function:: int eventfd_ctx_remove_wait_queue(struct eventfd_ctx *ctx, wait_queue_t *wait, __u64 *cnt)

    Read the current counter and removes wait queue.

    :param struct eventfd_ctx \*ctx:
        [in] Pointer to eventfd context.

    :param wait_queue_t \*wait:
        [in] Wait queue to be removed.

    :param __u64 \*cnt:
        [out] Pointer to the 64-bit counter value.

.. _`eventfd_ctx_remove_wait_queue.description`:

Description
-----------

Returns \ ``0``\  if successful, or the following error codes:

-EAGAIN      : The operation would have blocked.

This is used to atomically remove a wait queue entry from the eventfd wait
queue head, and read/reset the counter value.

.. _`eventfd_ctx_read`:

eventfd_ctx_read
================

.. c:function:: ssize_t eventfd_ctx_read(struct eventfd_ctx *ctx, int no_wait, __u64 *cnt)

    Reads the eventfd counter or wait if it is zero.

    :param struct eventfd_ctx \*ctx:
        [in] Pointer to eventfd context.

    :param int no_wait:
        [in] Different from zero if the operation should not block.

    :param __u64 \*cnt:
        [out] Pointer to the 64-bit counter value.

.. _`eventfd_ctx_read.description`:

Description
-----------

Returns \ ``0``\  if successful, or the following error codes:

 - -EAGAIN      : The operation would have blocked but \ ``no_wait``\  was non-zero.
 - -ERESTARTSYS : A signal interrupted the wait operation.

If \ ``no_wait``\  is zero, the function might sleep until the eventfd internal
counter becomes greater than zero.

.. _`eventfd_fget`:

eventfd_fget
============

.. c:function:: struct file *eventfd_fget(int fd)

    Acquire a reference of an eventfd file descriptor.

    :param int fd:
        [in] Eventfd file descriptor.

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

    :param int fd:
        [in] Eventfd file descriptor.

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

    :param struct file \*file:
        [in] Eventfd file pointer.

.. _`eventfd_ctx_fileget.description`:

Description
-----------

Returns a pointer to the internal eventfd context, otherwise the error

.. _`eventfd_ctx_fileget.pointer`:

pointer
-------


-EINVAL   : The \ ``fd``\  file descriptor is not an eventfd file.

.. _`eventfd_file_create`:

eventfd_file_create
===================

.. c:function:: struct file *eventfd_file_create(unsigned int count, int flags)

    Creates an eventfd file pointer.

    :param unsigned int count:
        Initial eventfd counter value.

    :param int flags:
        Flags for the eventfd file.

.. _`eventfd_file_create.description`:

Description
-----------

This function creates an eventfd file pointer, w/out installing it into
the fd table. This is useful when the eventfd file is used during the
initialization of data structures that require extra setup after the eventfd
creation. So the eventfd creation is split into the file pointer creation
phase, and the file descriptor installation phase.
In this way races with userspace closing the newly installed file descriptor
can be avoided.
Returns an eventfd file pointer, or a proper error pointer.

.. This file was automatic generated / don't edit.

