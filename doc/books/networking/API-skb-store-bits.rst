.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-store-bits:

==============
skb_store_bits
==============

*man skb_store_bits(9)*

*4.6.0-rc5*

store bits from kernel buffer to skb


Synopsis
========

.. c:function:: int skb_store_bits( struct sk_buff * skb, int offset, const void * from, int len )

Arguments
=========

``skb``
    destination buffer

``offset``
    offset in destination

``from``
    source buffer

``len``
    number of bytes to copy


Description
===========

Copy the specified number of bytes from the source buffer to the
destination skb. This function handles all the messy bits of traversing
fragment lists and such.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
