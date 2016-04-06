
.. _API-read-cache-page:

===============
read_cache_page
===============

*man read_cache_page(9)*

*4.6.0-rc1*

read into page cache, fill it if needed


Synopsis
========

.. c:function:: struct page ⋆ read_cache_page( struct address_space * mapping, pgoff_t index, int (*filler) void *, struct page *, void * data )

Arguments
=========

``mapping``
    the page's address_space

``index``
    the page index

``filler``
    function to perform the read

``data``
    first arg to filler(data, page) function, often left as NULL


Description
===========

Read into the page cache. If a page already exists, and ``PageUptodate`` is not set, try to fill the page and wait for it to become unlocked.

If the page does not get brought uptodate, return -EIO.
