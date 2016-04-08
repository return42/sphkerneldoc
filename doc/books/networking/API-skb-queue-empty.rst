
.. _API-skb-queue-empty:

===============
skb_queue_empty
===============

*man skb_queue_empty(9)*

*4.6.0-rc1*

check if a queue is empty


Synopsis
========

.. c:function:: int skb_queue_empty( const struct sk_buff_head * list )

Arguments
=========

``list``
    queue head


Description
===========

Returns true if the queue is empty, false otherwise.
