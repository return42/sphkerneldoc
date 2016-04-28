.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-sanitize-settings:

=====================
phy_sanitize_settings
=====================

*man phy_sanitize_settings(9)*

*4.6.0-rc5*

make sure the PHY is set to supported speed and duplex


Synopsis
========

.. c:function:: void phy_sanitize_settings( struct phy_device * phydev )

Arguments
=========

``phydev``
    the target phy_device struct


Description
===========

Make sure the PHY is set to supported speeds and duplexes. Drop down by
one in this order: 1000/FULL, 1000/HALF, 100/FULL, 100/HALF, 10/FULL,
10/HALF.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
