.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_immed.c

.. _`vxfs_immed_readpage`:

vxfs_immed_readpage
===================

.. c:function:: int vxfs_immed_readpage(struct file *fp, struct page *pp)

    read part of an immed inode into pagecache

    :param fp:
        *undescribed*
    :type fp: struct file \*

    :param pp:
        *undescribed*
    :type pp: struct page \*

.. _`vxfs_immed_readpage.description`:

Description
-----------

vxfs_immed_readpage reads a part of the immed area of the
file that hosts \ ``pp``\  into the pagecache.

.. _`vxfs_immed_readpage.return`:

Return
------

Zero on success, else a negative error code.

.. _`vxfs_immed_readpage.locking-status`:

Locking status
--------------

\ ``page``\  is locked and will be unlocked.

.. This file was automatic generated / don't edit.

