.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/bmap.c

.. _`gfs2_unstuffer_page`:

gfs2_unstuffer_page
===================

.. c:function:: int gfs2_unstuffer_page(struct gfs2_inode *ip, struct buffer_head *dibh, u64 block, struct page *page)

    unstuff a stuffed inode into a block cached by a page

    :param struct gfs2_inode \*ip:
        the inode

    :param struct buffer_head \*dibh:
        the dinode buffer

    :param u64 block:
        the block number that was allocated

    :param struct page \*page:
        The (optional) page. This is looked up if \ ``page``\  is NULL

.. _`gfs2_unstuffer_page.return`:

Return
------

errno

.. _`gfs2_unstuff_dinode`:

gfs2_unstuff_dinode
===================

.. c:function:: int gfs2_unstuff_dinode(struct gfs2_inode *ip, struct page *page)

    Unstuff a dinode when the data has grown too big

    :param struct gfs2_inode \*ip:
        The GFS2 inode to unstuff

    :param struct page \*page:
        The (optional) page. This is looked up if the \ ``page``\  is NULL

.. _`gfs2_unstuff_dinode.description`:

Description
-----------

This routine unstuffs a dinode and returns it to a "normal" state such
that the height can be grown in the traditional way.

.. _`gfs2_unstuff_dinode.return`:

Return
------

errno

.. _`find_metapath`:

find_metapath
=============

.. c:function:: void find_metapath(const struct gfs2_sbd *sdp, u64 block, struct metapath *mp, unsigned int height)

    Find path through the metadata tree

    :param const struct gfs2_sbd \*sdp:
        The superblock

    :param u64 block:
        The disk block to look up

    :param struct metapath \*mp:
        The metapath to return the result in

    :param unsigned int height:
        The pre-calculated height of the metadata tree

.. _`find_metapath.description`:

Description
-----------

This routine returns a struct metapath structure that defines a path
through the metadata of inode "ip" to get to block "block".

.. _`find_metapath.given`:

Given
-----

"ip" is a height 3 file, "offset" is 101342453, and this is a
filesystem with a blocksize of 4096.

\ :c:func:`find_metapath`\  would return a struct metapath structure set to:
mp_offset = 101342453, mp_height = 3, mp_list[0] = 0, mp_list[1] = 48,
and mp_list[2] = 165.

That means that in order to get to the block containing the byte at
offset 101342453, we would load the indirect block pointed to by pointer
0 in the dinode.  We would then load the indirect block pointed to by
pointer 48 in that indirect block.  We would then load the data block
pointed to by pointer 165 in that indirect block.

----------------------------------------
\| Dinode \|                             \|
\|        \|                            4\|
\|        \|0 1 2 3 4 5                 9\|
\|        \|                            6\|
----------------------------------------
\|
\|
V
----------------------------------------
\| Indirect Block                       \|
\|                                     5\|
\|            4 4 4 4 4 5 5            1\|
\|0           5 6 7 8 9 0 1            2\|
----------------------------------------
\|
\|
V
----------------------------------------
\| Indirect Block                       \|
\|                         1 1 1 1 1   5\|
\|                         6 6 6 6 6   1\|
\|0                        3 4 5 6 7   2\|
----------------------------------------
\|
\|
V
----------------------------------------
\| Data block containing offset         \|
\|            101342453                 \|
\|                                      \|
\|                                      \|
----------------------------------------

.. _`metaptr1`:

metaptr1
========

.. c:function:: __be64 *metaptr1(unsigned int height, const struct metapath *mp)

    Return the first possible metadata pointer in a metapath buffer

    :param unsigned int height:
        The metadata height (0 = dinode)

    :param const struct metapath \*mp:
        The metapath

.. _`metapointer`:

metapointer
===========

.. c:function:: __be64 *metapointer(unsigned int height, const struct metapath *mp)

    Return pointer to start of metadata in a buffer

    :param unsigned int height:
        The metadata height (0 = dinode)

    :param const struct metapath \*mp:
        The metapath

.. _`metapointer.description`:

Description
-----------

Return a pointer to the block number of the next height of the metadata
tree given a buffer containing the pointer to the current height of the
metadata tree.

.. _`lookup_mp_height`:

lookup_mp_height
================

.. c:function:: int lookup_mp_height(struct gfs2_inode *ip, struct metapath *mp, int h)

    helper function for lookup_metapath

    :param struct gfs2_inode \*ip:
        the inode

    :param struct metapath \*mp:
        the metapath

    :param int h:
        the height which needs looking up

.. _`lookup_metapath`:

lookup_metapath
===============

.. c:function:: int lookup_metapath(struct gfs2_inode *ip, struct metapath *mp)

    Walk the metadata tree to a specific point

    :param struct gfs2_inode \*ip:
        The inode

    :param struct metapath \*mp:
        The metapath

.. _`lookup_metapath.description`:

Description
-----------

Assumes that the inode's buffer has already been looked up and
hooked onto mp->mp_bh[0] and that the metapath has been initialised
by \ :c:func:`find_metapath`\ .

If this function encounters part of the tree which has not been
allocated, it returns the current height of the tree at the point
at which it found the unallocated block. Blocks which are found are
added to the mp->mp_bh[] list.

.. _`lookup_metapath.return`:

Return
------

error or height of metadata tree

.. _`fillup_metapath`:

fillup_metapath
===============

.. c:function:: int fillup_metapath(struct gfs2_inode *ip, struct metapath *mp, int h)

    fill up buffers for the metadata path to a specific height

    :param struct gfs2_inode \*ip:
        The inode

    :param struct metapath \*mp:
        The metapath

    :param int h:
        The height to which it should be mapped

.. _`fillup_metapath.description`:

Description
-----------

Similar to lookup_metapath, but does lookups for a range of heights

.. _`fillup_metapath.return`:

Return
------

error or height of metadata tree

.. _`gfs2_extent_length`:

gfs2_extent_length
==================

.. c:function:: unsigned int gfs2_extent_length(void *start, unsigned int len, __be64 *ptr, size_t limit, int *eob)

    Returns length of an extent of blocks

    :param void \*start:
        Start of the buffer

    :param unsigned int len:
        Length of the buffer in bytes

    :param __be64 \*ptr:
        Current position in the buffer

    :param size_t limit:
        Max extent length to return (0 = unlimited)

    :param int \*eob:
        Set to 1 if we hit "end of block"

.. _`gfs2_extent_length.description`:

Description
-----------

If the first block is zero (unallocated) it will return the number of
unallocated blocks in the extent, otherwise it will return the number
of contiguous blocks in the extent.

.. _`gfs2_extent_length.return`:

Return
------

The length of the extent (minimum of one block)

.. _`gfs2_iomap_alloc`:

gfs2_iomap_alloc
================

.. c:function:: int gfs2_iomap_alloc(struct inode *inode, struct iomap *iomap, unsigned flags, struct metapath *mp)

    Build a metadata tree of the requested height

    :param struct inode \*inode:
        The GFS2 inode

    :param struct iomap \*iomap:
        *undescribed*

    :param unsigned flags:
        *undescribed*

    :param struct metapath \*mp:
        The metapath, with proper height information calculated

.. _`gfs2_iomap_alloc.in-this-routine-we-may-have-to-alloc`:

In this routine we may have to alloc
------------------------------------

i) Indirect blocks to grow the metadata tree height
ii) Indirect blocks to fill in lower part of the metadata tree
iii) Data blocks

The function is in two parts. The first part works out the total
number of blocks which we need. The second part does the actual
allocation asking for an extent at a time (if enough contiguous free
blocks are available, there will only be one request per bmap call)
and uses the state machine to initialise the blocks in order.

.. _`gfs2_iomap_alloc.return`:

Return
------

errno on error

.. _`hole_size`:

hole_size
=========

.. c:function:: u64 hole_size(struct inode *inode, sector_t lblock, struct metapath *mp)

    figure out the size of a hole

    :param struct inode \*inode:
        The inode

    :param sector_t lblock:
        The logical starting block number

    :param struct metapath \*mp:
        The metapath

.. _`hole_size.return`:

Return
------

The hole size in bytes

.. _`gfs2_iomap_begin`:

gfs2_iomap_begin
================

.. c:function:: int gfs2_iomap_begin(struct inode *inode, loff_t pos, loff_t length, unsigned flags, struct iomap *iomap)

    Map blocks from an inode to disk blocks

    :param struct inode \*inode:
        The inode

    :param loff_t pos:
        Starting position in bytes

    :param loff_t length:
        Length to map, in bytes

    :param unsigned flags:
        iomap flags

    :param struct iomap \*iomap:
        The iomap structure

.. _`gfs2_iomap_begin.return`:

Return
------

errno

.. _`gfs2_block_map`:

gfs2_block_map
==============

.. c:function:: int gfs2_block_map(struct inode *inode, sector_t lblock, struct buffer_head *bh_map, int create)

    Map a block from an inode to a disk block

    :param struct inode \*inode:
        The inode

    :param sector_t lblock:
        The logical block number

    :param struct buffer_head \*bh_map:
        The bh to be mapped

    :param int create:
        True if its ok to alloc blocks to satify the request

.. _`gfs2_block_map.description`:

Description
-----------

Sets \ :c:func:`buffer_mapped`\  if successful, sets \ :c:func:`buffer_boundary`\  if a
read of metadata will be required before the next block can be
mapped. Sets \ :c:func:`buffer_new`\  if new blocks were allocated.

.. _`gfs2_block_map.return`:

Return
------

errno

.. _`gfs2_block_truncate_page`:

gfs2_block_truncate_page
========================

.. c:function:: int gfs2_block_truncate_page(struct address_space *mapping, loff_t from)

    Deal with zeroing out data for truncate

    :param struct address_space \*mapping:
        *undescribed*

    :param loff_t from:
        *undescribed*

.. _`gfs2_block_truncate_page.description`:

Description
-----------

This is partly borrowed from ext3.

.. _`gfs2_journaled_truncate`:

gfs2_journaled_truncate
=======================

.. c:function:: int gfs2_journaled_truncate(struct inode *inode, u64 oldsize, u64 newsize)

    Wrapper for truncate_pagecache for jdata files

    :param struct inode \*inode:
        The inode being truncated

    :param u64 oldsize:
        The original (larger) size

    :param u64 newsize:
        The new smaller size

.. _`gfs2_journaled_truncate.description`:

Description
-----------

With jdata files, we have to journal a revoke for each block which is
truncated. As a result, we need to split this into separate transactions
if the number of pages being truncated gets too large.

.. _`sweep_bh_for_rgrps`:

sweep_bh_for_rgrps
==================

.. c:function:: int sweep_bh_for_rgrps(struct gfs2_inode *ip, struct gfs2_holder *rd_gh, const struct metapath *mp, u32 *btotal, int hgt, bool preserve1)

    find an rgrp in a meta buffer and free blocks therein

    :param struct gfs2_inode \*ip:
        inode

    :param struct gfs2_holder \*rd_gh:
        *undescribed*

    :param const struct metapath \*mp:
        current metapath fully populated with buffers

    :param u32 \*btotal:
        place to keep count of total blocks freed

    :param int hgt:
        height we're processing

    :param bool preserve1:
        *undescribed*

.. _`sweep_bh_for_rgrps.description`:

Description
-----------

We sweep a metadata buffer (provided by the metapath) for blocks we need to
free, and free them all. However, we do it one rgrp at a time. If this
block has references to multiple rgrps, we break it into individual
transactions. This allows other processes to use the rgrps while we're
focused on a single one, for better concurrency / performance.
At every transaction boundary, we rewrite the inode into the journal.
That way the bitmaps are kept consistent with the inode and we can recover
if we're interrupted by power-outages.

.. _`sweep_bh_for_rgrps.return`:

Return
------

0, or return code if an error occurred.
\*btotal has the total number of blocks freed

.. _`find_nonnull_ptr`:

find_nonnull_ptr
================

.. c:function:: bool find_nonnull_ptr(struct gfs2_sbd *sdp, struct metapath *mp, unsigned int h)

    find a non-null pointer given a metapath and height assumes the metapath is valid (with buffers) out to height h

    :param struct gfs2_sbd \*sdp:
        *undescribed*

    :param struct metapath \*mp:
        starting metapath

    :param unsigned int h:
        desired height to search

.. _`find_nonnull_ptr.return`:

Return
------

true if a non-null pointer was found in the metapath buffer
false if all remaining pointers are NULL in the buffer

.. _`trunc_dealloc`:

trunc_dealloc
=============

.. c:function:: int trunc_dealloc(struct gfs2_inode *ip, u64 newsize)

    truncate a file down to a desired size

    :param struct gfs2_inode \*ip:
        inode to truncate

    :param u64 newsize:
        The desired size of the file

.. _`trunc_dealloc.description`:

Description
-----------

This function truncates a file to newsize. It works from the
bottom up, and from the right to the left. In other words, it strips off
the highest layer (data) before stripping any of the metadata. Doing it
this way is best in case the operation is interrupted by power failure, etc.
The dinode is rewritten in every transaction to guarantee integrity.

.. _`do_shrink`:

do_shrink
=========

.. c:function:: int do_shrink(struct inode *inode, u64 oldsize, u64 newsize)

    make a file smaller

    :param struct inode \*inode:
        the inode

    :param u64 oldsize:
        the current inode size

    :param u64 newsize:
        the size to make the file

.. _`do_shrink.description`:

Description
-----------

Called with an exclusive lock on \ ``inode``\ . The \ ``size``\  must
be equal to or smaller than the current inode size.

.. _`do_shrink.return`:

Return
------

errno

.. _`do_grow`:

do_grow
=======

.. c:function:: int do_grow(struct inode *inode, u64 size)

    Touch and update inode size

    :param struct inode \*inode:
        The inode

    :param u64 size:
        The new size

.. _`do_grow.description`:

Description
-----------

This function updates the timestamps on the inode and
may also increase the size of the inode. This function
must not be called with \ ``size``\  any smaller than the current
inode size.

Although it is not strictly required to unstuff files here,
earlier versions of GFS2 have a bug in the stuffed file reading
code which will result in a buffer overrun if the size is larger
than the max stuffed file size. In order to prevent this from
occurring, such files are unstuffed, but in other cases we can
just update the inode size directly.

.. _`do_grow.return`:

Return
------

0 on success, or -ve on error

.. _`gfs2_setattr_size`:

gfs2_setattr_size
=================

.. c:function:: int gfs2_setattr_size(struct inode *inode, u64 newsize)

    make a file a given size

    :param struct inode \*inode:
        the inode

    :param u64 newsize:
        the size to make the file

.. _`gfs2_setattr_size.description`:

Description
-----------

The file size can grow, shrink, or stay the same size. This
is called holding i_mutex and an exclusive glock on the inode
in question.

.. _`gfs2_setattr_size.return`:

Return
------

errno

.. _`gfs2_free_journal_extents`:

gfs2_free_journal_extents
=========================

.. c:function:: void gfs2_free_journal_extents(struct gfs2_jdesc *jd)

    Free cached journal bmap info

    :param struct gfs2_jdesc \*jd:
        The journal

.. _`gfs2_add_jextent`:

gfs2_add_jextent
================

.. c:function:: int gfs2_add_jextent(struct gfs2_jdesc *jd, u64 lblock, u64 dblock, u64 blocks)

    Add or merge a new extent to extent cache

    :param struct gfs2_jdesc \*jd:
        The journal descriptor

    :param u64 lblock:
        The logical block at start of new extent

    :param u64 dblock:
        The physical block at start of new extent

    :param u64 blocks:
        Size of extent in fs blocks

.. _`gfs2_add_jextent.return`:

Return
------

0 on success or -ENOMEM

.. _`gfs2_map_journal_extents`:

gfs2_map_journal_extents
========================

.. c:function:: int gfs2_map_journal_extents(struct gfs2_sbd *sdp, struct gfs2_jdesc *jd)

    Cache journal bmap info

    :param struct gfs2_sbd \*sdp:
        The super block

    :param struct gfs2_jdesc \*jd:
        The journal to map

.. _`gfs2_map_journal_extents.description`:

Description
-----------

Create a reusable "extent" mapping from all logical
blocks to all physical blocks for the given journal.  This will save
us time when writing journal blocks.  Most journals will have only one
extent that maps all their logical blocks.  That's because gfs2.mkfs
arranges the journal blocks sequentially to maximize performance.
So the extent would map the first block for the entire file length.
However, gfs2_jadd can happen while file activity is happening, so
those journals may not be sequential.  Less likely is the case where
the users created their own journals by mounting the metafs and
laying it out.  But it's still possible.  These journals might have
several extents.

.. _`gfs2_map_journal_extents.return`:

Return
------

0 on success, or error on failure

.. _`gfs2_write_alloc_required`:

gfs2_write_alloc_required
=========================

.. c:function:: int gfs2_write_alloc_required(struct gfs2_inode *ip, u64 offset, unsigned int len)

    figure out if a write will require an allocation

    :param struct gfs2_inode \*ip:
        the file being written to

    :param u64 offset:
        the offset to write to

    :param unsigned int len:
        the number of bytes being written

.. _`gfs2_write_alloc_required.return`:

Return
------

1 if an alloc is required, 0 otherwise

.. This file was automatic generated / don't edit.

