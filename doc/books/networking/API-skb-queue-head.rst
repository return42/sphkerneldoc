
.. _API-skb-queue-head:

==============
skb_queue_head
==============

*man skb_queue_head(9)*

*4.6.0-rc1*

queue a buffer at the list head


Synopsis
========

.. c:function:: void skb_queue_head( struct sk_buff_head * list, struct sk_buff * newsk )

Arguments
=========

``list``
    list to use

``newsk``
    buffer to queue


Description
===========

Queue a buffer at the start of the list. This function takes the list lock and can be used safely with other locking ``sk_buff`` functions safely.

A buffer cannot be placed on two lists at the same time.
