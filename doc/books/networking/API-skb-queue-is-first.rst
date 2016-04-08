
.. _API-skb-queue-is-first:

==================
skb_queue_is_first
==================

*man skb_queue_is_first(9)*

*4.6.0-rc1*

check if skb is the first entry in the queue


Synopsis
========

.. c:function:: bool skb_queue_is_first( const struct sk_buff_head * list, const struct sk_buff * skb )

Arguments
=========

``list``
    queue head

``skb``
    buffer


Description
===========

Returns true if ``skb`` is the first buffer on the list.
