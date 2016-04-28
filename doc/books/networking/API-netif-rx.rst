.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-rx:

========
netif_rx
========

*man netif_rx(9)*

*4.6.0-rc5*

post buffer to the network code


Synopsis
========

.. c:function:: int netif_rx( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to post


Description
===========

This function receives a packet from a device driver and queues it for
the upper (protocol) levels to process. It always succeeds. The buffer
may be dropped during processing for congestion control or by the
protocol layers.


return values
=============

NET_RX_SUCCESS (no congestion) NET_RX_DROP (packet was dropped)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
