.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-ethtool-get-eee:

===================
phy_ethtool_get_eee
===================

*man phy_ethtool_get_eee(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
