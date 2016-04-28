.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-postpull-rcsum:

==================
skb_postpull_rcsum
==================

*man skb_postpull_rcsum(9)*

*4.6.0-rc5*

update checksum for received skb after pull


Synopsis
========

.. c:function:: void skb_postpull_rcsum( struct sk_buff * skb, const void * start, unsigned int len )

Arguments
=========

``skb``
    buffer to update

``start``
    start of data before pull

``len``
    length of data pulled


Description
===========

After doing a pull on a received packet, you need to call this to update
the CHECKSUM_COMPLETE checksum, or set ip_summed to CHECKSUM_NONE so
that it can be recomputed from scratch.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
