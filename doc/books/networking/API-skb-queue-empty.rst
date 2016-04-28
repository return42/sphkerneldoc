.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-queue-empty:

===============
skb_queue_empty
===============

*man skb_queue_empty(9)*

*4.6.0-rc5*

check if a queue is empty


Synopsis
========

.. c:function:: int skb_queue_empty( const struct sk_buff_head * list )

Arguments
=========

``list``
    queue head


Description
===========

Returns true if the queue is empty, false otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
