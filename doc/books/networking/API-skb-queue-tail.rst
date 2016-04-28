.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-queue-tail:

==============
skb_queue_tail
==============

*man skb_queue_tail(9)*

*4.6.0-rc5*

queue a buffer at the list tail


Synopsis
========

.. c:function:: void skb_queue_tail( struct sk_buff_head * list, struct sk_buff * newsk )

Arguments
=========

``list``
    list to use

``newsk``
    buffer to queue


Description
===========

Queue a buffer at the tail of the list. This function takes the list
lock and can be used safely with other locking ``sk_buff`` functions
safely.

A buffer cannot be placed on two lists at the same time.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
