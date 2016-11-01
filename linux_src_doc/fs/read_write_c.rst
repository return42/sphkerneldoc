.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/read_write.c

.. _`vfs_setpos`:

vfs_setpos
==========

.. c:function:: loff_t vfs_setpos(struct file *file, loff_t offset, loff_t maxsize)

    update the file offset for lseek

    :param struct file \*file:
        file structure in question

    :param loff_t offset:
        file offset to seek to

    :param loff_t maxsize:
        maximum file size

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

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek

    :param loff_t maxsize:
        *undescribed*

    :param loff_t eof:
        offset used for SEEK_END position

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

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek

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

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek

    :param loff_t size:
        size of the file

.. _`no_seek_end_llseek`:

no_seek_end_llseek
==================

.. c:function:: loff_t no_seek_end_llseek(struct file *file, loff_t offset, int whence)

    llseek implementation for fixed-sized devices

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek

.. _`no_seek_end_llseek_size`:

no_seek_end_llseek_size
=======================

.. c:function:: loff_t no_seek_end_llseek_size(struct file *file, loff_t offset, int whence, loff_t size)

    llseek implementation for fixed-sized devices

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek

    :param loff_t size:
        maximal offset allowed

.. _`noop_llseek`:

noop_llseek
===========

.. c:function:: loff_t noop_llseek(struct file *file, loff_t offset, int whence)

    No Operation Performed llseek implementation

    :param struct file \*file:
        file structure to seek on

    :param loff_t offset:
        file offset to seek to

    :param int whence:
        type of seek

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

    :param int type:
        One of \ ``CHECK_IOVEC_ONLY``\ , \ ``READ``\ , or \ ``WRITE``\ .

    :param const struct iovec __user \*uvector:
        Pointer to the userspace array.

    :param unsigned long nr_segs:
        Number of elements in userspace array.

    :param unsigned long fast_segs:
        Number of elements in \ ``fast_pointer``\ .

    :param struct iovec \*fast_pointer:
        Pointer to (usually small on-stack) kernel array.

    :param struct iovec \*\*ret_pointer:
        (output parameter) Pointer to a variable that will point to
        either \ ``fast_pointer``\ , a newly allocated kernel array, or NULL,
        depending on which array was used.

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

