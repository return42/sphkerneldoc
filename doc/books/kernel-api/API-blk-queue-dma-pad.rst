.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-dma-pad:

=================
blk_queue_dma_pad
=================

*man blk_queue_dma_pad(9)*

*4.6.0-rc5*

set pad mask


Synopsis
========

.. c:function:: void blk_queue_dma_pad( struct request_queue * q, unsigned int mask )

Arguments
=========

``q``
    the request queue for the device

``mask``
    pad mask


Description
===========

Set dma pad mask.

Appending pad buffer to a request modifies the last entry of a scatter
list such that it includes the pad buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
