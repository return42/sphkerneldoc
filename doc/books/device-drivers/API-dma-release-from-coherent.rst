
.. _API-dma-release-from-coherent:

=========================
dma_release_from_coherent
=========================

*man dma_release_from_coherent(9)*

*4.6.0-rc1*

try to free the memory allocated from per-device coherent memory pool


Synopsis
========

.. c:function:: int dma_release_from_coherent( struct device * dev, int order, void * vaddr )

Arguments
=========

``dev``
    device from which the memory was allocated

``order``
    the order of pages allocated

``vaddr``
    virtual address of allocated pages


Description
===========

This checks whether the memory was allocated from the per-device coherent memory pool and if so, releases that memory.

Returns 1 if we correctly released the memory, or 0 if ``dma_release_coherent`` should proceed with releasing memory from generic pools.
