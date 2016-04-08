
.. _API-eth-hw-addr-random:

==================
eth_hw_addr_random
==================

*man eth_hw_addr_random(9)*

*4.6.0-rc1*

Generate software assigned random Ethernet and set device flag


Synopsis
========

.. c:function:: void eth_hw_addr_random( struct net_device * dev )

Arguments
=========

``dev``
    pointer to net_device structure


Description
===========

Generate a random Ethernet address (MAC) to be used by a net device and set addr_assign_type so the state can be read by sysfs and be used by userspace.
