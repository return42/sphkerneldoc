.. -*- coding: utf-8; mode: rst -*-

.. _API---dev-alloc-pages:

=================
__dev_alloc_pages
=================

*man __dev_alloc_pages(9)*

*4.6.0-rc5*

allocate page for network Rx


Synopsis
========

.. c:function:: struct page * __dev_alloc_pages( gfp_t gfp_mask, unsigned int order )

Arguments
=========

``gfp_mask``
    allocation priority. Set __GFP_NOMEMALLOC if not for network Rx

``order``
    size of the allocation


Description
===========

Allocate a new page.

``NULL`` is returned if there is no free memory.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
