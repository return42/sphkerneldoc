.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dma-program:

===============
snd_dma_program
===============

*man snd_dma_program(9)*

*4.6.0-rc5*

program an ISA DMA transfer


Synopsis
========

.. c:function:: void snd_dma_program( unsigned long dma, unsigned long addr, unsigned int size, unsigned short mode )

Arguments
=========

``dma``
    the dma number

``addr``
    the physical address of the buffer

``size``
    the DMA transfer size

``mode``
    the DMA transfer mode, DMA_MODE_XXX


Description
===========

Programs an ISA DMA transfer for the given buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
