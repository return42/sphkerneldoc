
.. _API-dmam-pool-create:

================
dmam_pool_create
================

*man dmam_pool_create(9)*

*4.6.0-rc1*

Managed ``dma_pool_create``


Synopsis
========

.. c:function:: struct dma_pool ⋆ dmam_pool_create( const char * name, struct device * dev, size_t size, size_t align, size_t allocation )

Arguments
=========

``name``
    name of pool, for diagnostics

``dev``
    device that will be doing the DMA

``size``
    size of the blocks in this pool.

``align``
    alignment requirement for blocks; must be a power of two

``allocation``
    returned blocks won't cross this boundary (or zero)


Description
===========

Managed ``dma_pool_create``. DMA pool created with this function is automatically destroyed on driver detach.
