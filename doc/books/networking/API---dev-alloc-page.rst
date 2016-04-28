.. -*- coding: utf-8; mode: rst -*-

.. _API---dev-alloc-page:

================
__dev_alloc_page
================

*man __dev_alloc_page(9)*

*4.6.0-rc5*

allocate a page for network Rx


Synopsis
========

.. c:function:: struct page * __dev_alloc_page( gfp_t gfp_mask )

Arguments
=========

``gfp_mask``
    allocation priority. Set __GFP_NOMEMALLOC if not for network Rx


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
