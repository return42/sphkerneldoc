.. -*- coding: utf-8; mode: rst -*-

.. _API-free-bootmem-with-active-regions:

================================
free_bootmem_with_active_regions
================================

*man free_bootmem_with_active_regions(9)*

*4.6.0-rc5*

Call memblock_free_early_nid for each active range


Synopsis
========

.. c:function:: void free_bootmem_with_active_regions( int nid, unsigned long max_low_pfn )

Arguments
=========

``nid``
    The node to free memory on. If MAX_NUMNODES, all nodes are freed.

``max_low_pfn``
    The highest PFN that will be passed to memblock_free_early_nid


Description
===========

If an architecture guarantees that all ranges registered contain no
holes and may be freed, this this function may be used instead of
calling ``memblock_free_early_nid`` manually.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
