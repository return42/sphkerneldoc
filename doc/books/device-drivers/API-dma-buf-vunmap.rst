
.. _API-dma-buf-vunmap:

==============
dma_buf_vunmap
==============

*man dma_buf_vunmap(9)*

*4.6.0-rc1*

Unmap a vmap obtained by dma_buf_vmap.


Synopsis
========

.. c:function:: void dma_buf_vunmap( struct dma_buf * dmabuf, void * vaddr )

Arguments
=========

``dmabuf``
    [in] buffer to vunmap

``vaddr``
    [in] vmap to vunmap
