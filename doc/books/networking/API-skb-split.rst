
.. _API-skb-split:

=========
skb_split
=========

*man skb_split(9)*

*4.6.0-rc1*

Split fragmented skb to two parts at length len.


Synopsis
========

.. c:function:: void skb_split( struct sk_buff * skb, struct sk_buff * skb1, const u32 len )

Arguments
=========

``skb``
    the buffer to split

``skb1``
    the buffer to receive the second part

``len``
    new length for skb
