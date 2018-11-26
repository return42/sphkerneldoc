.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/inode.c

.. _`nilfs_iget_args`:

struct nilfs_iget_args
======================

.. c:type:: struct nilfs_iget_args

    arguments used during comparison between inodes

.. _`nilfs_iget_args.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_iget_args {
        u64 ino;
        __u64 cno;
        struct nilfs_root *root;
        int for_gc;
    }

.. _`nilfs_iget_args.members`:

Members
-------

ino
    inode number

cno
    checkpoint number

root
    pointer on NILFS root object (mounted checkpoint)

for_gc
    inode for GC flag

.. _`nilfs_get_block`:

nilfs_get_block
===============

.. c:function:: int nilfs_get_block(struct inode *inode, sector_t blkoff, struct buffer_head *bh_result, int create)

    get a file block on the filesystem (callback function) \ ``inode``\  - inode struct of the target file \ ``blkoff``\  - file block number \ ``bh_result``\  - buffer head to be mapped on \ ``create``\  - indicate whether allocating the block or not when it has not been allocated yet.

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param blkoff:
        *undescribed*
    :type blkoff: sector_t

    :param bh_result:
        *undescribed*
    :type bh_result: struct buffer_head \*

    :param create:
        *undescribed*
    :type create: int

.. _`nilfs_get_block.description`:

Description
-----------

This function does not issue actual read request of the specified data
block. It is done by VFS.

.. _`nilfs_readpage`:

nilfs_readpage
==============

.. c:function:: int nilfs_readpage(struct file *file, struct page *page)

    implement \ :c:func:`readpage`\  method of nilfs_aops {} address_space_operations. \ ``file``\  - file struct of the file to be read \ ``page``\  - the page to be read

    :param file:
        *undescribed*
    :type file: struct file \*

    :param page:
        *undescribed*
    :type page: struct page \*

.. _`nilfs_readpages`:

nilfs_readpages
===============

.. c:function:: int nilfs_readpages(struct file *file, struct address_space *mapping, struct list_head *pages, unsigned int nr_pages)

    implement \ :c:func:`readpages`\  method of nilfs_aops {} address_space_operations. \ ``file``\  - file struct of the file to be read \ ``mapping``\  - address_space struct used for reading multiple pages \ ``pages``\  - the pages to be read \ ``nr_pages``\  - number of pages to be read

    :param file:
        *undescribed*
    :type file: struct file \*

    :param mapping:
        *undescribed*
    :type mapping: struct address_space \*

    :param pages:
        *undescribed*
    :type pages: struct list_head \*

    :param nr_pages:
        *undescribed*
    :type nr_pages: unsigned int

.. _`nilfs_dirty_inode`:

nilfs_dirty_inode
=================

.. c:function:: void nilfs_dirty_inode(struct inode *inode, int flags)

    reflect changes on given inode to an inode block.

    :param inode:
        inode of the file to be registered.
    :type inode: struct inode \*

    :param flags:
        *undescribed*
    :type flags: int

.. _`nilfs_dirty_inode.description`:

Description
-----------

\ :c:func:`nilfs_dirty_inode`\  loads a inode block containing the specified
\ ``inode``\  and copies data from a nilfs_inode to a corresponding inode
entry in the inode block. This operation is excluded from the segment
construction. This function can be called both as a single operation
and as a part of indivisible file operations.

.. This file was automatic generated / don't edit.

