.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-queue-purge:

===============
skb_queue_purge
===============

*man skb_queue_purge(9)*

*4.6.0-rc5*

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

Delete all buffers on an ``sk_buff`` list. Each buffer is removed from
the list and one reference dropped. This function takes the list lock
and is atomic with respect to other list locking functions.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
