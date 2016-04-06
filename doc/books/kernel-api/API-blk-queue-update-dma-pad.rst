
.. _API-blk-queue-update-dma-pad:

========================
blk_queue_update_dma_pad
========================

*man blk_queue_update_dma_pad(9)*

*4.6.0-rc1*

update pad mask


Synopsis
========

.. c:function:: void blk_queue_update_dma_pad( struct request_queue * q, unsigned int mask )

Arguments
=========

``q``
    the request queue for the device

``mask``
    pad mask


Description
===========

Update dma pad mask.

Appending pad buffer to a request modifies the last entry of a scatter list such that it includes the pad buffer.
