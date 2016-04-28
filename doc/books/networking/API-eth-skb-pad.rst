.. -*- coding: utf-8; mode: rst -*-

.. _API-eth-skb-pad:

===========
eth_skb_pad
===========

*man eth_skb_pad(9)*

*4.6.0-rc5*

Pad buffer to mininum number of octets for Ethernet frame


Synopsis
========

.. c:function:: int eth_skb_pad( struct sk_buff * skb )

Arguments
=========

``skb``
    Buffer to pad


Description
===========

An Ethernet frame should have a minimum size of 60 bytes. This function
takes short frames and pads them with zeros up to the 60 byte limit.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
