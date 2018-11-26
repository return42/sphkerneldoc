.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/bmap.c

.. _`gfs2_unstuffer_page`:

gfs2_unstuffer_page
===================

.. c:function:: int gfs2_unstuffer_page(struct gfs2_inode *ip, struct buffer_head *dibh, u64 block, struct page *page)

    unstuff a stuffed inode into a block cached by a page

    :param ip:
        the inode
    :type ip: struct gfs2_inode \*

    :param dibh:
        the dinode buffer
    :type dibh: struct buffer_head \*

    :param block:
        the block number that was allocated
    :type block: u64

    :param page:
        The (optional) page. This is looked up if \ ``page``\  is NULL
    :type page: struct page \*

.. _`gfs2_unstuffer_page.return`:

Return
------

errno

.. _`gfs2_unstuff_dinode`:

gfs2_unstuff_dinode
===================

.. c:function:: int gfs2_unstuff_dinode(struct gfs2_inode *ip, struct page *page)

    Unstuff a dinode when the data has grown too big

    :param ip:
        The GFS2 inode to unstuff
    :type ip: struct gfs2_inode \*

    :param page:
        The (optional) page. This is looked up if the \ ``page``\  is NULL
    :type page: struct page \*

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

    :param sdp:
        The superblock
    :type sdp: const struct gfs2_sbd \*

    :param block:
        The disk block to look up
    :type block: u64

    :param mp:
        The metapath to return the result in
    :type mp: struct metapath \*

    :param height:
        The pre-calculated height of the metadata tree
    :type height: unsigned int

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
mp_fheight = 3, mp_list[0] = 0, mp_list[1] = 48, and mp_list[2] = 165.

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

    :param height:
        The metadata height (0 = dinode)
    :type height: unsigned int

    :param mp:
        The metapath
    :type mp: const struct metapath \*

.. _`metapointer`:

metapointer
===========

.. c:function:: __be64 *metapointer(unsigned int height, const struct metapath *mp)

    Return pointer to start of metadata in a buffer

    :param height:
        The metadata height (0 = dinode)
    :type height: unsigned int

    :param mp:
        The metapath
    :type mp: const struct metapath \*

.. _`metapointer.description`:

Description
-----------

Return a pointer to the block number of the next height of the metadata
tree given a buffer containing the pointer to the current height of the
metadata tree.

.. _`lookup_metapath`:

lookup_metapath
===============

.. c:function:: int lookup_metapath(struct gfs2_inode *ip, struct metapath *mp)

    Walk the metadata tree to a specific point

    :param ip:
        The inode
    :type ip: struct gfs2_inode \*

    :param mp:
        The metapath
    :type mp: struct metapath \*

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

error

.. _`fillup_metapath`:

fillup_metapath
===============

.. c:function:: int fillup_metapath(struct gfs2_inode *ip, struct metapath *mp, int h)

    fill up buffers for the metadata path to a specific height

    :param ip:
        The inode
    :type ip: struct gfs2_inode \*

    :param mp:
        The metapath
    :type mp: struct metapath \*

    :param h:
        The height to which it should be mapped
    :type h: int

.. _`fillup_metapath.description`:

Description
-----------

Similar to lookup_metapath, but does lookups for a range of heights

.. _`fillup_metapath.return`:

Return
------

error or the number of buffers filled

.. _`gfs2_extent_length`:

gfs2_extent_length
==================

.. c:function:: unsigned int gfs2_extent_length(struct buffer_head *bh, __be64 *ptr, size_t limit, int *eob)

    Returns length of an extent of blocks

    :param bh:
        The metadata block
    :type bh: struct buffer_head \*

    :param ptr:
        Current position in \ ``bh``\ 
    :type ptr: __be64 \*

    :param limit:
        Max extent length to return
    :type limit: size_t

    :param eob:
        Set to 1 if we hit "end of block"
    :type eob: int \*

.. _`gfs2_extent_length.return`:

Return
------

The length of the extent (minimum of one block)

.. _`gfs2_hole_size`:

gfs2_hole_size
==============

.. c:function:: int gfs2_hole_size(struct inode *inode, sector_t lblock, u64 len, struct metapath *mp, struct iomap *iomap)

    figure out the size of a hole

    :param inode:
        The inode
    :type inode: struct inode \*

    :param lblock:
        The logical starting block number
    :type lblock: sector_t

    :param len:
        How far to look (in blocks)
    :type len: u64

    :param mp:
        The metapath at lblock
    :type mp: struct metapath \*

    :param iomap:
        The iomap to store the hole size in
    :type iomap: struct iomap \*

.. _`gfs2_hole_size.description`:

Description
-----------

This function modifies \ ``mp``\ .

.. _`gfs2_hole_size.return`:

Return
------

errno on error

.. _`gfs2_iomap_alloc`:

gfs2_iomap_alloc
================

.. c:function:: int gfs2_iomap_alloc(struct inode *inode, struct iomap *iomap, unsigned flags, struct metapath *mp)

    Build a metadata tree of the requested height

    :param inode:
        The GFS2 inode
    :type inode: struct inode \*

    :param iomap:
        The iomap structure
    :type iomap: struct iomap \*

    :param flags:
        iomap flags
    :type flags: unsigned

    :param mp:
        The metapath, with proper height information calculated
    :type mp: struct metapath \*

.. _`gfs2_iomap_alloc.in-this-routine-we-may-have-to-alloc`:

In this routine we may have to alloc
------------------------------------

i) Indirect blocks to grow the metadata tree height
ii) Indirect blocks to fill in lower part of the metadata tree
iii) Data blocks

This function is called after gfs2_iomap_get, which works out the
total number of blocks which we need via gfs2_alloc_size.

We then do the actual allocation asking for an extent at a time (if
enough contiguous free blocks are available, there will only be one
allocation request per call) and uses the state machine to initialise
the blocks in order.

Right now, this function will allocate at most one indirect block
worth of data -- with a default block size of 4K, that's slightly
less than 2M.  If this limitation is ever removed to allow huge
allocations, we would probably still want to limit the iomap size we
return to avoid stalling other tasks during huge writes; the next
iomap iteration would then find the blocks already allocated.

.. _`gfs2_iomap_alloc.return`:

Return
------

errno on error

.. _`gfs2_alloc_size`:

gfs2_alloc_size
===============

.. c:function:: u64 gfs2_alloc_size(struct inode *inode, struct metapath *mp, u64 size)

    Compute the maximum allocation size

    :param inode:
        The inode
    :type inode: struct inode \*

    :param mp:
        The metapath
    :type mp: struct metapath \*

    :param size:
        Requested size in blocks
    :type size: u64

.. _`gfs2_alloc_size.description`:

Description
-----------

Compute the maximum size of the next allocation at \ ``mp``\ .

.. _`gfs2_alloc_size.return`:

Return
------

size in blocks

.. _`gfs2_iomap_get`:

gfs2_iomap_get
==============

.. c:function:: int gfs2_iomap_get(struct inode *inode, loff_t pos, loff_t length, unsigned flags, struct iomap *iomap, struct metapath *mp)

    Map blocks from an inode to disk blocks

    :param inode:
        The inode
    :type inode: struct inode \*

    :param pos:
        Starting position in bytes
    :type pos: loff_t

    :param length:
        Length to map, in bytes
    :type length: loff_t

    :param flags:
        iomap flags
    :type flags: unsigned

    :param iomap:
        The iomap structure
    :type iomap: struct iomap \*

    :param mp:
        The metapath
    :type mp: struct metapath \*

.. _`gfs2_iomap_get.return`:

Return
------

errno

.. _`gfs2_block_map`:

gfs2_block_map
==============

.. c:function:: int gfs2_block_map(struct inode *inode, sector_t lblock, struct buffer_head *bh_map, int create)

    Map one or more blocks of an inode to a disk block

    :param inode:
        The inode
    :type inode: struct inode \*

    :param lblock:
        The logical block number
    :type lblock: sector_t

    :param bh_map:
        The bh to be mapped
    :type bh_map: struct buffer_head \*

    :param create:
        True if its ok to alloc blocks to satify the request
    :type create: int

.. _`gfs2_block_map.description`:

Description
-----------

The size of the requested mapping is defined in bh_map->b_size.

Clears buffer_mapped(bh_map) and leaves bh_map->b_size unchanged
when \ ``lblock``\  is not mapped.  Sets buffer_mapped(bh_map) and
bh_map->b_size to indicate the size of the mapping when \ ``lblock``\  and
successive blocks are mapped, up to the requested size.

Sets \ :c:func:`buffer_boundary`\  if a read of metadata will be required
before the next block can be mapped. Sets \ :c:func:`buffer_new`\  if new
blocks were allocated.

.. _`gfs2_block_map.return`:

Return
------

errno

.. _`gfs2_block_zero_range`:

gfs2_block_zero_range
=====================

.. c:function:: int gfs2_block_zero_range(struct inode *inode, loff_t from, unsigned int length)

    Deal with zeroing out data

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param length:
        *undescribed*
    :type length: unsigned int

.. _`gfs2_block_zero_range.description`:

Description
-----------

This is partly borrowed from ext3.

.. _`gfs2_journaled_truncate`:

gfs2_journaled_truncate
=======================

.. c:function:: int gfs2_journaled_truncate(struct inode *inode, u64 oldsize, u64 newsize)

    Wrapper for truncate_pagecache for jdata files

    :param inode:
        The inode being truncated
    :type inode: struct inode \*

    :param oldsize:
        The original (larger) size
    :type oldsize: u64

    :param newsize:
        The new smaller size
    :type newsize: u64

.. _`gfs2_journaled_truncate.description`:

Description
-----------

With jdata files, we have to journal a revoke for each block which is
truncated. As a result, we need to split this into separate transactions
if the number of pages being truncated gets too large.

.. _`sweep_bh_for_rgrps`:

sweep_bh_for_rgrps
==================

.. c:function:: int sweep_bh_for_rgrps(struct gfs2_inode *ip, struct gfs2_holder *rd_gh, struct buffer_head *bh, __be64 *start, __be64 *end, bool meta, u32 *btotal)

    find an rgrp in a meta buffer and free blocks therein

    :param ip:
        inode
    :type ip: struct gfs2_inode \*

    :param rd_gh:
        *undescribed*
    :type rd_gh: struct gfs2_holder \*

    :param bh:
        buffer head to sweep
    :type bh: struct buffer_head \*

    :param start:
        starting point in bh
    :type start: __be64 \*

    :param end:
        end point in bh
    :type end: __be64 \*

    :param meta:
        true if bh points to metadata (rather than data)
    :type meta: bool

    :param btotal:
        place to keep count of total blocks freed
    :type btotal: u32 \*

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

.. c:function:: bool find_nonnull_ptr(struct gfs2_sbd *sdp, struct metapath *mp, unsigned int h, __u16 *end_list, unsigned int end_aligned)

    find a non-null pointer given a metapath and height

    :param sdp:
        *undescribed*
    :type sdp: struct gfs2_sbd \*

    :param mp:
        starting metapath
    :type mp: struct metapath \*

    :param h:
        desired height to search
    :type h: unsigned int

    :param end_list:
        *undescribed*
    :type end_list: __u16 \*

    :param end_aligned:
        *undescribed*
    :type end_aligned: unsigned int

.. _`find_nonnull_ptr.description`:

Description
-----------

Assumes the metapath is valid (with buffers) out to height h.

.. _`find_nonnull_ptr.return`:

Return
------

true if a non-null pointer was found in the metapath buffer
false if all remaining pointers are NULL in the buffer

.. _`punch_hole`:

punch_hole
==========

.. c:function:: int punch_hole(struct gfs2_inode *ip, u64 offset, u64 length)

    deallocate blocks in a file

    :param ip:
        inode to truncate
    :type ip: struct gfs2_inode \*

    :param offset:
        the start of the hole
    :type offset: u64

    :param length:
        the size of the hole (or 0 for truncate)
    :type length: u64

.. _`punch_hole.description`:

Description
-----------

Punch a hole into a file or truncate a file at a given position.  This
function operates in whole blocks (@offset and \ ``length``\  are rounded
accordingly); partially filled blocks must be cleared otherwise.

This function works from the bottom up, and from the right to the left. In
other words, it strips off the highest layer (data) before stripping any of
the metadata. Doing it this way is best in case the operation is interrupted
by power failure, etc.  The dinode is rewritten in every transaction to
guarantee integrity.

.. _`do_shrink`:

do_shrink
=========

.. c:function:: int do_shrink(struct inode *inode, u64 newsize)

    make a file smaller

    :param inode:
        the inode
    :type inode: struct inode \*

    :param newsize:
        the size to make the file
    :type newsize: u64

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

    :param inode:
        The inode
    :type inode: struct inode \*

    :param size:
        The new size
    :type size: u64

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

    :param inode:
        the inode
    :type inode: struct inode \*

    :param newsize:
        the size to make the file
    :type newsize: u64

.. _`gfs2_setattr_size.description`:

Description
-----------

The file size can grow, shrink, or stay the same size. This
is called holding i_rwsem and an exclusive glock on the inode
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

    :param jd:
        The journal
    :type jd: struct gfs2_jdesc \*

.. _`gfs2_add_jextent`:

gfs2_add_jextent
================

.. c:function:: int gfs2_add_jextent(struct gfs2_jdesc *jd, u64 lblock, u64 dblock, u64 blocks)

    Add or merge a new extent to extent cache

    :param jd:
        The journal descriptor
    :type jd: struct gfs2_jdesc \*

    :param lblock:
        The logical block at start of new extent
    :type lblock: u64

    :param dblock:
        The physical block at start of new extent
    :type dblock: u64

    :param blocks:
        Size of extent in fs blocks
    :type blocks: u64

.. _`gfs2_add_jextent.return`:

Return
------

0 on success or -ENOMEM

.. _`gfs2_map_journal_extents`:

gfs2_map_journal_extents
========================

.. c:function:: int gfs2_map_journal_extents(struct gfs2_sbd *sdp, struct gfs2_jdesc *jd)

    Cache journal bmap info

    :param sdp:
        The super block
    :type sdp: struct gfs2_sbd \*

    :param jd:
        The journal to map
    :type jd: struct gfs2_jdesc \*

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

    :param ip:
        the file being written to
    :type ip: struct gfs2_inode \*

    :param offset:
        the offset to write to
    :type offset: u64

    :param len:
        the number of bytes being written
    :type len: unsigned int

.. _`gfs2_write_alloc_required.return`:

Return
------

1 if an alloc is required, 0 otherwise

.. This file was automatic generated / don't edit.

