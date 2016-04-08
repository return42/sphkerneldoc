
.. _API-skb-reserve:

===========
skb_reserve
===========

*man skb_reserve(9)*

*4.6.0-rc1*

adjust headroom


Synopsis
========

.. c:function:: void skb_reserve( struct sk_buff * skb, int len )

Arguments
=========

``skb``
    buffer to alter

``len``
    bytes to move


Description
===========

Increase the headroom of an empty ``sk_buff`` by reducing the tail room. This is only allowed for an empty buffer.
