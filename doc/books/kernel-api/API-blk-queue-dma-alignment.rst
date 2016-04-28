.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-dma-alignment:

=======================
blk_queue_dma_alignment
=======================

*man blk_queue_dma_alignment(9)*

*4.6.0-rc5*

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

set required memory and length alignment for direct dma transactions.
this is used when building direct io requests for the queue.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
