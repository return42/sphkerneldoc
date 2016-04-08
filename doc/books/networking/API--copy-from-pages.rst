
.. _API--copy-from-pages:

================
_copy_from_pages
================

*man _copy_from_pages(9)*

*4.6.0-rc1*


Synopsis
========

.. c:function:: void _copy_from_pages( char * p, struct page ** pages, size_t pgbase, size_t len )

Arguments
=========

``p``
    pointer to destination

``pages``
    array of pages

``pgbase``
    offset of source data

``len``
    length


Description
===========

Copies data into an arbitrary memory location from an array of pages The copy is assumed to be non-overlapping.
