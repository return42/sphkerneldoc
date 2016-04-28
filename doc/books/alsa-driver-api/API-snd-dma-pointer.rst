.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dma-pointer:

===============
snd_dma_pointer
===============

*man snd_dma_pointer(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
