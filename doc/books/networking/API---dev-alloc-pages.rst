
.. _API---dev-alloc-pages:

=================
__dev_alloc_pages
=================

*man __dev_alloc_pages(9)*

*4.6.0-rc1*

allocate page for network Rx


Synopsis
========

.. c:function:: struct page ⋆ __dev_alloc_pages( gfp_t gfp_mask, unsigned int order )

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
