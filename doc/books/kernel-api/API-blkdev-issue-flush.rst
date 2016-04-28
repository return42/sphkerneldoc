.. -*- coding: utf-8; mode: rst -*-

.. _API-blkdev-issue-flush:

==================
blkdev_issue_flush
==================

*man blkdev_issue_flush(9)*

*4.6.0-rc5*

queue a flush


Synopsis
========

.. c:function:: int blkdev_issue_flush( struct block_device * bdev, gfp_t gfp_mask, sector_t * error_sector )

Arguments
=========

``bdev``
    blockdev to issue flush for

``gfp_mask``
    memory allocation flags (for bio_alloc)

``error_sector``
    error sector


Description
===========

Issue a flush for the block device in question. Caller can supply room
for storing the error offset in case of a flush error, if they wish to.
If WAIT flag is not passed then caller may check only what request was
pushed in some internal queue for later handling.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
