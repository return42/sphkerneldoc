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

.. _`gfs2_bmap_alloc`:

gfs2_bmap_alloc
===============

.. c:function:: int gfs2_bmap_alloc(struct inode *inode, const sector_t lblock, struct buffer_head *bh_map, struct metapath *mp, const unsigned int sheight, const unsigned int height, const size_t maxlen)

    Build a metadata tree of the requested height

    :param struct inode \*inode:
        The GFS2 inode

    :param const sector_t lblock:
        The logical starting block of the extent

    :param struct buffer_head \*bh_map:
        This is used to return the mapping details

    :param struct metapath \*mp:
        The metapath

    :param const unsigned int sheight:
        The starting height (i.e. whats already mapped)

    :param const unsigned int height:
        The height to build to

    :param const size_t maxlen:
        The max number of data blocks to alloc

.. _`gfs2_bmap_alloc.in-this-routine-we-may-have-to-alloc`:

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

.. _`gfs2_bmap_alloc.return`:

Return
------

errno on error

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

.. _`do_strip`:

do_strip
========

.. c:function:: int do_strip(struct gfs2_inode *ip, struct buffer_head *dibh, struct buffer_head *bh, __be64 *top, __be64 *bottom, unsigned int height, struct strip_mine *sm)

    Look for a layer a particular layer of the file and strip it off

    :param struct gfs2_inode \*ip:
        the inode

    :param struct buffer_head \*dibh:
        the dinode buffer

    :param struct buffer_head \*bh:
        A buffer of pointers

    :param __be64 \*top:
        The first pointer in the buffer

    :param __be64 \*bottom:
        One more than the last pointer

    :param unsigned int height:
        the height this buffer is at

    :param struct strip_mine \*sm:
        a pointer to a struct strip_mine

.. _`do_strip.return`:

Return
------

errno

.. _`recursive_scan`:

recursive_scan
==============

.. c:function:: int recursive_scan(struct gfs2_inode *ip, struct buffer_head *dibh, struct metapath *mp, unsigned int height, u64 block, int first, struct strip_mine *sm)

    recursively scan through the end of a file

    :param struct gfs2_inode \*ip:
        the inode

    :param struct buffer_head \*dibh:
        the dinode buffer

    :param struct metapath \*mp:
        the path through the metadata to the point to start

    :param unsigned int height:
        the height the recursion is at

    :param u64 block:
        the indirect block to look at

    :param int first:
        1 if this is the first block

    :param struct strip_mine \*sm:
        data opaque to this function to pass to \ ``bc``\ 

.. _`recursive_scan.description`:

Description
-----------

When this is first called \ ``height``\  and \ ``block``\  should be zero and
\ ``first``\  should be 1.

.. _`recursive_scan.return`:

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

