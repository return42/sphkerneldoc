.. -*- coding: utf-8; mode: rst -*-

.. _API--copy-from-pages:

================
_copy_from_pages
================

*man _copy_from_pages(9)*

*4.6.0-rc5*


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

Copies data into an arbitrary memory location from an array of pages The
copy is assumed to be non-overlapping.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
