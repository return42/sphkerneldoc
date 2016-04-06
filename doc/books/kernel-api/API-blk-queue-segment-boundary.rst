
.. _API-blk-queue-segment-boundary:

==========================
blk_queue_segment_boundary
==========================

*man blk_queue_segment_boundary(9)*

*4.6.0-rc1*

set boundary rules for segment merging


Synopsis
========

.. c:function:: void blk_queue_segment_boundary( struct request_queue * q, unsigned long mask )

Arguments
=========

``q``
    the request queue for the device

``mask``
    the memory boundary mask
