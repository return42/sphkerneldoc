.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/vfs_file.c

.. _`v9fs_file_open`:

v9fs_file_open
==============

.. c:function:: int v9fs_file_open(struct inode *inode, struct file *file)

    open a file (or directory)

    :param inode:
        inode to be opened
    :type inode: struct inode \*

    :param file:
        file being opened
    :type file: struct file \*

.. _`v9fs_file_lock`:

v9fs_file_lock
==============

.. c:function:: int v9fs_file_lock(struct file *filp, int cmd, struct file_lock *fl)

    lock a file (or directory)

    :param filp:
        file to be locked
    :type filp: struct file \*

    :param cmd:
        lock command
    :type cmd: int

    :param fl:
        file lock structure
    :type fl: struct file_lock \*

.. _`v9fs_file_lock.bugs`:

Bugs
----

this looks like a local only lock, we should extend into 9P
by using open exclusive

.. _`v9fs_file_lock_dotl`:

v9fs_file_lock_dotl
===================

.. c:function:: int v9fs_file_lock_dotl(struct file *filp, int cmd, struct file_lock *fl)

    lock a file (or directory)

    :param filp:
        file to be locked
    :type filp: struct file \*

    :param cmd:
        lock command
    :type cmd: int

    :param fl:
        file lock structure
    :type fl: struct file_lock \*

.. _`v9fs_file_flock_dotl`:

v9fs_file_flock_dotl
====================

.. c:function:: int v9fs_file_flock_dotl(struct file *filp, int cmd, struct file_lock *fl)

    lock a file

    :param filp:
        file to be locked
    :type filp: struct file \*

    :param cmd:
        lock command
    :type cmd: int

    :param fl:
        file lock structure
    :type fl: struct file_lock \*

.. _`v9fs_file_read_iter`:

v9fs_file_read_iter
===================

.. c:function:: ssize_t v9fs_file_read_iter(struct kiocb *iocb, struct iov_iter *to)

    read from a file

    :param iocb:
        *undescribed*
    :type iocb: struct kiocb \*

    :param to:
        *undescribed*
    :type to: struct iov_iter \*

.. _`v9fs_file_write_iter`:

v9fs_file_write_iter
====================

.. c:function:: ssize_t v9fs_file_write_iter(struct kiocb *iocb, struct iov_iter *from)

    write to a file

    :param iocb:
        *undescribed*
    :type iocb: struct kiocb \*

    :param from:
        *undescribed*
    :type from: struct iov_iter \*

.. _`v9fs_mmap_file_read_iter`:

v9fs_mmap_file_read_iter
========================

.. c:function:: ssize_t v9fs_mmap_file_read_iter(struct kiocb *iocb, struct iov_iter *to)

    read from a file

    :param iocb:
        *undescribed*
    :type iocb: struct kiocb \*

    :param to:
        *undescribed*
    :type to: struct iov_iter \*

.. _`v9fs_mmap_file_write_iter`:

v9fs_mmap_file_write_iter
=========================

.. c:function:: ssize_t v9fs_mmap_file_write_iter(struct kiocb *iocb, struct iov_iter *from)

    write to a file

    :param iocb:
        *undescribed*
    :type iocb: struct kiocb \*

    :param from:
        *undescribed*
    :type from: struct iov_iter \*

.. This file was automatic generated / don't edit.

