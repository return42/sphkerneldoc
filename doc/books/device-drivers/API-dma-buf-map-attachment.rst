
.. _API-dma-buf-map-attachment:

======================
dma_buf_map_attachment
======================

*man dma_buf_map_attachment(9)*

*4.6.0-rc1*

Returns the scatterlist table of the attachment; mapped into _device_ address space. Is a wrapper for ``map_dma_buf`` of the dma_buf_ops.


Synopsis
========

.. c:function:: struct sg_table ⋆ dma_buf_map_attachment( struct dma_buf_attachment * attach, enum dma_data_direction direction )

Arguments
=========

``attach``
    [in] attachment whose scatterlist is to be returned

``direction``
    [in] direction of DMA transfer


Description
===========

Returns sg_table containing the scatterlist to be returned; returns ERR_PTR on error.
