
.. _API-alloc-contig-range:

==================
alloc_contig_range
==================

*man alloc_contig_range(9)*

*4.6.0-rc1*

- tries to allocate given range of pages


Synopsis
========

.. c:function:: int alloc_contig_range( unsigned long start, unsigned long end, unsigned migratetype )

Arguments
=========

``start``
    start PFN to allocate

``end``
    one-past-the-last PFN to allocate

``migratetype``
    migratetype of the underlaying pageblocks (either #MIGRATE_MOVABLE or #MIGRATE_CMA). All pageblocks in range must have the same migratetype and it must be either of the two.


Description
===========

The PFN range does not have to be pageblock or MAX_ORDER_NR_PAGES aligned, however it's the caller's responsibility to guarantee that we are the only thread that changes migrate
type of pageblocks the pages fall in.

The PFN range must belong to a single zone.

Returns zero on success or negative error code. On success all pages which PFN is in [start, end) are allocated for the caller and need to be freed with ``free_contig_range``.
