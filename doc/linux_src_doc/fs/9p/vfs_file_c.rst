.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/vfs_file.c

.. _`v9fs_file_open`:

v9fs_file_open
==============

.. c:function:: int v9fs_file_open(struct inode *inode, struct file *file)

    open a file (or directory)

    :param struct inode \*inode:
        inode to be opened

    :param struct file \*file:
        file being opened

.. _`v9fs_file_lock`:

v9fs_file_lock
==============

.. c:function:: int v9fs_file_lock(struct file *filp, int cmd, struct file_lock *fl)

    lock a file (or directory)

    :param struct file \*filp:
        file to be locked

    :param int cmd:
        lock command

    :param struct file_lock \*fl:
        file lock structure

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

    :param struct file \*filp:
        file to be locked

    :param int cmd:
        lock command

    :param struct file_lock \*fl:
        file lock structure

.. _`v9fs_file_flock_dotl`:

v9fs_file_flock_dotl
====================

.. c:function:: int v9fs_file_flock_dotl(struct file *filp, int cmd, struct file_lock *fl)

    lock a file

    :param struct file \*filp:
        file to be locked

    :param int cmd:
        lock command

    :param struct file_lock \*fl:
        file lock structure

.. _`v9fs_file_read_iter`:

v9fs_file_read_iter
===================

.. c:function:: ssize_t v9fs_file_read_iter(struct kiocb *iocb, struct iov_iter *to)

    read from a file

    :param struct kiocb \*iocb:
        *undescribed*

    :param struct iov_iter \*to:
        *undescribed*

.. _`v9fs_file_write_iter`:

v9fs_file_write_iter
====================

.. c:function:: ssize_t v9fs_file_write_iter(struct kiocb *iocb, struct iov_iter *from)

    write to a file

    :param struct kiocb \*iocb:
        *undescribed*

    :param struct iov_iter \*from:
        *undescribed*

.. _`v9fs_mmap_file_read_iter`:

v9fs_mmap_file_read_iter
========================

.. c:function:: ssize_t v9fs_mmap_file_read_iter(struct kiocb *iocb, struct iov_iter *to)

    read from a file

    :param struct kiocb \*iocb:
        *undescribed*

    :param struct iov_iter \*to:
        *undescribed*

.. _`v9fs_mmap_file_write_iter`:

v9fs_mmap_file_write_iter
=========================

.. c:function:: ssize_t v9fs_mmap_file_write_iter(struct kiocb *iocb, struct iov_iter *from)

    write to a file

    :param struct kiocb \*iocb:
        *undescribed*

    :param struct iov_iter \*from:
        *undescribed*

.. This file was automatic generated / don't edit.

