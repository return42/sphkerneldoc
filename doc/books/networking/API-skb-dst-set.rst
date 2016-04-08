
.. _API-skb-dst-set:

===========
skb_dst_set
===========

*man skb_dst_set(9)*

*4.6.0-rc1*

sets skb dst


Synopsis
========

.. c:function:: void skb_dst_set( struct sk_buff * skb, struct dst_entry * dst )

Arguments
=========

``skb``
    buffer

``dst``
    dst entry


Description
===========

Sets skb dst, assuming a reference was taken on dst and should be released by ``skb_dst_drop``
