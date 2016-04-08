
.. _API-rio-request-mport-dma:

=====================
rio_request_mport_dma
=====================

*man rio_request_mport_dma(9)*

*4.6.0-rc1*

request RapidIO capable DMA channel associated with specified local RapidIO mport device.


Synopsis
========

.. c:function:: struct dma_chan ⋆ rio_request_mport_dma( struct rio_mport * mport )

Arguments
=========

``mport``
    RIO mport to perform DMA data transfers


Description
===========

Returns pointer to allocated DMA channel or NULL if failed.
