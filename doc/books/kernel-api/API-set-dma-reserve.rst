.. -*- coding: utf-8; mode: rst -*-

.. _API-set-dma-reserve:

===============
set_dma_reserve
===============

*man set_dma_reserve(9)*

*4.6.0-rc5*

set the specified number of pages reserved in the first zone


Synopsis
========

.. c:function:: void set_dma_reserve( unsigned long new_dma_reserve )

Arguments
=========

``new_dma_reserve``
    The number of pages to mark reserved


Description
===========

The per-cpu batchsize and zone watermarks are determined by
managed_pages. In the DMA zone, a significant percentage may be
consumed by kernel image and other unfreeable allocations which can skew
the watermarks badly. This function may optionally be used to account
for unfreeable pages in the first zone (e.g., ZONE_DMA). The effect
will be lower watermarks and smaller per-cpu batchsize.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
