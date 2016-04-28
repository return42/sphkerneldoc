.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-queue-is-last:

=================
skb_queue_is_last
=================

*man skb_queue_is_last(9)*

*4.6.0-rc5*

check if skb is the last entry in the queue


Synopsis
========

.. c:function:: bool skb_queue_is_last( const struct sk_buff_head * list, const struct sk_buff * skb )

Arguments
=========

``list``
    queue head

``skb``
    buffer


Description
===========

Returns true if ``skb`` is the last buffer on the list.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
