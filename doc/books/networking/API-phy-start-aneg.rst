.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-start-aneg:

==============
phy_start_aneg
==============

*man phy_start_aneg(9)*

*4.6.0-rc5*

start auto-negotiation for this PHY device


Synopsis
========

.. c:function:: int phy_start_aneg( struct phy_device * phydev )

Arguments
=========

``phydev``
    the phy_device struct


Description
===========

Sanitizes the settings (if we're not autonegotiating them), and then
calls the driver's config_aneg function. If the PHYCONTROL Layer is
operating, we change the state to reflect the beginning of
Auto-negotiation or forcing.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
