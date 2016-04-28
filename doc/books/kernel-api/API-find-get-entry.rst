.. -*- coding: utf-8; mode: rst -*-

.. _API-find-get-entry:

==============
find_get_entry
==============

*man find_get_entry(9)*

*4.6.0-rc5*

find and get a page cache entry


Synopsis
========

.. c:function:: struct page * find_get_entry( struct address_space * mapping, pgoff_t offset )

Arguments
=========

``mapping``
    the address_space to search

``offset``
    the page cache index


Description
===========

Looks up the page cache slot at ``mapping`` & ``offset``. If there is a
page cache page, it is returned with an increased refcount.

If the slot holds a shadow entry of a previously evicted page, or a swap
entry from shmem/tmpfs, it is returned.

Otherwise, ``NULL`` is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
