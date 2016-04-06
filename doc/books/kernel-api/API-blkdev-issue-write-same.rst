
.. _API-blkdev-issue-write-same:

=======================
blkdev_issue_write_same
=======================

*man blkdev_issue_write_same(9)*

*4.6.0-rc1*

queue a write same operation


Synopsis
========

.. c:function:: int blkdev_issue_write_same( struct block_device * bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, struct page * page )

Arguments
=========

``bdev``
    target blockdev

``sector``
    start sector

``nr_sects``
    number of sectors to write

``gfp_mask``
    memory allocation flags (for bio_alloc)

``page``
    page containing data to write


Description
===========

Issue a write same request for the sectors in question.
