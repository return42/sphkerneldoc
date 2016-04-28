.. -*- coding: utf-8; mode: rst -*-

.. _API-eth-mac-addr:

============
eth_mac_addr
============

*man eth_mac_addr(9)*

*4.6.0-rc5*

set new Ethernet hardware address


Synopsis
========

.. c:function:: int eth_mac_addr( struct net_device * dev, void * p )

Arguments
=========

``dev``
    network device

``p``
    socket address


Description
===========

Change hardware address of device.

This doesn't change hardware matching, so needs to be overridden for
most real devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
