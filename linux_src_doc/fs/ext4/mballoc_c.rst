.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/mballoc.c

.. _`ext4_free_blocks`:

ext4_free_blocks
================

.. c:function:: void ext4_free_blocks(handle_t *handle, struct inode *inode, struct buffer_head *bh, ext4_fsblk_t block, unsigned long count, int flags)

    - Free given blocks and update quota

    :param handle:
        handle for this transaction
    :type handle: handle_t \*

    :param inode:
        inode
    :type inode: struct inode \*

    :param bh:
        *undescribed*
    :type bh: struct buffer_head \*

    :param block:
        start physical block to free
    :type block: ext4_fsblk_t

    :param count:
        number of blocks to count
    :type count: unsigned long

    :param flags:
        flags used by ext4_free_blocks
    :type flags: int

.. _`ext4_group_add_blocks`:

ext4_group_add_blocks
=====================

.. c:function:: int ext4_group_add_blocks(handle_t *handle, struct super_block *sb, ext4_fsblk_t block, unsigned long count)

    - Add given blocks to an existing group

    :param handle:
        handle to this transaction
    :type handle: handle_t \*

    :param sb:
        super block
    :type sb: struct super_block \*

    :param block:
        start physical block to add to the block group
    :type block: ext4_fsblk_t

    :param count:
        number of blocks to free
    :type count: unsigned long

.. _`ext4_group_add_blocks.description`:

Description
-----------

This marks the blocks as free in the bitmap and buddy.

.. _`ext4_trim_extent`:

ext4_trim_extent
================

.. c:function:: int ext4_trim_extent(struct super_block *sb, int start, int count, ext4_group_t group, struct ext4_buddy *e4b)

    - function to TRIM one single free extent in the group

    :param sb:
        super block for the file system
    :type sb: struct super_block \*

    :param start:
        starting block of the free extent in the alloc. group
    :type start: int

    :param count:
        number of blocks to TRIM
    :type count: int

    :param group:
        alloc. group we are working with
    :type group: ext4_group_t

    :param e4b:
        ext4 buddy for the group
    :type e4b: struct ext4_buddy \*

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

    :param sb:
        super block for file system
    :type sb: struct super_block \*

    :param group:
        group to be trimmed
    :type group: ext4_group_t

    :param start:
        first group block to examine
    :type start: ext4_grpblk_t

    :param max:
        last group block to examine
    :type max: ext4_grpblk_t

    :param minblocks:
        minimum extent block count
    :type minblocks: ext4_grpblk_t

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

    :param sb:
        superblock for filesystem
    :type sb: struct super_block \*

    :param range:
        fstrim_range structure
    :type range: struct fstrim_range \*

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

