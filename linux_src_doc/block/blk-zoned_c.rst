.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-zoned.c

.. _`blkdev_report_zones`:

blkdev_report_zones
===================

.. c:function:: int blkdev_report_zones(struct block_device *bdev, sector_t sector, struct blk_zone *zones, unsigned int *nr_zones, gfp_t gfp_mask)

    Get zones information

    :param struct block_device \*bdev:
        Target block device

    :param sector_t sector:
        Sector from which to report zones

    :param struct blk_zone \*zones:
        Array of zone structures where to return the zones information

    :param unsigned int \*nr_zones:
        Number of zone structures in the zone array

    :param gfp_t gfp_mask:
        Memory allocation flags (for bio_alloc)

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

    :param struct block_device \*bdev:
        Target block device

    :param sector_t sector:
        Start sector of the first zone to reset

    :param sector_t nr_sectors:
        Number of sectors, at least the length of one zone

    :param gfp_t gfp_mask:
        Memory allocation flags (for bio_alloc)

.. _`blkdev_reset_zones.description`:

Description
-----------

Reset the write pointer of the zones contained in the range
\ ``sector``\ ..@sector+@nr_sectors. Specifying the entire disk sector range
is valid, but the specified range should not contain conventional zones.

.. _`blkdev_report_zones_ioctl`:

blkdev_report_zones_ioctl
=========================

.. c:function:: int blkdev_report_zones_ioctl(struct block_device *bdev, fmode_t mode, unsigned int cmd, unsigned long arg)

    Called from blkdev_ioctl.

    :param struct block_device \*bdev:
        *undescribed*

    :param fmode_t mode:
        *undescribed*

    :param unsigned int cmd:
        *undescribed*

    :param unsigned long arg:
        *undescribed*

.. _`blkdev_reset_zones_ioctl`:

blkdev_reset_zones_ioctl
========================

.. c:function:: int blkdev_reset_zones_ioctl(struct block_device *bdev, fmode_t mode, unsigned int cmd, unsigned long arg)

    Called from blkdev_ioctl.

    :param struct block_device \*bdev:
        *undescribed*

    :param fmode_t mode:
        *undescribed*

    :param unsigned int cmd:
        *undescribed*

    :param unsigned long arg:
        *undescribed*

.. This file was automatic generated / don't edit.

