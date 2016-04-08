
.. _API-skb-queue-prev:

==============
skb_queue_prev
==============

*man skb_queue_prev(9)*

*4.6.0-rc1*

return the prev packet in the queue


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_queue_prev( const struct sk_buff_head * list, const struct sk_buff * skb )

Arguments
=========

``list``
    queue head

``skb``
    current buffer


Description
===========

Return the prev packet in ``list`` before ``skb``. It is only valid to call this if ``skb_queue_is_first`` evaluates to false.
