
.. _API-skb-queue-len:

=============
skb_queue_len
=============

*man skb_queue_len(9)*

*4.6.0-rc1*

get queue length


Synopsis
========

.. c:function:: __u32 skb_queue_len( const struct sk_buff_head * list_ )

Arguments
=========

``list_``
    list to measure


Description
===========

Return the length of an ``sk_buff`` queue.
