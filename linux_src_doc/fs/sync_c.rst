.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/sync.c

.. _`vfs_fsync_range`:

vfs_fsync_range
===============

.. c:function:: int vfs_fsync_range(struct file *file, loff_t start, loff_t end, int datasync)

    helper to sync a range of data & metadata to disk

    :param file:
        file to sync
    :type file: struct file \*

    :param start:
        offset in bytes of the beginning of data range to sync
    :type start: loff_t

    :param end:
        offset in bytes of the end of data range (inclusive)
    :type end: loff_t

    :param datasync:
        perform only datasync
    :type datasync: int

.. _`vfs_fsync_range.description`:

Description
-----------

Write back data in range \ ``start``\ ..@end and metadata for \ ``file``\  to disk.  If
\ ``datasync``\  is set only metadata needed to access modified file data is
written.

.. _`vfs_fsync`:

vfs_fsync
=========

.. c:function:: int vfs_fsync(struct file *file, int datasync)

    perform a fsync or fdatasync on a file

    :param file:
        file to sync
    :type file: struct file \*

    :param datasync:
        only perform a fdatasync operation
    :type datasync: int

.. _`vfs_fsync.description`:

Description
-----------

Write back data and metadata for \ ``file``\  to disk.  If \ ``datasync``\  is
set only metadata needed to access modified file data is written.

.. This file was automatic generated / don't edit.

