.. -*- coding: utf-8; mode: rst -*-

.. _API-read-cache-pages:

================
read_cache_pages
================

*man read_cache_pages(9)*

*4.6.0-rc5*

populate an address space with some pages & start reads against them


Synopsis
========

.. c:function:: int read_cache_pages( struct address_space * mapping, struct list_head * pages, int (*filler) void *, struct page *, void * data )

Arguments
=========

``mapping``
    the address_space

``pages``
    The address of a list_head which contains the target pages. These
    pages have their ->index populated and are otherwise uninitialised.

``filler``
    callback routine for filling a single page.

``data``
    private data for the callback routine.


Description
===========

Hides the details of the LRU cache etc from the filesystems.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
