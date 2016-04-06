
.. _API-dma-buf-vmap:

============
dma_buf_vmap
============

*man dma_buf_vmap(9)*

*4.6.0-rc1*

Create virtual mapping for the buffer object into kernel address space. Same restrictions as for vmap and friends apply.


Synopsis
========

.. c:function:: void ⋆ dma_buf_vmap( struct dma_buf * dmabuf )

Arguments
=========

``dmabuf``
    [in] buffer to vmap


Description
===========

This call may fail due to lack of virtual mapping address space. These calls are optional in drivers. The intended use for them is for mapping objects linear in kernel space for
high use objects. Please attempt to use kmap/kunmap before thinking about these interfaces.

Returns NULL on error.
