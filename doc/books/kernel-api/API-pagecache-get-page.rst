
.. _API-pagecache-get-page:

==================
pagecache_get_page
==================

*man pagecache_get_page(9)*

*4.6.0-rc1*

find and get a page reference


Synopsis
========

.. c:function:: struct page ⋆ pagecache_get_page( struct address_space * mapping, pgoff_t offset, int fgp_flags, gfp_t gfp_mask )

Arguments
=========

``mapping``
    the address_space to search

``offset``
    the page index

``fgp_flags``
    PCG flags

``gfp_mask``
    gfp mask to use for the page cache data page allocation


Description
===========

Looks up the page cache slot at ``mapping`` & ``offset``.

PCG flags modify how the page is returned.


FGP_ACCESSED
============

the page will be marked accessed


FGP_LOCK
========

Page is return locked


FGP_CREAT
=========

If page is not present then a new page is allocated using ``gfp_mask`` and added to the page cache and the VM's LRU list. The page is returned locked and with an increased
refcount. Otherwise, ``NULL`` is returned.

If FGP_LOCK or FGP_CREAT are specified then the function may sleep even if the GFP flags specified for FGP_CREAT are atomic.

If there is a page cache page, it is returned with an increased refcount.
