.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/mballoc.c

.. _`ext4_free_blocks`:

ext4_free_blocks
================

.. c:function:: void ext4_free_blocks(handle_t *handle, struct inode *inode, struct buffer_head *bh, ext4_fsblk_t block, unsigned long count, int flags)

    - Free given blocks and update quota

    :param handle_t \*handle:
        handle for this transaction

    :param struct inode \*inode:
        inode

    :param struct buffer_head \*bh:
        *undescribed*

    :param ext4_fsblk_t block:
        start physical block to free

    :param unsigned long count:
        number of blocks to count

    :param int flags:
        flags used by ext4_free_blocks

.. _`ext4_group_add_blocks`:

ext4_group_add_blocks
=====================

.. c:function:: int ext4_group_add_blocks(handle_t *handle, struct super_block *sb, ext4_fsblk_t block, unsigned long count)

    - Add given blocks to an existing group

    :param handle_t \*handle:
        handle to this transaction

    :param struct super_block \*sb:
        super block

    :param ext4_fsblk_t block:
        start physical block to add to the block group

    :param unsigned long count:
        number of blocks to free

.. _`ext4_group_add_blocks.description`:

Description
-----------

This marks the blocks as free in the bitmap and buddy.

.. _`ext4_trim_extent`:

ext4_trim_extent
================

.. c:function:: int ext4_trim_extent(struct super_block *sb, int start, int count, ext4_group_t group, struct ext4_buddy *e4b)

    - function to TRIM one single free extent in the group

    :param struct super_block \*sb:
        super block for the file system

    :param int start:
        starting block of the free extent in the alloc. group

    :param int count:
        number of blocks to TRIM

    :param ext4_group_t group:
        alloc. group we are working with

    :param struct ext4_buddy \*e4b:
        ext4 buddy for the group

.. _`ext4_trim_extent.description`:

Description
-----------

Trim "count" blocks starting at "start" in the "group". To assure that no
one will allocate those blocks, mark it as used in buddy bitmap. This must
be called with under the group lock.

.. _`ext4_trim_all_free`:

ext4_trim_all_free
==================

.. c:function:: ext4_grpblk_t ext4_trim_all_free(struct super_block *sb, ext4_group_t group, ext4_grpblk_t start, ext4_grpblk_t max, ext4_grpblk_t minblocks)

    - function to trim all free space in alloc. group

    :param struct super_block \*sb:
        super block for file system

    :param ext4_group_t group:
        group to be trimmed

    :param ext4_grpblk_t start:
        first group block to examine

    :param ext4_grpblk_t max:
        last group block to examine

    :param ext4_grpblk_t minblocks:
        minimum extent block count

.. _`ext4_trim_all_free.description`:

Description
-----------

ext4_trim_all_free walks through group's buddy bitmap searching for free
extents. When the free block is found, ext4_trim_extent is called to TRIM
the extent.


ext4_trim_all_free walks through group's block bitmap searching for free
extents. When the free extent is found, mark it as used in group buddy
bitmap. Then issue a TRIM command on this extent and free the extent in
the group buddy bitmap. This is done until whole group is scanned.

.. _`ext4_trim_fs`:

ext4_trim_fs
============

.. c:function:: int ext4_trim_fs(struct super_block *sb, struct fstrim_range *range)

    - trim ioctl handle function

    :param struct super_block \*sb:
        superblock for filesystem

    :param struct fstrim_range \*range:
        fstrim_range structure

.. _`ext4_trim_fs.start`:

start
-----

First Byte to trim

.. _`ext4_trim_fs.len`:

len
---

number of Bytes to trim from start

.. _`ext4_trim_fs.minlen`:

minlen
------

minimum extent length in Bytes
ext4_trim_fs goes through all allocation groups containing Bytes from
start to start+len. For each such a group ext4_trim_all_free function
is invoked to trim all free space.

.. This file was automatic generated / don't edit.

