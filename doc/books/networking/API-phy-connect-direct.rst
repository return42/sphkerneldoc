.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-connect-direct:

==================
phy_connect_direct
==================

*man phy_connect_direct(9)*

*4.6.0-rc5*

connect an ethernet device to a specific phy_device


Synopsis
========

.. c:function:: int phy_connect_direct( struct net_device * dev, struct phy_device * phydev, void (*handler) struct net_device *, phy_interface_t interface )

Arguments
=========

``dev``
    the network device to connect

``phydev``
    the pointer to the phy device

``handler``
    callback function for state change notifications

``interface``
    PHY device's interface


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
