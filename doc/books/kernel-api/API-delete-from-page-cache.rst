
.. _API-delete-from-page-cache:

======================
delete_from_page_cache
======================

*man delete_from_page_cache(9)*

*4.6.0-rc1*

delete page from page cache


Synopsis
========

.. c:function:: void delete_from_page_cache( struct page * page )

Arguments
=========

``page``
    the page which the kernel is trying to remove from page cache


Description
===========

This must be called only on pages that have been verified to be in the page cache and locked. It will never put the page into the free list, the caller has a reference on the page.
