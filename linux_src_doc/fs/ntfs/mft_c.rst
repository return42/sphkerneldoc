.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/mft.c

.. _`map_mft_record_page`:

map_mft_record_page
===================

.. c:function:: MFT_RECORD *map_mft_record_page(ntfs_inode *ni)

    NTFS kernel mft record operations. Part of the Linux-NTFS project.

    :param ntfs_inode \*ni:
        *undescribed*

.. _`map_mft_record_page.description`:

Description
-----------

Copyright (c) 2001-2012 Anton Altaparmakov and Tuxera Inc.
Copyright (c) 2002 Richard Russon

This program/include file is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program/include file is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program (in the main directory of the Linux-NTFS
distribution in the file COPYING); if not, write to the Free Software
Foundation,Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

.. _`map_mft_record`:

map_mft_record
==============

.. c:function:: MFT_RECORD *map_mft_record(ntfs_inode *ni)

    map, pin and lock an mft record

    :param ntfs_inode \*ni:
        ntfs inode whose MFT record to map

.. _`map_mft_record.description`:

Description
-----------

First, take the mrec_lock mutex.  We might now be sleeping, while waiting
for the mutex if it was already locked by someone else.

The page of the record is mapped using \ :c:func:`map_mft_record_page`\  before being
returned to the caller.

This in turn uses \ :c:func:`ntfs_map_page`\  to get the page containing the wanted mft
record (it in turn calls \ :c:func:`read_cache_page`\  which reads it in from disk if
necessary, increments the use count on the page so that it cannot disappear
under us and returns a reference to the page cache page).

If \ :c:func:`read_cache_page`\  invokes \ :c:func:`ntfs_readpage`\  to load the page from disk, it
sets PG_locked and clears PG_uptodate on the page. Once I/O has completed
and the post-read mst fixups on each mft record in the page have been
performed, the page gets PG_uptodate set and PG_locked cleared (this is done
in our asynchronous I/O completion handler \ :c:func:`end_buffer_read_mft_async`\ ).
\ :c:func:`ntfs_map_page`\  waits for PG_locked to become clear and checks if
PG_uptodate is set and returns an error code if not. This provides
sufficient protection against races when reading/using the page.

However there is the write mapping to think about. Doing the above described
checking here will be fine, because when initiating the write we will set
PG_locked and clear PG_uptodate making sure nobody is touching the page
contents. Doing the locking this way means that the commit to disk code in
the page cache code paths is automatically sufficiently locked with us as
we will not touch a page that has been locked or is not uptodate. The only
locking problem then is them locking the page while we are accessing it.

So that code will end up having to own the mrec_lock of all mft
records/inodes present in the page before I/O can proceed. In that case we
wouldn't need to bother with PG_locked and PG_uptodate as nobody will be
accessing anything without owning the mrec_lock mutex.  But we do need to
use them because of the \ :c:func:`read_cache_page`\  invocation and the code becomes so
much simpler this way that it is well worth it.

The mft record is now ours and we return a pointer to it. You need to check
the returned pointer with \ :c:func:`IS_ERR`\  and if that is true, \ :c:func:`PTR_ERR`\  will return
the error code.

.. _`map_mft_record.note`:

NOTE
----

Caller is responsible for setting the mft record dirty before calling
\ :c:func:`unmap_mft_record`\ . This is obviously only necessary if the caller really
modified the mft record...
Q: Do we want to recycle one of the VFS inode state bits instead?
A: No, the inode ones mean we want to change the mft record, not we want to
write it out.

.. _`unmap_mft_record_page`:

unmap_mft_record_page
=====================

.. c:function:: void unmap_mft_record_page(ntfs_inode *ni)

    unmap the page in which a specific mft record resides

    :param ntfs_inode \*ni:
        ntfs inode whose mft record page to unmap

.. _`unmap_mft_record_page.description`:

Description
-----------

This unmaps the page in which the mft record of the ntfs inode \ ``ni``\  is
situated and returns. This is a NOOP if highmem is not configured.

The unmap happens via \ :c:func:`ntfs_unmap_page`\  which in turn decrements the use
count on the page thus releasing it from the pinned state.

We do not actually unmap the page from memory of course, as that will be
done by the page cache code itself when memory pressure increases or
whatever.

.. _`unmap_mft_record`:

unmap_mft_record
================

.. c:function:: void unmap_mft_record(ntfs_inode *ni)

    release a mapped mft record

    :param ntfs_inode \*ni:
        ntfs inode whose MFT record to unmap

.. _`unmap_mft_record.description`:

Description
-----------

We release the page mapping and the mrec_lock mutex which unmaps the mft
record and releases it for others to get hold of. We also release the ntfs
inode by decrementing the ntfs inode reference count.

.. _`unmap_mft_record.note`:

NOTE
----

If caller has modified the mft record, it is imperative to set the mft
record dirty BEFORE calling \ :c:func:`unmap_mft_record`\ .

.. _`map_extent_mft_record`:

map_extent_mft_record
=====================

.. c:function:: MFT_RECORD *map_extent_mft_record(ntfs_inode *base_ni, MFT_REF mref, ntfs_inode **ntfs_ino)

    load an extent inode and attach it to its base

    :param ntfs_inode \*base_ni:
        base ntfs inode

    :param MFT_REF mref:
        mft reference of the extent inode to load

    :param ntfs_inode \*\*ntfs_ino:
        on successful return, pointer to the ntfs_inode structure

.. _`map_extent_mft_record.description`:

Description
-----------

Load the extent mft record \ ``mref``\  and attach it to its base inode \ ``base_ni``\ .
Return the mapped extent mft record if IS_ERR(result) is false.  Otherwise
PTR_ERR(result) gives the negative error code.

On successful return, \ ``ntfs_ino``\  contains a pointer to the ntfs_inode
structure of the mapped extent inode.

.. _`__mark_mft_record_dirty`:

__mark_mft_record_dirty
=======================

.. c:function:: void __mark_mft_record_dirty(ntfs_inode *ni)

    set the mft record and the page containing it dirty

    :param ntfs_inode \*ni:
        ntfs inode describing the mapped mft record

.. _`__mark_mft_record_dirty.description`:

Description
-----------

Internal function.  Users should call \ :c:func:`mark_mft_record_dirty`\  instead.

Set the mapped (extent) mft record of the (base or extent) ntfs inode \ ``ni``\ ,
as well as the page containing the mft record, dirty.  Also, mark the base
vfs inode dirty.  This ensures that any changes to the mft record are
written out to disk.

.. _`__mark_mft_record_dirty.note`:

NOTE
----

We only set I_DIRTY_SYNC and I_DIRTY_DATASYNC (and not I_DIRTY_PAGES)
on the base vfs inode, because even though file data may have been modified,
it is dirty in the inode meta data rather than the data page cache of the
inode, and thus there are no data pages that need writing out.  Therefore, a
full \ :c:func:`mark_inode_dirty`\  is overkill.  A \ :c:func:`mark_inode_dirty_sync`\ , on the
other hand, is not sufficient, because ->write_inode needs to be called even
in case of fdatasync. This needs to happen or the file data would not
necessarily hit the device synchronously, even though the vfs inode has the
O_SYNC flag set.  Also, I_DIRTY_DATASYNC simply "feels" better than just
I_DIRTY_SYNC, since the file data has not actually hit the block device yet,
which is not what I_DIRTY_SYNC on its own would suggest.

.. _`ntfs_sync_mft_mirror_umount`:

ntfs_sync_mft_mirror_umount
===========================

.. c:function:: int ntfs_sync_mft_mirror_umount(ntfs_volume *vol, const unsigned long mft_no, MFT_RECORD *m)

    synchronise an mft record to the mft mirror

    :param ntfs_volume \*vol:
        ntfs volume on which the mft record to synchronize resides

    :param const unsigned long mft_no:
        mft record number of mft record to synchronize

    :param MFT_RECORD \*m:
        mapped, mst protected (extent) mft record to synchronize

.. _`ntfs_sync_mft_mirror_umount.description`:

Description
-----------

Write the mapped, mst protected (extent) mft record \ ``m``\  with mft record
number \ ``mft_no``\  to the mft mirror ($MFTMirr) of the ntfs volume \ ``vol``\ ,
bypassing the page cache and the \ ``$MFTMirr``\  inode itself.

This function is only for use at umount time when the mft mirror inode has
already been disposed off.  We \ :c:func:`BUG`\  if we are called while the mft mirror
inode is still attached to the volume.

On success return 0.  On error return -errno.

.. _`ntfs_sync_mft_mirror_umount.note`:

NOTE
----

This function is not implemented yet as I am not convinced it can
actually be triggered considering the sequence of commits we do in super.c::
\ :c:func:`ntfs_put_super`\ .  But just in case we provide this place holder as the
alternative would be either to \ :c:func:`BUG`\  or to get a NULL pointer dereference
and Oops.

.. _`ntfs_sync_mft_mirror`:

ntfs_sync_mft_mirror
====================

.. c:function:: int ntfs_sync_mft_mirror(ntfs_volume *vol, const unsigned long mft_no, MFT_RECORD *m, int sync)

    synchronize an mft record to the mft mirror

    :param ntfs_volume \*vol:
        ntfs volume on which the mft record to synchronize resides

    :param const unsigned long mft_no:
        mft record number of mft record to synchronize

    :param MFT_RECORD \*m:
        mapped, mst protected (extent) mft record to synchronize

    :param int sync:
        if true, wait for i/o completion

.. _`ntfs_sync_mft_mirror.description`:

Description
-----------

Write the mapped, mst protected (extent) mft record \ ``m``\  with mft record
number \ ``mft_no``\  to the mft mirror ($MFTMirr) of the ntfs volume \ ``vol``\ .

On success return 0.  On error return -errno and set the volume errors flag
in the ntfs volume \ ``vol``\ .

.. _`ntfs_sync_mft_mirror.note`:

NOTE
----

We always perform synchronous i/o and ignore the \ ``sync``\  parameter.

.. _`ntfs_sync_mft_mirror.todo`:

TODO
----

If \ ``sync``\  is false, want to do truly asynchronous i/o, i.e. just
schedule i/o via ->writepage or do it via kntfsd or whatever.

.. _`write_mft_record_nolock`:

write_mft_record_nolock
=======================

.. c:function:: int write_mft_record_nolock(ntfs_inode *ni, MFT_RECORD *m, int sync)

    write out a mapped (extent) mft record

    :param ntfs_inode \*ni:
        ntfs inode describing the mapped (extent) mft record

    :param MFT_RECORD \*m:
        mapped (extent) mft record to write

    :param int sync:
        if true, wait for i/o completion

.. _`write_mft_record_nolock.description`:

Description
-----------

Write the mapped (extent) mft record \ ``m``\  described by the (regular or extent)
ntfs inode \ ``ni``\  to backing store.  If the mft record \ ``m``\  has a counterpart in
the mft mirror, that is also updated.

We only write the mft record if the ntfs inode \ ``ni``\  is dirty and the first
buffer belonging to its mft record is dirty, too.  We ignore the dirty state
of subsequent buffers because we could have raced with
fs/ntfs/aops.c::mark_ntfs_record_dirty().

On success, clean the mft record and return 0.  On error, leave the mft
record dirty and return -errno.

.. _`write_mft_record_nolock.note`:

NOTE
----

We always perform synchronous i/o and ignore the \ ``sync``\  parameter.
However, if the mft record has a counterpart in the mft mirror and \ ``sync``\  is
true, we write the mft record, wait for i/o completion, and only then write
the mft mirror copy.  This ensures that if the system crashes either the mft
or the mft mirror will contain a self-consistent mft record \ ``m``\ .  If \ ``sync``\  is
false on the other hand, we start i/o on both and then wait for completion
on them.  This provides a speedup but no longer guarantees that you will end
up with a self-consistent mft record in the case of a crash but if you asked
for asynchronous writing you probably do not care about that anyway.

.. _`write_mft_record_nolock.todo`:

TODO
----

If \ ``sync``\  is false, want to do truly asynchronous i/o, i.e. just
schedule i/o via ->writepage or do it via kntfsd or whatever.

.. _`ntfs_may_write_mft_record`:

ntfs_may_write_mft_record
=========================

.. c:function:: bool ntfs_may_write_mft_record(ntfs_volume *vol, const unsigned long mft_no, const MFT_RECORD *m, ntfs_inode **locked_ni)

    check if an mft record may be written out

    :param ntfs_volume \*vol:
        [IN]  ntfs volume on which the mft record to check resides

    :param const unsigned long mft_no:
        [IN]  mft record number of the mft record to check

    :param const MFT_RECORD \*m:
        [IN]  mapped mft record to check

    :param ntfs_inode \*\*locked_ni:
        [OUT] caller has to unlock this ntfs inode if one is returned

.. _`ntfs_may_write_mft_record.description`:

Description
-----------

Check if the mapped (base or extent) mft record \ ``m``\  with mft record number
\ ``mft_no``\  belonging to the ntfs volume \ ``vol``\  may be written out.  If necessary
and possible the ntfs inode of the mft record is locked and the base vfs
inode is pinned.  The locked ntfs inode is then returned in \ ``locked_ni``\ .  The
caller is responsible for unlocking the ntfs inode and unpinning the base
vfs inode.

Return 'true' if the mft record may be written out and 'false' if not.

The caller has locked the page and cleared the uptodate flag on it which
means that we can safely write out any dirty mft records that do not have
their inodes in icache as determined by \ :c:func:`ilookup5`\  as anyone
opening/creating such an inode would block when attempting to map the mft
record in \ :c:func:`read_cache_page`\  until we are finished with the write out.

.. _`ntfs_may_write_mft_record.here-is-a-description-of-the-tests-we-perform`:

Here is a description of the tests we perform
---------------------------------------------


If the inode is found in icache we know the mft record must be a base mft
record.  If it is dirty, we do not write it and return 'false' as the vfs
inode write paths will result in the access times being updated which would
cause the base mft record to be redirtied and written out again.  (We know
the access time update will modify the base mft record because Windows
chkdsk complains if the standard information attribute is not in the base
mft record.)

If the inode is in icache and not dirty, we attempt to lock the mft record
and if we find the lock was already taken, it is not safe to write the mft
record and we return 'false'.

If we manage to obtain the lock we have exclusive access to the mft record,
which also allows us safe writeout of the mft record.  We then set
\ ``locked_ni``\  to the locked ntfs inode and return 'true'.

Note we cannot just lock the mft record and sleep while waiting for the lock
because this would deadlock due to lock reversal (normally the mft record is
locked before the page is locked but we already have the page locked here
when we try to lock the mft record).

If the inode is not in icache we need to perform further checks.

If the mft record is not a FILE record or it is a base mft record, we can
safely write it and return 'true'.

We now know the mft record is an extent mft record.  We check if the inode
corresponding to its base mft record is in icache and obtain a reference to
it if it is.  If it is not, we can safely write it and return 'true'.

We now have the base inode for the extent mft record.  We check if it has an
ntfs inode for the extent mft record attached and if not it is safe to write
the extent mft record and we return 'true'.

The ntfs inode for the extent mft record is attached to the base inode so we
attempt to lock the extent mft record and if we find the lock was already
taken, it is not safe to write the extent mft record and we return 'false'.

If we manage to obtain the lock we have exclusive access to the extent mft
record, which also allows us safe writeout of the extent mft record.  We
set the ntfs inode of the extent mft record clean and then set \ ``locked_ni``\  to
the now locked ntfs inode and return 'true'.

Note, the reason for actually writing dirty mft records here and not just
relying on the vfs inode dirty code paths is that we can have mft records
modified without them ever having actual inodes in memory.  Also we can have
dirty mft records with clean ntfs inodes in memory.  None of the described
cases would result in the dirty mft records being written out if we only
relied on the vfs inode dirty code paths.  And these cases can really occur
during allocation of new mft records and in particular when the
initialized_size of the \ ``$MFT``\ /$DATA attribute is extended and the new space
is initialized using \ :c:func:`ntfs_mft_record_format`\ .  The clean inode can then
appear if the mft record is reused for a new inode before it got written
out.

.. _`ntfs_mft_bitmap_find_and_alloc_free_rec_nolock`:

ntfs_mft_bitmap_find_and_alloc_free_rec_nolock
==============================================

.. c:function:: int ntfs_mft_bitmap_find_and_alloc_free_rec_nolock(ntfs_volume *vol, ntfs_inode *base_ni)

    see name

    :param ntfs_volume \*vol:
        volume on which to search for a free mft record

    :param ntfs_inode \*base_ni:
        open base inode if allocating an extent mft record or NULL

.. _`ntfs_mft_bitmap_find_and_alloc_free_rec_nolock.description`:

Description
-----------

Search for a free mft record in the mft bitmap attribute on the ntfs volume
\ ``vol``\ .

If \ ``base_ni``\  is NULL start the search at the default allocator position.

If \ ``base_ni``\  is not NULL start the search at the mft record after the base
mft record \ ``base_ni``\ .

Return the free mft record on success and -errno on error.  An error code of
-ENOSPC means that there are no free mft records in the currently
initialized mft bitmap.

.. _`ntfs_mft_bitmap_find_and_alloc_free_rec_nolock.locking`:

Locking
-------

Caller must hold vol->mftbmp_lock for writing.

.. _`ntfs_mft_bitmap_extend_allocation_nolock`:

ntfs_mft_bitmap_extend_allocation_nolock
========================================

.. c:function:: int ntfs_mft_bitmap_extend_allocation_nolock(ntfs_volume *vol)

    extend mft bitmap by a cluster

    :param ntfs_volume \*vol:
        volume on which to extend the mft bitmap attribute

.. _`ntfs_mft_bitmap_extend_allocation_nolock.description`:

Description
-----------

Extend the mft bitmap attribute on the ntfs volume \ ``vol``\  by one cluster.

.. _`ntfs_mft_bitmap_extend_allocation_nolock.note`:

Note
----

Only changes allocated_size, i.e. does not touch initialized_size or
data_size.

Return 0 on success and -errno on error.

.. _`ntfs_mft_bitmap_extend_allocation_nolock.locking`:

Locking
-------

- Caller must hold vol->mftbmp_lock for writing.
- This function takes NTFS_I(vol->mftbmp_ino)->runlist.lock for
writing and releases it before returning.
- This function takes vol->lcnbmp_lock for writing and releases it
before returning.

.. _`ntfs_mft_bitmap_extend_initialized_nolock`:

ntfs_mft_bitmap_extend_initialized_nolock
=========================================

.. c:function:: int ntfs_mft_bitmap_extend_initialized_nolock(ntfs_volume *vol)

    extend mftbmp initialized data

    :param ntfs_volume \*vol:
        volume on which to extend the mft bitmap attribute

.. _`ntfs_mft_bitmap_extend_initialized_nolock.description`:

Description
-----------

Extend the initialized portion of the mft bitmap attribute on the ntfs
volume \ ``vol``\  by 8 bytes.

.. _`ntfs_mft_bitmap_extend_initialized_nolock.note`:

Note
----

Only changes initialized_size and data_size, i.e. requires that
allocated_size is big enough to fit the new initialized_size.

Return 0 on success and -error on error.

.. _`ntfs_mft_bitmap_extend_initialized_nolock.locking`:

Locking
-------

Caller must hold vol->mftbmp_lock for writing.

.. _`ntfs_mft_data_extend_allocation_nolock`:

ntfs_mft_data_extend_allocation_nolock
======================================

.. c:function:: int ntfs_mft_data_extend_allocation_nolock(ntfs_volume *vol)

    extend mft data attribute

    :param ntfs_volume \*vol:
        volume on which to extend the mft data attribute

.. _`ntfs_mft_data_extend_allocation_nolock.description`:

Description
-----------

Extend the mft data attribute on the ntfs volume \ ``vol``\  by 16 mft records
worth of clusters or if not enough space for this by one mft record worth
of clusters.

.. _`ntfs_mft_data_extend_allocation_nolock.note`:

Note
----

Only changes allocated_size, i.e. does not touch initialized_size or
data_size.

Return 0 on success and -errno on error.

.. _`ntfs_mft_data_extend_allocation_nolock.locking`:

Locking
-------

- Caller must hold vol->mftbmp_lock for writing.
- This function takes NTFS_I(vol->mft_ino)->runlist.lock for
writing and releases it before returning.
- This function calls functions which take vol->lcnbmp_lock for
writing and release it before returning.

.. _`ntfs_mft_record_layout`:

ntfs_mft_record_layout
======================

.. c:function:: int ntfs_mft_record_layout(const ntfs_volume *vol, const s64 mft_no, MFT_RECORD *m)

    layout an mft record into a memory buffer

    :param const ntfs_volume \*vol:
        volume to which the mft record will belong

    :param const s64 mft_no:
        mft reference specifying the mft record number

    :param MFT_RECORD \*m:
        destination buffer of size >= \ ``vol``\ ->mft_record_size bytes

.. _`ntfs_mft_record_layout.description`:

Description
-----------

Layout an empty, unused mft record with the mft record number \ ``mft_no``\  into
the buffer \ ``m``\ .  The volume \ ``vol``\  is needed because the mft record structure
was modified in NTFS 3.1 so we need to know which volume version this mft
record will be used on.

Return 0 on success and -errno on error.

.. _`ntfs_mft_record_format`:

ntfs_mft_record_format
======================

.. c:function:: int ntfs_mft_record_format(const ntfs_volume *vol, const s64 mft_no)

    format an mft record on an ntfs volume

    :param const ntfs_volume \*vol:
        volume on which to format the mft record

    :param const s64 mft_no:
        mft record number to format

.. _`ntfs_mft_record_format.description`:

Description
-----------

Format the mft record \ ``mft_no``\  in \ ``$MFT``\ /$DATA, i.e. lay out an empty, unused
mft record into the appropriate place of the mft data attribute.  This is
used when extending the mft data attribute.

Return 0 on success and -errno on error.

.. _`ntfs_mft_record_alloc`:

ntfs_mft_record_alloc
=====================

.. c:function:: ntfs_inode *ntfs_mft_record_alloc(ntfs_volume *vol, const int mode, ntfs_inode *base_ni, MFT_RECORD **mrec)

    allocate an mft record on an ntfs volume

    :param ntfs_volume \*vol:
        [IN]  volume on which to allocate the mft record

    :param const int mode:
        [IN]  mode if want a file or directory, i.e. base inode or 0

    :param ntfs_inode \*base_ni:
        [IN]  open base inode if allocating an extent mft record or NULL

    :param MFT_RECORD \*\*mrec:
        [OUT] on successful return this is the mapped mft record

.. _`ntfs_mft_record_alloc.description`:

Description
-----------

Allocate an mft record in \ ``$MFT``\ /$DATA of an open ntfs volume \ ``vol``\ .

If \ ``base_ni``\  is NULL make the mft record a base mft record, i.e. a file or
direvctory inode, and allocate it at the default allocator position.  In
this case \ ``mode``\  is the file mode as given to us by the caller.  We in
particular use \ ``mode``\  to distinguish whether a file or a directory is being
created (S_IFDIR(mode) and S_IFREG(mode), respectively).

If \ ``base_ni``\  is not NULL make the allocated mft record an extent record,
allocate it starting at the mft record after the base mft record and attach
the allocated and opened ntfs inode to the base inode \ ``base_ni``\ .  In this
case \ ``mode``\  must be 0 as it is meaningless for extent inodes.

You need to check the return value with \ :c:func:`IS_ERR`\ .  If false, the function
was successful and the return value is the now opened ntfs inode of the
allocated mft record.  \*@mrec is then set to the allocated, mapped, pinned,
and locked mft record.  If \ :c:func:`IS_ERR`\  is true, the function failed and the
error code is obtained from PTR_ERR(return value).  \*@mrec is undefined in
this case.

.. _`ntfs_mft_record_alloc.allocation-strategy`:

Allocation strategy
-------------------


To find a free mft record, we scan the mft bitmap for a zero bit.  To
optimize this we start scanning at the place specified by \ ``base_ni``\  or if
\ ``base_ni``\  is NULL we start where we last stopped and we perform wrap around
when we reach the end.  Note, we do not try to allocate mft records below
number 24 because numbers 0 to 15 are the defined system files anyway and 16
to 24 are special in that they are used for storing extension mft records
for the \ ``$DATA``\  attribute of \ ``$MFT``\ .  This is required to avoid the possibility
of creating a runlist with a circular dependency which once written to disk
can never be read in again.  Windows will only use records 16 to 24 for
normal files if the volume is completely out of space.  We never use them
which means that when the volume is really out of space we cannot create any
more files while Windows can still create up to 8 small files.  We can start
doing this at some later time, it does not matter much for now.

When scanning the mft bitmap, we only search up to the last allocated mft
record.  If there are no free records left in the range 24 to number of
allocated mft records, then we extend the \ ``$MFT``\ /$DATA attribute in order to
create free mft records.  We extend the allocated size of \ ``$MFT``\ /$DATA by 16
records at a time or one cluster, if cluster size is above 16kiB.  If there
is not sufficient space to do this, we try to extend by a single mft record
or one cluster, if cluster size is above the mft record size.

No matter how many mft records we allocate, we initialize only the first
allocated mft record, incrementing mft data size and initialized size
accordingly, open an ntfs_inode for it and return it to the caller, unless
there are less than 24 mft records, in which case we allocate and initialize
mft records until we reach record 24 which we consider as the first free mft
record for use by normal files.

If during any stage we overflow the initialized data in the mft bitmap, we
extend the initialized size (and data size) by 8 bytes, allocating another
cluster if required.  The bitmap data size has to be at least equal to the
number of mft records in the mft, but it can be bigger, in which case the
superflous bits are padded with zeroes.

Thus, when we return successfully (IS_ERR() is false), we will have:
- initialized / extended the mft bitmap if necessary,
- initialized / extended the mft data if necessary,
- set the bit corresponding to the mft record being allocated in the
mft bitmap,
- opened an ntfs_inode for the allocated mft record, and we will have
- returned the ntfs_inode as well as the allocated mapped, pinned, and
locked mft record.

On error, the volume will be left in a consistent state and no record will
be allocated.  If rolling back a partial operation fails, we may leave some
inconsistent metadata in which case we set \ :c:func:`NVolErrors`\  so the volume is
left dirty when unmounted.

Note, this function cannot make use of most of the normal functions, like
for example for attribute resizing, etc, because when the run list overflows
the base mft record and an attribute list is used, it is very important that
the extension mft records used to store the \ ``$DATA``\  attribute of \ ``$MFT``\  can be
reached without having to read the information contained inside them, as
this would make it impossible to find them in the first place after the
volume is unmounted.  \ ``$MFT``\ /$BITMAP probably does not need to follow this
rule because the bitmap is not essential for finding the mft records, but on
the other hand, handling the bitmap in this special way would make life
easier because otherwise there might be circular invocations of functions
when reading the bitmap.

.. _`ntfs_extent_mft_record_free`:

ntfs_extent_mft_record_free
===========================

.. c:function:: int ntfs_extent_mft_record_free(ntfs_inode *ni, MFT_RECORD *m)

    free an extent mft record on an ntfs volume

    :param ntfs_inode \*ni:
        ntfs inode of the mapped extent mft record to free

    :param MFT_RECORD \*m:
        mapped extent mft record of the ntfs inode \ ``ni``\ 

.. _`ntfs_extent_mft_record_free.description`:

Description
-----------

Free the mapped extent mft record \ ``m``\  of the extent ntfs inode \ ``ni``\ .

Note that this function unmaps the mft record and closes and destroys \ ``ni``\ 
internally and hence you cannot use either \ ``ni``\  nor \ ``m``\  any more after this
function returns success.

On success return 0 and on error return -errno.  \ ``ni``\  and \ ``m``\  are still valid
in this case and have not been freed.

For some errors an error message is displayed and the success code 0 is
returned and the volume is then left dirty on umount.  This makes sense in
case we could not rollback the changes that were already done since the
caller no longer wants to reference this mft record so it does not matter to
the caller if something is wrong with it as long as it is properly detached
from the base inode.

.. This file was automatic generated / don't edit.

