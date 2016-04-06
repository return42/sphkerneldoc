
.. _API-blk-queue-max-discard-sectors:

=============================
blk_queue_max_discard_sectors
=============================

*man blk_queue_max_discard_sectors(9)*

*4.6.0-rc1*

set max sectors for a single discard


Synopsis
========

.. c:function:: void blk_queue_max_discard_sectors( struct request_queue * q, unsigned int max_discard_sectors )

Arguments
=========

``q``
    the request queue for the device

``max_discard_sectors``
    maximum number of sectors to discard
