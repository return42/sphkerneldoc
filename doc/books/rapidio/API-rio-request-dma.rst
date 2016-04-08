
.. _API-rio-request-dma:

===============
rio_request_dma
===============

*man rio_request_dma(9)*

*4.6.0-rc1*

request RapidIO capable DMA channel that supports specified target RapidIO device.


Synopsis
========

.. c:function:: struct dma_chan ⋆ rio_request_dma( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device associated with DMA transfer


Description
===========

Returns pointer to allocated DMA channel or NULL if failed.
