.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-pool-alloc:

==============
dma_pool_alloc
==============

*man dma_pool_alloc(9)*

*4.6.0-rc5*

get a block of consistent memory


Synopsis
========

.. c:function:: void * dma_pool_alloc( struct dma_pool * pool, gfp_t mem_flags, dma_addr_t * handle )

Arguments
=========

``pool``
    dma pool that will produce the block

``mem_flags``
    GFP_* bitmask

``handle``
    pointer to dma address of block


Description
===========

This returns the kernel virtual address of a currently unused block, and
reports its dma address through the handle. If such a memory block can't
be allocated, ``NULL`` is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
