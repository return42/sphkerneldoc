.. -*- coding: utf-8; mode: rst -*-

.. _API-z8530-sync-dma-open:

===================
z8530_sync_dma_open
===================

*man z8530_sync_dma_open(9)*

*4.6.0-rc5*

Open a Z8530 for DMA I/O


Synopsis
========

.. c:function:: int z8530_sync_dma_open( struct net_device * dev, struct z8530_channel * c )

Arguments
=========

``dev``
    The network device to attach

``c``
    The Z8530 channel to configure in sync DMA mode.


Description
===========

Set up a Z85x30 device for synchronous DMA in both directions. Two ISA
DMA channels must be available for this to work. We assume ISA DMA
driven I/O and PC limits on access.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
