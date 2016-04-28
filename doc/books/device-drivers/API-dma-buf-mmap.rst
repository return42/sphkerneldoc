.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-buf-mmap:

============
dma_buf_mmap
============

*man dma_buf_mmap(9)*

*4.6.0-rc5*

Setup up a userspace mmap with the given vma


Synopsis
========

.. c:function:: int dma_buf_mmap( struct dma_buf * dmabuf, struct vm_area_struct * vma, unsigned long pgoff )

Arguments
=========

``dmabuf``
    [in] buffer that should back the vma

``vma``
    [in] vma for the mmap

``pgoff``
    [in] offset in pages where this mmap should start within the dma-buf
    buffer.


Description
===========

This function adjusts the passed in vma so that it points at the file of
the dma_buf operation. It also adjusts the starting pgoff and does
bounds checking on the size of the vma. Then it calls the exporters mmap
function to set up the mapping.

Can return negative error values, returns 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
