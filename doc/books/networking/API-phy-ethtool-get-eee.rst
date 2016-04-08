
.. _API-phy-ethtool-get-eee:

===================
phy_ethtool_get_eee
===================

*man phy_ethtool_get_eee(9)*

*4.6.0-rc1*

get EEE supported and status


Synopsis
========

.. c:function:: int phy_ethtool_get_eee( struct phy_device * phydev, struct ethtool_eee * data )

Arguments
=========

``phydev``
    target phy_device struct

``data``
    ethtool_eee data


Description
===========

it reportes the Supported/Advertisement/LP Advertisement capabilities.
