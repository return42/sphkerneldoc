.. -*- coding: utf-8; mode: rst -*-

.. _API-find-get-entries-tag:

====================
find_get_entries_tag
====================

*man find_get_entries_tag(9)*

*4.6.0-rc5*

find and return entries that match ``tag``


Synopsis
========

.. c:function:: unsigned find_get_entries_tag( struct address_space * mapping, pgoff_t start, int tag, unsigned int nr_entries, struct page ** entries, pgoff_t * indices )

Arguments
=========

``mapping``
    the address_space to search

``start``
    the starting page cache index

``tag``
    the tag index

``nr_entries``
    the maximum number of entries

``entries``
    where the resulting entries are placed

``indices``
    the cache indices corresponding to the entries in ``entries``


Description
===========

Like find_get_entries, except we only return entries which are tagged
with ``tag``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
