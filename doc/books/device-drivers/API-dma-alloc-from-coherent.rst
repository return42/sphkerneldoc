
.. _API-dma-alloc-from-coherent:

=======================
dma_alloc_from_coherent
=======================

*man dma_alloc_from_coherent(9)*

*4.6.0-rc1*

try to allocate memory from the per-device coherent area


Synopsis
========

.. c:function:: int dma_alloc_from_coherent( struct device * dev, ssize_t size, dma_addr_t * dma_handle, void ** ret )

Arguments
=========

``dev``
    device from which we allocate memory

``size``
    size of requested memory area

``dma_handle``
    This will be filled with the correct dma handle

``ret``
    This pointer will be filled with the virtual address to allocated area.


Description
===========

This function should be only called from per-arch ``dma_alloc_coherent`` to support allocation from per-device coherent memory pools.

Returns 0 if dma_alloc_coherent should continue with allocating from generic memory areas, or !0 if dma_alloc_coherent should return ``ret``.
