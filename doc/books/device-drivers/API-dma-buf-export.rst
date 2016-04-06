
.. _API-dma-buf-export:

==============
dma_buf_export
==============

*man dma_buf_export(9)*

*4.6.0-rc1*

Creates a new dma_buf, and associates an anon file with this buffer, so it can be exported. Also connect the allocator specific data and ops to the buffer. Additionally, provide a
name string for exporter; useful in debugging.


Synopsis
========

.. c:function:: struct dma_buf ⋆ dma_buf_export( const struct dma_buf_export_info * exp_info )

Arguments
=========

``exp_info``
    [in] holds all the export related information provided by the exporter. see struct dma_buf_export_info for further details.


Description
===========

Returns, on success, a newly created dma_buf object, which wraps the supplied private data and operations for dma_buf_ops. On either missing ops, or error in allocating struct
dma_buf, will return negative error.
