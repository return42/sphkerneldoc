
.. _API-dma-buf-kunmap:

==============
dma_buf_kunmap
==============

*man dma_buf_kunmap(9)*

*4.6.0-rc1*

Unmap a page obtained by dma_buf_kmap.


Synopsis
========

.. c:function:: void dma_buf_kunmap( struct dma_buf * dmabuf, unsigned long page_num, void * vaddr )

Arguments
=========

``dmabuf``
    [in] buffer to unmap page from.

``page_num``
    [in] page in PAGE_SIZE units to unmap.

``vaddr``
    [in] kernel space pointer obtained from dma_buf_kmap.


Description
===========

This call must always succeed.
