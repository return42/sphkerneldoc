.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-dequeue-tail:

================
skb_dequeue_tail
================

*man skb_dequeue_tail(9)*

*4.6.0-rc5*

remove from the tail of the queue


Synopsis
========

.. c:function:: struct sk_buff * skb_dequeue_tail( struct sk_buff_head * list )

Arguments
=========

``list``
    list to dequeue from


Description
===========

Remove the tail of the list. The list lock is taken so the function may
be used safely with other locking list functions. The tail item is
returned or ``NULL`` if the list is empty.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
