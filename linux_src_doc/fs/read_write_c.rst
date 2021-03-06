.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/read_write.c

.. _`vfs_setpos`:

vfs_setpos
==========

.. c:function:: loff_t vfs_setpos(struct file *file, loff_t offset, loff_t maxsize)

    update the file offset for lseek

    :param file:
        file structure in question
    :type file: struct file \*

    :param offset:
        file offset to seek to
    :type offset: loff_t

    :param maxsize:
        maximum file size
    :type maxsize: loff_t

.. _`vfs_setpos.description`:

Description
-----------

This is a low-level filesystem helper for updating the file offset to
the value specified by \ ``offset``\  if the given offset is valid and it is
not equal to the current file offset.

Return the specified offset on success and -EINVAL on invalid offset.

.. _`generic_file_llseek_size`:

generic_file_llseek_size
========================

.. c:function:: loff_t generic_file_llseek_size(struct file *file, loff_t offset, int whence, loff_t maxsize, loff_t eof)

    generic llseek implementation for regular files

    :param file:
        file structure to seek on
    :type file: struct file \*

    :param offset:
        file offset to seek to
    :type offset: loff_t

    :param whence:
        type of seek
    :type whence: int

    :param maxsize:
        *undescribed*
    :type maxsize: loff_t

    :param eof:
        offset used for SEEK_END position
    :type eof: loff_t

.. _`generic_file_llseek_size.description`:

Description
-----------

This is a variant of generic_file_llseek that allows passing in a custom
maximum file size and a custom EOF position, for e.g. hashed directories

.. _`generic_file_llseek_size.synchronization`:

Synchronization
---------------

SEEK_SET and SEEK_END are unsynchronized (but atomic on 64bit platforms)
SEEK_CUR is synchronized against other SEEK_CURs, but not read/writes.
read/writes behave like SEEK_SET against seeks.

.. _`generic_file_llseek`:

generic_file_llseek
===================

.. c:function:: loff_t generic_file_llseek(struct file *file, loff_t offset, int whence)

    generic llseek implementation for regular files

    :param file:
        file structure to seek on
    :type file: struct file \*

    :param offset:
        file offset to seek to
    :type offset: loff_t

    :param whence:
        type of seek
    :type whence: int

.. _`generic_file_llseek.description`:

Description
-----------

This is a generic implemenation of ->llseek useable for all normal local
filesystems.  It just updates the file offset to the value specified by
\ ``offset``\  and \ ``whence``\ .

.. _`fixed_size_llseek`:

fixed_size_llseek
=================

.. c:function:: loff_t fixed_size_llseek(struct file *file, loff_t offset, int whence, loff_t size)

    llseek implementation for fixed-sized devices

    :param file:
        file structure to seek on
    :type file: struct file \*

    :param offset:
        file offset to seek to
    :type offset: loff_t

    :param whence:
        type of seek
    :type whence: int

    :param size:
        size of the file
    :type size: loff_t

.. _`no_seek_end_llseek`:

no_seek_end_llseek
==================

.. c:function:: loff_t no_seek_end_llseek(struct file *file, loff_t offset, int whence)

    llseek implementation for fixed-sized devices

    :param file:
        file structure to seek on
    :type file: struct file \*

    :param offset:
        file offset to seek to
    :type offset: loff_t

    :param whence:
        type of seek
    :type whence: int

.. _`no_seek_end_llseek_size`:

no_seek_end_llseek_size
=======================

.. c:function:: loff_t no_seek_end_llseek_size(struct file *file, loff_t offset, int whence, loff_t size)

    llseek implementation for fixed-sized devices

    :param file:
        file structure to seek on
    :type file: struct file \*

    :param offset:
        file offset to seek to
    :type offset: loff_t

    :param whence:
        type of seek
    :type whence: int

    :param size:
        maximal offset allowed
    :type size: loff_t

.. _`noop_llseek`:

noop_llseek
===========

.. c:function:: loff_t noop_llseek(struct file *file, loff_t offset, int whence)

    No Operation Performed llseek implementation

    :param file:
        file structure to seek on
    :type file: struct file \*

    :param offset:
        file offset to seek to
    :type offset: loff_t

    :param whence:
        type of seek
    :type whence: int

.. _`noop_llseek.description`:

Description
-----------

This is an implementation of ->llseek useable for the rare special case when
userspace expects the seek to succeed but the (device) file is actually not
able to perform the seek. In this case you use \ :c:func:`noop_llseek`\  instead of
falling back to the default implementation of ->llseek.

.. _`rw_copy_check_uvector`:

rw_copy_check_uvector
=====================

.. c:function:: ssize_t rw_copy_check_uvector(int type, const struct iovec __user *uvector, unsigned long nr_segs, unsigned long fast_segs, struct iovec *fast_pointer, struct iovec **ret_pointer)

    Copy an array of \ :c:type:`struct iovec <iovec>`\  from userspace into the kernel and check that it is valid.

    :param type:
        One of \ ``CHECK_IOVEC_ONLY``\ , \ ``READ``\ , or \ ``WRITE``\ .
    :type type: int

    :param uvector:
        Pointer to the userspace array.
    :type uvector: const struct iovec __user \*

    :param nr_segs:
        Number of elements in userspace array.
    :type nr_segs: unsigned long

    :param fast_segs:
        Number of elements in \ ``fast_pointer``\ .
    :type fast_segs: unsigned long

    :param fast_pointer:
        Pointer to (usually small on-stack) kernel array.
    :type fast_pointer: struct iovec \*

    :param ret_pointer:
        (output parameter) Pointer to a variable that will point to
        either \ ``fast_pointer``\ , a newly allocated kernel array, or NULL,
        depending on which array was used.
    :type ret_pointer: struct iovec \*\*

.. _`rw_copy_check_uvector.description`:

Description
-----------

This function copies an array of \ :c:type:`struct iovec <iovec>`\  of \ ``nr_segs``\  from
userspace into the kernel and checks that each element is valid (e.g.
it does not point to a kernel address or cause overflow by being too
large, etc.).

As an optimization, the caller may provide a pointer to a small
on-stack array in \ ``fast_pointer``\ , typically \ ``UIO_FASTIOV``\  elements long
(the size of this array, or 0 if unused, should be given in \ ``fast_segs``\ ).

\ ``ret_pointer``\  will always point to the array that was used, so the
caller must take care not to call \ :c:func:`kfree`\  on it e.g. in case the
\ ``fast_pointer``\  array was used and it was allocated on the stack.

.. _`rw_copy_check_uvector.return`:

Return
------

The total number of bytes covered by the iovec array on success
or a negative error code on error.

.. This file was automatic generated / don't edit.

