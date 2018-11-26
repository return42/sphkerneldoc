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

    :param ifile:
        ifile inode
    :type ifile: struct inode \*

    :param out_ino:
        pointer to a variable to store inode number
    :type out_ino: ino_t \*

    :param out_bh:
        buffer_head contains newly allocated disk inode
    :type out_bh: struct buffer_head \*\*

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

    :param ifile:
        ifile inode
    :type ifile: struct inode \*

    :param ino:
        inode number
    :type ino: ino_t

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

    :param ifile:
        ifile inode
    :type ifile: struct inode \*

    :param nmaxinodes:
        current maximum of available inodes count [out]
    :type nmaxinodes: u64 \*

    :param nfreeinodes:
        free inodes count [out]
    :type nfreeinodes: u64 \*

.. _`nilfs_ifile_read`:

nilfs_ifile_read
================

.. c:function:: int nilfs_ifile_read(struct super_block *sb, struct nilfs_root *root, size_t inode_size, struct nilfs_inode *raw_inode, struct inode **inodep)

    read or get ifile inode

    :param sb:
        super block instance
    :type sb: struct super_block \*

    :param root:
        root object
    :type root: struct nilfs_root \*

    :param inode_size:
        size of an inode
    :type inode_size: size_t

    :param raw_inode:
        on-disk ifile inode
    :type raw_inode: struct nilfs_inode \*

    :param inodep:
        buffer to store the inode
    :type inodep: struct inode \*\*

.. This file was automatic generated / don't edit.

