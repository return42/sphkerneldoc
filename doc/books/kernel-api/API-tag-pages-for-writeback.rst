.. -*- coding: utf-8; mode: rst -*-

.. _API-tag-pages-for-writeback:

=======================
tag_pages_for_writeback
=======================

*man tag_pages_for_writeback(9)*

*4.6.0-rc5*

tag pages to be written by write_cache_pages


Synopsis
========

.. c:function:: void tag_pages_for_writeback( struct address_space * mapping, pgoff_t start, pgoff_t end )

Arguments
=========

``mapping``
    address space structure to write

``start``
    starting page index

``end``
    ending page index (inclusive)


Description
===========

This function scans the page range from ``start`` to ``end`` (inclusive)
and tags all pages that have DIRTY tag set with a special TOWRITE tag.
The idea is that write_cache_pages (or whoever calls this function)
will then use TOWRITE tag to identify pages eligible for writeback. This
mechanism is used to avoid livelocking of writeback by a process
steadily creating new dirty pages in the file (thus it is important for
this function to be quick so that it can tag pages faster than a
dirtying process can create them).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
