.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-settings.c

.. _`blk_queue_prep_rq`:

blk_queue_prep_rq
=================

.. c:function:: void blk_queue_prep_rq(struct request_queue *q, prep_rq_fn *pfn)

    set a prepare_request function for queue

    :param struct request_queue \*q:
        queue

    :param prep_rq_fn \*pfn:
        prepare_request function

.. _`blk_queue_prep_rq.description`:

Description
-----------

It's possible for a queue to register a prepare_request callback which
is invoked before the request is handed to the request_fn. The goal of
the function is to prepare a request for I/O, it can be used to build a
cdb from the request data for instance.

.. _`blk_queue_unprep_rq`:

blk_queue_unprep_rq
===================

.. c:function:: void blk_queue_unprep_rq(struct request_queue *q, unprep_rq_fn *ufn)

    set an unprepare_request function for queue

    :param struct request_queue \*q:
        queue

    :param unprep_rq_fn \*ufn:
        unprepare_request function

.. _`blk_queue_unprep_rq.description`:

Description
-----------

It's possible for a queue to register an unprepare_request callback
which is invoked before the request is finally completed. The goal
of the function is to deallocate any data that was allocated in the
prepare_request callback.

.. _`blk_set_default_limits`:

blk_set_default_limits
======================

.. c:function:: void blk_set_default_limits(struct queue_limits *lim)

    reset limits to default values

    :param struct queue_limits \*lim:
        the queue_limits structure to reset

.. _`blk_set_default_limits.description`:

Description
-----------

Returns a queue_limit struct to its default state.

.. _`blk_set_stacking_limits`:

blk_set_stacking_limits
=======================

.. c:function:: void blk_set_stacking_limits(struct queue_limits *lim)

    set default limits for stacking devices

    :param struct queue_limits \*lim:
        the queue_limits structure to reset

.. _`blk_set_stacking_limits.description`:

Description
-----------

Returns a queue_limit struct to its default state. Should be used
by stacking drivers like DM that have no internal limits.

.. _`blk_queue_make_request`:

blk_queue_make_request
======================

.. c:function:: void blk_queue_make_request(struct request_queue *q, make_request_fn *mfn)

    define an alternate make_request function for a device

    :param struct request_queue \*q:
        the request queue for the device to be affected

    :param make_request_fn \*mfn:
        the alternate make_request function

.. _`blk_queue_make_request.description`:

Description
-----------

The normal way for \ :c:type:`struct bios <bios>`\  to be passed to a device
driver is for them to be collected into requests on a request
queue, and then to allow the device driver to select requests
off that queue when it is ready.  This works well for many block
devices. However some block devices (typically virtual devices
such as md or lvm) do not benefit from the processing on the
request queue, and are served best by having the requests passed
directly to them.  This can be achieved by providing a function
to \ :c:func:`blk_queue_make_request`\ .

.. _`blk_queue_make_request.caveat`:

Caveat
------

The driver that does this \*must\* be able to deal appropriately
with buffers in "highmemory". This can be accomplished by either calling
\__bio_kmap_atomic() to get a temporary kernel mapping, or by calling
\ :c:func:`blk_queue_bounce`\  to create a buffer in normal memory.

.. _`blk_queue_bounce_limit`:

blk_queue_bounce_limit
======================

.. c:function:: void blk_queue_bounce_limit(struct request_queue *q, u64 max_addr)

    set bounce buffer limit for queue

    :param struct request_queue \*q:
        the request queue for the device

    :param u64 max_addr:
        the maximum address the device can handle

.. _`blk_queue_bounce_limit.description`:

Description
-----------

Different hardware can have different requirements as to what pages
it can do I/O directly to. A low level driver can call
blk_queue_bounce_limit to have lower memory pages allocated as bounce
buffers for doing I/O to pages residing above \ ``max_addr``\ .

.. _`blk_queue_max_hw_sectors`:

blk_queue_max_hw_sectors
========================

.. c:function:: void blk_queue_max_hw_sectors(struct request_queue *q, unsigned int max_hw_sectors)

    set max sectors for a request for this queue

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int max_hw_sectors:
        max hardware sectors in the usual 512b unit

.. _`blk_queue_max_hw_sectors.description`:

Description
-----------

Enables a low level driver to set a hard upper limit,
max_hw_sectors, on the size of requests.  max_hw_sectors is set by
the device driver based upon the capabilities of the I/O
controller.

max_dev_sectors is a hard limit imposed by the storage device for
READ/WRITE requests. It is set by the disk driver.

max_sectors is a soft limit imposed by the block layer for
filesystem type requests.  This value can be overridden on a
per-device basis in /sys/block/<device>/queue/max_sectors_kb.
The soft limit can not exceed max_hw_sectors.

.. _`blk_queue_chunk_sectors`:

blk_queue_chunk_sectors
=======================

.. c:function:: void blk_queue_chunk_sectors(struct request_queue *q, unsigned int chunk_sectors)

    set size of the chunk for this queue

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int chunk_sectors:
        chunk sectors in the usual 512b unit

.. _`blk_queue_chunk_sectors.description`:

Description
-----------

If a driver doesn't want IOs to cross a given chunk size, it can set
this limit and prevent merging across chunks. Note that the chunk size
must currently be a power-of-2 in sectors. Also note that the block
layer must accept a page worth of data at any offset. So if the
crossing of chunks is a hard limitation in the driver, it must still be
prepared to split single page bios.

.. _`blk_queue_max_discard_sectors`:

blk_queue_max_discard_sectors
=============================

.. c:function:: void blk_queue_max_discard_sectors(struct request_queue *q, unsigned int max_discard_sectors)

    set max sectors for a single discard

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int max_discard_sectors:
        maximum number of sectors to discard

.. _`blk_queue_max_write_same_sectors`:

blk_queue_max_write_same_sectors
================================

.. c:function:: void blk_queue_max_write_same_sectors(struct request_queue *q, unsigned int max_write_same_sectors)

    set max sectors for a single write same

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int max_write_same_sectors:
        maximum number of sectors to write per command

.. _`blk_queue_max_segments`:

blk_queue_max_segments
======================

.. c:function:: void blk_queue_max_segments(struct request_queue *q, unsigned short max_segments)

    set max hw segments for a request for this queue

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned short max_segments:
        max number of segments

.. _`blk_queue_max_segments.description`:

Description
-----------

Enables a low level driver to set an upper limit on the number of
hw data segments in a request.

.. _`blk_queue_max_segment_size`:

blk_queue_max_segment_size
==========================

.. c:function:: void blk_queue_max_segment_size(struct request_queue *q, unsigned int max_size)

    set max segment size for blk_rq_map_sg

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int max_size:
        max size of segment in bytes

.. _`blk_queue_max_segment_size.description`:

Description
-----------

Enables a low level driver to set an upper limit on the size of a
coalesced segment

.. _`blk_queue_logical_block_size`:

blk_queue_logical_block_size
============================

.. c:function:: void blk_queue_logical_block_size(struct request_queue *q, unsigned short size)

    set logical block size for the queue

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned short size:
        the logical block size, in bytes

.. _`blk_queue_logical_block_size.description`:

Description
-----------

This should be set to the lowest possible block size that the
storage device can address.  The default of 512 covers most
hardware.

.. _`blk_queue_physical_block_size`:

blk_queue_physical_block_size
=============================

.. c:function:: void blk_queue_physical_block_size(struct request_queue *q, unsigned int size)

    set physical block size for the queue

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int size:
        the physical block size, in bytes

.. _`blk_queue_physical_block_size.description`:

Description
-----------

This should be set to the lowest possible sector size that the
hardware can operate on without reverting to read-modify-write
operations.

.. _`blk_queue_alignment_offset`:

blk_queue_alignment_offset
==========================

.. c:function:: void blk_queue_alignment_offset(struct request_queue *q, unsigned int offset)

    set physical block alignment offset

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int offset:
        alignment offset in bytes

.. _`blk_queue_alignment_offset.description`:

Description
-----------

Some devices are naturally misaligned to compensate for things like
the legacy DOS partition table 63-sector offset.  Low-level drivers
should call this function for devices whose first sector is not
naturally aligned.

.. _`blk_limits_io_min`:

blk_limits_io_min
=================

.. c:function:: void blk_limits_io_min(struct queue_limits *limits, unsigned int min)

    set minimum request size for a device

    :param struct queue_limits \*limits:
        the queue limits

    :param unsigned int min:
        smallest I/O size in bytes

.. _`blk_limits_io_min.description`:

Description
-----------

Some devices have an internal block size bigger than the reported
hardware sector size.  This function can be used to signal the
smallest I/O the device can perform without incurring a performance
penalty.

.. _`blk_queue_io_min`:

blk_queue_io_min
================

.. c:function:: void blk_queue_io_min(struct request_queue *q, unsigned int min)

    set minimum request size for the queue

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int min:
        smallest I/O size in bytes

.. _`blk_queue_io_min.description`:

Description
-----------

Storage devices may report a granularity or preferred minimum I/O
size which is the smallest request the device can perform without
incurring a performance penalty.  For disk drives this is often the
physical block size.  For RAID arrays it is often the stripe chunk
size.  A properly aligned multiple of minimum_io_size is the
preferred request size for workloads where a high number of I/O
operations is desired.

.. _`blk_limits_io_opt`:

blk_limits_io_opt
=================

.. c:function:: void blk_limits_io_opt(struct queue_limits *limits, unsigned int opt)

    set optimal request size for a device

    :param struct queue_limits \*limits:
        the queue limits

    :param unsigned int opt:
        smallest I/O size in bytes

.. _`blk_limits_io_opt.description`:

Description
-----------

Storage devices may report an optimal I/O size, which is the
device's preferred unit for sustained I/O.  This is rarely reported
for disk drives.  For RAID arrays it is usually the stripe width or
the internal track size.  A properly aligned multiple of
optimal_io_size is the preferred request size for workloads where
sustained throughput is desired.

.. _`blk_queue_io_opt`:

blk_queue_io_opt
================

.. c:function:: void blk_queue_io_opt(struct request_queue *q, unsigned int opt)

    set optimal request size for the queue

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int opt:
        optimal request size in bytes

.. _`blk_queue_io_opt.description`:

Description
-----------

Storage devices may report an optimal I/O size, which is the
device's preferred unit for sustained I/O.  This is rarely reported
for disk drives.  For RAID arrays it is usually the stripe width or
the internal track size.  A properly aligned multiple of
optimal_io_size is the preferred request size for workloads where
sustained throughput is desired.

.. _`blk_queue_stack_limits`:

blk_queue_stack_limits
======================

.. c:function:: void blk_queue_stack_limits(struct request_queue *t, struct request_queue *b)

    inherit underlying queue limits for stacked drivers

    :param struct request_queue \*t:
        the stacking driver (top)

    :param struct request_queue \*b:
        the underlying device (bottom)

.. _`blk_stack_limits`:

blk_stack_limits
================

.. c:function:: int blk_stack_limits(struct queue_limits *t, struct queue_limits *b, sector_t start)

    adjust queue_limits for stacked devices

    :param struct queue_limits \*t:
        the stacking driver limits (top device)

    :param struct queue_limits \*b:
        the underlying queue limits (bottom, component device)

    :param sector_t start:
        first data sector within component device

.. _`blk_stack_limits.description`:

Description
-----------

This function is used by stacking drivers like MD and DM to ensure
that all component devices have compatible block sizes and
alignments.  The stacking driver must provide a queue_limits
struct (top) and then iteratively call the stacking function for
all component (bottom) devices.  The stacking function will
attempt to combine the values and ensure proper alignment.

Returns 0 if the top and bottom queue_limits are compatible.  The
top device's block sizes and alignment offsets may be adjusted to
ensure alignment with the bottom device. If no compatible sizes
and alignments exist, -1 is returned and the resulting top
queue_limits will have the misaligned flag set to indicate that
the alignment_offset is undefined.

.. _`bdev_stack_limits`:

bdev_stack_limits
=================

.. c:function:: int bdev_stack_limits(struct queue_limits *t, struct block_device *bdev, sector_t start)

    adjust queue limits for stacked drivers

    :param struct queue_limits \*t:
        the stacking driver limits (top device)

    :param struct block_device \*bdev:
        the component block_device (bottom)

    :param sector_t start:
        first data sector within component device

.. _`bdev_stack_limits.description`:

Description
-----------

Merges queue limits for a top device and a block_device.  Returns
0 if alignment didn't change.  Returns -1 if adding the bottom
device caused misalignment.

.. _`disk_stack_limits`:

disk_stack_limits
=================

.. c:function:: void disk_stack_limits(struct gendisk *disk, struct block_device *bdev, sector_t offset)

    adjust queue limits for stacked drivers

    :param struct gendisk \*disk:
        MD/DM gendisk (top)

    :param struct block_device \*bdev:
        the underlying block device (bottom)

    :param sector_t offset:
        offset to beginning of data within component device

.. _`disk_stack_limits.description`:

Description
-----------

Merges the limits for a top level gendisk and a bottom level
block_device.

.. _`blk_queue_dma_pad`:

blk_queue_dma_pad
=================

.. c:function:: void blk_queue_dma_pad(struct request_queue *q, unsigned int mask)

    set pad mask

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int mask:
        pad mask

.. _`blk_queue_dma_pad.description`:

Description
-----------

Set dma pad mask.

Appending pad buffer to a request modifies the last entry of a
scatter list such that it includes the pad buffer.

.. _`blk_queue_update_dma_pad`:

blk_queue_update_dma_pad
========================

.. c:function:: void blk_queue_update_dma_pad(struct request_queue *q, unsigned int mask)

    update pad mask

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned int mask:
        pad mask

.. _`blk_queue_update_dma_pad.description`:

Description
-----------

Update dma pad mask.

Appending pad buffer to a request modifies the last entry of a
scatter list such that it includes the pad buffer.

.. _`blk_queue_dma_drain`:

blk_queue_dma_drain
===================

.. c:function:: int blk_queue_dma_drain(struct request_queue *q, dma_drain_needed_fn *dma_drain_needed, void *buf, unsigned int size)

    Set up a drain buffer for excess dma.

    :param struct request_queue \*q:
        the request queue for the device

    :param dma_drain_needed_fn \*dma_drain_needed:
        fn which returns non-zero if drain is necessary

    :param void \*buf:
        physically contiguous buffer

    :param unsigned int size:
        size of the buffer in bytes

.. _`blk_queue_dma_drain.description`:

Description
-----------

Some devices have excess DMA problems and can't simply discard (or
zero fill) the unwanted piece of the transfer.  They have to have a
real area of memory to transfer it into.  The use case for this is
ATAPI devices in DMA mode.  If the packet command causes a transfer
bigger than the transfer size some HBAs will lock up if there
aren't DMA elements to contain the excess transfer.  What this API
does is adjust the queue so that the buf is always appended
silently to the scatterlist.

.. _`blk_queue_dma_drain.note`:

Note
----

This routine adjusts max_hw_segments to make room for appending
the drain buffer.  If you call \ :c:func:`blk_queue_max_segments`\  after calling
this routine, you must set the limit to one fewer than your device
can support otherwise there won't be room for the drain buffer.

.. _`blk_queue_segment_boundary`:

blk_queue_segment_boundary
==========================

.. c:function:: void blk_queue_segment_boundary(struct request_queue *q, unsigned long mask)

    set boundary rules for segment merging

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned long mask:
        the memory boundary mask

.. _`blk_queue_virt_boundary`:

blk_queue_virt_boundary
=======================

.. c:function:: void blk_queue_virt_boundary(struct request_queue *q, unsigned long mask)

    set boundary rules for bio merging

    :param struct request_queue \*q:
        the request queue for the device

    :param unsigned long mask:
        the memory boundary mask

.. _`blk_queue_dma_alignment`:

blk_queue_dma_alignment
=======================

.. c:function:: void blk_queue_dma_alignment(struct request_queue *q, int mask)

    set dma length and memory alignment

    :param struct request_queue \*q:
        the request queue for the device

    :param int mask:
        alignment mask

.. _`blk_queue_dma_alignment.description`:

Description
-----------

set required memory and length alignment for direct dma transactions.
this is used when building direct io requests for the queue.

.. _`blk_queue_update_dma_alignment`:

blk_queue_update_dma_alignment
==============================

.. c:function:: void blk_queue_update_dma_alignment(struct request_queue *q, int mask)

    update dma length and memory alignment

    :param struct request_queue \*q:
        the request queue for the device

    :param int mask:
        alignment mask

.. _`blk_queue_update_dma_alignment.description`:

Description
-----------

update required memory and length alignment for direct dma transactions.
If the requested alignment is larger than the current alignment, then
the current queue alignment is updated to the new value, otherwise it
is left alone.  The design of this is to allow multiple objects
(driver, device, transport etc) to set their respective
alignments without having them interfere.

.. _`blk_queue_write_cache`:

blk_queue_write_cache
=====================

.. c:function:: void blk_queue_write_cache(struct request_queue *q, bool wc, bool fua)

    configure queue's write cache

    :param struct request_queue \*q:
        the request queue for the device

    :param bool wc:
        write back cache on or off

    :param bool fua:
        device supports FUA writes, if true

.. _`blk_queue_write_cache.description`:

Description
-----------

Tell the block layer about the write cache of \ ``q``\ .

.. This file was automatic generated / don't edit.

