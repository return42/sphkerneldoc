
.. _API---skb-queue-after:

=================
__skb_queue_after
=================

*man __skb_queue_after(9)*

*4.6.0-rc1*

queue a buffer at the list head


Synopsis
========

.. c:function:: void __skb_queue_after( struct sk_buff_head * list, struct sk_buff * prev, struct sk_buff * newsk )

Arguments
=========

``list``
    list to use

``prev``
    place after this buffer

``newsk``
    buffer to queue


Description
===========

Queue a buffer int the middle of a list. This function takes no locks and you must therefore hold required locks before calling it.

A buffer cannot be placed on two lists at the same time.
