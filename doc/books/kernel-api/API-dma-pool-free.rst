
.. _API-dma-pool-free:

=============
dma_pool_free
=============

*man dma_pool_free(9)*

*4.6.0-rc1*

put block back into dma pool


Synopsis
========

.. c:function:: void dma_pool_free( struct dma_pool * pool, void * vaddr, dma_addr_t dma )

Arguments
=========

``pool``
    the dma pool holding the block

``vaddr``
    virtual address of block

``dma``
    dma address of block


Description
===========

Caller promises neither device nor driver will again touch this block unless it is first re-allocated.
