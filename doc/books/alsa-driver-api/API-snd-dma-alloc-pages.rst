
.. _API-snd-dma-alloc-pages:

===================
snd_dma_alloc_pages
===================

*man snd_dma_alloc_pages(9)*

*4.6.0-rc1*

allocate the buffer area according to the given type


Synopsis
========

.. c:function:: int snd_dma_alloc_pages( int type, struct device * device, size_t size, struct snd_dma_buffer * dmab )

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


Return
======

Zero if the buffer with the given size is allocated successfully, otherwise a negative value on error.
