.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/extent-tree.c

.. _`may_commit_transaction`:

may_commit_transaction
======================

.. c:function:: int may_commit_transaction(struct btrfs_root *root, struct btrfs_space_info *space_info, u64 bytes, int force)

    possibly commit the transaction if its ok to \ ``root``\  - the root we're allocating for \ ``bytes``\  - the number of bytes we want to reserve \ ``force``\  - force the commit

    :param struct btrfs_root \*root:
        *undescribed*

    :param struct btrfs_space_info \*space_info:
        *undescribed*

    :param u64 bytes:
        *undescribed*

    :param int force:
        *undescribed*

.. _`may_commit_transaction.description`:

Description
-----------

This will check to make sure that committing the transaction will actually
get us somewhere and then commit the transaction if it does.  Otherwise it
will return -ENOSPC.

.. _`__reserve_metadata_bytes`:

__reserve_metadata_bytes
========================

.. c:function:: int __reserve_metadata_bytes(struct btrfs_root *root, struct btrfs_space_info *space_info, u64 orig_bytes, enum btrfs_reserve_flush_enum flush)

    try to reserve bytes from the block_rsv's space \ ``root``\  - the root we're allocating for \ ``space_info``\  - the space info we want to allocate from \ ``orig_bytes``\  - the number of bytes we want \ ``flush``\  - whether or not we can flush to make our reservation

    :param struct btrfs_root \*root:
        *undescribed*

    :param struct btrfs_space_info \*space_info:
        *undescribed*

    :param u64 orig_bytes:
        *undescribed*

    :param enum btrfs_reserve_flush_enum flush:
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

.. _`drop_outstanding_extent`:

drop_outstanding_extent
=======================

.. c:function:: unsigned drop_outstanding_extent(struct inode *inode, u64 num_bytes)

    drop an outstanding extent

    :param struct inode \*inode:
        the inode we're dropping the extent for

    :param u64 num_bytes:
        the number of bytes we're releasing.

.. _`drop_outstanding_extent.description`:

Description
-----------

This is called when we are freeing up an outstanding extent, either called
after an error or after an extent is written.  This will return the number of
reserved extents that need to be freed.  This must be called with
BTRFS_I(inode)->lock held.

.. _`calc_csum_metadata_size`:

calc_csum_metadata_size
=======================

.. c:function:: u64 calc_csum_metadata_size(struct inode *inode, u64 num_bytes, int reserve)

    return the amount of metadata space that must be reserved/freed for the given bytes.

    :param struct inode \*inode:
        the inode we're manipulating

    :param u64 num_bytes:
        the number of bytes in question

    :param int reserve:
        1 if we are reserving space, 0 if we are freeing space

.. _`calc_csum_metadata_size.description`:

Description
-----------

This adjusts the number of csum_bytes in the inode and then returns the
correct amount of metadata that must either be reserved or freed.  We
calculate how many checksums we can fit into one leaf and then divide the
number of bytes that will need to be checksumed by this value to figure out
how many checksums will be required.  If we are adding bytes then the number
may go up and we will return the number of additional bytes that must be
reserved.  If it is going down we will return the number of bytes that must
be freed.

This must be called with BTRFS_I(inode)->lock held.

.. _`btrfs_delalloc_release_metadata`:

btrfs_delalloc_release_metadata
===============================

.. c:function:: void btrfs_delalloc_release_metadata(struct inode *inode, u64 num_bytes)

    release a metadata reservation for an inode

    :param struct inode \*inode:
        the inode to release the reservation for

    :param u64 num_bytes:
        the number of bytes we're releasing

.. _`btrfs_delalloc_release_metadata.description`:

Description
-----------

This will release the metadata reservation for an inode.  This can be called
once we complete IO for a given set of bytes to release their metadata
reservations.

.. _`btrfs_delalloc_reserve_space`:

btrfs_delalloc_reserve_space
============================

.. c:function:: int btrfs_delalloc_reserve_space(struct inode *inode, u64 start, u64 len)

    reserve data and metadata space for delalloc

    :param struct inode \*inode:
        inode we're writing to

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

.. c:function:: void btrfs_delalloc_release_space(struct inode *inode, u64 start, u64 len)

    release data and metadata space for delalloc

    :param struct inode \*inode:
        inode we're releasing space for

    :param u64 start:
        start position of the space already reserved

    :param u64 len:
        the len of the space already reserved

.. _`btrfs_delalloc_release_space.description`:

Description
-----------

This must be matched with a call to btrfs_delalloc_reserve_space.  This is
called in the case that we don't need the metadata AND data reservations
anymore.  So if there is an error or we insert an inline extent.

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

This is called by the allocator when it reserves space. Metadata
reservations should be called with RESERVE_ALLOC so we do the proper
ENOSPC accounting.  For data we handle the reservation through clearing the
delalloc bits in the io_tree.  We have to do this since we could end up
allocating less disk space for the amount of data we have reserved in the
case of compression.

If this is a reservation and the block group has become read only we cannot
make the reservation and return -EAGAIN, otherwise this function always
succeeds.

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

