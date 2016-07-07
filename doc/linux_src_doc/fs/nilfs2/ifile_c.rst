.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/ifile.c

.. _`nilfs_ifile_info`:

struct nilfs_ifile_info
=======================

.. c:type:: struct nilfs_ifile_info

    on-memory private data of ifile

.. _`nilfs_ifile_info.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_ifile_info {
        struct nilfs_mdt_info mi;
        struct nilfs_palloc_cache palloc_cache;
    }

.. _`nilfs_ifile_info.members`:

Members
-------

mi
    on-memory private data of metadata file

palloc_cache
    persistent object allocator cache of ifile

.. _`nilfs_ifile_create_inode`:

nilfs_ifile_create_inode
========================

.. c:function:: int nilfs_ifile_create_inode(struct inode *ifile, ino_t *out_ino, struct buffer_head **out_bh)

    create a new disk inode

    :param struct inode \*ifile:
        ifile inode

    :param ino_t \*out_ino:
        pointer to a variable to store inode number

    :param struct buffer_head \*\*out_bh:
        buffer_head contains newly allocated disk inode

.. _`nilfs_ifile_create_inode.return-value`:

Return Value
------------

On success, 0 is returned and the newly allocated inode
number is stored in the place pointed by \ ``ino``\ , and buffer_head pointer
that contains newly allocated disk inode structure is stored in the
place pointed by \ ``out_bh``\ 
On error, one of the following negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOSPC``\  - No inode left.

.. _`nilfs_ifile_delete_inode`:

nilfs_ifile_delete_inode
========================

.. c:function:: int nilfs_ifile_delete_inode(struct inode *ifile, ino_t ino)

    delete a disk inode

    :param struct inode \*ifile:
        ifile inode

    :param ino_t ino:
        inode number

.. _`nilfs_ifile_delete_inode.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - The inode number \ ``ino``\  have not been allocated.

.. _`nilfs_ifile_count_free_inodes`:

nilfs_ifile_count_free_inodes
=============================

.. c:function:: int nilfs_ifile_count_free_inodes(struct inode *ifile, u64 *nmaxinodes, u64 *nfreeinodes)

    calculate free inodes count

    :param struct inode \*ifile:
        ifile inode

    :param u64 \*nmaxinodes:
        current maximum of available inodes count [out]

    :param u64 \*nfreeinodes:
        free inodes count [out]

.. _`nilfs_ifile_read`:

nilfs_ifile_read
================

.. c:function:: int nilfs_ifile_read(struct super_block *sb, struct nilfs_root *root, size_t inode_size, struct nilfs_inode *raw_inode, struct inode **inodep)

    read or get ifile inode

    :param struct super_block \*sb:
        super block instance

    :param struct nilfs_root \*root:
        root object

    :param size_t inode_size:
        size of an inode

    :param struct nilfs_inode \*raw_inode:
        on-disk ifile inode

    :param struct inode \*\*inodep:
        buffer to store the inode

.. This file was automatic generated / don't edit.

