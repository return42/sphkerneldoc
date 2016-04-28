.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-dequeue:

===========
skb_dequeue
===========

*man skb_dequeue(9)*

*4.6.0-rc5*

remove from the head of the queue


Synopsis
========

.. c:function:: struct sk_buff * skb_dequeue( struct sk_buff_head * list )

Arguments
=========

``list``
    list to dequeue from


Description
===========

Remove the head of the list. The list lock is taken so the function may
be used safely with other locking list functions. The head item is
returned or ``NULL`` if the list is empty.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
