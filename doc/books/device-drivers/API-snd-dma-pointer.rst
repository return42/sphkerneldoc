
.. _API-snd-dma-pointer:

===============
snd_dma_pointer
===============

*man snd_dma_pointer(9)*

*4.6.0-rc1*

return the current pointer to DMA transfer buffer in bytes


Synopsis
========

.. c:function:: unsigned int snd_dma_pointer( unsigned long dma, unsigned int size )

Arguments
=========

``dma``
    the dma number

``size``
    the dma transfer size


Return
======

The current pointer in DMA transfer buffer in bytes.
