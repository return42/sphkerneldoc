
.. _API-dma-buf-put:

===========
dma_buf_put
===========

*man dma_buf_put(9)*

*4.6.0-rc1*

decreases refcount of the buffer


Synopsis
========

.. c:function:: void dma_buf_put( struct dma_buf * dmabuf )

Arguments
=========

``dmabuf``
    [in] buffer to reduce refcount of


Description
===========

Uses file's refcounting done implicitly by ``fput``
