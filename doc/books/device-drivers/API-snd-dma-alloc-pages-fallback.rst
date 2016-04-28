.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dma-alloc-pages-fallback:

============================
snd_dma_alloc_pages_fallback
============================

*man snd_dma_alloc_pages_fallback(9)*

*4.6.0-rc5*

allocate the buffer area according to the given type with fallback


Synopsis
========

.. c:function:: int snd_dma_alloc_pages_fallback( int type, struct device * device, size_t size, struct snd_dma_buffer * dmab )

Arguments
=========

``type``
    the DMA buffer type

``device``
    the device pointer

``size``
    the buffer size to allocate

``dmab``
    buffer allocation record to store the allocated data


Description
===========

Calls the memory-allocator function for the corresponding buffer type.
When no space is left, this function reduces the size and tries to
allocate again. The size actually allocated is stored in res_size
argument.


Return
======

Zero if the buffer with the given size is allocated successfully,
otherwise a negative value on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
