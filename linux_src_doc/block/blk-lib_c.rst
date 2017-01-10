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
        BLKDEV_IFL\_\* flags to control behaviour

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

.. _`__blkdev_issue_write_zeroes`:

__blkdev_issue_write_zeroes
===========================

.. c:function:: int __blkdev_issue_write_zeroes(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, struct bio **biop)

    generate number of bios with WRITE ZEROES

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

.. _`__blkdev_issue_write_zeroes.description`:

Description
-----------

Generate and issue number of bios(REQ_OP_WRITE_ZEROES) with zerofiled pages.

.. _`__blkdev_issue_zeroout`:

__blkdev_issue_zeroout
======================

.. c:function:: int __blkdev_issue_zeroout(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, struct bio **biop, bool discard)

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

    :param bool discard:
        discard flag

.. _`__blkdev_issue_zeroout.description`:

Description
-----------

Generate and issue number of bios with zerofiled pages.

.. _`blkdev_issue_zeroout`:

blkdev_issue_zeroout
====================

.. c:function:: int blkdev_issue_zeroout(struct block_device *bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, bool discard)

    zero-fill a block range

    :param struct block_device \*bdev:
        blockdev to write

    :param sector_t sector:
        start sector

    :param sector_t nr_sects:
        number of sectors to write

    :param gfp_t gfp_mask:
        memory allocation flags (for bio_alloc)

    :param bool discard:
        whether to discard the block range

.. _`blkdev_issue_zeroout.description`:

Description
-----------

Zero-fill a block range.  If the discard flag is set and the block
device guarantees that subsequent READ operations to the block range
in question will return zeroes, the blocks will be discarded. Should
the discard request fail, if the discard flag is not set, or if
discard_zeroes_data is not supported, this function will resort to
zeroing the blocks manually, thus provisioning (allocating,
anchoring) them. If the block device supports WRITE ZEROES or WRITE SAME
command(s), \ :c:func:`blkdev_issue_zeroout`\  will use it to optimize the process of
clearing the block range. Otherwise the zeroing will be performed
using regular WRITE calls.

.. This file was automatic generated / don't edit.

