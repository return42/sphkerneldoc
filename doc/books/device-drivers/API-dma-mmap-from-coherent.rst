.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-mmap-from-coherent:

======================
dma_mmap_from_coherent
======================

*man dma_mmap_from_coherent(9)*

*4.6.0-rc5*

try to mmap the memory allocated from per-device coherent memory pool to
userspace


Synopsis
========

.. c:function:: int dma_mmap_from_coherent( struct device * dev, struct vm_area_struct * vma, void * vaddr, size_t size, int * ret )

Arguments
=========

``dev``
    device from which the memory was allocated

``vma``
    vm_area for the userspace memory

``vaddr``
    cpu address returned by dma_alloc_from_coherent

``size``
    size of the memory buffer allocated by dma_alloc_from_coherent

``ret``
    result from ``remap_pfn_range``


Description
===========

This checks whether the memory was allocated from the per-device
coherent memory pool and if so, maps that memory to the provided vma.

Returns 1 if we correctly mapped the memory, or 0 if the caller should
proceed with mapping memory from generic pools.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
