.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/strncpy_from_user.c

.. _`strncpy_from_user`:

strncpy_from_user
=================

.. c:function:: long strncpy_from_user(char *dst, const char __user *src, long count)

    - Copy a NUL terminated string from userspace.

    :param dst:
        Destination address, in kernel space.  This buffer must be at
        least \ ``count``\  bytes long.
    :type dst: char \*

    :param src:
        Source address, in user space.
    :type src: const char __user \*

    :param count:
        Maximum number of bytes to copy, including the trailing NUL.
    :type count: long

.. _`strncpy_from_user.description`:

Description
-----------

Copies a NUL-terminated string from userspace to kernel space.

On success, returns the length of the string (not including the trailing
NUL).

If access to userspace fails, returns -EFAULT (some data may have been
copied).

If \ ``count``\  is smaller than the length of the string, copies \ ``count``\  bytes
and returns \ ``count``\ .

.. This file was automatic generated / don't edit.

