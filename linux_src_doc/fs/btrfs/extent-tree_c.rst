.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/extent-tree.c

.. _`may_commit_transaction`:

may_commit_transaction
======================

.. c:function:: int may_commit_transaction(struct btrfs_fs_info *fs_info, struct btrfs_space_info *space_info)

    possibly commit the transaction if its ok to \ ``root``\  - the root we're allocating for \ ``bytes``\  - the number of bytes we want to reserve \ ``force``\  - force the commit

    :param struct btrfs_fs_info \*fs_info:
        *undescribed*

    :param struct btrfs_space_info \*space_info:
        *undescribed*

.. _`may_commit_transaction.description`:

Description
-----------

This will check to make sure that committing the transaction will actually
get us somewhere and then commit the transaction if it does.  Otherwise it
will return -ENOSPC.

.. _`__reserve_metadata_bytes`:

\__reserve_metadata_bytes
=========================

.. c:function:: int __reserve_metadata_bytes(struct btrfs_fs_info *fs_info, struct btrfs_space_info *space_info, u64 orig_bytes, enum btrfs_reserve_flush_enum flush, bool system_chunk)

    try to reserve bytes from the block_rsv's space \ ``root``\  - the root we're allocating for \ ``space_info``\  - the space info we want to allocate from \ ``orig_bytes``\  - the number of bytes we want \ ``flush``\  - whether or not we can flush to make our reservation

    :param struct btrfs_fs_info \*fs_info:
        *undescribed*

    :param struct btrfs_space_info \*space_info:
        *undescribed*

    :param u64 orig_bytes:
        *undescribed*

    :param enum btrfs_reserve_flush_enum flush:
        *undescribed*

    :param bool system_chunk:
        *undescribed*

.. _`__reserve_metadata_bytes.description`:

Description
-----------

This will reserve orig_bytes number of bytes from the space info associated
with the block_rsv.  If there is not enough space it will make an attempt to
flush out space to make room.  It will do this by flushing delalloc if
possible or committing the transaction.  If flush is 0 then no attempts to
regain reservations will be made and this will fail if there is not enough
space already.

.. _`reserve_metadata_bytes`:

reserve_metadata_bytes
======================

.. c:function:: int reserve_metadata_bytes(struct btrfs_root *root, struct btrfs_block_rsv *block_rsv, u64 orig_bytes, enum btrfs_reserve_flush_enum flush)

    try to reserve bytes from the block_rsv's space \ ``root``\  - the root we're allocating for \ ``block_rsv``\  - the block_rsv we're allocating for \ ``orig_bytes``\  - the number of bytes we want \ ``flush``\  - whether or not we can flush to make our reservation

    :param struct btrfs_root \*root:
        *undescribed*

    :param struct btrfs_block_rsv \*block_rsv:
        *undescribed*

    :param u64 orig_bytes:
        *undescribed*

    :param enum btrfs_reserve_flush_enum flush:
        *undescribed*

.. _`reserve_metadata_bytes.description`:

Description
-----------

This will reserve orgi_bytes number of bytes from the space info associated
with the block_rsv.  If there is not enough space it will make an attempt to
flush out space to make room.  It will do this by flushing delalloc if
possible or committing the transaction.  If flush is 0 then no attempts to
regain reservations will be made and this will fail if there is not enough
space already.

.. _`btrfs_inode_rsv_refill`:

btrfs_inode_rsv_refill
======================

.. c:function:: int btrfs_inode_rsv_refill(struct btrfs_inode *inode, enum btrfs_reserve_flush_enum flush)

    refill the inode block rsv. \ ``inode``\  - the inode we are refilling. \ ``flush``\  - the flusing restriction.

    :param struct btrfs_inode \*inode:
        *undescribed*

    :param enum btrfs_reserve_flush_enum flush:
        *undescribed*

.. _`btrfs_inode_rsv_refill.description`:

Description
-----------

Essentially the same as btrfs_block_rsv_refill, except it uses the
block_rsv->size as the minimum size.  We'll either refill the missing amount
or return if we already have enough space.  This will also handle the resreve
tracepoint for the reserved amount.

.. _`btrfs_inode_rsv_release`:

btrfs_inode_rsv_release
=======================

.. c:function:: void btrfs_inode_rsv_release(struct btrfs_inode *inode)

    release any excessive reservation. \ ``inode``\  - the inode we need to release from.

    :param struct btrfs_inode \*inode:
        *undescribed*

.. _`btrfs_inode_rsv_release.description`:

Description
-----------

This is the same as btrfs_block_rsv_release, except that it handles the
tracepoint for the reservation.

.. _`btrfs_delalloc_release_metadata`:

btrfs_delalloc_release_metadata
===============================

.. c:function:: void btrfs_delalloc_release_metadata(struct btrfs_inode *inode, u64 num_bytes)

    release a metadata reservation for an inode

    :param struct btrfs_inode \*inode:
        the inode to release the reservation for.

    :param u64 num_bytes:
        the number of bytes we are releasing.

.. _`btrfs_delalloc_release_metadata.description`:

Description
-----------

This will release the metadata reservation for an inode.  This can be called
once we complete IO for a given set of bytes to release their metadata
reservations, or on error for the same reason.

.. _`btrfs_delalloc_release_extents`:

btrfs_delalloc_release_extents
==============================

.. c:function:: void btrfs_delalloc_release_extents(struct btrfs_inode *inode, u64 num_bytes)

    release our outstanding_extents

    :param struct btrfs_inode \*inode:
        the inode to balance the reservation for.

    :param u64 num_bytes:
        the number of bytes we originally reserved with

.. _`btrfs_delalloc_release_extents.description`:

Description
-----------

When we reserve space we increase outstanding_extents for the extents we may
add.  Once we've set the range as delalloc or created our ordered extents we
have outstanding_extents to track the real usage, so we use this to free our
temporarily tracked outstanding_extents.  This \_must\_ be used in conjunction
with btrfs_delalloc_reserve_metadata.

.. _`btrfs_delalloc_reserve_space`:

btrfs_delalloc_reserve_space
============================

.. c:function:: int btrfs_delalloc_reserve_space(struct inode *inode, struct extent_changeset **reserved, u64 start, u64 len)

    reserve data and metadata space for delalloc

    :param struct inode \*inode:
        inode we're writing to

    :param struct extent_changeset \*\*reserved:
        mandatory parameter, record actually reserved qgroup ranges of
        current reservation.

    :param u64 start:
        start range we are writing to

    :param u64 len:
        how long the range we are writing to

.. _`btrfs_delalloc_reserve_space.description`:

Description
-----------

This will do the following things

o reserve space in data space info for num bytes
and reserve precious corresponding qgroup space
(Done in check_data_free_space)

o reserve space for metadata space, based on the number of outstanding
extents and how much csums will be needed
also reserve metadata space in a per root over-reserve method.
o add to the inodes->delalloc_bytes
o add it to the fs_info's delalloc inodes list.
(Above 3 all done in delalloc_reserve_metadata)

Return 0 for success
Return <0 for error(-ENOSPC or -EQUOT)

.. _`btrfs_delalloc_release_space`:

btrfs_delalloc_release_space
============================

.. c:function:: void btrfs_delalloc_release_space(struct inode *inode, struct extent_changeset *reserved, u64 start, u64 len)

    release data and metadata space for delalloc

    :param struct inode \*inode:
        inode we're releasing space for

    :param struct extent_changeset \*reserved:
        *undescribed*

    :param u64 start:
        start position of the space already reserved

    :param u64 len:
        the len of the space already reserved

.. _`btrfs_delalloc_release_space.description`:

Description
-----------

This function will release the metadata space that was not used and will
decrement ->delalloc_bytes and remove it from the fs_info delalloc_inodes
list if there are no delalloc bytes left.
Also it will handle the qgroup reserved space.

.. _`btrfs_add_reserved_bytes`:

btrfs_add_reserved_bytes
========================

.. c:function:: int btrfs_add_reserved_bytes(struct btrfs_block_group_cache *cache, u64 ram_bytes, u64 num_bytes, int delalloc)

    update the block_group and space info counters

    :param struct btrfs_block_group_cache \*cache:
        The cache we are manipulating

    :param u64 ram_bytes:
        The number of bytes of file content, and will be same to
        \ ``num_bytes``\  except for the compress path.

    :param u64 num_bytes:
        The number of bytes in question

    :param int delalloc:
        The blocks are allocated for the delalloc write

.. _`btrfs_add_reserved_bytes.description`:

Description
-----------

This is called by the allocator when it reserves space. If this is a
reservation and the block group has become read only we cannot make the
reservation and return -EAGAIN, otherwise this function always succeeds.

.. _`btrfs_free_reserved_bytes`:

btrfs_free_reserved_bytes
=========================

.. c:function:: int btrfs_free_reserved_bytes(struct btrfs_block_group_cache *cache, u64 num_bytes, int delalloc)

    update the block_group and space info counters

    :param struct btrfs_block_group_cache \*cache:
        The cache we are manipulating

    :param u64 num_bytes:
        The number of bytes in question

    :param int delalloc:
        The blocks are allocated for the delalloc write

.. _`btrfs_free_reserved_bytes.description`:

Description
-----------

This is called by somebody who is freeing space that was never actually used
on disk.  For example if you reserve some space for a new leaf in transaction
A and before transaction A commits you free that leaf, you call this with
reserve set to 0 in order to clear the reservation.

.. This file was automatic generated / don't edit.

