.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/nilfs.h

.. _`nilfs_inode_info`:

struct nilfs_inode_info
=======================

.. c:type:: struct nilfs_inode_info

    nilfs inode data in memory

.. _`nilfs_inode_info.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_inode_info {
        __u32 i_flags;
        unsigned long i_state;
        struct nilfs_bmap *i_bmap;
        struct nilfs_bmap i_bmap_data;
        __u64 i_xattr;
        __u32 i_dir_start_lookup;
        __u64 i_cno;
        struct address_space i_btnode_cache;
        struct list_head i_dirty;
        #ifdef CONFIG_NILFS_XATTR
        struct rw_semaphore xattr_sem;
        #endif
        struct buffer_head *i_bh;
        struct nilfs_root *i_root;
        struct inode vfs_inode;
    }

.. _`nilfs_inode_info.members`:

Members
-------

i_flags
    inode flags

i_state
    dynamic state flags

i_bmap
    pointer on i_bmap_data

i_bmap_data
    raw block mapping

i_xattr
    <TODO>

i_dir_start_lookup
    page index of last successful search

i_cno
    checkpoint number for GC inode

i_btnode_cache
    cached pages of b-tree nodes

i_dirty
    list for connecting dirty files

xattr_sem
    semaphore for extended attributes processing

i_bh
    buffer contains disk inode

i_root
    root object of the current filesystem tree

vfs_inode
    VFS inode object

.. _`nilfs_transaction_info`:

struct nilfs_transaction_info
=============================

.. c:type:: struct nilfs_transaction_info

    context information for synchronization

.. _`nilfs_transaction_info.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_transaction_info {
        u32 ti_magic;
        void *ti_save;
        unsigned short ti_flags;
        unsigned short ti_count;
    }

.. _`nilfs_transaction_info.members`:

Members
-------

ti_magic
    Magic number

ti_save
    Backup of journal_info field of task_struct

ti_flags
    Flags

ti_count
    Nest level

.. This file was automatic generated / don't edit.

