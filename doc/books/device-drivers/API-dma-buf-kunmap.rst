.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-buf-kunmap:

==============
dma_buf_kunmap
==============

*man dma_buf_kunmap(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
