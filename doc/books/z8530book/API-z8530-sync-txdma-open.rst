
.. _API-z8530-sync-txdma-open:

=====================
z8530_sync_txdma_open
=====================

*man z8530_sync_txdma_open(9)*

*4.6.0-rc1*

Open a Z8530 for TX driven DMA


Synopsis
========

.. c:function:: int z8530_sync_txdma_open( struct net_device * dev, struct z8530_channel * c )

Arguments
=========

``dev``
    The network device to attach

``c``
    The Z8530 channel to configure in sync DMA mode.


Description
===========

Set up a Z85x30 device for synchronous DMA transmission. One ISA DMA channel must be available for this to work. The receive side is run in PIO mode, but then it has the bigger
FIFO.
