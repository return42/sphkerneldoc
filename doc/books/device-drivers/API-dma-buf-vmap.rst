.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-buf-vmap:

============
dma_buf_vmap
============

*man dma_buf_vmap(9)*

*4.6.0-rc5*

Create virtual mapping for the buffer object into kernel address space.
Same restrictions as for vmap and friends apply.


Synopsis
========

.. c:function:: void * dma_buf_vmap( struct dma_buf * dmabuf )

Arguments
=========

``dmabuf``
    [in] buffer to vmap


Description
===========

This call may fail due to lack of virtual mapping address space. These
calls are optional in drivers. The intended use for them is for mapping
objects linear in kernel space for high use objects. Please attempt to
use kmap/kunmap before thinking about these interfaces.

Returns NULL on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
