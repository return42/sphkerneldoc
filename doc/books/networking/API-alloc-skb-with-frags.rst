.. -*- coding: utf-8; mode: rst -*-

.. _API-alloc-skb-with-frags:

====================
alloc_skb_with_frags
====================

*man alloc_skb_with_frags(9)*

*4.6.0-rc5*

allocate skb with page frags


Synopsis
========

.. c:function:: struct sk_buff * alloc_skb_with_frags( unsigned long header_len, unsigned long data_len, int max_page_order, int * errcode, gfp_t gfp_mask )

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

This can be used to allocate a paged skb, given a maximal order for
frags.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
