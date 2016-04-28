.. -*- coding: utf-8; mode: rst -*-

.. _API-eth-change-mtu:

==============
eth_change_mtu
==============

*man eth_change_mtu(9)*

*4.6.0-rc5*

set new MTU size


Synopsis
========

.. c:function:: int eth_change_mtu( struct net_device * dev, int new_mtu )

Arguments
=========

``dev``
    network device

``new_mtu``
    new Maximum Transfer Unit


Description
===========

Allow changing MTU size. Needs to be overridden for devices supporting
jumbo frames.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
