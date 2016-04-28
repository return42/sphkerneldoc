.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-queue-splice-tail:

=====================
skb_queue_splice_tail
=====================

*man skb_queue_splice_tail(9)*

*4.6.0-rc5*

join two skb lists, each list being a queue


Synopsis
========

.. c:function:: void skb_queue_splice_tail( const struct sk_buff_head * list, struct sk_buff_head * head )

Arguments
=========

``list``
    the new list to add

``head``
    the place to add it in the first list


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
