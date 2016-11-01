.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext2/inode.c

.. _`ext2_block_to_path`:

ext2_block_to_path
==================

.. c:function:: int ext2_block_to_path(struct inode *inode, long i_block, int offsets[4], int *boundary)

    parse the block number into array of offsets

    :param struct inode \*inode:
        inode in question (we are only interested in its superblock)

    :param long i_block:
        block number to be parsed

    :param int offsets:
        array to store the offsets in

    :param int \*boundary:
        set this non-zero if the referred-to block is likely to be
        followed (on disk) by an indirect block.
        To store the locations of file's data ext2 uses a data structure common
        for UNIX filesystems - tree of pointers anchored in the inode, with
        data blocks at leaves and indirect blocks in intermediate nodes.
        This function translates the block number into path in that tree -
        return value is the path length and \ ``offsets``\ [n] is the offset of
        pointer to (n+1)th node in the nth one. If \ ``block``\  is out of range
        (negative or too large) warning is printed and zero returned.

.. _`ext2_block_to_path.note`:

Note
----

function doesn't find node addresses, so no IO is needed. All
we need to know is the capacity of indirect blocks (taken from the
inode->i_sb).

.. _`ext2_get_branch`:

ext2_get_branch
===============

.. c:function:: Indirect *ext2_get_branch(struct inode *inode, int depth, int *offsets, Indirect chain[4], int *err)

    read the chain of indirect blocks leading to data

    :param struct inode \*inode:
        inode in question

    :param int depth:
        depth of the chain (1 - direct pointer, etc.)

    :param int \*offsets:
        offsets of pointers in inode/indirect blocks

    :param Indirect chain:
        place to store the result

    :param int \*err:
        here we store the error value

.. _`ext2_get_branch.description`:

Description
-----------

Function fills the array of triples <key, p, bh> and returns \ ``NULL``\ 
if everything went OK or the pointer to the last filled triple
(incomplete one) otherwise. Upon the return chain[i].key contains
the number of (i+1)-th block in the chain (as it is stored in memory,
i.e. little-endian 32-bit), chain[i].p contains the address of that
number (it points into struct inode for i==0 and into the bh->b_data
for i>0) and chain[i].bh points to the buffer_head of i-th indirect
block for i>0 and NULL for i==0. In other words, it holds the block
numbers of the chain, addresses they were taken from (and where we can
verify that chain did not change) and buffer_heads hosting these
numbers.

Function stops when it stumbles upon zero pointer (absent block)
(pointer to last triple returned, \*@err == 0)
or when it gets an IO error reading an indirect block
(ditto, \*@err == -EIO)
or when it notices that chain had been changed while it was reading
(ditto, \*@err == -EAGAIN)
or when it reads all \ ``depth``\ -1 indirect blocks successfully and finds
the whole chain, all way to the data (returns \ ``NULL``\ , \*err == 0).

.. _`ext2_find_near`:

ext2_find_near
==============

.. c:function:: ext2_fsblk_t ext2_find_near(struct inode *inode, Indirect *ind)

    find a place for allocation with sufficient locality

    :param struct inode \*inode:
        owner

    :param Indirect \*ind:
        descriptor of indirect block.

.. _`ext2_find_near.description`:

Description
-----------

This function returns the preferred place for block allocation.
It is used when heuristic for sequential allocation fails.

.. _`ext2_find_near.rules-are`:

Rules are
---------

+ if there is a block to the left of our position - allocate near it.
+ if pointer will live in indirect block - allocate near that block.
+ if pointer will live in inode - allocate in the same cylinder group.

In the latter case we colour the starting block by the callers PID to
prevent it from clashing with concurrent allocations for a different inode
in the same block group.   The PID is used here so that functionally related
files will be close-by on-disk.

Caller must make sure that \ ``ind``\  is valid and will stay that way.

.. _`ext2_find_goal`:

ext2_find_goal
==============

.. c:function:: ext2_fsblk_t ext2_find_goal(struct inode *inode, long block, Indirect *partial)

    find a preferred place for allocation.

    :param struct inode \*inode:
        owner

    :param long block:
        block we want

    :param Indirect \*partial:
        pointer to the last triple within a chain

.. _`ext2_find_goal.description`:

Description
-----------

Returns preferred place for a block (the goal).

.. _`ext2_blks_to_allocate`:

ext2_blks_to_allocate
=====================

.. c:function:: int ext2_blks_to_allocate(Indirect *branch, int k, unsigned long blks, int blocks_to_boundary)

    Look up the block map and count the number of direct blocks need to be allocated for the given branch.

    :param Indirect \*branch:
        chain of indirect blocks

    :param int k:
        number of blocks need for indirect blocks

    :param unsigned long blks:
        number of data blocks to be mapped.

    :param int blocks_to_boundary:
        the offset in the indirect block

.. _`ext2_blks_to_allocate.description`:

Description
-----------

return the total number of blocks to be allocate, including the
direct and indirect blocks.

.. _`ext2_alloc_blocks`:

ext2_alloc_blocks
=================

.. c:function:: int ext2_alloc_blocks(struct inode *inode, ext2_fsblk_t goal, int indirect_blks, int blks, ext2_fsblk_t new_blocks[4], int *err)

    multiple allocate blocks needed for a branch

    :param struct inode \*inode:
        *undescribed*

    :param ext2_fsblk_t goal:
        *undescribed*

    :param int indirect_blks:
        the number of blocks need to allocate for indirect
        blocks

    :param int blks:
        on return it will store the total number of allocated
        direct blocks

    :param ext2_fsblk_t new_blocks:
        on return it will store the new block numbers for
        the indirect blocks(if needed) and the first direct block,

    :param int \*err:
        *undescribed*

.. _`ext2_alloc_branch`:

ext2_alloc_branch
=================

.. c:function:: int ext2_alloc_branch(struct inode *inode, int indirect_blks, int *blks, ext2_fsblk_t goal, int *offsets, Indirect *branch)

    allocate and set up a chain of blocks.

    :param struct inode \*inode:
        owner

    :param int indirect_blks:
        *undescribed*

    :param int \*blks:
        *undescribed*

    :param ext2_fsblk_t goal:
        *undescribed*

    :param int \*offsets:
        offsets (in the blocks) to store the pointers to next.

    :param Indirect \*branch:
        place to store the chain in.

.. _`ext2_alloc_branch.description`:

Description
-----------

This function allocates \ ``num``\  blocks, zeroes out all but the last one,
links them into chain and (if we are synchronous) writes them to disk.
In other words, it prepares a branch that can be spliced onto the
inode. It stores the information about that chain in the branch[], in
the same format as \ :c:func:`ext2_get_branch`\  would do. We are calling it after
we had read the existing part of chain and partial points to the last
triple of that (one with zero ->key). Upon the exit we have the same
picture as after the successful \ :c:func:`ext2_get_block`\ , except that in one
place chain is disconnected - \*branch->p is still zero (we did not
set the last link), but branch->key contains the number that should
be placed into \*branch->p to fill that gap.

If allocation fails we free all blocks we've allocated (and forget
their buffer_heads) and return the error value the from failed
\ :c:func:`ext2_alloc_block`\  (normally -ENOSPC). Otherwise we set the chain
as described above and return 0.

.. _`ext2_splice_branch`:

ext2_splice_branch
==================

.. c:function:: void ext2_splice_branch(struct inode *inode, long block, Indirect *where, int num, int blks)

    splice the allocated branch onto inode.

    :param struct inode \*inode:
        owner

    :param long block:
        (logical) number of block we are adding

    :param Indirect \*where:
        location of missing link

    :param int num:
        number of indirect blocks we are adding

    :param int blks:
        number of direct blocks we are adding

.. _`ext2_splice_branch.description`:

Description
-----------

This function fills the missing link and does all housekeeping needed in
inode (->i_blocks, etc.). In case of success we end up with the full
chain to new block and return 0.

.. _`ext2_find_shared`:

ext2_find_shared
================

.. c:function:: Indirect *ext2_find_shared(struct inode *inode, int depth, int offsets[4], Indirect chain[4], __le32 *top)

    find the indirect blocks for partial truncation.

    :param struct inode \*inode:
        inode in question

    :param int depth:
        depth of the affected branch

    :param int offsets:
        offsets of pointers in that branch (see ext2_block_to_path)

    :param Indirect chain:
        place to store the pointers to partial indirect blocks

    :param __le32 \*top:
        place to the (detached) top of branch

.. _`ext2_find_shared.description`:

Description
-----------

This is a helper function used by \ :c:func:`ext2_truncate`\ .

When we do \ :c:func:`truncate`\  we may have to clean the ends of several indirect
blocks but leave the blocks themselves alive. Block is partially
truncated if some data below the new i_size is referred from it (and
it is on the path to the first completely truncated data block, indeed).
We have to free the top of that path along with everything to the right
of the path. Since no allocation past the truncation point is possible
until \ :c:func:`ext2_truncate`\  finishes, we may safely do the latter, but top
of branch may require special attention - pageout below the truncation
point might try to populate it.

We atomically detach the top of branch from the tree, store the block
number of its root in \*@top, pointers to buffer_heads of partially
truncated blocks - in \ ``chain``\ [].bh and pointers to their last elements
that should not be removed - in \ ``chain``\ [].p. Return value is the pointer
to last filled element of \ ``chain``\ .

.. _`ext2_find_shared.the-work-left-to-caller-to-do-the-actual-freeing-of-subtrees`:

The work left to caller to do the actual freeing of subtrees
------------------------------------------------------------

a) free the subtree starting from \*@top
b) free the subtrees whose roots are stored in
(@chain[i].p+1 .. end of \ ``chain``\ [i].bh->b_data)
c) free the subtrees growing from the inode past the \ ``chain``\ [0].p
(no partially truncated stuff there).

.. _`ext2_free_data`:

ext2_free_data
==============

.. c:function:: void ext2_free_data(struct inode *inode, __le32 *p, __le32 *q)

    free a list of data blocks

    :param struct inode \*inode:
        inode we are dealing with

    :param __le32 \*p:
        array of block numbers

    :param __le32 \*q:
        points immediately past the end of array

.. _`ext2_free_data.description`:

Description
-----------

We are freeing all blocks referred from that array (numbers are
stored as little-endian 32-bit) and updating \ ``inode``\ ->i_blocks
appropriately.

.. _`ext2_free_branches`:

ext2_free_branches
==================

.. c:function:: void ext2_free_branches(struct inode *inode, __le32 *p, __le32 *q, int depth)

    free an array of branches

    :param struct inode \*inode:
        inode we are dealing with

    :param __le32 \*p:
        array of block numbers

    :param __le32 \*q:
        pointer immediately past the end of array

    :param int depth:
        depth of the branches to free

.. _`ext2_free_branches.description`:

Description
-----------

We are freeing all blocks referred from these branches (numbers are
stored as little-endian 32-bit) and updating \ ``inode``\ ->i_blocks
appropriately.

.. This file was automatic generated / don't edit.

