.. -*- coding: utf-8; mode: rst -*-

.. _API-delete-from-page-cache:

======================
delete_from_page_cache
======================

*man delete_from_page_cache(9)*

*4.6.0-rc5*

delete page from page cache


Synopsis
========

.. c:function:: void delete_from_page_cache( struct page * page )

Arguments
=========

``page``
    the page which the kernel is trying to remove from page cache


Description
===========

This must be called only on pages that have been verified to be in the
page cache and locked. It will never put the page into the free list,
the caller has a reference on the page.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
