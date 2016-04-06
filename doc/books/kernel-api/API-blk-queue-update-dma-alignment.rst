
.. _API-blk-queue-update-dma-alignment:

==============================
blk_queue_update_dma_alignment
==============================

*man blk_queue_update_dma_alignment(9)*

*4.6.0-rc1*

update dma length and memory alignment


Synopsis
========

.. c:function:: void blk_queue_update_dma_alignment( struct request_queue * q, int mask )

Arguments
=========

``q``
    the request queue for the device

``mask``
    alignment mask


description
===========

update required memory and length alignment for direct dma transactions. If the requested alignment is larger than the current alignment, then the current queue alignment is
updated to the new value, otherwise it is left alone. The design of this is to allow multiple objects (driver, device, transport etc) to set their respective alignments without
having them interfere.
