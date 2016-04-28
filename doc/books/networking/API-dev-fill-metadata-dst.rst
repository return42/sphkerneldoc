.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-fill-metadata-dst:

=====================
dev_fill_metadata_dst
=====================

*man dev_fill_metadata_dst(9)*

*4.6.0-rc5*

Retrieve tunnel egress information.


Synopsis
========

.. c:function:: int dev_fill_metadata_dst( struct net_device * dev, struct sk_buff * skb )

Arguments
=========

``dev``
    targeted interface

``skb``
    The packet.


Description
===========

For better visibility of tunnel traffic OVS needs to retrieve egress
tunnel information for a packet. Following API allows user to get this
info.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
