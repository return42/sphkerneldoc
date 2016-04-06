
.. _API-dma-buf-kunmap-atomic:

=====================
dma_buf_kunmap_atomic
=====================

*man dma_buf_kunmap_atomic(9)*

*4.6.0-rc1*

Unmap a page obtained by dma_buf_kmap_atomic.


Synopsis
========

.. c:function:: void dma_buf_kunmap_atomic( struct dma_buf * dmabuf, unsigned long page_num, void * vaddr )

Arguments
=========

``dmabuf``
    [in] buffer to unmap page from.

``page_num``
    [in] page in PAGE_SIZE units to unmap.

``vaddr``
    [in] kernel space pointer obtained from dma_buf_kmap_atomic.


Description
===========

This call must always succeed.
