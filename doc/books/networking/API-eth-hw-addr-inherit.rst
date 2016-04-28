.. -*- coding: utf-8; mode: rst -*-

.. _API-eth-hw-addr-inherit:

===================
eth_hw_addr_inherit
===================

*man eth_hw_addr_inherit(9)*

*4.6.0-rc5*

Copy dev_addr from another net_device


Synopsis
========

.. c:function:: void eth_hw_addr_inherit( struct net_device * dst, struct net_device * src )

Arguments
=========

``dst``
    pointer to net_device to copy dev_addr to

``src``
    pointer to net_device to copy dev_addr from


Description
===========

Copy the Ethernet address from one net_device to another along with the
address attributes (addr_assign_type).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
