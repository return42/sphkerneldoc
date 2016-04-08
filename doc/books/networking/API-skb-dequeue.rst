
.. _API-skb-dequeue:

===========
skb_dequeue
===========

*man skb_dequeue(9)*

*4.6.0-rc1*

remove from the head of the queue


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_dequeue( struct sk_buff_head * list )

Arguments
=========

``list``
    list to dequeue from


Description
===========

Remove the head of the list. The list lock is taken so the function may be used safely with other locking list functions. The head item is returned or ``NULL`` if the list is
empty.
