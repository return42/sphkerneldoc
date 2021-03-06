.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/genhd.c

.. _`disk_get_part`:

disk_get_part
=============

.. c:function:: struct hd_struct *disk_get_part(struct gendisk *disk, int partno)

    get partition

    :param disk:
        disk to look partition from
    :type disk: struct gendisk \*

    :param partno:
        partition number
    :type partno: int

.. _`disk_get_part.description`:

Description
-----------

Look for partition \ ``partno``\  from \ ``disk``\ .  If found, increment
reference count and return it.

.. _`disk_get_part.context`:

Context
-------

Don't care.

.. _`disk_get_part.return`:

Return
------

Pointer to the found partition on success, NULL if not found.

.. _`disk_part_iter_init`:

disk_part_iter_init
===================

.. c:function:: void disk_part_iter_init(struct disk_part_iter *piter, struct gendisk *disk, unsigned int flags)

    initialize partition iterator

    :param piter:
        iterator to initialize
    :type piter: struct disk_part_iter \*

    :param disk:
        disk to iterate over
    :type disk: struct gendisk \*

    :param flags:
        DISK_PITER_* flags
    :type flags: unsigned int

.. _`disk_part_iter_init.description`:

Description
-----------

Initialize \ ``piter``\  so that it iterates over partitions of \ ``disk``\ .

.. _`disk_part_iter_init.context`:

Context
-------

Don't care.

.. _`disk_part_iter_next`:

disk_part_iter_next
===================

.. c:function:: struct hd_struct *disk_part_iter_next(struct disk_part_iter *piter)

    proceed iterator to the next partition and return it

    :param piter:
        iterator of interest
    :type piter: struct disk_part_iter \*

.. _`disk_part_iter_next.description`:

Description
-----------

Proceed \ ``piter``\  to the next partition and return it.

.. _`disk_part_iter_next.context`:

Context
-------

Don't care.

.. _`disk_part_iter_exit`:

disk_part_iter_exit
===================

.. c:function:: void disk_part_iter_exit(struct disk_part_iter *piter)

    finish up partition iteration

    :param piter:
        iter of interest
    :type piter: struct disk_part_iter \*

.. _`disk_part_iter_exit.description`:

Description
-----------

Called when iteration is over.  Cleans up \ ``piter``\ .

.. _`disk_part_iter_exit.context`:

Context
-------

Don't care.

.. _`disk_map_sector_rcu`:

disk_map_sector_rcu
===================

.. c:function:: struct hd_struct *disk_map_sector_rcu(struct gendisk *disk, sector_t sector)

    map sector to partition

    :param disk:
        gendisk of interest
    :type disk: struct gendisk \*

    :param sector:
        sector to map
    :type sector: sector_t

.. _`disk_map_sector_rcu.description`:

Description
-----------

Find out which partition \ ``sector``\  maps to on \ ``disk``\ .  This is
primarily used for stats accounting.

.. _`disk_map_sector_rcu.context`:

Context
-------

RCU read locked.  The returned partition pointer is valid only
while preemption is disabled.

.. _`disk_map_sector_rcu.return`:

Return
------

Found partition on success, part0 is returned if no partition matches

.. _`register_blkdev`:

register_blkdev
===============

.. c:function:: int register_blkdev(unsigned int major, const char *name)

    register a new block device

    :param major:
        the requested major device number [1..BLKDEV_MAJOR_MAX-1]. If
        \ ``major``\  = 0, try to allocate any unused major number.
    :type major: unsigned int

    :param name:
        the name of the new block device as a zero terminated string
    :type name: const char \*

.. _`register_blkdev.description`:

Description
-----------

The \ ``name``\  must be unique within the system.

The return value depends on the \ ``major``\  input parameter:

 - if a major device number was requested in range [1..BLKDEV_MAJOR_MAX-1]
   then the function returns zero on success, or a negative error code
 - if any unused major number was requested with \ ``major``\  = 0 parameter
   then the return value is the allocated major number in range
   [1..BLKDEV_MAJOR_MAX-1] or a negative error code otherwise

See Documentation/admin-guide/devices.txt for the list of allocated
major numbers.

.. _`blk_mangle_minor`:

blk_mangle_minor
================

.. c:function:: int blk_mangle_minor(int minor)

    scatter minor numbers apart

    :param minor:
        minor number to mangle
    :type minor: int

.. _`blk_mangle_minor.description`:

Description
-----------

Scatter consecutively allocated \ ``minor``\  number apart if MANGLE_DEVT
is enabled.  Mangling twice gives the original value.

.. _`blk_mangle_minor.return`:

Return
------

Mangled value.

.. _`blk_mangle_minor.context`:

Context
-------

Don't care.

.. _`blk_alloc_devt`:

blk_alloc_devt
==============

.. c:function:: int blk_alloc_devt(struct hd_struct *part, dev_t *devt)

    allocate a dev_t for a partition

    :param part:
        partition to allocate dev_t for
    :type part: struct hd_struct \*

    :param devt:
        out parameter for resulting dev_t
    :type devt: dev_t \*

.. _`blk_alloc_devt.description`:

Description
-----------

Allocate a dev_t for block device.

.. _`blk_alloc_devt.return`:

Return
------

0 on success, allocated dev_t is returned in *@devt.  -errno on
failure.

.. _`blk_alloc_devt.context`:

Context
-------

Might sleep.

.. _`blk_free_devt`:

blk_free_devt
=============

.. c:function:: void blk_free_devt(dev_t devt)

    free a dev_t

    :param devt:
        dev_t to free
    :type devt: dev_t

.. _`blk_free_devt.description`:

Description
-----------

Free \ ``devt``\  which was allocated using \ :c:func:`blk_alloc_devt`\ .

.. _`blk_free_devt.context`:

Context
-------

Might sleep.

.. _`__device_add_disk`:

__device_add_disk
=================

.. c:function:: void __device_add_disk(struct device *parent, struct gendisk *disk, const struct attribute_group **groups, bool register_queue)

    add disk information to kernel list

    :param parent:
        parent device for the disk
    :type parent: struct device \*

    :param disk:
        per-device partitioning information
    :type disk: struct gendisk \*

    :param groups:
        Additional per-device sysfs groups
    :type groups: const struct attribute_group \*\*

    :param register_queue:
        register the queue if set to true
    :type register_queue: bool

.. _`__device_add_disk.description`:

Description
-----------

This function registers the partitioning information in \ ``disk``\ 
with the kernel.

FIXME: error handling

.. _`get_gendisk`:

get_gendisk
===========

.. c:function:: struct gendisk *get_gendisk(dev_t devt, int *partno)

    get partitioning information for a given device

    :param devt:
        device to get partitioning information for
    :type devt: dev_t

    :param partno:
        returned partition index
    :type partno: int \*

.. _`get_gendisk.description`:

Description
-----------

This function gets the structure containing partitioning
information for the given device \ ``devt``\ .

.. _`bdget_disk`:

bdget_disk
==========

.. c:function:: struct block_device *bdget_disk(struct gendisk *disk, int partno)

    do \ :c:func:`bdget`\  by gendisk and partition number

    :param disk:
        gendisk of interest
    :type disk: struct gendisk \*

    :param partno:
        partition number
    :type partno: int

.. _`bdget_disk.description`:

Description
-----------

Find partition \ ``partno``\  from \ ``disk``\ , do \ :c:func:`bdget`\  on it.

.. _`bdget_disk.context`:

Context
-------

Don't care.

.. _`bdget_disk.return`:

Return
------

Resulting block_device on success, NULL on failure.

.. _`disk_replace_part_tbl`:

disk_replace_part_tbl
=====================

.. c:function:: void disk_replace_part_tbl(struct gendisk *disk, struct disk_part_tbl *new_ptbl)

    replace disk->part_tbl in RCU-safe way

    :param disk:
        disk to replace part_tbl for
    :type disk: struct gendisk \*

    :param new_ptbl:
        new part_tbl to install
    :type new_ptbl: struct disk_part_tbl \*

.. _`disk_replace_part_tbl.description`:

Description
-----------

Replace disk->part_tbl with \ ``new_ptbl``\  in RCU-safe way.  The
original ptbl is freed using RCU callback.

.. _`disk_replace_part_tbl.locking`:

LOCKING
-------

Matching bd_mutex locked or the caller is the only user of \ ``disk``\ .

.. _`disk_expand_part_tbl`:

disk_expand_part_tbl
====================

.. c:function:: int disk_expand_part_tbl(struct gendisk *disk, int partno)

    expand disk->part_tbl

    :param disk:
        disk to expand part_tbl for
    :type disk: struct gendisk \*

    :param partno:
        expand such that this partno can fit in
    :type partno: int

.. _`disk_expand_part_tbl.description`:

Description
-----------

Expand disk->part_tbl such that \ ``partno``\  can fit in.  disk->part_tbl
uses RCU to allow unlocked dereferencing for stats and other stuff.

.. _`disk_expand_part_tbl.locking`:

LOCKING
-------

Matching bd_mutex locked or the caller is the only user of \ ``disk``\ .
Might sleep.

.. _`disk_expand_part_tbl.return`:

Return
------

0 on success, -errno on failure.

.. _`disk_block_events`:

disk_block_events
=================

.. c:function:: void disk_block_events(struct gendisk *disk)

    block and flush disk event checking

    :param disk:
        disk to block events for
    :type disk: struct gendisk \*

.. _`disk_block_events.description`:

Description
-----------

On return from this function, it is guaranteed that event checking
isn't in progress and won't happen until unblocked by
\ :c:func:`disk_unblock_events`\ .  Events blocking is counted and the actual
unblocking happens after the matching number of unblocks are done.

Note that this intentionally does not block event checking from
\ :c:func:`disk_clear_events`\ .

.. _`disk_block_events.context`:

Context
-------

Might sleep.

.. _`disk_unblock_events`:

disk_unblock_events
===================

.. c:function:: void disk_unblock_events(struct gendisk *disk)

    unblock disk event checking

    :param disk:
        disk to unblock events for
    :type disk: struct gendisk \*

.. _`disk_unblock_events.description`:

Description
-----------

Undo \ :c:func:`disk_block_events`\ .  When the block count reaches zero, it
starts events polling if configured.

.. _`disk_unblock_events.context`:

Context
-------

Don't care.  Safe to call from irq context.

.. _`disk_flush_events`:

disk_flush_events
=================

.. c:function:: void disk_flush_events(struct gendisk *disk, unsigned int mask)

    schedule immediate event checking and flushing

    :param disk:
        disk to check and flush events for
    :type disk: struct gendisk \*

    :param mask:
        events to flush
    :type mask: unsigned int

.. _`disk_flush_events.description`:

Description
-----------

Schedule immediate event checking on \ ``disk``\  if not blocked.  Events in
\ ``mask``\  are scheduled to be cleared from the driver.  Note that this
doesn't clear the events from \ ``disk->ev``\ .

.. _`disk_flush_events.context`:

Context
-------

If \ ``mask``\  is non-zero must be called with bdev->bd_mutex held.

.. _`disk_clear_events`:

disk_clear_events
=================

.. c:function:: unsigned int disk_clear_events(struct gendisk *disk, unsigned int mask)

    synchronously check, clear and return pending events

    :param disk:
        disk to fetch and clear events from
    :type disk: struct gendisk \*

    :param mask:
        mask of events to be fetched and cleared
    :type mask: unsigned int

.. _`disk_clear_events.description`:

Description
-----------

Disk events are synchronously checked and pending events in \ ``mask``\ 
are cleared and returned.  This ignores the block count.

.. _`disk_clear_events.context`:

Context
-------

Might sleep.

.. This file was automatic generated / don't edit.

