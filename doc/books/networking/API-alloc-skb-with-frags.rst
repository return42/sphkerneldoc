
.. _API-alloc-skb-with-frags:

====================
alloc_skb_with_frags
====================

*man alloc_skb_with_frags(9)*

*4.6.0-rc1*

allocate skb with page frags


Synopsis
========

.. c:function:: struct sk_buff ⋆ alloc_skb_with_frags( unsigned long header_len, unsigned long data_len, int max_page_order, int * errcode, gfp_t gfp_mask )

Arguments
=========

``header_len``
    size of linear part

``data_len``
    needed length in frags

``max_page_order``
    max page order desired.

``errcode``
    pointer to error code if any

``gfp_mask``
    allocation mask


Description
===========

This can be used to allocate a paged skb, given a maximal order for frags.
