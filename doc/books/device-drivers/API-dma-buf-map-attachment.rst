.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-buf-map-attachment:

======================
dma_buf_map_attachment
======================

*man dma_buf_map_attachment(9)*

*4.6.0-rc5*

Returns the scatterlist table of the attachment; mapped into _device_
address space. Is a wrapper for ``map_dma_buf`` of the dma_buf_ops.


Synopsis
========

.. c:function:: struct sg_table * dma_buf_map_attachment( struct dma_buf_attachment * attach, enum dma_data_direction direction )

Arguments
=========

``attach``
    [in] attachment whose scatterlist is to be returned

``direction``
    [in] direction of DMA transfer


Description
===========

Returns sg_table containing the scatterlist to be returned; returns
ERR_PTR on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
