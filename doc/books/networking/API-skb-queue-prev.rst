.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-queue-prev:

==============
skb_queue_prev
==============

*man skb_queue_prev(9)*

*4.6.0-rc5*

return the prev packet in the queue


Synopsis
========

.. c:function:: struct sk_buff * skb_queue_prev( const struct sk_buff_head * list, const struct sk_buff * skb )

Arguments
=========

``list``
    queue head

``skb``
    current buffer


Description
===========

Return the prev packet in ``list`` before ``skb``. It is only valid to
call this if ``skb_queue_is_first`` evaluates to false.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
