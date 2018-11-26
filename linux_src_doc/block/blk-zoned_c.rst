.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-zoned.c

.. _`blkdev_nr_zones`:

blkdev_nr_zones
===============

.. c:function:: unsigned int blkdev_nr_zones(struct block_device *bdev)

    Get number of zones

    :param bdev:
        Target block device
    :type bdev: struct block_device \*

.. _`blkdev_nr_zones.description`:

Description
-----------

Return the total number of zones of a zoned block device.
For a regular block device, the number of zones is always 0.

.. _`blkdev_report_zones`:

blkdev_report_zones
===================

.. c:function:: int blkdev_report_zones(struct block_device *bdev, sector_t sector, struct blk_zone *zones, unsigned int *nr_zones, gfp_t gfp_mask)

    Get zones information

    :param bdev:
        Target block device
    :type bdev: struct block_device \*

    :param sector:
        Sector from which to report zones
    :type sector: sector_t

    :param zones:
        Array of zone structures where to return the zones information
    :type zones: struct blk_zone \*

    :param nr_zones:
        Number of zone structures in the zone array
    :type nr_zones: unsigned int \*

    :param gfp_mask:
        Memory allocation flags (for bio_alloc)
    :type gfp_mask: gfp_t

.. _`blkdev_report_zones.description`:

Description
-----------

Get zone information starting from the zone containing \ ``sector``\ .
The number of zone information reported may be less than the number
requested by \ ``nr_zones``\ . The number of zones actually reported is
returned in \ ``nr_zones``\ .

.. _`blkdev_reset_zones`:

blkdev_reset_zones
==================

.. c:function:: int blkdev_reset_zones(struct block_device *bdev, sector_t sector, sector_t nr_sectors, gfp_t gfp_mask)

    Reset zones write pointer

    :param bdev:
        Target block device
    :type bdev: struct block_device \*

    :param sector:
        Start sector of the first zone to reset
    :type sector: sector_t

    :param nr_sectors:
        Number of sectors, at least the length of one zone
    :type nr_sectors: sector_t

    :param gfp_mask:
        Memory allocation flags (for bio_alloc)
    :type gfp_mask: gfp_t

.. _`blkdev_reset_zones.description`:

Description
-----------

Reset the write pointer of the zones contained in the range
\ ``sector``\ ..@sector+@nr_sectors. Specifying the entire disk sector range
is valid, but the specified range should not contain conventional zones.

.. _`blk_revalidate_disk_zones`:

blk_revalidate_disk_zones
=========================

.. c:function:: int blk_revalidate_disk_zones(struct gendisk *disk)

    (re)allocate and initialize zone bitmaps

    :param disk:
        Target disk
    :type disk: struct gendisk \*

.. _`blk_revalidate_disk_zones.description`:

Description
-----------

Helper function for low-level device drivers to (re) allocate and initialize
a disk request queue zone bitmaps. This functions should normally be called
within the disk ->revalidate method. For BIO based queues, no zone bitmap
is allocated.

.. This file was automatic generated / don't edit.

