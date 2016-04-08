
.. _API-phy-ethtool-set-eee:

===================
phy_ethtool_set_eee
===================

*man phy_ethtool_set_eee(9)*

*4.6.0-rc1*

set EEE supported and status


Synopsis
========

.. c:function:: int phy_ethtool_set_eee( struct phy_device * phydev, struct ethtool_eee * data )

Arguments
=========

``phydev``
    target phy_device struct

``data``
    ethtool_eee data


Description
===========

it is to program the Advertisement EEE register.
