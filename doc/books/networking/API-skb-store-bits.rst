
.. _API-skb-store-bits:

==============
skb_store_bits
==============

*man skb_store_bits(9)*

*4.6.0-rc1*

store bits from kernel buffer to skb


Synopsis
========

.. c:function:: int skb_store_bits( struct sk_buff * skb, int offset, const void * from, int len )

Arguments
=========

``skb``
    destination buffer

``offset``
    offset in destination

``from``
    source buffer

``len``
    number of bytes to copy


Description
===========

Copy the specified number of bytes from the source buffer to the destination skb. This function handles all the messy bits of traversing fragment lists and such.
