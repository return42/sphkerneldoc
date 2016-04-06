
.. _API-dma-buf-unmap-attachment:

========================
dma_buf_unmap_attachment
========================

*man dma_buf_unmap_attachment(9)*

*4.6.0-rc1*

unmaps and decreases usecount of the buffer;might deallocate the scatterlist associated. Is a wrapper for ``unmap_dma_buf`` of dma_buf_ops.


Synopsis
========

.. c:function:: void dma_buf_unmap_attachment( struct dma_buf_attachment * attach, struct sg_table * sg_table, enum dma_data_direction direction )

Arguments
=========

``attach``
    [in] attachment to unmap buffer from

``sg_table``
    [in] scatterlist info of the buffer to unmap

``direction``
    [in] direction of DMA transfer
