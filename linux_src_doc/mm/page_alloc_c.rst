.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/page_alloc.c

.. _`__get_pfnblock_flags_mask`:

__get_pfnblock_flags_mask
=========================

.. c:function:: unsigned long __get_pfnblock_flags_mask(struct page *page, unsigned long pfn, unsigned long end_bitidx, unsigned long mask)

    Return the requested group of flags for the pageblock_nr_pages block of pages

    :param page:
        The page within the block of interest
    :type page: struct page \*

    :param pfn:
        The target page frame number
    :type pfn: unsigned long

    :param end_bitidx:
        The last bit of interest to retrieve
    :type end_bitidx: unsigned long

    :param mask:
        mask of bits that the caller is interested in
    :type mask: unsigned long

.. _`__get_pfnblock_flags_mask.return`:

Return
------

pageblock_bits flags

.. _`set_pfnblock_flags_mask`:

set_pfnblock_flags_mask
=======================

.. c:function:: void set_pfnblock_flags_mask(struct page *page, unsigned long flags, unsigned long pfn, unsigned long end_bitidx, unsigned long mask)

    Set the requested group of flags for a pageblock_nr_pages block of pages

    :param page:
        The page within the block of interest
    :type page: struct page \*

    :param flags:
        The flags to set
    :type flags: unsigned long

    :param pfn:
        The target page frame number
    :type pfn: unsigned long

    :param end_bitidx:
        The last bit of interest
    :type end_bitidx: unsigned long

    :param mask:
        mask of bits that the caller is interested in
    :type mask: unsigned long

.. _`alloc_pages_exact`:

alloc_pages_exact
=================

.. c:function:: void *alloc_pages_exact(size_t size, gfp_t gfp_mask)

    allocate an exact number physically-contiguous pages.

    :param size:
        the number of bytes to allocate
    :type size: size_t

    :param gfp_mask:
        GFP flags for the allocation
    :type gfp_mask: gfp_t

.. _`alloc_pages_exact.description`:

Description
-----------

This function is similar to \ :c:func:`alloc_pages`\ , except that it allocates the
minimum number of pages to satisfy the request.  \ :c:func:`alloc_pages`\  can only
allocate memory in power-of-two pages.

This function is also limited by MAX_ORDER.

Memory allocated by this function must be released by \ :c:func:`free_pages_exact`\ .

.. _`alloc_pages_exact_nid`:

alloc_pages_exact_nid
=====================

.. c:function:: void *alloc_pages_exact_nid(int nid, size_t size, gfp_t gfp_mask)

    allocate an exact number of physically-contiguous pages on a node.

    :param nid:
        the preferred node ID where memory should be allocated
    :type nid: int

    :param size:
        the number of bytes to allocate
    :type size: size_t

    :param gfp_mask:
        GFP flags for the allocation
    :type gfp_mask: gfp_t

.. _`alloc_pages_exact_nid.description`:

Description
-----------

Like \ :c:func:`alloc_pages_exact`\ , but try to allocate on node nid first before falling
back.

.. _`free_pages_exact`:

free_pages_exact
================

.. c:function:: void free_pages_exact(void *virt, size_t size)

    release memory allocated via \ :c:func:`alloc_pages_exact`\ 

    :param virt:
        the value returned by alloc_pages_exact.
    :type virt: void \*

    :param size:
        size of allocation, same value as passed to \ :c:func:`alloc_pages_exact`\ .
    :type size: size_t

.. _`free_pages_exact.description`:

Description
-----------

Release the memory allocated by a previous call to alloc_pages_exact.

.. _`nr_free_zone_pages`:

nr_free_zone_pages
==================

.. c:function:: unsigned long nr_free_zone_pages(int offset)

    count number of pages beyond high watermark

    :param offset:
        The zone index of the highest zone
    :type offset: int

.. _`nr_free_zone_pages.description`:

Description
-----------

\ :c:func:`nr_free_zone_pages`\  counts the number of counts pages which are beyond the
high watermark within all zones at or below a given zone index.  For each
zone, the number of pages is calculated as:

    nr_free_zone_pages = managed_pages - high_pages

.. _`nr_free_buffer_pages`:

nr_free_buffer_pages
====================

.. c:function:: unsigned long nr_free_buffer_pages( void)

    count number of pages beyond high watermark

    :param void:
        no arguments
    :type void: 

.. _`nr_free_buffer_pages.description`:

Description
-----------

\ :c:func:`nr_free_buffer_pages`\  counts the number of pages which are beyond the high
watermark within ZONE_DMA and ZONE_NORMAL.

.. _`nr_free_pagecache_pages`:

nr_free_pagecache_pages
=======================

.. c:function:: unsigned long nr_free_pagecache_pages( void)

    count number of pages beyond high watermark

    :param void:
        no arguments
    :type void: 

.. _`nr_free_pagecache_pages.description`:

Description
-----------

\ :c:func:`nr_free_pagecache_pages`\  counts the number of pages which are beyond the
high watermark within all zones.

.. _`find_next_best_node`:

find_next_best_node
===================

.. c:function:: int find_next_best_node(int node, nodemask_t *used_node_mask)

    find the next node that should appear in a given node's fallback list

    :param node:
        node whose fallback list we're appending
    :type node: int

    :param used_node_mask:
        nodemask_t of already used nodes
    :type used_node_mask: nodemask_t \*

.. _`find_next_best_node.description`:

Description
-----------

We use a number of factors to determine which is the next node that should
appear on a given node's fallback list.  The node should not have appeared
already in \ ``node``\ 's fallback list, and it should be the next closest node
according to the distance array (which contains arbitrary distance values
from each node to each node in the system), and should also prefer nodes
with no CPUs, since presumably they'll have very little allocation pressure
on them otherwise.
It returns -1 if no node is found.

.. _`free_bootmem_with_active_regions`:

free_bootmem_with_active_regions
================================

.. c:function:: void free_bootmem_with_active_regions(int nid, unsigned long max_low_pfn)

    Call memblock_free_early_nid for each active range

    :param nid:
        The node to free memory on. If MAX_NUMNODES, all nodes are freed.
    :type nid: int

    :param max_low_pfn:
        The highest PFN that will be passed to memblock_free_early_nid
    :type max_low_pfn: unsigned long

.. _`free_bootmem_with_active_regions.description`:

Description
-----------

If an architecture guarantees that all ranges registered contain no holes
and may be freed, this this function may be used instead of calling
\ :c:func:`memblock_free_early_nid`\  manually.

.. _`sparse_memory_present_with_active_regions`:

sparse_memory_present_with_active_regions
=========================================

.. c:function:: void sparse_memory_present_with_active_regions(int nid)

    Call memory_present for each active range

    :param nid:
        The node to call memory_present for. If MAX_NUMNODES, all nodes will be used.
    :type nid: int

.. _`sparse_memory_present_with_active_regions.description`:

Description
-----------

If an architecture guarantees that all ranges registered contain no holes and may
be freed, this function may be used instead of calling \ :c:func:`memory_present`\  manually.

.. _`get_pfn_range_for_nid`:

get_pfn_range_for_nid
=====================

.. c:function:: void get_pfn_range_for_nid(unsigned int nid, unsigned long *start_pfn, unsigned long *end_pfn)

    Return the start and end page frames for a node

    :param nid:
        The nid to return the range for. If MAX_NUMNODES, the min and max PFN are returned.
    :type nid: unsigned int

    :param start_pfn:
        Passed by reference. On return, it will have the node start_pfn.
    :type start_pfn: unsigned long \*

    :param end_pfn:
        Passed by reference. On return, it will have the node end_pfn.
    :type end_pfn: unsigned long \*

.. _`get_pfn_range_for_nid.description`:

Description
-----------

It returns the start and end page frame of a node based on information
provided by \ :c:func:`memblock_set_node`\ . If called for a node
with no available memory, a warning is printed and the start and end
PFNs will be 0.

.. _`absent_pages_in_range`:

absent_pages_in_range
=====================

.. c:function:: unsigned long absent_pages_in_range(unsigned long start_pfn, unsigned long end_pfn)

    Return number of page frames in holes within a range

    :param start_pfn:
        The start PFN to start searching for holes
    :type start_pfn: unsigned long

    :param end_pfn:
        The end PFN to stop searching for holes
    :type end_pfn: unsigned long

.. _`absent_pages_in_range.description`:

Description
-----------

It returns the number of pages frames in memory holes within a range.

.. _`node_map_pfn_alignment`:

node_map_pfn_alignment
======================

.. c:function:: unsigned long node_map_pfn_alignment( void)

    determine the maximum internode alignment

    :param void:
        no arguments
    :type void: 

.. _`node_map_pfn_alignment.description`:

Description
-----------

This function should be called after node map is populated and sorted.
It calculates the maximum power of two alignment which can distinguish
all the nodes.

For example, if all nodes are 1GiB and aligned to 1GiB, the return value
would indicate 1GiB alignment with (1 << (30 - PAGE_SHIFT)).  If the
nodes are shifted by 256MiB, 256MiB.  Note that if only the last node is
shifted, 1GiB is enough and this function will indicate so.

This is used to test whether pfn -> nid mapping of the chosen memory
model has fine enough granularity to avoid incorrect mapping for the
populated node map.

Returns the determined alignment in pfn's.  0 if there is no alignment
requirement (single node).

.. _`find_min_pfn_with_active_regions`:

find_min_pfn_with_active_regions
================================

.. c:function:: unsigned long find_min_pfn_with_active_regions( void)

    Find the minimum PFN registered

    :param void:
        no arguments
    :type void: 

.. _`find_min_pfn_with_active_regions.description`:

Description
-----------

It returns the minimum PFN based on information provided via
\ :c:func:`memblock_set_node`\ .

.. _`free_area_init_nodes`:

free_area_init_nodes
====================

.. c:function:: void free_area_init_nodes(unsigned long *max_zone_pfn)

    Initialise all pg_data_t and zone data

    :param max_zone_pfn:
        an array of max PFNs for each zone
    :type max_zone_pfn: unsigned long \*

.. _`free_area_init_nodes.description`:

Description
-----------

This will call \ :c:func:`free_area_init_node`\  for each active node in the system.
Using the page ranges provided by \ :c:func:`memblock_set_node`\ , the size of each
zone in each node and their holes is calculated. If the maximum PFN
between two adjacent zones match, it is assumed that the zone is empty.
For example, if arch_max_dma_pfn == arch_max_dma32_pfn, it is assumed
that arch_max_dma32_pfn has no pages. It is also assumed that a zone
starts where the previous one ended. For example, ZONE_DMA32 starts
at arch_max_dma_pfn.

.. _`set_dma_reserve`:

set_dma_reserve
===============

.. c:function:: void set_dma_reserve(unsigned long new_dma_reserve)

    set the specified number of pages reserved in the first zone

    :param new_dma_reserve:
        The number of pages to mark reserved
    :type new_dma_reserve: unsigned long

.. _`set_dma_reserve.description`:

Description
-----------

The per-cpu batchsize and zone watermarks are determined by managed_pages.
In the DMA zone, a significant percentage may be consumed by kernel image
and other unfreeable allocations which can skew the watermarks badly. This
function may optionally be used to account for unfreeable pages in the
first zone (e.g., ZONE_DMA). The effect will be lower watermarks and
smaller per-cpu batchsize.

.. _`setup_per_zone_wmarks`:

setup_per_zone_wmarks
=====================

.. c:function:: void setup_per_zone_wmarks( void)

    called when min_free_kbytes changes or when memory is hot-{added|removed}

    :param void:
        no arguments
    :type void: 

.. _`setup_per_zone_wmarks.description`:

Description
-----------

Ensures that the watermark[min,low,high] values for each zone are set
correctly with respect to min_free_kbytes.

.. _`alloc_contig_range`:

alloc_contig_range
==================

.. c:function:: int alloc_contig_range(unsigned long start, unsigned long end, unsigned migratetype, gfp_t gfp_mask)

    - tries to allocate given range of pages

    :param start:
        start PFN to allocate
    :type start: unsigned long

    :param end:
        one-past-the-last PFN to allocate
    :type end: unsigned long

    :param migratetype:
        migratetype of the underlaying pageblocks (either
        #MIGRATE_MOVABLE or #MIGRATE_CMA).  All pageblocks
        in range must have the same migratetype and it must
        be either of the two.
    :type migratetype: unsigned

    :param gfp_mask:
        GFP mask to use during compaction
    :type gfp_mask: gfp_t

.. _`alloc_contig_range.description`:

Description
-----------

The PFN range does not have to be pageblock or MAX_ORDER_NR_PAGES
aligned.  The PFN range must belong to a single zone.

The first thing this routine does is attempt to MIGRATE_ISOLATE all
pageblocks in the range.  Once isolated, the pageblocks should not
be modified by others.

Returns zero on success or negative error code.  On success all
pages which PFN is in [start, end) are allocated for the caller and
need to be freed with \ :c:func:`free_contig_range`\ .

.. This file was automatic generated / don't edit.

