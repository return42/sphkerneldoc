.. -*- coding: utf-8; mode: rst -*-

.. _API-z8530-sync-dma-close:

====================
z8530_sync_dma_close
====================

*man z8530_sync_dma_close(9)*

*4.6.0-rc5*

Close down DMA I/O


Synopsis
========

.. c:function:: int z8530_sync_dma_close( struct net_device * dev, struct z8530_channel * c )

Arguments
=========

``dev``
    Network device to detach

``c``
    Z8530 channel to move into discard mode


Description
===========

Shut down a DMA mode synchronous interface. Halt the DMA, and free the
buffers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
