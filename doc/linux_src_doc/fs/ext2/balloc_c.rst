.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext2/balloc.c

.. _`__rsv_window_dump`:

__rsv_window_dump
=================

.. c:function:: void __rsv_window_dump(struct rb_root *root, int verbose, const char *fn)

    - Dump the filesystem block allocation reservation map

    :param struct rb_root \*root:
        *undescribed*

    :param int verbose:
        verbose mode

    :param const char \*fn:
        function which wishes to dump the reservation map

.. _`__rsv_window_dump.description`:

Description
-----------

If verbose is turned on, it will print the whole block reservation
windows(start, end). Otherwise, it will only print out the "bad" windows,
those windows that overlap with their immediate neighbors.

.. _`goal_in_my_reservation`:

goal_in_my_reservation
======================

.. c:function:: int goal_in_my_reservation(struct ext2_reserve_window *rsv, ext2_grpblk_t grp_goal, unsigned int group, struct super_block *sb)

    :param struct ext2_reserve_window \*rsv:
        inode's reservation window

    :param ext2_grpblk_t grp_goal:
        given goal block relative to the allocation block group

    :param unsigned int group:
        the current allocation block group

    :param struct super_block \*sb:
        filesystem super block

.. _`goal_in_my_reservation.description`:

Description
-----------

Test if the given goal block (group relative) is within the file's
own block reservation window range.

If the reservation window is outside the goal allocation group, return 0;
grp_goal (given goal block) could be -1, which means no specific
goal block. In this case, always return 1.
If the goal block is within the reservation window, return 1;
otherwise, return 0;

.. _`search_reserve_window`:

search_reserve_window
=====================

.. c:function:: struct ext2_reserve_window_node *search_reserve_window(struct rb_root *root, ext2_fsblk_t goal)

    :param struct rb_root \*root:
        *undescribed*

    :param ext2_fsblk_t goal:
        target allocation block

.. _`search_reserve_window.description`:

Description
-----------

Find the reserved window which includes the goal, or the previous one
if the goal is not in any window.
Returns NULL if there are no windows or if all windows start after the goal.

.. _`rsv_window_remove`:

rsv_window_remove
=================

.. c:function:: void rsv_window_remove(struct super_block *sb, struct ext2_reserve_window_node *rsv)

    - unlink a window from the reservation rb tree

    :param struct super_block \*sb:
        super block

    :param struct ext2_reserve_window_node \*rsv:
        reservation window to remove

.. _`rsv_window_remove.description`:

Description
-----------

Mark the block reservation window as not allocated, and unlink it
from the filesystem reservation window rb tree. Must be called with
rsv_lock held.

.. _`ext2_init_block_alloc_info`:

ext2_init_block_alloc_info
==========================

.. c:function:: void ext2_init_block_alloc_info(struct inode *inode)

    :param struct inode \*inode:
        file inode structure

.. _`ext2_init_block_alloc_info.description`:

Description
-----------

Allocate and initialize the  reservation window structure, and
link the window to the ext2 inode structure at last

The reservation window structure is only dynamically allocated
and linked to ext2 inode the first time the open file
needs a new block. So, before every ext2_new_block(s) call, for
regular files, we should check whether the reservation window
structure exists or not. In the latter case, this function is called.
Fail to do so will result in block reservation being turned off for that
open file.

This function is called from \ :c:func:`ext2_get_blocks_handle`\ , also called
when setting the reservation window size through ioctl before the file
is open for write (needs block allocation).

Needs truncate_mutex protection prior to calling this function.

.. _`ext2_discard_reservation`:

ext2_discard_reservation
========================

.. c:function:: void ext2_discard_reservation(struct inode *inode)

    :param struct inode \*inode:
        inode

.. _`ext2_discard_reservation.description`:

Description
-----------

Discard(free) block reservation window on last file close, or truncate
or at last \ :c:func:`iput`\ .

.. _`ext2_discard_reservation.it-is-being-called-in-three-cases`:

It is being called in three cases
---------------------------------

\ :c:func:`ext2_release_file`\ : last writer closes the file
\ :c:func:`ext2_clear_inode`\ : last \ :c:func:`iput`\ , when nobody links to this file.
\ :c:func:`ext2_truncate`\ : when the block indirect map is about to change.

.. _`ext2_free_blocks`:

ext2_free_blocks
================

.. c:function:: void ext2_free_blocks(struct inode *inode, unsigned long block, unsigned long count)

    - Free given blocks and update quota and i_blocks

    :param struct inode \*inode:
        inode

    :param unsigned long block:
        start physical block to free

    :param unsigned long count:
        number of blocks to free

.. _`bitmap_search_next_usable_block`:

bitmap_search_next_usable_block
===============================

.. c:function:: ext2_grpblk_t bitmap_search_next_usable_block(ext2_grpblk_t start, struct buffer_head *bh, ext2_grpblk_t maxblocks)

    :param ext2_grpblk_t start:
        the starting block (group relative) of the search

    :param struct buffer_head \*bh:
        bufferhead contains the block group bitmap

    :param ext2_grpblk_t maxblocks:
        the ending block (group relative) of the reservation

.. _`bitmap_search_next_usable_block.description`:

Description
-----------

The bitmap search --- search forward through the actual bitmap on disk until
we find a bit free.

.. _`find_next_usable_block`:

find_next_usable_block
======================

.. c:function:: ext2_grpblk_t find_next_usable_block(int start, struct buffer_head *bh, int maxblocks)

    :param int start:
        the starting block (group relative) to find next
        allocatable block in bitmap.

    :param struct buffer_head \*bh:
        bufferhead contains the block group bitmap

    :param int maxblocks:
        the ending block (group relative) for the search

.. _`find_next_usable_block.description`:

Description
-----------

Find an allocatable block in a bitmap.  We perform the "most
appropriate allocation" algorithm of looking for a free block near
the initial goal; then for a free byte somewhere in the bitmap;
then for any free bit in the bitmap.

.. _`ext2_try_to_allocate`:

ext2_try_to_allocate
====================

.. c:function:: int ext2_try_to_allocate(struct super_block *sb, int group, struct buffer_head *bitmap_bh, ext2_grpblk_t grp_goal, unsigned long *count, struct ext2_reserve_window *my_rsv)

    :param struct super_block \*sb:
        superblock

    :param int group:
        given allocation block group

    :param struct buffer_head \*bitmap_bh:
        bufferhead holds the block bitmap

    :param ext2_grpblk_t grp_goal:
        given target block within the group

    :param unsigned long \*count:
        target number of blocks to allocate

    :param struct ext2_reserve_window \*my_rsv:
        reservation window

.. _`ext2_try_to_allocate.description`:

Description
-----------

Attempt to allocate blocks within a give range. Set the range of allocation
first, then find the first free bit(s) from the bitmap (within the range),
and at last, allocate the blocks by claiming the found free bit as allocated.

.. _`ext2_try_to_allocate.to-set-the-range-of-this-allocation`:

To set the range of this allocation
-----------------------------------

if there is a reservation window, only try to allocate block(s)
from the file's own reservation window;
Otherwise, the allocation range starts from the give goal block,
ends at the block group's last block.

If we failed to allocate the desired block then we may end up crossing to a
new bitmap.

.. _`find_next_reservable_window`:

find_next_reservable_window
===========================

.. c:function:: int find_next_reservable_window(struct ext2_reserve_window_node *search_head, struct ext2_reserve_window_node *my_rsv, struct super_block *sb, ext2_fsblk_t start_block, ext2_fsblk_t last_block)

    find a reservable space within the given range. It does not allocate the reservation window for now: \ :c:func:`alloc_new_reservation`\  will do the work later.

    :param struct ext2_reserve_window_node \*search_head:
        the head of the searching list;
        This is not necessarily the list head of the whole filesystem

    :param struct ext2_reserve_window_node \*my_rsv:
        *undescribed*

    :param struct super_block \*sb:
        *undescribed*

    :param ext2_fsblk_t start_block:
        *undescribed*

    :param ext2_fsblk_t last_block:
        the maximum block number that our goal reservable space
        could start from. This is normally the last block in this
        group. The search will end when we found the start of next
        possible reservable space is out of this boundary.
        This could handle the cross boundary reservation window
        request.

.. _`find_next_reservable_window.description`:

Description
-----------

We have both head and start_block to assist the search
for the reservable space. The list starts from head,
but we will shift to the place where start_block is,
then start from there, when looking for a reservable space.

basically we search from the given range, rather than the whole
reservation double linked list, (start_block, last_block)
to find a free region that is of my size and has not
been reserved.

.. _`alloc_new_reservation`:

alloc_new_reservation
=====================

.. c:function:: int alloc_new_reservation(struct ext2_reserve_window_node *my_rsv, ext2_grpblk_t grp_goal, struct super_block *sb, unsigned int group, struct buffer_head *bitmap_bh)

    -allocate a new reservation window

    :param struct ext2_reserve_window_node \*my_rsv:
        *undescribed*

    :param ext2_grpblk_t grp_goal:
        The goal (group-relative).  It is where the search for a
        free reservable space should start from.
        if we have a goal(goal >0 ), then start from there,
        no goal(goal = -1), we start from the first block
        of the group.

    :param struct super_block \*sb:
        the super block

    :param unsigned int group:
        the group we are trying to allocate in

    :param struct buffer_head \*bitmap_bh:
        the block group block bitmap

.. _`alloc_new_reservation.description`:

Description
-----------

To make a new reservation, we search part of the filesystem
reservation list (the list that inside the group). We try to
allocate a new reservation window near the allocation goal,
or the beginning of the group, if there is no goal.

We first find a reservable space after the goal, then from
there, we check the bitmap for the first free block after
it. If there is no free block until the end of group, then the
whole group is full, we failed. Otherwise, check if the free
block is inside the expected reservable space, if so, we
succeed.
If the first free block is outside the reservable space, then
start from the first free block, we search for next available
space, and go on.

on succeed, a new reservation will be found and inserted into the list
It contains at least one free block, and it does not overlap with other
reservation windows.

.. _`alloc_new_reservation.failed`:

failed
------

we failed to find a reservation window in this group

.. _`try_to_extend_reservation`:

try_to_extend_reservation
=========================

.. c:function:: void try_to_extend_reservation(struct ext2_reserve_window_node *my_rsv, struct super_block *sb, int size)

    :param struct ext2_reserve_window_node \*my_rsv:
        given reservation window

    :param struct super_block \*sb:
        super block

    :param int size:
        the delta to extend

.. _`try_to_extend_reservation.description`:

Description
-----------

Attempt to expand the reservation window large enough to have
required number of free blocks

Since \ :c:func:`ext2_try_to_allocate`\  will always allocate blocks within
the reservation window range, if the window size is too small,
multiple blocks allocation has to stop at the end of the reservation
window. To make this more efficient, given the total number of
blocks needed and the current size of the window, we try to
expand the reservation window size if necessary on a best-effort
basis before \ :c:func:`ext2_new_blocks`\  tries to allocate blocks.

.. _`ext2_try_to_allocate_with_rsv`:

ext2_try_to_allocate_with_rsv
=============================

.. c:function:: ext2_grpblk_t ext2_try_to_allocate_with_rsv(struct super_block *sb, unsigned int group, struct buffer_head *bitmap_bh, ext2_grpblk_t grp_goal, struct ext2_reserve_window_node *my_rsv, unsigned long *count)

    :param struct super_block \*sb:
        superblock

    :param unsigned int group:
        given allocation block group

    :param struct buffer_head \*bitmap_bh:
        bufferhead holds the block bitmap

    :param ext2_grpblk_t grp_goal:
        given target block within the group

    :param struct ext2_reserve_window_node \*my_rsv:
        reservation window

    :param unsigned long \*count:
        target number of blocks to allocate

.. _`ext2_try_to_allocate_with_rsv.description`:

Description
-----------

This is the main function used to allocate a new block and its reservation
window.

Each time when a new block allocation is need, first try to allocate from
its own reservation.  If it does not have a reservation window, instead of
looking for a free bit on bitmap first, then look up the reservation list to
see if it is inside somebody else's reservation window, we try to allocate a
reservation window for it starting from the goal first. Then do the block
allocation within the reservation window.

This will avoid keeping on searching the reservation list again and
again when somebody is looking for a free block (without
reservation), and there are lots of free blocks, but they are all
being reserved.

We use a red-black tree for the per-filesystem reservation list.

.. _`ext2_has_free_blocks`:

ext2_has_free_blocks
====================

.. c:function:: int ext2_has_free_blocks(struct ext2_sb_info *sbi)

    :param struct ext2_sb_info \*sbi:
        in-core super block structure.

.. _`ext2_has_free_blocks.description`:

Description
-----------

Check if filesystem has at least 1 free block available for allocation.

.. _`ext2_bg_has_super`:

ext2_bg_has_super
=================

.. c:function:: int ext2_bg_has_super(struct super_block *sb, int group)

    number of blocks used by the superblock in group

    :param struct super_block \*sb:
        superblock for filesystem

    :param int group:
        group number to check

.. _`ext2_bg_has_super.description`:

Description
-----------

Return the number of blocks used by the superblock (primary or backup)
in this group.  Currently this will be only 0 or 1.

.. _`ext2_bg_num_gdb`:

ext2_bg_num_gdb
===============

.. c:function:: unsigned long ext2_bg_num_gdb(struct super_block *sb, int group)

    number of blocks used by the group table in group

    :param struct super_block \*sb:
        superblock for filesystem

    :param int group:
        group number to check

.. _`ext2_bg_num_gdb.description`:

Description
-----------

Return the number of blocks used by the group descriptor table
(primary or backup) in this group.  In the future there may be a
different number of descriptor blocks in each group.

.. This file was automatic generated / don't edit.

