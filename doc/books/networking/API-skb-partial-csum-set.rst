.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-partial-csum-set:

====================
skb_partial_csum_set
====================

*man skb_partial_csum_set(9)*

*4.6.0-rc5*

set up and verify partial csum values for packet


Synopsis
========

.. c:function:: bool skb_partial_csum_set( struct sk_buff * skb, u16 start, u16 off )

Arguments
=========

``skb``
    the skb to set

``start``
    the number of bytes after skb->data to start checksumming.

``off``
    the offset from start to place the checksum.


Description
===========

For untrusted partially-checksummed packets, we need to make sure the
values for skb->csum_start and skb->csum_offset are valid so we don't
oops.

This function checks and sets those values and skb->ip_summed: if this
returns false you should drop the packet.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
