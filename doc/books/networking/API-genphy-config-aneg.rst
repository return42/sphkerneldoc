
.. _API-genphy-config-aneg:

==================
genphy_config_aneg
==================

*man genphy_config_aneg(9)*

*4.6.0-rc1*

restart auto-negotiation or write BMCR


Synopsis
========

.. c:function:: int genphy_config_aneg( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

If auto-negotiation is enabled, we configure the advertising, and then restart auto-negotiation. If it is not enabled, then we write the BMCR.
