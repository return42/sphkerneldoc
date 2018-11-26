.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/block_dev.c

.. _`freeze_bdev`:

freeze_bdev
===========

.. c:function:: struct super_block *freeze_bdev(struct block_device *bdev)

    -  lock a filesystem and force it into a consistent state

    :param bdev:
        blockdevice to lock
    :type bdev: struct block_device \*

.. _`freeze_bdev.description`:

Description
-----------

If a superblock is found on this device, we take the s_umount semaphore
on it to make sure nobody unmounts until the snapshot creation is done.
The reference counter (bd_fsfreeze_count) guarantees that only the last
unfreeze process can unfreeze the frozen filesystem actually when multiple
freeze requests arrive simultaneously. It counts up in \ :c:func:`freeze_bdev`\  and
count down in \ :c:func:`thaw_bdev`\ . When it becomes 0, \ :c:func:`thaw_bdev`\  will unfreeze
actually.

.. _`thaw_bdev`:

thaw_bdev
=========

.. c:function:: int thaw_bdev(struct block_device *bdev, struct super_block *sb)

    - unlock filesystem

    :param bdev:
        blockdevice to unlock
    :type bdev: struct block_device \*

    :param sb:
        associated superblock
    :type sb: struct super_block \*

.. _`thaw_bdev.description`:

Description
-----------

Unlocks the filesystem and marks it writeable again after \ :c:func:`freeze_bdev`\ .

.. _`bdev_read_page`:

bdev_read_page
==============

.. c:function:: int bdev_read_page(struct block_device *bdev, sector_t sector, struct page *page)

    Start reading a page from a block device

    :param bdev:
        The device to read the page from
    :type bdev: struct block_device \*

    :param sector:
        The offset on the device to read the page to (need not be aligned)
    :type sector: sector_t

    :param page:
        The page to read
    :type page: struct page \*

.. _`bdev_read_page.description`:

Description
-----------

On entry, the page should be locked.  It will be unlocked when the page
has been read.  If the block driver implements rw_page synchronously,
that will be true on exit from this function, but it need not be.

Errors returned by this function are usually "soft", eg out of memory, or
queue full; callers should try a different route to read this page rather
than propagate an error back up the stack.

.. _`bdev_read_page.return`:

Return
------

negative errno if an error occurs, 0 if submission was successful.

.. _`bdev_write_page`:

bdev_write_page
===============

.. c:function:: int bdev_write_page(struct block_device *bdev, sector_t sector, struct page *page, struct writeback_control *wbc)

    Start writing a page to a block device

    :param bdev:
        The device to write the page to
    :type bdev: struct block_device \*

    :param sector:
        The offset on the device to write the page to (need not be aligned)
    :type sector: sector_t

    :param page:
        The page to write
    :type page: struct page \*

    :param wbc:
        The writeback_control for the write
    :type wbc: struct writeback_control \*

.. _`bdev_write_page.description`:

Description
-----------

On entry, the page should be locked and not currently under writeback.
On exit, if the write started successfully, the page will be unlocked and
under writeback.  If the write failed already (eg the driver failed to
queue the page to the device), the page will still be locked.  If the
caller is a ->writepage implementation, it will need to unlock the page.

Errors returned by this function are usually "soft", eg out of memory, or
queue full; callers should try a different route to write this page rather
than propagate an error back up the stack.

.. _`bdev_write_page.return`:

Return
------

negative errno if an error occurs, 0 if submission was successful.

.. _`bdgrab`:

bdgrab
======

.. c:function:: struct block_device *bdgrab(struct block_device *bdev)

    - Grab a reference to an already referenced block device

    :param bdev:
        Block device to grab a reference to.
    :type bdev: struct block_device \*

.. _`bd_may_claim`:

bd_may_claim
============

.. c:function:: bool bd_may_claim(struct block_device *bdev, struct block_device *whole, void *holder)

    test whether a block device can be claimed

    :param bdev:
        block device of interest
    :type bdev: struct block_device \*

    :param whole:
        whole block device containing \ ``bdev``\ , may equal \ ``bdev``\ 
    :type whole: struct block_device \*

    :param holder:
        holder trying to claim \ ``bdev``\ 
    :type holder: void \*

.. _`bd_may_claim.description`:

Description
-----------

Test whether \ ``bdev``\  can be claimed by \ ``holder``\ .

.. _`bd_may_claim.context`:

Context
-------

spin_lock(&bdev_lock).

.. _`bd_may_claim.return`:

Return
------

\ ``true``\  if \ ``bdev``\  can be claimed, \ ``false``\  otherwise.

.. _`bd_prepare_to_claim`:

bd_prepare_to_claim
===================

.. c:function:: int bd_prepare_to_claim(struct block_device *bdev, struct block_device *whole, void *holder)

    prepare to claim a block device

    :param bdev:
        block device of interest
    :type bdev: struct block_device \*

    :param whole:
        the whole device containing \ ``bdev``\ , may equal \ ``bdev``\ 
    :type whole: struct block_device \*

    :param holder:
        holder trying to claim \ ``bdev``\ 
    :type holder: void \*

.. _`bd_prepare_to_claim.description`:

Description
-----------

Prepare to claim \ ``bdev``\ .  This function fails if \ ``bdev``\  is already
claimed by another holder and waits if another claiming is in
progress.  This function doesn't actually claim.  On successful
return, the caller has ownership of bd_claiming and bd_holder[s].

.. _`bd_prepare_to_claim.context`:

Context
-------

spin_lock(&bdev_lock).  Might release bdev_lock, sleep and regrab
it multiple times.

.. _`bd_prepare_to_claim.return`:

Return
------

0 if \ ``bdev``\  can be claimed, -EBUSY otherwise.

.. _`bd_start_claiming`:

bd_start_claiming
=================

.. c:function:: struct block_device *bd_start_claiming(struct block_device *bdev, void *holder)

    start claiming a block device

    :param bdev:
        block device of interest
    :type bdev: struct block_device \*

    :param holder:
        holder trying to claim \ ``bdev``\ 
    :type holder: void \*

.. _`bd_start_claiming.description`:

Description
-----------

\ ``bdev``\  is about to be opened exclusively.  Check \ ``bdev``\  can be opened
exclusively and mark that an exclusive open is in progress.  Each
successful call to this function must be matched with a call to
either \ :c:func:`bd_finish_claiming`\  or \ :c:func:`bd_abort_claiming`\  (which do not
fail).

This function is used to gain exclusive access to the block device
without actually causing other exclusive open attempts to fail. It
should be used when the open sequence itself requires exclusive
access but may subsequently fail.

.. _`bd_start_claiming.context`:

Context
-------

Might sleep.

.. _`bd_start_claiming.return`:

Return
------

Pointer to the block device containing \ ``bdev``\  on success, \ :c:func:`ERR_PTR`\ 
value on failure.

.. _`bd_link_disk_holder`:

bd_link_disk_holder
===================

.. c:function:: int bd_link_disk_holder(struct block_device *bdev, struct gendisk *disk)

    create symlinks between holding disk and slave bdev

    :param bdev:
        the claimed slave bdev
    :type bdev: struct block_device \*

    :param disk:
        the holding disk
    :type disk: struct gendisk \*

.. _`bd_link_disk_holder.description`:

Description
-----------

DON'T USE THIS UNLESS YOU'RE ALREADY USING IT.

This functions creates the following sysfs symlinks.

- from "slaves" directory of the holder \ ``disk``\  to the claimed \ ``bdev``\ 
- from "holders" directory of the \ ``bdev``\  to the holder \ ``disk``\ 

For example, if /dev/dm-0 maps to /dev/sda and disk for dm-0 is
passed to \ :c:func:`bd_link_disk_holder`\ , then:

  /sys/block/dm-0/slaves/sda --> /sys/block/sda
  /sys/block/sda/holders/dm-0 --> /sys/block/dm-0

The caller must have claimed \ ``bdev``\  before calling this function and
ensure that both \ ``bdev``\  and \ ``disk``\  are valid during the creation and
lifetime of these symlinks.

.. _`bd_link_disk_holder.context`:

Context
-------

Might sleep.

.. _`bd_link_disk_holder.return`:

Return
------

0 on success, -errno on failure.

.. _`bd_unlink_disk_holder`:

bd_unlink_disk_holder
=====================

.. c:function:: void bd_unlink_disk_holder(struct block_device *bdev, struct gendisk *disk)

    destroy symlinks created by \ :c:func:`bd_link_disk_holder`\ 

    :param bdev:
        the calimed slave bdev
    :type bdev: struct block_device \*

    :param disk:
        the holding disk
    :type disk: struct gendisk \*

.. _`bd_unlink_disk_holder.description`:

Description
-----------

DON'T USE THIS UNLESS YOU'RE ALREADY USING IT.

.. _`bd_unlink_disk_holder.context`:

Context
-------

Might sleep.

.. _`flush_disk`:

flush_disk
==========

.. c:function:: void flush_disk(struct block_device *bdev, bool kill_dirty)

    invalidates all buffer-cache entries on a disk

    :param bdev:
        struct block device to be flushed
    :type bdev: struct block_device \*

    :param kill_dirty:
        flag to guide handling of dirty inodes
    :type kill_dirty: bool

.. _`flush_disk.description`:

Description
-----------

Invalidates all buffer-cache entries on a disk. It should be called
when a disk has been changed -- either by a media change or online
resize.

.. _`check_disk_size_change`:

check_disk_size_change
======================

.. c:function:: void check_disk_size_change(struct gendisk *disk, struct block_device *bdev, bool verbose)

    checks for disk size change and adjusts bdev size.

    :param disk:
        struct gendisk to check
    :type disk: struct gendisk \*

    :param bdev:
        struct bdev to adjust.
    :type bdev: struct block_device \*

    :param verbose:
        if \ ``true``\  log a message about a size change if there is any
    :type verbose: bool

.. _`check_disk_size_change.description`:

Description
-----------

This routine checks to see if the bdev size does not match the disk size
and adjusts it if it differs. When shrinking the bdev size, its all caches
are freed.

.. _`revalidate_disk`:

revalidate_disk
===============

.. c:function:: int revalidate_disk(struct gendisk *disk)

    wrapper for lower-level driver's revalidate_disk call-back

    :param disk:
        struct gendisk to be revalidated
    :type disk: struct gendisk \*

.. _`revalidate_disk.description`:

Description
-----------

This routine is a wrapper for lower-level driver's revalidate_disk
call-backs.  It is used to do common pre and post operations needed
for all revalidate_disk operations.

.. _`blkdev_get`:

blkdev_get
==========

.. c:function:: int blkdev_get(struct block_device *bdev, fmode_t mode, void *holder)

    open a block device

    :param bdev:
        block_device to open
    :type bdev: struct block_device \*

    :param mode:
        FMODE_* mask
    :type mode: fmode_t

    :param holder:
        exclusive holder identifier
    :type holder: void \*

.. _`blkdev_get.description`:

Description
-----------

Open \ ``bdev``\  with \ ``mode``\ .  If \ ``mode``\  includes \ ``FMODE_EXCL``\ , \ ``bdev``\  is
open with exclusive access.  Specifying \ ``FMODE_EXCL``\  with \ ``NULL``\ 
\ ``holder``\  is invalid.  Exclusive opens may nest for the same \ ``holder``\ .

On success, the reference count of \ ``bdev``\  is unchanged.  On failure,
\ ``bdev``\  is put.

.. _`blkdev_get.context`:

Context
-------

Might sleep.

.. _`blkdev_get.return`:

Return
------

0 on success, -errno on failure.

.. _`blkdev_get_by_path`:

blkdev_get_by_path
==================

.. c:function:: struct block_device *blkdev_get_by_path(const char *path, fmode_t mode, void *holder)

    open a block device by name

    :param path:
        path to the block device to open
    :type path: const char \*

    :param mode:
        FMODE_* mask
    :type mode: fmode_t

    :param holder:
        exclusive holder identifier
    :type holder: void \*

.. _`blkdev_get_by_path.description`:

Description
-----------

Open the blockdevice described by the device file at \ ``path``\ .  \ ``mode``\ 
and \ ``holder``\  are identical to \ :c:func:`blkdev_get`\ .

On success, the returned block_device has reference count of one.

.. _`blkdev_get_by_path.context`:

Context
-------

Might sleep.

.. _`blkdev_get_by_path.return`:

Return
------

Pointer to block_device on success, ERR_PTR(-errno) on failure.

.. _`blkdev_get_by_dev`:

blkdev_get_by_dev
=================

.. c:function:: struct block_device *blkdev_get_by_dev(dev_t dev, fmode_t mode, void *holder)

    open a block device by device number

    :param dev:
        device number of block device to open
    :type dev: dev_t

    :param mode:
        FMODE_* mask
    :type mode: fmode_t

    :param holder:
        exclusive holder identifier
    :type holder: void \*

.. _`blkdev_get_by_dev.description`:

Description
-----------

Open the blockdevice described by device number \ ``dev``\ .  \ ``mode``\  and
\ ``holder``\  are identical to \ :c:func:`blkdev_get`\ .

Use it ONLY if you really do not have anything better - i.e. when
you are behind a truly sucky interface and all you are given is a
device number.  _Never_ to be used for internal purposes.  If you
ever need it - reconsider your API.

On success, the returned block_device has reference count of one.

.. _`blkdev_get_by_dev.context`:

Context
-------

Might sleep.

.. _`blkdev_get_by_dev.return`:

Return
------

Pointer to block_device on success, ERR_PTR(-errno) on failure.

.. _`lookup_bdev`:

lookup_bdev
===========

.. c:function:: struct block_device *lookup_bdev(const char *pathname)

    lookup a struct block_device by name

    :param pathname:
        special file representing the block device
    :type pathname: const char \*

.. _`lookup_bdev.description`:

Description
-----------

Get a reference to the blockdevice at \ ``pathname``\  in the current
namespace if possible and return it.  Return ERR_PTR(error)
otherwise.

.. This file was automatic generated / don't edit.

