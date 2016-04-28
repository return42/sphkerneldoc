.. -*- coding: utf-8; mode: rst -*-

.. _API-eth-header:

==========
eth_header
==========

*man eth_header(9)*

*4.6.0-rc5*

create the Ethernet header


Synopsis
========

.. c:function:: int eth_header( struct sk_buff * skb, struct net_device * dev, unsigned short type, const void * daddr, const void * saddr, unsigned int len )

Arguments
=========

``skb``
    buffer to alter

``dev``
    source device

``type``
    Ethernet type field

``daddr``
    destination address (NULL leave destination address)

``saddr``
    source address (NULL use device source address)

``len``
    packet length (<= skb->len)


Description
===========

Set the protocol type. For a packet of type ETH_P_802_3/2 we put the
length in here instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
