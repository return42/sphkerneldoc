
.. _API-skb-queue-purge:

===============
skb_queue_purge
===============

*man skb_queue_purge(9)*

*4.6.0-rc1*

empty a list


Synopsis
========

.. c:function:: void skb_queue_purge( struct sk_buff_head * list )

Arguments
=========

``list``
    list to empty


Description
===========

Delete all buffers on an ``sk_buff`` list. Each buffer is removed from the list and one reference dropped. This function takes the list lock and is atomic with respect to other
list locking functions.
