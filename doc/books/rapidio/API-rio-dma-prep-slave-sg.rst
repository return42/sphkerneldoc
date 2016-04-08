
.. _API-rio-dma-prep-slave-sg:

=====================
rio_dma_prep_slave_sg
=====================

*man rio_dma_prep_slave_sg(9)*

*4.6.0-rc1*

RapidIO specific wrapper for device_prep_slave_sg callback defined by DMAENGINE.


Synopsis
========

.. c:function:: struct dma_async_tx_descriptor ⋆ rio_dma_prep_slave_sg( struct rio_dev * rdev, struct dma_chan * dchan, struct rio_dma_data * data, enum dma_transfer_direction direction, unsigned long flags )

Arguments
=========

``rdev``
    RIO device control structure

``dchan``
    DMA channel to configure

``data``
    RIO specific data descriptor

``direction``
    DMA data transfer direction (TO or FROM the device)

``flags``
    dmaengine defined flags


Description
===========

Initializes RapidIO capable DMA channel for the specified data transfer. Uses DMA channel private extension to pass information related to remote target RIO device. Returns pointer
to DMA transaction descriptor or NULL if failed.
