.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-queue-next:

==============
skb_queue_next
==============

*man skb_queue_next(9)*

*4.6.0-rc5*

return the next packet in the queue


Synopsis
========

.. c:function:: struct sk_buff * skb_queue_next( const struct sk_buff_head * list, const struct sk_buff * skb )

Arguments
=========

``list``
    queue head

``skb``
    current buffer


Description
===========

Return the next packet in ``list`` after ``skb``. It is only valid to
call this if ``skb_queue_is_last`` evaluates to false.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
