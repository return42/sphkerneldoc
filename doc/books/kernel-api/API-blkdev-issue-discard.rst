
.. _API-blkdev-issue-discard:

====================
blkdev_issue_discard
====================

*man blkdev_issue_discard(9)*

*4.6.0-rc1*

queue a discard


Synopsis
========

.. c:function:: int blkdev_issue_discard( struct block_device * bdev, sector_t sector, sector_t nr_sects, gfp_t gfp_mask, unsigned long flags )

Arguments
=========

``bdev``
    blockdev to issue discard for

``sector``
    start sector

``nr_sects``
    number of sectors to discard

``gfp_mask``
    memory allocation flags (for bio_alloc)

``flags``
    BLKDEV_IFL_⋆ flags to control behaviour


Description
===========

Issue a discard request for the sectors in question.
