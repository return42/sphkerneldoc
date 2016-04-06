
.. _API-dmam-alloc-coherent:

===================
dmam_alloc_coherent
===================

*man dmam_alloc_coherent(9)*

*4.6.0-rc1*

Managed ``dma_alloc_coherent``


Synopsis
========

.. c:function:: void ⋆ dmam_alloc_coherent( struct device * dev, size_t size, dma_addr_t * dma_handle, gfp_t gfp )

Arguments
=========

``dev``
    Device to allocate coherent memory for

``size``
    Size of allocation

``dma_handle``
    Out argument for allocated DMA handle

``gfp``
    Allocation flags


Description
===========

Managed ``dma_alloc_coherent``. Memory allocated using this function will be automatically released on driver detach.


RETURNS
=======

Pointer to allocated memory on success, NULL on failure.
