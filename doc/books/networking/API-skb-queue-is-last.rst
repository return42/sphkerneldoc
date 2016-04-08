
.. _API-skb-queue-is-last:

=================
skb_queue_is_last
=================

*man skb_queue_is_last(9)*

*4.6.0-rc1*

check if skb is the last entry in the queue


Synopsis
========

.. c:function:: bool skb_queue_is_last( const struct sk_buff_head * list, const struct sk_buff * skb )

Arguments
=========

``list``
    queue head

``skb``
    buffer


Description
===========

Returns true if ``skb`` is the last buffer on the list.
