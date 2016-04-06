
.. _API-blk-queue-max-write-same-sectors:

================================
blk_queue_max_write_same_sectors
================================

*man blk_queue_max_write_same_sectors(9)*

*4.6.0-rc1*

set max sectors for a single write same


Synopsis
========

.. c:function:: void blk_queue_max_write_same_sectors( struct request_queue * q, unsigned int max_write_same_sectors )

Arguments
=========

``q``
    the request queue for the device

``max_write_same_sectors``
    maximum number of sectors to write per command
