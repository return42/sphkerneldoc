
.. _API-skb-peek-tail:

=============
skb_peek_tail
=============

*man skb_peek_tail(9)*

*4.6.0-rc1*

peek at the tail of an ``sk_buff_head``


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_peek_tail( const struct sk_buff_head * list_ )

Arguments
=========

``list_``
    list to peek at


Description
===========

Peek an ``sk_buff``. Unlike most other operations you _MUST_ be careful with this one. A peek leaves the buffer on the list and someone else may run off with it. You must hold
the appropriate locks or have a private queue to do this.

Returns ``NULL`` for an empty list or a pointer to the tail element. The reference count is not incremented and the reference is therefore volatile. Use with caution.
