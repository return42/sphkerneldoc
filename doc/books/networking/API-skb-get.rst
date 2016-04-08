
.. _API-skb-get:

=======
skb_get
=======

*man skb_get(9)*

*4.6.0-rc1*

reference buffer


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_get( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to reference


Description
===========

Makes another reference to a socket buffer and returns a pointer to the buffer.
