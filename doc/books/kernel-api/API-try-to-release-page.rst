.. -*- coding: utf-8; mode: rst -*-

.. _API-try-to-release-page:

===================
try_to_release_page
===================

*man try_to_release_page(9)*

*4.6.0-rc5*

release old fs-specific metadata on a page


Synopsis
========

.. c:function:: int try_to_release_page( struct page * page, gfp_t gfp_mask )

Arguments
=========

``page``
    the page which the kernel is trying to free

``gfp_mask``
    memory allocation flags (and I/O mode)


Description
===========

The address_space is to try to release any data against the page
(presumably at page->private). If the release was successful, return
`1'. Otherwise return zero.

This may also be called if PG_fscache is set on a page, indicating that
the page is known to the local caching routines.

The ``gfp_mask`` argument specifies whether I/O may be performed to
release this page (__GFP_IO), and whether the call may block
(__GFP_RECLAIM & __GFP_FS).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
