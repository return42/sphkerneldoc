.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/blkdev.h

.. _`bio_integrity_intervals`:

bio_integrity_intervals
=======================

.. c:function:: unsigned int bio_integrity_intervals(struct blk_integrity *bi, unsigned int sectors)

    Return number of integrity intervals for a bio

    :param bi:
        blk_integrity profile for device
    :type bi: struct blk_integrity \*

    :param sectors:
        Size of the bio in 512-byte sectors
    :type sectors: unsigned int

.. _`bio_integrity_intervals.description`:

Description
-----------

The block layer calculates everything in 512 byte
sectors but integrity metadata is done in terms of the data integrity
interval size of the storage device.  Convert the block layer sectors
to the appropriate number of integrity intervals.

.. This file was automatic generated / don't edit.

