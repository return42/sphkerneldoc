.. -*- coding: utf-8; mode: rst -*-

.. _API-free-area-init-nodes:

====================
free_area_init_nodes
====================

*man free_area_init_nodes(9)*

*4.6.0-rc5*

Initialise all pg_data_t and zone data


Synopsis
========

.. c:function:: void free_area_init_nodes( unsigned long * max_zone_pfn )

Arguments
=========

``max_zone_pfn``
    an array of max PFNs for each zone


Description
===========

This will call ``free_area_init_node`` for each active node in the
system. Using the page ranges provided by ``memblock_set_node``, the
size of each zone in each node and their holes is calculated. If the
maximum PFN between two adjacent zones match, it is assumed that the
zone is empty. For example, if arch_max_dma_pfn ==
arch_max_dma32_pfn, it is assumed that arch_max_dma32_pfn has no
pages. It is also assumed that a zone starts where the previous one
ended. For example, ZONE_DMA32 starts at arch_max_dma_pfn.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
