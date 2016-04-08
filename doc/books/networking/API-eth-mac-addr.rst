
.. _API-eth-mac-addr:

============
eth_mac_addr
============

*man eth_mac_addr(9)*

*4.6.0-rc1*

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

This doesn't change hardware matching, so needs to be overridden for most real devices.
