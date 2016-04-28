.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-request-mport-dma:

=====================
rio_request_mport_dma
=====================

*man rio_request_mport_dma(9)*

*4.6.0-rc5*

request RapidIO capable DMA channel associated with specified local
RapidIO mport device.


Synopsis
========

.. c:function:: struct dma_chan * rio_request_mport_dma( struct rio_mport * mport )

Arguments
=========

``mport``
    RIO mport to perform DMA data transfers


Description
===========

Returns pointer to allocated DMA channel or NULL if failed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
