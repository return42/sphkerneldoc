.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-pool-destroy:

================
dma_pool_destroy
================

*man dma_pool_destroy(9)*

*4.6.0-rc5*

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

Caller guarantees that no more memory from the pool is in use, and that
nothing will try to use the pool after this call.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
