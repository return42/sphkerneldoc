.. -*- coding: utf-8; mode: rst -*-

.. _API-dmam-free-coherent:

==================
dmam_free_coherent
==================

*man dmam_free_coherent(9)*

*4.6.0-rc5*

Managed ``dma_free_coherent``


Synopsis
========

.. c:function:: void dmam_free_coherent( struct device * dev, size_t size, void * vaddr, dma_addr_t dma_handle )

Arguments
=========

``dev``
    Device to free coherent memory for

``size``
    Size of allocation

``vaddr``
    Virtual address of the memory to free

``dma_handle``
    DMA handle of the memory to free


Description
===========

Managed ``dma_free_coherent``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
