
.. _API-dma-buf-kmap-atomic:

===================
dma_buf_kmap_atomic
===================

*man dma_buf_kmap_atomic(9)*

*4.6.0-rc1*

Map a page of the buffer object into kernel address space. The same restrictions as for kmap_atomic and friends apply.


Synopsis
========

.. c:function:: void ⋆ dma_buf_kmap_atomic( struct dma_buf * dmabuf, unsigned long page_num )

Arguments
=========

``dmabuf``
    [in] buffer to map page from.

``page_num``
    [in] page in PAGE_SIZE units to map.


Description
===========

This call must always succeed, any necessary preparations that might fail need to be done in begin_cpu_access.
