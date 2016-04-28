.. -*- coding: utf-8; mode: rst -*-

.. _API-blkdev-issue-zeroout:

====================
blkdev_issue_zeroout
====================

*man blkdev_issue_zeroout(9)*

*4.6.0-rc5*

zero-fill a block range


Synopsis
========

.. c:function:: int blkdev_issue_zeroout( struct block_device * bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, bool discard )

Arguments
=========

``bdev``
    blockdev to write

``sector``
    start sector

``nr_sects``
    number of sectors to write

``gfp_mask``
    memory allocation flags (for bio_alloc)

``discard``
    whether to discard the block range


Description
===========

Zero-fill a block range. If the discard flag is set and the block device
guarantees that subsequent READ operations to the block range in
question will return zeroes, the blocks will be discarded. Should the
discard request fail, if the discard flag is not set, or if
discard_zeroes_data is not supported, this function will resort to
zeroing the blocks manually, thus provisioning (allocating, anchoring)
them. If the block device supports the WRITE SAME command
``blkdev_issue_zeroout`` will use it to optimize the process of clearing
the block range. Otherwise the zeroing will be performed using regular
WRITE calls.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
