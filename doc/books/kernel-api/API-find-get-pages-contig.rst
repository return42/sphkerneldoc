.. -*- coding: utf-8; mode: rst -*-

.. _API-find-get-pages-contig:

=====================
find_get_pages_contig
=====================

*man find_get_pages_contig(9)*

*4.6.0-rc5*

gang contiguous pagecache lookup


Synopsis
========

.. c:function:: unsigned find_get_pages_contig( struct address_space * mapping, pgoff_t index, unsigned int nr_pages, struct page ** pages )

Arguments
=========

``mapping``
    The address_space to search

``index``
    The starting page index

``nr_pages``
    The maximum number of pages

``pages``
    Where the resulting pages are placed


Description
===========

``find_get_pages_contig`` works exactly like ``find_get_pages``, except
that the returned number of pages are guaranteed to be contiguous.

``find_get_pages_contig`` returns the number of pages which were found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
