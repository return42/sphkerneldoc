
.. _API---dev-alloc-page:

================
__dev_alloc_page
================

*man __dev_alloc_page(9)*

*4.6.0-rc1*

allocate a page for network Rx


Synopsis
========

.. c:function:: struct page ⋆ __dev_alloc_page( gfp_t gfp_mask )

Arguments
=========

``gfp_mask``
    allocation priority. Set __GFP_NOMEMALLOC if not for network Rx


Description
===========

Allocate a new page.

``NULL`` is returned if there is no free memory.
