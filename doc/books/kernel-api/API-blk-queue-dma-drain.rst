.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-dma-drain:

===================
blk_queue_dma_drain
===================

*man blk_queue_dma_drain(9)*

*4.6.0-rc5*

Set up a drain buffer for excess dma.


Synopsis
========

.. c:function:: int blk_queue_dma_drain( struct request_queue * q, dma_drain_needed_fn * dma_drain_needed, void * buf, unsigned int size )

Arguments
=========

``q``
    the request queue for the device

``dma_drain_needed``
    fn which returns non-zero if drain is necessary

``buf``
    physically contiguous buffer

``size``
    size of the buffer in bytes


Description
===========

Some devices have excess DMA problems and can't simply discard (or zero
fill) the unwanted piece of the transfer. They have to have a real area
of memory to transfer it into. The use case for this is ATAPI devices in
DMA mode. If the packet command causes a transfer bigger than the
transfer size some HBAs will lock up if there aren't DMA elements to
contain the excess transfer. What this API does is adjust the queue so
that the buf is always appended silently to the scatterlist.


Note
====

This routine adjusts max_hw_segments to make room for appending the
drain buffer. If you call ``blk_queue_max_segments`` after calling this
routine, you must set the limit to one fewer than your device can
support otherwise there won't be room for the drain buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
