.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-lib.c

.. _`blkdev_issue_discard`:

blkdev_issue_discard
====================

.. c:function:: int blkdev_issue_discard(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, unsigned long flags)

    queue a discard

    :param bdev:
        blockdev to issue discard for
    :type bdev: struct block_device \*

    :param sector:
        start sector
    :type sector: sector_t

    :param nr_sects:
        number of sectors to discard
    :type nr_sects: sector_t

    :param gfp_mask:
        memory allocation flags (for bio_alloc)
    :type gfp_mask: gfp_t

    :param flags:
        BLKDEV_DISCARD_* flags to control behaviour
    :type flags: unsigned long

.. _`blkdev_issue_discard.description`:

Description
-----------

   Issue a discard request for the sectors in question.

.. _`__blkdev_issue_write_same`:

__blkdev_issue_write_same
=========================

.. c:function:: int __blkdev_issue_write_same(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, struct page *page, struct bio **biop)

    generate number of bios with same page

    :param bdev:
        target blockdev
    :type bdev: struct block_device \*

    :param sector:
        start sector
    :type sector: sector_t

    :param nr_sects:
        number of sectors to write
    :type nr_sects: sector_t

    :param gfp_mask:
        memory allocation flags (for bio_alloc)
    :type gfp_mask: gfp_t

    :param page:
        page containing data to write
    :type page: struct page \*

    :param biop:
        pointer to anchor bio
    :type biop: struct bio \*\*

.. _`__blkdev_issue_write_same.description`:

Description
-----------

 Generate and issue number of bios(REQ_OP_WRITE_SAME) with same page.

.. _`blkdev_issue_write_same`:

blkdev_issue_write_same
=======================

.. c:function:: int blkdev_issue_write_same(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, struct page *page)

    queue a write same operation

    :param bdev:
        target blockdev
    :type bdev: struct block_device \*

    :param sector:
        start sector
    :type sector: sector_t

    :param nr_sects:
        number of sectors to write
    :type nr_sects: sector_t

    :param gfp_mask:
        memory allocation flags (for bio_alloc)
    :type gfp_mask: gfp_t

    :param page:
        page containing data
    :type page: struct page \*

.. _`blkdev_issue_write_same.description`:

Description
-----------

   Issue a write same request for the sectors in question.

.. _`__blkdev_issue_zeroout`:

__blkdev_issue_zeroout
======================

.. c:function:: int __blkdev_issue_zeroout(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, struct bio **biop, unsigned flags)

    generate number of zero filed write bios

    :param bdev:
        blockdev to issue
    :type bdev: struct block_device \*

    :param sector:
        start sector
    :type sector: sector_t

    :param nr_sects:
        number of sectors to write
    :type nr_sects: sector_t

    :param gfp_mask:
        memory allocation flags (for bio_alloc)
    :type gfp_mask: gfp_t

    :param biop:
        pointer to anchor bio
    :type biop: struct bio \*\*

    :param flags:
        controls detailed behavior
    :type flags: unsigned

.. _`__blkdev_issue_zeroout.description`:

Description
-----------

 Zero-fill a block range, either using hardware offload or by explicitly
 writing zeroes to the device.

 If a device is using logical block provisioning, the underlying space will
 not be released if \ ``flags``\  contains BLKDEV_ZERO_NOUNMAP.

 If \ ``flags``\  contains BLKDEV_ZERO_NOFALLBACK, the function will return
 -EOPNOTSUPP if no explicit hardware offload for zeroing is provided.

.. _`blkdev_issue_zeroout`:

blkdev_issue_zeroout
====================

.. c:function:: int blkdev_issue_zeroout(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, unsigned flags)

    zero-fill a block range

    :param bdev:
        blockdev to write
    :type bdev: struct block_device \*

    :param sector:
        start sector
    :type sector: sector_t

    :param nr_sects:
        number of sectors to write
    :type nr_sects: sector_t

    :param gfp_mask:
        memory allocation flags (for bio_alloc)
    :type gfp_mask: gfp_t

    :param flags:
        controls detailed behavior
    :type flags: unsigned

.. _`blkdev_issue_zeroout.description`:

Description
-----------

 Zero-fill a block range, either using hardware offload or by explicitly
 writing zeroes to the device.  See \ :c:func:`__blkdev_issue_zeroout`\  for the
 valid values for \ ``flags``\ .

.. This file was automatic generated / don't edit.

