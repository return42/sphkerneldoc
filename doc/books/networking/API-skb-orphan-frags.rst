
.. _API-skb-orphan-frags:

================
skb_orphan_frags
================

*man skb_orphan_frags(9)*

*4.6.0-rc1*

orphan the frags contained in a buffer


Synopsis
========

.. c:function:: int skb_orphan_frags( struct sk_buff * skb, gfp_t gfp_mask )

Arguments
=========

``skb``
    buffer to orphan frags from

``gfp_mask``
    allocation mask for replacement pages


Description
===========

For each frag in the SKB which needs a destructor (i.e. has an owner) create a copy of that frag and release the original page by calling the destructor.
