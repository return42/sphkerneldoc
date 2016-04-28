.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-prepare-link:

================
phy_prepare_link
================

*man phy_prepare_link(9)*

*4.6.0-rc5*

prepares the PHY layer to monitor link status


Synopsis
========

.. c:function:: void phy_prepare_link( struct phy_device * phydev, void (*handler) struct net_device * )

Arguments
=========

``phydev``
    target phy_device struct

``handler``
    callback function for link status change notifications


Description
===========

Tells the PHY infrastructure to handle the gory details on monitoring
link status (whether through polling or an interrupt), and to call back
to the connected device driver when the link status changes. If you want
to monitor your own link state, don't call this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
