.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-tx-timestamp:

================
skb_tx_timestamp
================

*man skb_tx_timestamp(9)*

*4.6.0-rc5*

Driver hook for transmit timestamping


Synopsis
========

.. c:function:: void skb_tx_timestamp( struct sk_buff * skb )

Arguments
=========

``skb``
    A socket buffer.


Description
===========

Ethernet MAC Drivers should call this function in their ``hard_xmit``
function immediately before giving the sk_buff to the MAC hardware.

Specifically, one should make absolutely sure that this function is
called before TX completion of this packet can trigger. Otherwise the
packet could potentially already be freed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
