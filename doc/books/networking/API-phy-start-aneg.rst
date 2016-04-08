
.. _API-phy-start-aneg:

==============
phy_start_aneg
==============

*man phy_start_aneg(9)*

*4.6.0-rc1*

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

Sanitizes the settings (if we're not autonegotiating them), and then calls the driver's config_aneg function. If the PHYCONTROL Layer is operating, we change the state to reflect
the beginning of Auto-negotiation or forcing.
