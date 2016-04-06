
.. _API-find-get-pages-tag:

==================
find_get_pages_tag
==================

*man find_get_pages_tag(9)*

*4.6.0-rc1*

find and return pages that match ``tag``


Synopsis
========

.. c:function:: unsigned find_get_pages_tag( struct address_space * mapping, pgoff_t * index, int tag, unsigned int nr_pages, struct page ** pages )

Arguments
=========

``mapping``
    the address_space to search

``index``
    the starting page index

``tag``
    the tag index

``nr_pages``
    the maximum number of pages

``pages``
    where the resulting pages are placed


Description
===========

Like find_get_pages, except we only return pages which are tagged with ``tag``. We update ``index`` to index the next page for the traversal.
