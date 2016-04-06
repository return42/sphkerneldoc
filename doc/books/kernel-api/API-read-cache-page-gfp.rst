
.. _API-read-cache-page-gfp:

===================
read_cache_page_gfp
===================

*man read_cache_page_gfp(9)*

*4.6.0-rc1*

read into page cache, using specified page allocation flags.


Synopsis
========

.. c:function:: struct page ⋆ read_cache_page_gfp( struct address_space * mapping, pgoff_t index, gfp_t gfp )

Arguments
=========

``mapping``
    the page's address_space

``index``
    the page index

``gfp``
    the page allocator flags to use if allocating


Description
===========

This is the same as “read_mapping_page(mapping, index, NULL)”, but with any new page allocations done using the specified allocation flags.

If the page does not get brought uptodate, return -EIO.
