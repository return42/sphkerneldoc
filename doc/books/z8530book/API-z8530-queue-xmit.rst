.. -*- coding: utf-8; mode: rst -*-

.. _API-z8530-queue-xmit:

================
z8530_queue_xmit
================

*man z8530_queue_xmit(9)*

*4.6.0-rc5*

Queue a packet


Synopsis
========

.. c:function:: netdev_tx_t z8530_queue_xmit( struct z8530_channel * c, struct sk_buff * skb )

Arguments
=========

``c``
    The channel to use

``skb``
    The packet to kick down the channel


Description
===========

Queue a packet for transmission. Because we have rather hard to hit
interrupt latencies for the Z85230 per packet even in DMA mode we do the
flip to DMA buffer if needed here not in the IRQ.

Called from the network code. The lock is not held at this point.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
