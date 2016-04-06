.. -*- coding: utf-8; mode: rst -*-

=======
genhd.c
=======



.. _xref_disk_get_part:

disk_get_part
=============

.. c:function:: struct hd_struct * disk_get_part (struct gendisk * disk, int partno)

    get partition

    :param struct gendisk * disk:
        disk to look partition from

    :param int partno:
        partition number



Description
-----------

Look for partition **partno** from **disk**.  If found, increment
reference count and return it.



CONTEXT
-------

Don't care.



RETURNS
-------

Pointer to the found partition on success, NULL if not found.




.. _xref_disk_part_iter_init:

disk_part_iter_init
===================

.. c:function:: void disk_part_iter_init (struct disk_part_iter * piter, struct gendisk * disk, unsigned int flags)

    initialize partition iterator

    :param struct disk_part_iter * piter:
        iterator to initialize

    :param struct gendisk * disk:
        disk to iterate over

    :param unsigned int flags:
        DISK_PITER_* flags



Description
-----------

Initialize **piter** so that it iterates over partitions of **disk**.



CONTEXT
-------

Don't care.




.. _xref_disk_part_iter_next:

disk_part_iter_next
===================

.. c:function:: struct hd_struct * disk_part_iter_next (struct disk_part_iter * piter)

    proceed iterator to the next partition and return it

    :param struct disk_part_iter * piter:
        iterator of interest



Description
-----------

Proceed **piter** to the next partition and return it.



CONTEXT
-------

Don't care.




.. _xref_disk_part_iter_exit:

disk_part_iter_exit
===================

.. c:function:: void disk_part_iter_exit (struct disk_part_iter * piter)

    finish up partition iteration

    :param struct disk_part_iter * piter:
        iter of interest



Description
-----------

Called when iteration is over.  Cleans up **piter**.



CONTEXT
-------

Don't care.




.. _xref_disk_map_sector_rcu:

disk_map_sector_rcu
===================

.. c:function:: struct hd_struct * disk_map_sector_rcu (struct gendisk * disk, sector_t sector)

    map sector to partition

    :param struct gendisk * disk:
        gendisk of interest

    :param sector_t sector:
        sector to map



Description
-----------

Find out which partition **sector** maps to on **disk**.  This is
primarily used for stats accounting.



CONTEXT
-------

RCU read locked.  The returned partition pointer is valid only
while preemption is disabled.



RETURNS
-------

Found partition on success, part0 is returned if no partition matches




.. _xref_register_blkdev:

register_blkdev
===============

.. c:function:: int register_blkdev (unsigned int major, const char * name)

    register a new block device

    :param unsigned int major:
        the requested major device number [1..255]. If **major**=0, try to
                allocate any unused major number.

    :param const char * name:
        the name of the new block device as a zero terminated string



Description
-----------

The **name** must be unique within the system.


The return value depends on the **major** input parameter.
 - if a major device number was requested in range [1..255] then the
   function returns zero on success, or a negative error code
 - if any unused major number was requested with **major**=0 parameter
   then the return value is the allocated major number in range
   [1..255] or a negative error code otherwise




.. _xref_blk_mangle_minor:

blk_mangle_minor
================

.. c:function:: int blk_mangle_minor (int minor)

    scatter minor numbers apart

    :param int minor:
        minor number to mangle



Description
-----------

Scatter consecutively allocated **minor** number apart if MANGLE_DEVT
is enabled.  Mangling twice gives the original value.



RETURNS
-------

Mangled value.



CONTEXT
-------

Don't care.




.. _xref_blk_alloc_devt:

blk_alloc_devt
==============

.. c:function:: int blk_alloc_devt (struct hd_struct * part, dev_t * devt)

    allocate a dev_t for a partition

    :param struct hd_struct * part:
        partition to allocate dev_t for

    :param dev_t * devt:
        out parameter for resulting dev_t



Description
-----------

Allocate a dev_t for block device.



RETURNS
-------

0 on success, allocated dev_t is returned in ***devt**.  -errno on
failure.



CONTEXT
-------

Might sleep.




.. _xref_blk_free_devt:

blk_free_devt
=============

.. c:function:: void blk_free_devt (dev_t devt)

    free a dev_t

    :param dev_t devt:
        dev_t to free



Description
-----------

Free **devt** which was allocated using :c:func:`blk_alloc_devt`.



CONTEXT
-------

Might sleep.




.. _xref_add_disk:

add_disk
========

.. c:function:: void add_disk (struct gendisk * disk)

    add partitioning information to kernel list

    :param struct gendisk * disk:
        per-device partitioning information



Description
-----------

This function registers the partitioning information in **disk**
with the kernel.



FIXME
-----

error handling




.. _xref_get_gendisk:

get_gendisk
===========

.. c:function:: struct gendisk * get_gendisk (dev_t devt, int * partno)

    get partitioning information for a given device

    :param dev_t devt:
        device to get partitioning information for

    :param int * partno:
        returned partition index



Description
-----------

This function gets the structure containing partitioning
information for the given device **devt**.




.. _xref_bdget_disk:

bdget_disk
==========

.. c:function:: struct block_device * bdget_disk (struct gendisk * disk, int partno)

    do bdget() by gendisk and partition number

    :param struct gendisk * disk:
        gendisk of interest

    :param int partno:
        partition number



Description
-----------

Find partition **partno** from **disk**, do :c:func:`bdget` on it.



CONTEXT
-------

Don't care.



RETURNS
-------

Resulting block_device on success, NULL on failure.




.. _xref_disk_replace_part_tbl:

disk_replace_part_tbl
=====================

.. c:function:: void disk_replace_part_tbl (struct gendisk * disk, struct disk_part_tbl * new_ptbl)

    replace disk-\\\gt;part_tbl in RCU-safe way

    :param struct gendisk * disk:
        disk to replace part_tbl for

    :param struct disk_part_tbl * new_ptbl:
        new part_tbl to install



Description
-----------

Replace disk->part_tbl with **new_ptbl** in RCU-safe way.  The
original ptbl is freed using RCU callback.



LOCKING
-------

Matching bd_mutx locked.




.. _xref_disk_expand_part_tbl:

disk_expand_part_tbl
====================

.. c:function:: int disk_expand_part_tbl (struct gendisk * disk, int partno)

    expand disk-\\\gt;part_tbl

    :param struct gendisk * disk:
        disk to expand part_tbl for

    :param int partno:
        expand such that this partno can fit in



Description
-----------

Expand disk->part_tbl such that **partno** can fit in.  disk->part_tbl
uses RCU to allow unlocked dereferencing for stats and other stuff.



LOCKING
-------

Matching bd_mutex locked, might sleep.



RETURNS
-------

0 on success, -errno on failure.




.. _xref_disk_block_events:

disk_block_events
=================

.. c:function:: void disk_block_events (struct gendisk * disk)

    block and flush disk event checking

    :param struct gendisk * disk:
        disk to block events for



Description
-----------

On return from this function, it is guaranteed that event checking
isn't in progress and won't happen until unblocked by
:c:func:`disk_unblock_events`.  Events blocking is counted and the actual
unblocking happens after the matching number of unblocks are done.


Note that this intentionally does not block event checking from
:c:func:`disk_clear_events`.



CONTEXT
-------

Might sleep.




.. _xref_disk_unblock_events:

disk_unblock_events
===================

.. c:function:: void disk_unblock_events (struct gendisk * disk)

    unblock disk event checking

    :param struct gendisk * disk:
        disk to unblock events for



Description
-----------

Undo :c:func:`disk_block_events`.  When the block count reaches zero, it
starts events polling if configured.



CONTEXT
-------

Don't care.  Safe to call from irq context.




.. _xref_disk_flush_events:

disk_flush_events
=================

.. c:function:: void disk_flush_events (struct gendisk * disk, unsigned int mask)

    schedule immediate event checking and flushing

    :param struct gendisk * disk:
        disk to check and flush events for

    :param unsigned int mask:
        events to flush



Description
-----------

Schedule immediate event checking on **disk** if not blocked.  Events in
**mask** are scheduled to be cleared from the driver.  Note that this
doesn't clear the events from **disk**->ev.



CONTEXT
-------

If **mask** is non-zero must be called with bdev->bd_mutex held.




.. _xref_disk_clear_events:

disk_clear_events
=================

.. c:function:: unsigned int disk_clear_events (struct gendisk * disk, unsigned int mask)

    synchronously check, clear and return pending events

    :param struct gendisk * disk:
        disk to fetch and clear events from

    :param unsigned int mask:
        mask of events to be fetched and cleared



Description
-----------

Disk events are synchronously checked and pending events in **mask**
are cleared and returned.  This ignores the block count.



CONTEXT
-------

Might sleep.


