.. -*- coding: utf-8; mode: rst -*-

.. _API-eth-hw-addr-random:

==================
eth_hw_addr_random
==================

*man eth_hw_addr_random(9)*

*4.6.0-rc5*

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

Generate a random Ethernet address (MAC) to be used by a net device and
set addr_assign_type so the state can be read by sysfs and be used by
userspace.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
