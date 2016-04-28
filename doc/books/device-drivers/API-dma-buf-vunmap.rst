.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-buf-vunmap:

==============
dma_buf_vunmap
==============

*man dma_buf_vunmap(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
