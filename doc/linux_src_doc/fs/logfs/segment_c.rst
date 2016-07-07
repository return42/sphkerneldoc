.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/logfs/segment.c

.. _`logfs_segment_write`:

logfs_segment_write
===================

.. c:function:: int logfs_segment_write(struct inode *inode, struct page *page, struct logfs_shadow *shadow)

    write data block to object store

    :param struct inode \*inode:
        inode containing data

    :param struct page \*page:
        *undescribed*

    :param struct logfs_shadow \*shadow:
        *undescribed*

.. _`logfs_segment_write.description`:

Description
-----------

Returns an errno or zero.

.. _`logfs_segment_read`:

logfs_segment_read
==================

.. c:function:: int logfs_segment_read(struct inode *inode, struct page *page, u64 ofs, u64 bix, level_t level)

    read data block from object store

    :param struct inode \*inode:
        inode containing data

    :param struct page \*page:
        *undescribed*

    :param u64 ofs:
        physical data offset

    :param u64 bix:
        block index

    :param level_t level:
        block level

.. _`logfs_segment_read.description`:

Description
-----------

Returns 0 on success or a negative errno.

.. This file was automatic generated / don't edit.

