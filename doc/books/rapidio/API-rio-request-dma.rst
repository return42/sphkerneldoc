.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-request-dma:

===============
rio_request_dma
===============

*man rio_request_dma(9)*

*4.6.0-rc5*

request RapidIO capable DMA channel that supports specified target
RapidIO device.


Synopsis
========

.. c:function:: struct dma_chan * rio_request_dma( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device associated with DMA transfer


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
