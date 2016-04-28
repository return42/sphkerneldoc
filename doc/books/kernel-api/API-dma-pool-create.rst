.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-pool-create:

===============
dma_pool_create
===============

*man dma_pool_create(9)*

*4.6.0-rc5*

Creates a pool of consistent memory blocks, for dma.


Synopsis
========

.. c:function:: struct dma_pool * dma_pool_create( const char * name, struct device * dev, size_t size, size_t align, size_t boundary )

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

``boundary``
    returned blocks won't cross this power of two boundary


Context
=======

!\ ``in_interrupt``


Description
===========

Returns a dma allocation pool with the requested characteristics, or
null if one can't be created. Given one of these pools,
``dma_pool_alloc`` may be used to allocate memory. Such memory will all
have “consistent” DMA mappings, accessible by the device and its driver
without using cache flushing primitives. The actual size of blocks
allocated may be larger than requested because of alignment.

If ``boundary`` is nonzero, objects returned from ``dma_pool_alloc``
won't cross that size boundary. This is useful for devices which have
addressing restrictions on individual DMA transfers, such as not
crossing boundaries of 4KBytes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
