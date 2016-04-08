
.. _API-skb-peek-next:

=============
skb_peek_next
=============

*man skb_peek_next(9)*

*4.6.0-rc1*

peek skb following the given one from a queue


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_peek_next( struct sk_buff * skb, const struct sk_buff_head * list_ )

Arguments
=========

``skb``
    skb to start from

``list_``
    list to peek at


Description
===========

Returns ``NULL`` when the end of the list is met or a pointer to the next element. The reference count is not incremented and the reference is therefore volatile. Use with caution.
