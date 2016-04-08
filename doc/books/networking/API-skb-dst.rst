
.. _API-skb-dst:

=======
skb_dst
=======

*man skb_dst(9)*

*4.6.0-rc1*

returns skb dst_entry


Synopsis
========

.. c:function:: struct dst_entry ⋆ skb_dst( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer


Description
===========

Returns skb dst_entry, regardless of reference taken or not.
