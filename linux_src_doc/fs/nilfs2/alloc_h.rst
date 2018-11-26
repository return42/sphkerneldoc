.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/alloc.h

.. _`nilfs_palloc_entries_per_group`:

nilfs_palloc_entries_per_group
==============================

.. c:function:: unsigned long nilfs_palloc_entries_per_group(const struct inode *inode)

    get the number of entries per group

    :param inode:
        inode of metadata file using this allocator
    :type inode: const struct inode \*

.. _`nilfs_palloc_entries_per_group.description`:

Description
-----------

The number of entries per group is defined by the number of bits
that a bitmap block can maintain.

.. _`nilfs_bh_assoc`:

struct nilfs_bh_assoc
=====================

.. c:type:: struct nilfs_bh_assoc

    block offset and buffer head association

.. _`nilfs_bh_assoc.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_bh_assoc {
        unsigned long blkoff;
        struct buffer_head *bh;
    }

.. _`nilfs_bh_assoc.members`:

Members
-------

blkoff
    block offset

bh
    buffer head

.. _`nilfs_palloc_cache`:

struct nilfs_palloc_cache
=========================

.. c:type:: struct nilfs_palloc_cache

    persistent object allocator cache

.. _`nilfs_palloc_cache.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_palloc_cache {
        spinlock_t lock;
        struct nilfs_bh_assoc prev_desc;
        struct nilfs_bh_assoc prev_bitmap;
        struct nilfs_bh_assoc prev_entry;
    }

.. _`nilfs_palloc_cache.members`:

Members
-------

lock
    cache protecting lock

prev_desc
    blockgroup descriptors cache

prev_bitmap
    blockgroup bitmap cache

prev_entry
    translation entries cache

.. This file was automatic generated / don't edit.

