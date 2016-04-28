.. -*- coding: utf-8; mode: rst -*-

.. _API-replace-page-cache-page:

=======================
replace_page_cache_page
=======================

*man replace_page_cache_page(9)*

*4.6.0-rc5*

replace a pagecache page with a new one


Synopsis
========

.. c:function:: int replace_page_cache_page( struct page * old, struct page * new, gfp_t gfp_mask )

Arguments
=========

``old``
    page to be replaced

``new``
    page to replace with

``gfp_mask``
    allocation mode


Description
===========

This function replaces a page in the pagecache with a new one. On
success it acquires the pagecache reference for the new page and drops
it for the old page. Both the old and new pages must be locked. This
function does not add the new page to the LRU, the caller must do that.

The remove + add is atomic. The only way this function can fail is
memory allocation failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
