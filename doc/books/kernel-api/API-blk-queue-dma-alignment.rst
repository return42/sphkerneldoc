
.. _API-blk-queue-dma-alignment:

=======================
blk_queue_dma_alignment
=======================

*man blk_queue_dma_alignment(9)*

*4.6.0-rc1*

set dma length and memory alignment


Synopsis
========

.. c:function:: void blk_queue_dma_alignment( struct request_queue * q, int mask )

Arguments
=========

``q``
    the request queue for the device

``mask``
    alignment mask


description
===========

set required memory and length alignment for direct dma transactions. this is used when building direct io requests for the queue.
