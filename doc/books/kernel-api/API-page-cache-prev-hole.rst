
.. _API-page-cache-prev-hole:

====================
page_cache_prev_hole
====================

*man page_cache_prev_hole(9)*

*4.6.0-rc1*

find the prev hole (not-present entry)


Synopsis
========

.. c:function:: pgoff_t page_cache_prev_hole( struct address_space * mapping, pgoff_t index, unsigned long max_scan )

Arguments
=========

``mapping``
    mapping

``index``
    index

``max_scan``
    maximum range to search


Description
===========

Search backwards in the range [max(index-max_scan+1, 0), index] for the first hole.


Returns
=======

the index of the hole if found, otherwise returns an index outside of the set specified (in which case 'index - return >= max_scan' will be true). In rare cases of wrap-around,
ULONG_MAX will be returned.

page_cache_prev_hole may be called under rcu_read_lock. However, like radix_tree_gang_lookup, this will not atomically search a snapshot of the tree at a single point in
time. For example, if a hole is created at index 10, then subsequently a hole is created at index 5, page_cache_prev_hole covering both indexes may return 5 if called under
rcu_read_lock.
