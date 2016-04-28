.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-dma-prep-xfer:

=================
rio_dma_prep_xfer
=================

*man rio_dma_prep_xfer(9)*

*4.6.0-rc5*

RapidIO specific wrapper for device_prep_slave_sg callback defined by
DMAENGINE.


Synopsis
========

.. c:function:: struct dma_async_tx_descriptor * rio_dma_prep_xfer( struct dma_chan * dchan, u16 destid, struct rio_dma_data * data, enum dma_transfer_direction direction, unsigned long flags )

Arguments
=========

``dchan``
    DMA channel to configure

``destid``
    target RapidIO device destination ID

``data``
    RIO specific data descriptor

``direction``
    DMA data transfer direction (TO or FROM the device)

``flags``
    dmaengine defined flags


Description
===========

Initializes RapidIO capable DMA channel for the specified data transfer.
Uses DMA channel private extension to pass information related to remote
target RIO device. Returns pointer to DMA transaction descriptor or NULL
if failed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
