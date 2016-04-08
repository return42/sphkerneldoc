
.. _API-skb-cow-head:

============
skb_cow_head
============

*man skb_cow_head(9)*

*4.6.0-rc1*

skb_cow but only making the head writable


Synopsis
========

.. c:function:: int skb_cow_head( struct sk_buff * skb, unsigned int headroom )

Arguments
=========

``skb``
    buffer to cow

``headroom``
    needed headroom


Description
===========

This function is identical to skb_cow except that we replace the skb_cloned check by skb_header_cloned. It should be used when you only need to push on some header and do not
need to modify the data.
