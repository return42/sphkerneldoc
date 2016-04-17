.. -*- coding: utf-8; mode: rst -*-

======
sync.c
======


.. _`vfs_fsync_range`:

vfs_fsync_range
===============

.. c:function:: int vfs_fsync_range (struct file *file, loff_t start, loff_t end, int datasync)

    helper to sync a range of data & metadata to disk

    :param struct file \*file:
        file to sync

    :param loff_t start:
        offset in bytes of the beginning of data range to sync

    :param loff_t end:
        offset in bytes of the end of data range (inclusive)

    :param int datasync:
        perform only datasync



.. _`vfs_fsync_range.description`:

Description
-----------

Write back data in range ``start``\ ..\ ``end`` and metadata for ``file`` to disk.  If
``datasync`` is set only metadata needed to access modified file data is
written.



.. _`vfs_fsync`:

vfs_fsync
=========

.. c:function:: int vfs_fsync (struct file *file, int datasync)

    perform a fsync or fdatasync on a file

    :param struct file \*file:
        file to sync

    :param int datasync:
        only perform a fdatasync operation



.. _`vfs_fsync.description`:

Description
-----------

Write back data and metadata for ``file`` to disk.  If ``datasync`` is
set only metadata needed to access modified file data is written.

