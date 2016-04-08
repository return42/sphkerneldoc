
.. _API-skb-page-frag-refill:

====================
skb_page_frag_refill
====================

*man skb_page_frag_refill(9)*

*4.6.0-rc1*

check that a page_frag contains enough room


Synopsis
========

.. c:function:: bool skb_page_frag_refill( unsigned int sz, struct page_frag * pfrag, gfp_t gfp )

Arguments
=========

``sz``
    minimum size of the fragment we want to get

``pfrag``
    pointer to page_frag

``gfp``
    priority for memory allocation


Note
====

While this allocator tries to use high order pages, there is no guarantee that allocations succeed. Therefore, ``sz`` MUST be less or equal than PAGE_SIZE.
