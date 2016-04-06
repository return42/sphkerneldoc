
.. _API-node-map-pfn-alignment:

======================
node_map_pfn_alignment
======================

*man node_map_pfn_alignment(9)*

*4.6.0-rc1*

determine the maximum internode alignment


Synopsis
========

.. c:function:: unsigned long node_map_pfn_alignment( void )

Arguments
=========

``void``
    no arguments


Description
===========

This function should be called after node map is populated and sorted. It calculates the maximum power of two alignment which can distinguish all the nodes.

For example, if all nodes are 1GiB and aligned to 1GiB, the return value would indicate 1GiB alignment with (1 << (30 - PAGE_SHIFT)). If the nodes are shifted by 256MiB, 256MiB.
Note that if only the last node is shifted, 1GiB is enough and this function will indicate so.

This is used to test whether pfn -> nid mapping of the chosen memory model has fine enough granularity to avoid incorrect mapping for the populated node map.

Returns the determined alignment in pfn's. 0 if there is no alignment requirement (single node).
