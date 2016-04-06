
.. _API-page-cache-next-hole:

====================
page_cache_next_hole
====================

*man page_cache_next_hole(9)*

*4.6.0-rc1*

find the next hole (not-present entry)


Synopsis
========

.. c:function:: pgoff_t page_cache_next_hole( struct address_space * mapping, pgoff_t index, unsigned long max_scan )

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

Search the set [index, min(index+max_scan-1, MAX_INDEX)] for the lowest indexed hole.


Returns
=======

the index of the hole if found, otherwise returns an index outside of the set specified (in which case 'return - index >= max_scan' will be true). In rare cases of index
wrap-around, 0 will be returned.

page_cache_next_hole may be called under rcu_read_lock. However, like radix_tree_gang_lookup, this will not atomically search a snapshot of the tree at a single point in
time. For example, if a hole is created at index 5, then subsequently a hole is created at index 10, page_cache_next_hole covering both indexes may return 10 if called under
rcu_read_lock.
