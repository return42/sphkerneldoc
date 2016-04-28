.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-bonding-info-change:

==========================
netdev_bonding_info_change
==========================

*man netdev_bonding_info_change(9)*

*4.6.0-rc5*

Dispatch event about slave change


Synopsis
========

.. c:function:: void netdev_bonding_info_change( struct net_device * dev, struct netdev_bonding_info * bonding_info )

Arguments
=========

``dev``
    device

``bonding_info``
    info to dispatch


Description
===========

Send NETDEV_BONDING_INFO to netdev notifiers with info. The caller
must hold the RTNL lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
