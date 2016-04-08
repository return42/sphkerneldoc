
.. _API-dev-forward-skb:

===============
dev_forward_skb
===============

*man dev_forward_skb(9)*

*4.6.0-rc1*

loopback an skb to another netif


Synopsis
========

.. c:function:: int dev_forward_skb( struct net_device * dev, struct sk_buff * skb )

Arguments
=========

``dev``
    destination network device

``skb``
    buffer to forward


return values
=============

NET_RX_SUCCESS (no congestion) NET_RX_DROP (packet was dropped, but freed)

dev_forward_skb can be used for injecting an skb from the start_xmit function of one device into the receive queue of another device.

The receiving device may be in another namespace, so we have to clear all information in the skb that could impact namespace isolation.
