.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/indirect.c

.. _`ext4_block_to_path`:

ext4_block_to_path
==================

.. c:function:: int ext4_block_to_path(struct inode *inode, ext4_lblk_t i_block, ext4_lblk_t offsets[4], int *boundary)

    parse the block number into array of offsets

    :param struct inode \*inode:
        inode in question (we are only interested in its superblock)

    :param ext4_lblk_t i_block:
        block number to be parsed

    :param ext4_lblk_t offsets:
        array to store the offsets in

    :param int \*boundary:
        set this non-zero if the referred-to block is likely to be
        followed (on disk) by an indirect block.

.. _`ext4_block_to_path.description`:

Description
-----------

To store the locations of file's data ext4 uses a data structure common
for UNIX filesystems - tree of pointers anchored in the inode, with
data blocks at leaves and indirect blocks in intermediate nodes.
This function translates the block number into path in that tree -
return value is the path length and \ ``offsets``\ [n] is the offset of
pointer to (n+1)th node in the nth one. If \ ``block``\  is out of range
(negative or too large) warning is printed and zero returned.

.. _`ext4_block_to_path.note`:

Note
----

function doesn't find node addresses, so no IO is needed. All
we need to know is the capacity of indirect blocks (taken from the
inode->i_sb).

.. _`ext4_get_branch`:

ext4_get_branch
===============

.. c:function:: Indirect *ext4_get_branch(struct inode *inode, int depth, ext4_lblk_t *offsets, Indirect chain[4], int *err)

    read the chain of indirect blocks leading to data

    :param struct inode \*inode:
        inode in question

    :param int depth:
        depth of the chain (1 - direct pointer, etc.)

    :param ext4_lblk_t \*offsets:
        offsets of pointers in inode/indirect blocks

    :param Indirect chain:
        place to store the result

    :param int \*err:
        here we store the error value

.. _`ext4_get_branch.description`:

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
(pointer to last triple returned, \*\ ``err``\  == 0)
or when it gets an IO error reading an indirect block
(ditto, \*\ ``err``\  == -EIO)
or when it reads all \ ``depth``\ -1 indirect blocks successfully and finds
the whole chain, all way to the data (returns \ ``NULL``\ , \*err == 0).

Need to be called with
down_read(\ :c:type:`struct EXT4_I <EXT4_I>`(inode)->i_data_sem)

.. _`ext4_find_near`:

ext4_find_near
==============

.. c:function:: ext4_fsblk_t ext4_find_near(struct inode *inode, Indirect *ind)

    find a place for allocation with sufficient locality

    :param struct inode \*inode:
        owner

    :param Indirect \*ind:
        descriptor of indirect block.

.. _`ext4_find_near.description`:

Description
-----------

This function returns the preferred place for block allocation.
It is used when heuristic for sequential allocation fails.

.. _`ext4_find_near.rules-are`:

Rules are
---------

+ if there is a block to the left of our position - allocate near it.
+ if pointer will live in indirect block - allocate near that block.
+ if pointer will live in inode - allocate in the same
cylinder group.

In the latter case we colour the starting block by the callers PID to
prevent it from clashing with concurrent allocations for a different inode
in the same block group.   The PID is used here so that functionally related
files will be close-by on-disk.

Caller must make sure that \ ``ind``\  is valid and will stay that way.

.. _`ext4_find_goal`:

ext4_find_goal
==============

.. c:function:: ext4_fsblk_t ext4_find_goal(struct inode *inode, ext4_lblk_t block, Indirect *partial)

    find a preferred place for allocation.

    :param struct inode \*inode:
        owner

    :param ext4_lblk_t block:
        block we want

    :param Indirect \*partial:
        pointer to the last triple within a chain

.. _`ext4_find_goal.description`:

Description
-----------

Normally this function find the preferred place for block allocation,
returns it.
Because this is only used for non-extent files, we limit the block nr
to 32 bits.

.. _`ext4_blks_to_allocate`:

ext4_blks_to_allocate
=====================

.. c:function:: int ext4_blks_to_allocate(Indirect *branch, int k, unsigned int blks, int blocks_to_boundary)

    Look up the block map and count the number of direct blocks need to be allocated for the given branch.

    :param Indirect \*branch:
        chain of indirect blocks

    :param int k:
        number of blocks need for indirect blocks

    :param unsigned int blks:
        number of data blocks to be mapped.

    :param int blocks_to_boundary:
        the offset in the indirect block

.. _`ext4_blks_to_allocate.description`:

Description
-----------

return the total number of blocks to be allocate, including the
direct and indirect blocks.

.. _`ext4_alloc_branch`:

ext4_alloc_branch
=================

.. c:function:: int ext4_alloc_branch(handle_t *handle, struct ext4_allocation_request *ar, int indirect_blks, ext4_lblk_t *offsets, Indirect *branch)

    allocate and set up a chain of blocks.

    :param handle_t \*handle:
        handle for this transaction

    :param struct ext4_allocation_request \*ar:
        *undescribed*

    :param int indirect_blks:
        number of allocated indirect blocks

    :param ext4_lblk_t \*offsets:
        offsets (in the blocks) to store the pointers to next.

    :param Indirect \*branch:
        place to store the chain in.

.. _`ext4_alloc_branch.description`:

Description
-----------

This function allocates blocks, zeroes out all but the last one,
links them into chain and (if we are synchronous) writes them to disk.
In other words, it prepares a branch that can be spliced onto the
inode. It stores the information about that chain in the branch[], in
the same format as \ :c:func:`ext4_get_branch`\  would do. We are calling it after
we had read the existing part of chain and partial points to the last
triple of that (one with zero ->key). Upon the exit we have the same
picture as after the successful \ :c:func:`ext4_get_block`\ , except that in one
place chain is disconnected - \*branch->p is still zero (we did not
set the last link), but branch->key contains the number that should
be placed into \*branch->p to fill that gap.

If allocation fails we free all blocks we've allocated (and forget
their buffer_heads) and return the error value the from failed
\ :c:func:`ext4_alloc_block`\  (normally -ENOSPC). Otherwise we set the chain
as described above and return 0.

.. _`ext4_splice_branch`:

ext4_splice_branch
==================

.. c:function:: int ext4_splice_branch(handle_t *handle, struct ext4_allocation_request *ar, Indirect *where, int num)

    splice the allocated branch onto inode.

    :param handle_t \*handle:
        handle for this transaction

    :param struct ext4_allocation_request \*ar:
        *undescribed*

    :param Indirect \*where:
        location of missing link

    :param int num:
        number of indirect blocks we are adding

.. _`ext4_splice_branch.description`:

Description
-----------

This function fills the missing link and does all housekeeping needed in
inode (->i_blocks, etc.). In case of success we end up with the full
chain to new block and return 0.

.. _`ext4_find_shared`:

ext4_find_shared
================

.. c:function:: Indirect *ext4_find_shared(struct inode *inode, int depth, ext4_lblk_t offsets[4], Indirect chain[4], __le32 *top)

    find the indirect blocks for partial truncation.

    :param struct inode \*inode:
        inode in question

    :param int depth:
        depth of the affected branch

    :param ext4_lblk_t offsets:
        offsets of pointers in that branch (see ext4_block_to_path)

    :param Indirect chain:
        place to store the pointers to partial indirect blocks

    :param __le32 \*top:
        place to the (detached) top of branch

.. _`ext4_find_shared.description`:

Description
-----------

This is a helper function used by \ :c:func:`ext4_truncate`\ .

When we do \ :c:func:`truncate`\  we may have to clean the ends of several
indirect blocks but leave the blocks themselves alive. Block is
partially truncated if some data below the new i_size is referred
from it (and it is on the path to the first completely truncated
data block, indeed).  We have to free the top of that path along
with everything to the right of the path. Since no allocation
past the truncation point is possible until \ :c:func:`ext4_truncate`\ 
finishes, we may safely do the latter, but top of branch may
require special attention - pageout below the truncation point
might try to populate it.

We atomically detach the top of branch from the tree, store the
block number of its root in \*\ ``top``\ , pointers to buffer_heads of
partially truncated blocks - in \ ``chain``\ [].bh and pointers to
their last elements that should not be removed - in
\ ``chain``\ [].p. Return value is the pointer to last filled element
of \ ``chain``\ .

.. _`ext4_find_shared.the-work-left-to-caller-to-do-the-actual-freeing-of-subtrees`:

The work left to caller to do the actual freeing of subtrees
------------------------------------------------------------

a) free the subtree starting from \*\ ``top``\ 
b) free the subtrees whose roots are stored in
(\ ``chain``\ [i].p+1 .. end of \ ``chain``\ [i].bh->b_data)
c) free the subtrees growing from the inode past the \ ``chain``\ [0].

.. _`ext4_free_data`:

ext4_free_data
==============

.. c:function:: void ext4_free_data(handle_t *handle, struct inode *inode, struct buffer_head *this_bh, __le32 *first, __le32 *last)

    free a list of data blocks

    :param handle_t \*handle:
        handle for this transaction

    :param struct inode \*inode:
        inode we are dealing with

    :param struct buffer_head \*this_bh:
        indirect buffer_head which contains \*\ ``first``\  and \*\ ``last``\ 

    :param __le32 \*first:
        array of block numbers

    :param __le32 \*last:
        points immediately past the end of array

.. _`ext4_free_data.description`:

Description
-----------

We are freeing all blocks referred from that array (numbers are stored as
little-endian 32-bit) and updating \ ``inode``\ ->i_blocks appropriately.

We accumulate contiguous runs of blocks to free.  Conveniently, if these
blocks are contiguous then releasing them at one time will only affect one
or two bitmap blocks (+ group descriptor(s) and superblock) and we won't
actually use a lot of journal space.

\ ``this_bh``\  will be \ ``NULL``\  if \ ``first``\  and \ ``last``\  point into the inode's direct
block pointers.

.. _`ext4_free_branches`:

ext4_free_branches
==================

.. c:function:: void ext4_free_branches(handle_t *handle, struct inode *inode, struct buffer_head *parent_bh, __le32 *first, __le32 *last, int depth)

    free an array of branches

    :param handle_t \*handle:
        JBD handle for this transaction

    :param struct inode \*inode:
        inode we are dealing with

    :param struct buffer_head \*parent_bh:
        the buffer_head which contains \*\ ``first``\  and \*\ ``last``\ 

    :param __le32 \*first:
        array of block numbers

    :param __le32 \*last:
        pointer immediately past the end of array

    :param int depth:
        depth of the branches to free

.. _`ext4_free_branches.description`:

Description
-----------

We are freeing all blocks referred from these branches (numbers are
stored as little-endian 32-bit) and updating \ ``inode``\ ->i_blocks
appropriately.

.. _`ext4_ind_remove_space`:

ext4_ind_remove_space
=====================

.. c:function:: int ext4_ind_remove_space(handle_t *handle, struct inode *inode, ext4_lblk_t start, ext4_lblk_t end)

    remove space from the range

    :param handle_t \*handle:
        JBD handle for this transaction

    :param struct inode \*inode:
        inode we are dealing with

    :param ext4_lblk_t start:
        First block to remove

    :param ext4_lblk_t end:
        One block after the last block to remove (exclusive)

.. _`ext4_ind_remove_space.description`:

Description
-----------

Free the blocks in the defined range (end is exclusive endpoint of
range). This is used by \ :c:func:`ext4_punch_hole`\ .

.. This file was automatic generated / don't edit.

