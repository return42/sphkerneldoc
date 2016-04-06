
.. _API-dma-pool-destroy:

================
dma_pool_destroy
================

*man dma_pool_destroy(9)*

*4.6.0-rc1*

destroys a pool of dma memory blocks.


Synopsis
========

.. c:function:: void dma_pool_destroy( struct dma_pool * pool )

Arguments
=========

``pool``
    dma pool that will be destroyed


Context
=======

!\ ``in_interrupt``


Description
===========

Caller guarantees that no more memory from the pool is in use, and that nothing will try to use the pool after this call.
