.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-lib.c

.. _`blkdev_issue_discard`:

blkdev_issue_discard
====================

.. c:function:: int blkdev_issue_discard(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, unsigned long flags)

    queue a discard

    :param struct block_device \*bdev:
        blockdev to issue discard for

    :param sector_t sector:
        start sector

    :param sector_t nr_sects:
        number of sectors to discard

    :param gfp_t gfp_mask:
        memory allocation flags (for bio_alloc)

    :param unsigned long flags:
        BLKDEV_DISCARD_* flags to control behaviour

.. _`blkdev_issue_discard.description`:

Description
-----------

   Issue a discard request for the sectors in question.

.. _`__blkdev_issue_write_same`:

__blkdev_issue_write_same
=========================

.. c:function:: int __blkdev_issue_write_same(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, struct page *page, struct bio **biop)

    generate number of bios with same page

    :param struct block_device \*bdev:
        target blockdev

    :param sector_t sector:
        start sector

    :param sector_t nr_sects:
        number of sectors to write

    :param gfp_t gfp_mask:
        memory allocation flags (for bio_alloc)

    :param struct page \*page:
        page containing data to write

    :param struct bio \*\*biop:
        pointer to anchor bio

.. _`__blkdev_issue_write_same.description`:

Description
-----------

 Generate and issue number of bios(REQ_OP_WRITE_SAME) with same page.

.. _`blkdev_issue_write_same`:

blkdev_issue_write_same
=======================

.. c:function:: int blkdev_issue_write_same(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, struct page *page)

    queue a write same operation

    :param struct block_device \*bdev:
        target blockdev

    :param sector_t sector:
        start sector

    :param sector_t nr_sects:
        number of sectors to write

    :param gfp_t gfp_mask:
        memory allocation flags (for bio_alloc)

    :param struct page \*page:
        page containing data

.. _`blkdev_issue_write_same.description`:

Description
-----------

   Issue a write same request for the sectors in question.

.. _`__blkdev_issue_zeroout`:

__blkdev_issue_zeroout
======================

.. c:function:: int __blkdev_issue_zeroout(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, struct bio **biop, unsigned flags)

    generate number of zero filed write bios

    :param struct block_device \*bdev:
        blockdev to issue

    :param sector_t sector:
        start sector

    :param sector_t nr_sects:
        number of sectors to write

    :param gfp_t gfp_mask:
        memory allocation flags (for bio_alloc)

    :param struct bio \*\*biop:
        pointer to anchor bio

    :param unsigned flags:
        controls detailed behavior

.. _`__blkdev_issue_zeroout.description`:

Description
-----------

 Zero-fill a block range, either using hardware offload or by explicitly
 writing zeroes to the device.

 Note that this function may fail with -EOPNOTSUPP if the driver signals
 zeroing offload support, but the device fails to process the command (for
 some devices there is no non-destructive way to verify whether this
 operation is actually supported).  In this case the caller should call
 retry the call to \ :c:func:`blkdev_issue_zeroout`\  and the fallback path will be used.

 If a device is using logical block provisioning, the underlying space will
 not be released if \ ``flags``\  contains BLKDEV_ZERO_NOUNMAP.

 If \ ``flags``\  contains BLKDEV_ZERO_NOFALLBACK, the function will return
 -EOPNOTSUPP if no explicit hardware offload for zeroing is provided.

.. _`blkdev_issue_zeroout`:

blkdev_issue_zeroout
====================

.. c:function:: int blkdev_issue_zeroout(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, unsigned flags)

    zero-fill a block range

    :param struct block_device \*bdev:
        blockdev to write

    :param sector_t sector:
        start sector

    :param sector_t nr_sects:
        number of sectors to write

    :param gfp_t gfp_mask:
        memory allocation flags (for bio_alloc)

    :param unsigned flags:
        controls detailed behavior

.. _`blkdev_issue_zeroout.description`:

Description
-----------

 Zero-fill a block range, either using hardware offload or by explicitly
 writing zeroes to the device.  See \ :c:func:`__blkdev_issue_zeroout`\  for the
 valid values for \ ``flags``\ .

.. This file was automatic generated / don't edit.

