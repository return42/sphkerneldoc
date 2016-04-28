.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-receive-skb:

=================
netif_receive_skb
=================

*man netif_receive_skb(9)*

*4.6.0-rc5*

process receive buffer from network


Synopsis
========

.. c:function:: int netif_receive_skb( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to process


Description
===========

``netif_receive_skb`` is the main receive data processing function. It
always succeeds. The buffer may be dropped during processing for
congestion control or by the protocol layers.

This function may only be called from softirq context and interrupts
should be enabled.

Return values (usually ignored):


NET_RX_SUCCESS
==============

no congestion


NET_RX_DROP
===========

packet was dropped


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
