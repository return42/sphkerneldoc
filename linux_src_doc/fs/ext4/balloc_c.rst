.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/balloc.c

.. _`ext4_get_group_desc`:

ext4_get_group_desc
===================

.. c:function:: struct ext4_group_desc *ext4_get_group_desc(struct super_block *sb, ext4_group_t block_group, struct buffer_head **bh)

    - load group descriptor from disk

    :param struct super_block \*sb:
        super block

    :param ext4_group_t block_group:
        given block group

    :param struct buffer_head \*\*bh:
        pointer to the buffer head to store the block
        group descriptor

.. _`ext4_read_block_bitmap_nowait`:

ext4_read_block_bitmap_nowait
=============================

.. c:function:: struct buffer_head *ext4_read_block_bitmap_nowait(struct super_block *sb, ext4_group_t block_group)

    :param struct super_block \*sb:
        super block

    :param ext4_group_t block_group:
        given block group

.. _`ext4_read_block_bitmap_nowait.description`:

Description
-----------

Read the bitmap for a given block_group,and validate the
bits for block/inode/inode tables are set in the bitmaps

Return buffer_head on success or NULL in case of failure.

.. _`ext4_has_free_clusters`:

ext4_has_free_clusters
======================

.. c:function:: int ext4_has_free_clusters(struct ext4_sb_info *sbi, s64 nclusters, unsigned int flags)

    :param struct ext4_sb_info \*sbi:
        in-core super block structure.

    :param s64 nclusters:
        number of needed blocks

    :param unsigned int flags:
        flags from \ :c:func:`ext4_mb_new_blocks`\ 

.. _`ext4_has_free_clusters.description`:

Description
-----------

Check if filesystem has nclusters free & available for allocation.
On success return 1, return 0 on failure.

.. _`ext4_should_retry_alloc`:

ext4_should_retry_alloc
=======================

.. c:function:: int ext4_should_retry_alloc(struct super_block *sb, int *retries)

    :param struct super_block \*sb:
        super block
        \ ``retries``\              number of attemps has been made

    :param int \*retries:
        *undescribed*

.. _`ext4_should_retry_alloc.description`:

Description
-----------

ext4_should_retry_alloc() is called when ENOSPC is returned, and if
it is profitable to retry the operation, this function will wait
for the current or committing transaction to complete, and then
return TRUE.

if the total number of retries exceed three times, return FALSE.

.. _`ext4_count_free_clusters`:

ext4_count_free_clusters
========================

.. c:function:: ext4_fsblk_t ext4_count_free_clusters(struct super_block *sb)

    - count filesystem free clusters

    :param struct super_block \*sb:
        superblock

.. _`ext4_count_free_clusters.description`:

Description
-----------

Adds up the number of free clusters from each block group.

.. _`ext4_bg_has_super`:

ext4_bg_has_super
=================

.. c:function:: int ext4_bg_has_super(struct super_block *sb, ext4_group_t group)

    number of blocks used by the superblock in group

    :param struct super_block \*sb:
        superblock for filesystem

    :param ext4_group_t group:
        group number to check

.. _`ext4_bg_has_super.description`:

Description
-----------

Return the number of blocks used by the superblock (primary or backup)
in this group.  Currently this will be only 0 or 1.

.. _`ext4_bg_num_gdb`:

ext4_bg_num_gdb
===============

.. c:function:: unsigned long ext4_bg_num_gdb(struct super_block *sb, ext4_group_t group)

    number of blocks used by the group table in group

    :param struct super_block \*sb:
        superblock for filesystem

    :param ext4_group_t group:
        group number to check

.. _`ext4_bg_num_gdb.description`:

Description
-----------

Return the number of blocks used by the group descriptor table
(primary or backup) in this group.  In the future there may be a
different number of descriptor blocks in each group.

.. _`ext4_inode_to_goal_block`:

ext4_inode_to_goal_block
========================

.. c:function:: ext4_fsblk_t ext4_inode_to_goal_block(struct inode *inode)

    return a hint for block allocation

    :param struct inode \*inode:
        inode for block allocation

.. _`ext4_inode_to_goal_block.description`:

Description
-----------

Return the ideal location to start allocating blocks for a
newly created inode.

.. This file was automatic generated / don't edit.

