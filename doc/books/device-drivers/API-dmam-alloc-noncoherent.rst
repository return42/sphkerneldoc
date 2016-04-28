.. -*- coding: utf-8; mode: rst -*-

.. _API-dmam-alloc-noncoherent:

======================
dmam_alloc_noncoherent
======================

*man dmam_alloc_noncoherent(9)*

*4.6.0-rc5*

Managed ``dma_alloc_non_coherent``


Synopsis
========

.. c:function:: void * dmam_alloc_noncoherent( struct device * dev, size_t size, dma_addr_t * dma_handle, gfp_t gfp )

Arguments
=========

``dev``
    Device to allocate non_coherent memory for

``size``
    Size of allocation

``dma_handle``
    Out argument for allocated DMA handle

``gfp``
    Allocation flags


Description
===========

Managed ``dma_alloc_non_coherent``. Memory allocated using this function
will be automatically released on driver detach.


RETURNS
=======

Pointer to allocated memory on success, NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
