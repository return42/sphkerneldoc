
.. _API-phy-ethtool-sset:

================
phy_ethtool_sset
================

*man phy_ethtool_sset(9)*

*4.6.0-rc1*

generic ethtool sset function, handles all the details


Synopsis
========

.. c:function:: int phy_ethtool_sset( struct phy_device * phydev, struct ethtool_cmd * cmd )

Arguments
=========

``phydev``
    target phy_device struct

``cmd``
    ethtool_cmd


A few notes about parameter checking
====================================

- We don't set port or transceiver, so we don't care what they were set to. - ``phy_start_aneg`` will make sure forced settings are sane, and choose the next best ones from the
ones selected, so we don't care if ethtool tries to give us bad values.
