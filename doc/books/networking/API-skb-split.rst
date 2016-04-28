.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-split:

=========
skb_split
=========

*man skb_split(9)*

*4.6.0-rc5*

Split fragmented skb to two parts at length len.


Synopsis
========

.. c:function:: void skb_split( struct sk_buff * skb, struct sk_buff * skb1, const u32 len )

Arguments
=========

``skb``
    the buffer to split

``skb1``
    the buffer to receive the second part

``len``
    new length for skb


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
