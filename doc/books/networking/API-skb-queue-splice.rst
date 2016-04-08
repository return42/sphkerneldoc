
.. _API-skb-queue-splice:

================
skb_queue_splice
================

*man skb_queue_splice(9)*

*4.6.0-rc1*

join two skb lists, this is designed for stacks


Synopsis
========

.. c:function:: void skb_queue_splice( const struct sk_buff_head * list, struct sk_buff_head * head )

Arguments
=========

``list``
    the new list to add

``head``
    the place to add it in the first list
