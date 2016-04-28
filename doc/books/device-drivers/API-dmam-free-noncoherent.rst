.. -*- coding: utf-8; mode: rst -*-

.. _API-dmam-free-noncoherent:

=====================
dmam_free_noncoherent
=====================

*man dmam_free_noncoherent(9)*

*4.6.0-rc5*

Managed ``dma_free_noncoherent``


Synopsis
========

.. c:function:: void dmam_free_noncoherent( struct device * dev, size_t size, void * vaddr, dma_addr_t dma_handle )

Arguments
=========

``dev``
    Device to free noncoherent memory for

``size``
    Size of allocation

``vaddr``
    Virtual address of the memory to free

``dma_handle``
    DMA handle of the memory to free


Description
===========

Managed ``dma_free_noncoherent``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
