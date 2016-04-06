
.. _API-add-to-page-cache-locked:

========================
add_to_page_cache_locked
========================

*man add_to_page_cache_locked(9)*

*4.6.0-rc1*

add a locked page to the pagecache


Synopsis
========

.. c:function:: int add_to_page_cache_locked( struct page * page, struct address_space * mapping, pgoff_t offset, gfp_t gfp_mask )

Arguments
=========

``page``
    page to add

``mapping``
    the page's address_space

``offset``
    page index

``gfp_mask``
    page allocation mode


Description
===========

This function is used to add a page to the pagecache. It must be locked. This function does not add the page to the LRU. The caller must do that.
