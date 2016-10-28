.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/rgrp.c

.. _`gfs2_setbit`:

gfs2_setbit
===========

.. c:function:: void gfs2_setbit(const struct gfs2_rbm *rbm, bool do_clone, unsigned char new_state)

    Set a bit in the bitmaps

    :param const struct gfs2_rbm \*rbm:
        The position of the bit to set

    :param bool do_clone:
        Also set the clone bitmap, if it exists

    :param unsigned char new_state:
        the new state of the block

.. _`gfs2_testbit`:

gfs2_testbit
============

.. c:function:: u8 gfs2_testbit(const struct gfs2_rbm *rbm)

    test a bit in the bitmaps

    :param const struct gfs2_rbm \*rbm:
        The bit to test

.. _`gfs2_testbit.return`:

Return
------

The two bit block state of the requested bit

.. _`gfs2_bit_search`:

gfs2_bit_search
===============

.. c:function:: u64 gfs2_bit_search(const __le64 *ptr, u64 mask, u8 state)

    :param const __le64 \*ptr:
        Pointer to bitmap data

    :param u64 mask:
        Mask to use (normally 0x55555.... but adjusted for search start)

    :param u8 state:
        The state we are searching for

.. _`gfs2_bit_search.description`:

Description
-----------

We xor the bitmap data with a patter which is the bitwise opposite
of what we are looking for, this gives rise to a pattern of ones
wherever there is a match. Since we have two bits per entry, we
take this pattern, shift it down by one place and then and it with
the original. All the even bit positions (0,2,4, etc) then represent
successful matches, so we mask with 0x55555..... to remove the unwanted
odd bit positions.

This allows searching of a whole u64 at once (32 blocks) with a
single test (on 64 bit arches).

.. _`rs_cmp`:

rs_cmp
======

.. c:function:: int rs_cmp(u64 blk, u32 len, struct gfs2_blkreserv *rs)

    multi-block reservation range compare

    :param u64 blk:
        absolute file system block number of the new reservation

    :param u32 len:
        number of blocks in the new reservation

    :param struct gfs2_blkreserv \*rs:
        existing reservation to compare against

.. _`rs_cmp.return`:

Return
------

1 if the block range is beyond the reach of the reservation
-1 if the block range is before the start of the reservation
0 if the block range overlaps with the reservation

.. _`gfs2_bitfit`:

gfs2_bitfit
===========

.. c:function:: u32 gfs2_bitfit(const u8 *buf, const unsigned int len, u32 goal, u8 state)

    Search an rgrp's bitmap buffer to find a bit-pair representing a block in a given allocation state.

    :param const u8 \*buf:
        the buffer that holds the bitmaps

    :param const unsigned int len:
        the length (in bytes) of the buffer

    :param u32 goal:
        start search at this block's bit-pair (within \ ``buffer``\ )

    :param u8 state:
        GFS2_BLKST_XXX the state of the block we're looking for.

.. _`gfs2_bitfit.description`:

Description
-----------

Scope of \ ``goal``\  and returned block number is only within this bitmap buffer,
not entire rgrp or filesystem.  \ ``buffer``\  will be offset from the actual
beginning of a bitmap block buffer, skipping any header structures, but
headers are always a multiple of 64 bits long so that the buffer is
always aligned to a 64 bit boundary.

The size of the buffer is in bytes, but is it assumed that it is
always ok to read a complete multiple of 64 bits at the end
of the block in case the end is no aligned to a natural boundary.

.. _`gfs2_bitfit.return`:

Return
------

the block number (bitmap buffer scope) that was found

.. _`gfs2_rbm_from_block`:

gfs2_rbm_from_block
===================

.. c:function:: int gfs2_rbm_from_block(struct gfs2_rbm *rbm, u64 block)

    Set the rbm based upon rgd and block number

    :param struct gfs2_rbm \*rbm:
        The rbm with rgd already set correctly

    :param u64 block:
        The block number (filesystem relative)

.. _`gfs2_rbm_from_block.description`:

Description
-----------

This sets the bi and offset members of an rbm based on a
resource group and a filesystem relative block number. The
resource group must be set in the rbm on entry, the bi and
offset members will be set by this function.

.. _`gfs2_rbm_from_block.return`:

Return
------

0 on success, or an error code

.. _`gfs2_rbm_incr`:

gfs2_rbm_incr
=============

.. c:function:: bool gfs2_rbm_incr(struct gfs2_rbm *rbm)

    increment an rbm structure

    :param struct gfs2_rbm \*rbm:
        The rbm with rgd already set correctly

.. _`gfs2_rbm_incr.description`:

Description
-----------

This function takes an existing rbm structure and increments it to the next
viable block offset.

.. _`gfs2_rbm_incr.return`:

Return
------

If incrementing the offset would cause the rbm to go past the
end of the rgrp, true is returned, otherwise false.

.. _`gfs2_unaligned_extlen`:

gfs2_unaligned_extlen
=====================

.. c:function:: bool gfs2_unaligned_extlen(struct gfs2_rbm *rbm, u32 n_unaligned, u32 *len)

    Look for free blocks which are not byte aligned

    :param struct gfs2_rbm \*rbm:
        Position to search (value/result)

    :param u32 n_unaligned:
        Number of unaligned blocks to check

    :param u32 \*len:
        Decremented for each block found (terminate on zero)

.. _`gfs2_unaligned_extlen.return`:

Return
------

true if a non-free block is encountered

.. _`gfs2_free_extlen`:

gfs2_free_extlen
================

.. c:function:: u32 gfs2_free_extlen(const struct gfs2_rbm *rrbm, u32 len)

    Return extent length of free blocks

    :param const struct gfs2_rbm \*rrbm:
        Starting position

    :param u32 len:
        Max length to check

.. _`gfs2_free_extlen.description`:

Description
-----------

Starting at the block specified by the rbm, see how many free blocks
there are, not reading more than len blocks ahead. This can be done
using memchr_inv when the blocks are byte aligned, but has to be done
on a block by block basis in case of unaligned blocks. Also this
function can cope with bitmap boundaries (although it must stop on
a resource group boundary)

.. _`gfs2_free_extlen.return`:

Return
------

Number of free blocks in the extent

.. _`gfs2_bitcount`:

gfs2_bitcount
=============

.. c:function:: u32 gfs2_bitcount(struct gfs2_rgrpd *rgd, const u8 *buffer, unsigned int buflen, u8 state)

    count the number of bits in a certain state

    :param struct gfs2_rgrpd \*rgd:
        the resource group descriptor

    :param const u8 \*buffer:
        the buffer that holds the bitmaps

    :param unsigned int buflen:
        the length (in bytes) of the buffer

    :param u8 state:
        the state of the block we're looking for

.. _`gfs2_bitcount.return`:

Return
------

The number of bits

.. _`gfs2_rgrp_verify`:

gfs2_rgrp_verify
================

.. c:function:: void gfs2_rgrp_verify(struct gfs2_rgrpd *rgd)

    Verify that a resource group is consistent

    :param struct gfs2_rgrpd \*rgd:
        the rgrp

.. _`gfs2_blk2rgrpd`:

gfs2_blk2rgrpd
==============

.. c:function:: struct gfs2_rgrpd *gfs2_blk2rgrpd(struct gfs2_sbd *sdp, u64 blk, bool exact)

    Find resource group for a given data/meta block number

    :param struct gfs2_sbd \*sdp:
        The GFS2 superblock

    :param u64 blk:
        The data block number

    :param bool exact:
        True if this needs to be an exact match

.. _`gfs2_blk2rgrpd.return`:

Return
------

The resource group, or NULL if not found

.. _`gfs2_rgrpd_get_first`:

gfs2_rgrpd_get_first
====================

.. c:function:: struct gfs2_rgrpd *gfs2_rgrpd_get_first(struct gfs2_sbd *sdp)

    get the first Resource Group in the filesystem

    :param struct gfs2_sbd \*sdp:
        The GFS2 superblock

.. _`gfs2_rgrpd_get_first.return`:

Return
------

The first rgrp in the filesystem

.. _`gfs2_rgrpd_get_next`:

gfs2_rgrpd_get_next
===================

.. c:function:: struct gfs2_rgrpd *gfs2_rgrpd_get_next(struct gfs2_rgrpd *rgd)

    get the next RG

    :param struct gfs2_rgrpd \*rgd:
        the resource group descriptor

.. _`gfs2_rgrpd_get_next.return`:

Return
------

The next rgrp

.. _`gfs2_rsqa_alloc`:

gfs2_rsqa_alloc
===============

.. c:function:: int gfs2_rsqa_alloc(struct gfs2_inode *ip)

    make sure we have a reservation assigned to the inode plus a quota allocations data structure, if necessary

    :param struct gfs2_inode \*ip:
        the inode for this reservation

.. _`__rs_deltree`:

__rs_deltree
============

.. c:function:: void __rs_deltree(struct gfs2_blkreserv *rs)

    remove a multi-block reservation from the rgd tree

    :param struct gfs2_blkreserv \*rs:
        The reservation to remove

.. _`gfs2_rs_deltree`:

gfs2_rs_deltree
===============

.. c:function:: void gfs2_rs_deltree(struct gfs2_blkreserv *rs)

    remove a multi-block reservation from the rgd tree

    :param struct gfs2_blkreserv \*rs:
        The reservation to remove

.. _`gfs2_rsqa_delete`:

gfs2_rsqa_delete
================

.. c:function:: void gfs2_rsqa_delete(struct gfs2_inode *ip, atomic_t *wcount)

    delete a multi-block reservation and quota allocation

    :param struct gfs2_inode \*ip:
        The inode for this reservation

    :param atomic_t \*wcount:
        The inode's write count, or NULL

.. _`return_all_reservations`:

return_all_reservations
=======================

.. c:function:: void return_all_reservations(struct gfs2_rgrpd *rgd)

    return all reserved blocks back to the rgrp.

    :param struct gfs2_rgrpd \*rgd:
        the rgrp that needs its space back

.. _`return_all_reservations.description`:

Description
-----------

We previously reserved a bunch of blocks for allocation. Now we need to
give them back. This leave the reservation structures in tact, but removes
all of their corresponding "no-fly zones".

.. _`compute_bitstructs`:

compute_bitstructs
==================

.. c:function:: int compute_bitstructs(struct gfs2_rgrpd *rgd)

    Compute the bitmap sizes

    :param struct gfs2_rgrpd \*rgd:
        The resource group descriptor

.. _`compute_bitstructs.description`:

Description
-----------

Calculates bitmap descriptors, one for each block that contains bitmap data

.. _`compute_bitstructs.return`:

Return
------

errno

.. _`gfs2_ri_total`:

gfs2_ri_total
=============

.. c:function:: u64 gfs2_ri_total(struct gfs2_sbd *sdp)

    Total up the file system space, according to the rindex.

    :param struct gfs2_sbd \*sdp:
        the filesystem

.. _`read_rindex_entry`:

read_rindex_entry
=================

.. c:function:: int read_rindex_entry(struct gfs2_inode *ip)

    Pull in a new resource index entry from the disk

    :param struct gfs2_inode \*ip:
        Pointer to the rindex inode

.. _`read_rindex_entry.return`:

Return
------

0 on success, > 0 on EOF, error code otherwise

.. _`set_rgrp_preferences`:

set_rgrp_preferences
====================

.. c:function:: void set_rgrp_preferences(struct gfs2_sbd *sdp)

    Run all the rgrps, selecting some we prefer to use

    :param struct gfs2_sbd \*sdp:
        the GFS2 superblock

.. _`set_rgrp_preferences.description`:

Description
-----------

The purpose of this function is to select a subset of the resource groups
and mark them as PREFERRED. We do it in such a way that each node prefers
to use a unique set of rgrps to minimize glock contention.

.. _`gfs2_ri_update`:

gfs2_ri_update
==============

.. c:function:: int gfs2_ri_update(struct gfs2_inode *ip)

    Pull in a new resource index from the disk

    :param struct gfs2_inode \*ip:
        pointer to the rindex inode

.. _`gfs2_ri_update.return`:

Return
------

0 on successful update, error code otherwise

.. _`gfs2_rindex_update`:

gfs2_rindex_update
==================

.. c:function:: int gfs2_rindex_update(struct gfs2_sbd *sdp)

    Update the rindex if required

    :param struct gfs2_sbd \*sdp:
        The GFS2 superblock

.. _`gfs2_rindex_update.description`:

Description
-----------

We grab a lock on the rindex inode to make sure that it doesn't
change whilst we are performing an operation. We keep this lock
for quite long periods of time compared to other locks. This
doesn't matter, since it is shared and it is very, very rarely
accessed in the exclusive mode (i.e. only when expanding the filesystem).

This makes sure that we're using the latest copy of the resource index
special file, which might have been updated if someone expanded the
filesystem (via gfs2_grow utility), which adds new resource groups.

.. _`gfs2_rindex_update.return`:

Return
------

0 on succeess, error code otherwise

.. _`gfs2_rgrp_bh_get`:

gfs2_rgrp_bh_get
================

.. c:function:: int gfs2_rgrp_bh_get(struct gfs2_rgrpd *rgd)

    Read in a RG's header and bitmaps

    :param struct gfs2_rgrpd \*rgd:
        the struct gfs2_rgrpd describing the RG to read in

.. _`gfs2_rgrp_bh_get.description`:

Description
-----------

Read in all of a Resource Group's header and bitmap blocks.
Caller must eventually call \ :c:func:`gfs2_rgrp_relse`\  to free the bitmaps.

.. _`gfs2_rgrp_bh_get.return`:

Return
------

errno

.. _`gfs2_rgrp_brelse`:

gfs2_rgrp_brelse
================

.. c:function:: void gfs2_rgrp_brelse(struct gfs2_rgrpd *rgd)

    Release RG bitmaps read in with \ :c:func:`gfs2_rgrp_bh_get`\ 

    :param struct gfs2_rgrpd \*rgd:
        The resource group

.. _`gfs2_rgrp_go_unlock`:

gfs2_rgrp_go_unlock
===================

.. c:function:: void gfs2_rgrp_go_unlock(struct gfs2_holder *gh)

    Unlock a rgrp glock

    :param struct gfs2_holder \*gh:
        The glock holder for the resource group

.. _`gfs2_fitrim`:

gfs2_fitrim
===========

.. c:function:: int gfs2_fitrim(struct file *filp, void __user *argp)

    Generate discard requests for unused bits of the filesystem

    :param struct file \*filp:
        Any file on the filesystem

    :param void __user \*argp:
        Pointer to the arguments (also used to pass result)

.. _`gfs2_fitrim.return`:

Return
------

0 on success, otherwise error code

.. _`rs_insert`:

rs_insert
=========

.. c:function:: void rs_insert(struct gfs2_inode *ip)

    insert a new multi-block reservation into the rgrp's rb_tree

    :param struct gfs2_inode \*ip:
        the inode structure

.. _`rg_mblk_search`:

rg_mblk_search
==============

.. c:function:: void rg_mblk_search(struct gfs2_rgrpd *rgd, struct gfs2_inode *ip, const struct gfs2_alloc_parms *ap)

    find a group of multiple free blocks to form a reservation

    :param struct gfs2_rgrpd \*rgd:
        the resource group descriptor

    :param struct gfs2_inode \*ip:
        pointer to the inode for which we're reserving blocks

    :param const struct gfs2_alloc_parms \*ap:
        the allocation parameters

.. _`gfs2_next_unreserved_block`:

gfs2_next_unreserved_block
==========================

.. c:function:: u64 gfs2_next_unreserved_block(struct gfs2_rgrpd *rgd, u64 block, u32 length, const struct gfs2_inode *ip)

    Return next block that is not reserved

    :param struct gfs2_rgrpd \*rgd:
        The resource group

    :param u64 block:
        The starting block

    :param u32 length:
        The required length

    :param const struct gfs2_inode \*ip:
        Ignore any reservations for this inode

.. _`gfs2_next_unreserved_block.description`:

Description
-----------

If the block does not appear in any reservation, then return the
block number unchanged. If it does appear in the reservation, then
keep looking through the tree of reservations in order to find the
first block number which is not reserved.

.. _`gfs2_reservation_check_and_update`:

gfs2_reservation_check_and_update
=================================

.. c:function:: int gfs2_reservation_check_and_update(struct gfs2_rbm *rbm, const struct gfs2_inode *ip, u32 minext, struct gfs2_extent *maxext)

    Check for reservations during block alloc

    :param struct gfs2_rbm \*rbm:
        The current position in the resource group

    :param const struct gfs2_inode \*ip:
        The inode for which we are searching for blocks

    :param u32 minext:
        The minimum extent length

    :param struct gfs2_extent \*maxext:
        A pointer to the maximum extent structure

.. _`gfs2_reservation_check_and_update.description`:

Description
-----------

This checks the current position in the rgrp to see whether there is
a reservation covering this block. If not then this function is a
no-op. If there is, then the position is moved to the end of the
contiguous reservation(s) so that we are pointing at the first
non-reserved block.

.. _`gfs2_reservation_check_and_update.return`:

Return
------

0 if no reservation, 1 if \ ``rbm``\  has changed, otherwise an error

.. _`gfs2_rbm_find`:

gfs2_rbm_find
=============

.. c:function:: int gfs2_rbm_find(struct gfs2_rbm *rbm, u8 state, u32 *minext, const struct gfs2_inode *ip, bool nowrap)

    Look for blocks of a particular state

    :param struct gfs2_rbm \*rbm:
        Value/result starting position and final position

    :param u8 state:
        The state which we want to find

    :param u32 \*minext:
        Pointer to the requested extent length (NULL for a single block)
        This is updated to be the actual reservation size.

    :param const struct gfs2_inode \*ip:
        If set, check for reservations

    :param bool nowrap:
        Stop looking at the end of the rgrp, rather than wrapping
        around until we've reached the starting point.

.. _`gfs2_rbm_find.side-effects`:

Side effects
------------

- If looking for free blocks, we set GBF_FULL on each bitmap which
has no free blocks in it.
- If looking for free blocks, we set rd_extfail_pt on each rgrp which
has come up short on a free block search.

.. _`gfs2_rbm_find.return`:

Return
------

0 on success, -ENOSPC if there is no block of the requested state

.. _`try_rgrp_unlink`:

try_rgrp_unlink
===============

.. c:function:: void try_rgrp_unlink(struct gfs2_rgrpd *rgd, u64 *last_unlinked, u64 skip)

    Look for any unlinked, allocated, but unused inodes

    :param struct gfs2_rgrpd \*rgd:
        The rgrp

    :param u64 \*last_unlinked:
        block address of the last dinode we unlinked

    :param u64 skip:
        block address we should explicitly not unlink

.. _`try_rgrp_unlink.return`:

Return
------

0 if no error
The inode, if one has been found, in inode.

.. _`gfs2_rgrp_congested`:

gfs2_rgrp_congested
===================

.. c:function:: bool gfs2_rgrp_congested(const struct gfs2_rgrpd *rgd, int loops)

    Use stats to figure out whether an rgrp is congested

    :param const struct gfs2_rgrpd \*rgd:
        The rgrp in question

    :param int loops:
        An indication of how picky we can be (0=very, 1=less so)

.. _`gfs2_rgrp_congested.description`:

Description
-----------

This function uses the recently added glock statistics in order to
figure out whether a parciular resource group is suffering from
contention from multiple nodes. This is done purely on the basis
of timings, since this is the only data we have to work with and
our aim here is to reject a resource group which is highly contended
but (very important) not to do this too often in order to ensure that
we do not land up introducing fragmentation by changing resource
groups when not actually required.

The calculation is fairly simple, we want to know whether the SRTTB
(i.e. smoothed round trip time for blocking operations) to acquire
the lock for this rgrp's glock is significantly greater than the
time taken for resource groups on average. We introduce a margin in
the form of the variable \ ``var``\  which is computed as the sum of the two
respective variences, and multiplied by a factor depending on \ ``loops``\ 
and whether we have a lot of data to base the decision on. This is
then tested against the square difference of the means in order to
decide whether the result is statistically significant or not.

.. _`gfs2_rgrp_congested.return`:

Return
------

A boolean verdict on the congestion status

.. _`gfs2_rgrp_used_recently`:

gfs2_rgrp_used_recently
=======================

.. c:function:: bool gfs2_rgrp_used_recently(const struct gfs2_blkreserv *rs, u64 msecs)

    :param const struct gfs2_blkreserv \*rs:
        The block reservation with the rgrp to test

    :param u64 msecs:
        The time limit in milliseconds

.. _`gfs2_rgrp_used_recently.return`:

Return
------

True if the rgrp glock has been used within the time limit

.. _`fast_to_acquire`:

fast_to_acquire
===============

.. c:function:: int fast_to_acquire(struct gfs2_rgrpd *rgd)

    determine if a resource group will be fast to acquire

    :param struct gfs2_rgrpd \*rgd:
        *undescribed*

.. _`fast_to_acquire.description`:

Description
-----------

If this is one of our preferred rgrps, it should be quicker to acquire,
because we tried to set ourselves up as dlm lock master.

.. _`gfs2_inplace_reserve`:

gfs2_inplace_reserve
====================

.. c:function:: int gfs2_inplace_reserve(struct gfs2_inode *ip, struct gfs2_alloc_parms *ap)

    Reserve space in the filesystem

    :param struct gfs2_inode \*ip:
        the inode to reserve space for

    :param struct gfs2_alloc_parms \*ap:
        the allocation parameters

.. _`gfs2_inplace_reserve.description`:

Description
-----------

We try our best to find an rgrp that has at least ap->target blocks
available. After a couple of passes (loops == 2), the prospects of finding
such an rgrp diminish. At this stage, we return the first rgrp that has
atleast ap->min_target blocks available. Either way, we set ap->allowed to
the number of blocks available in the chosen rgrp.

.. _`gfs2_inplace_reserve.return`:

Return
------

0 on success,
-ENOMEM if a suitable rgrp can't be found
errno otherwise

.. _`gfs2_inplace_release`:

gfs2_inplace_release
====================

.. c:function:: void gfs2_inplace_release(struct gfs2_inode *ip)

    release an inplace reservation

    :param struct gfs2_inode \*ip:
        the inode the reservation was taken out on

.. _`gfs2_inplace_release.description`:

Description
-----------

Release a reservation made by \ :c:func:`gfs2_inplace_reserve`\ .

.. _`gfs2_get_block_type`:

gfs2_get_block_type
===================

.. c:function:: unsigned char gfs2_get_block_type(struct gfs2_rgrpd *rgd, u64 block)

    Check a block in a RG is of given type

    :param struct gfs2_rgrpd \*rgd:
        the resource group holding the block

    :param u64 block:
        the block number

.. _`gfs2_get_block_type.return`:

Return
------

The block type (GFS2_BLKST\_\*)

.. _`gfs2_alloc_extent`:

gfs2_alloc_extent
=================

.. c:function:: void gfs2_alloc_extent(const struct gfs2_rbm *rbm, bool dinode, unsigned int *n)

    allocate an extent from a given bitmap

    :param const struct gfs2_rbm \*rbm:
        the resource group information

    :param bool dinode:
        TRUE if the first block we allocate is for a dinode

    :param unsigned int \*n:
        The extent length (value/result)

.. _`gfs2_alloc_extent.description`:

Description
-----------

Add the bitmap buffer to the transaction.
Set the found bits to \ ``new_state``\  to change block's allocation state.

.. _`rgblk_free`:

rgblk_free
==========

.. c:function:: struct gfs2_rgrpd *rgblk_free(struct gfs2_sbd *sdp, u64 bstart, u32 blen, unsigned char new_state)

    Change alloc state of given block(s)

    :param struct gfs2_sbd \*sdp:
        the filesystem

    :param u64 bstart:
        the start of a run of blocks to free

    :param u32 blen:
        the length of the block run (all must lie within ONE RG!)

    :param unsigned char new_state:
        GFS2_BLKST_XXX the after-allocation block state

.. _`rgblk_free.return`:

Return
------

Resource group containing the block(s)

.. _`gfs2_rgrp_dump`:

gfs2_rgrp_dump
==============

.. c:function:: void gfs2_rgrp_dump(struct seq_file *seq, const struct gfs2_glock *gl)

    print out an rgrp

    :param struct seq_file \*seq:
        The iterator

    :param const struct gfs2_glock \*gl:
        The glock in question

.. _`gfs2_adjust_reservation`:

gfs2_adjust_reservation
=======================

.. c:function:: void gfs2_adjust_reservation(struct gfs2_inode *ip, const struct gfs2_rbm *rbm, unsigned len)

    Adjust (or remove) a reservation after allocation

    :param struct gfs2_inode \*ip:
        The inode we have just allocated blocks for

    :param const struct gfs2_rbm \*rbm:
        The start of the allocated blocks

    :param unsigned len:
        The extent length

.. _`gfs2_adjust_reservation.description`:

Description
-----------

Adjusts a reservation after an allocation has taken place. If the
reservation does not match the allocation, or if it is now empty
then it is removed.

.. _`gfs2_set_alloc_start`:

gfs2_set_alloc_start
====================

.. c:function:: void gfs2_set_alloc_start(struct gfs2_rbm *rbm, const struct gfs2_inode *ip, bool dinode)

    Set starting point for block allocation

    :param struct gfs2_rbm \*rbm:
        The rbm which will be set to the required location

    :param const struct gfs2_inode \*ip:
        The gfs2 inode

    :param bool dinode:
        Flag to say if allocation includes a new inode

.. _`gfs2_set_alloc_start.description`:

Description
-----------

This sets the starting point from the reservation if one is active
otherwise it falls back to guessing a start point based on the
inode's goal block or the last allocation point in the rgrp.

.. _`gfs2_alloc_blocks`:

gfs2_alloc_blocks
=================

.. c:function:: int gfs2_alloc_blocks(struct gfs2_inode *ip, u64 *bn, unsigned int *nblocks, bool dinode, u64 *generation)

    Allocate one or more blocks of data and/or a dinode

    :param struct gfs2_inode \*ip:
        the inode to allocate the block for

    :param u64 \*bn:
        Used to return the starting block number

    :param unsigned int \*nblocks:
        requested number of blocks/extent length (value/result)

    :param bool dinode:
        1 if we're allocating a dinode block, else 0

    :param u64 \*generation:
        the generation number of the inode

.. _`gfs2_alloc_blocks.return`:

Return
------

0 or error

.. _`__gfs2_free_blocks`:

__gfs2_free_blocks
==================

.. c:function:: void __gfs2_free_blocks(struct gfs2_inode *ip, u64 bstart, u32 blen, int meta)

    free a contiguous run of block(s)

    :param struct gfs2_inode \*ip:
        the inode these blocks are being freed from

    :param u64 bstart:
        first block of a run of contiguous blocks

    :param u32 blen:
        the length of the block run

    :param int meta:
        1 if the blocks represent metadata

.. _`gfs2_free_meta`:

gfs2_free_meta
==============

.. c:function:: void gfs2_free_meta(struct gfs2_inode *ip, u64 bstart, u32 blen)

    free a contiguous run of data block(s)

    :param struct gfs2_inode \*ip:
        the inode these blocks are being freed from

    :param u64 bstart:
        first block of a run of contiguous blocks

    :param u32 blen:
        the length of the block run

.. _`gfs2_check_blk_type`:

gfs2_check_blk_type
===================

.. c:function:: int gfs2_check_blk_type(struct gfs2_sbd *sdp, u64 no_addr, unsigned int type)

    Check the type of a block

    :param struct gfs2_sbd \*sdp:
        The superblock

    :param u64 no_addr:
        The block number to check

    :param unsigned int type:
        The block type we are looking for

.. _`gfs2_check_blk_type.return`:

Return
------

0 if the block type matches the expected type
-ESTALE if it doesn't match
or -ve errno if something went wrong while checking

.. _`gfs2_rlist_add`:

gfs2_rlist_add
==============

.. c:function:: void gfs2_rlist_add(struct gfs2_inode *ip, struct gfs2_rgrp_list *rlist, u64 block)

    add a RG to a list of RGs

    :param struct gfs2_inode \*ip:
        the inode

    :param struct gfs2_rgrp_list \*rlist:
        the list of resource groups

    :param u64 block:
        the block

.. _`gfs2_rlist_add.description`:

Description
-----------

Figure out what RG a block belongs to and add that RG to the list

.. _`gfs2_rlist_add.fixme`:

FIXME
-----

Don't use NOFAIL

.. _`gfs2_rlist_alloc`:

gfs2_rlist_alloc
================

.. c:function:: void gfs2_rlist_alloc(struct gfs2_rgrp_list *rlist, unsigned int state)

    all RGs have been added to the rlist, now allocate and initialize an array of glock holders for them

    :param struct gfs2_rgrp_list \*rlist:
        the list of resource groups

    :param unsigned int state:
        the lock state to acquire the RG lock in

.. _`gfs2_rlist_alloc.fixme`:

FIXME
-----

Don't use NOFAIL

.. _`gfs2_rlist_free`:

gfs2_rlist_free
===============

.. c:function:: void gfs2_rlist_free(struct gfs2_rgrp_list *rlist)

    free a resource group list

    :param struct gfs2_rgrp_list \*rlist:
        the list of resource groups

.. This file was automatic generated / don't edit.

