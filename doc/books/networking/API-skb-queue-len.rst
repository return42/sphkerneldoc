.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-queue-len:

=============
skb_queue_len
=============

*man skb_queue_len(9)*

*4.6.0-rc5*

get queue length


Synopsis
========

.. c:function:: __u32 skb_queue_len( const struct sk_buff_head * list_ )

Arguments
=========

``list_``
    list to measure


Description
===========

Return the length of an ``sk_buff`` queue.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
