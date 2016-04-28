.. -*- coding: utf-8; mode: rst -*-

.. _API-get-phy-device:

==============
get_phy_device
==============

*man get_phy_device(9)*

*4.6.0-rc5*

reads the specified PHY device and returns its ``phy_device`` struct


Synopsis
========

.. c:function:: struct phy_device * get_phy_device( struct mii_bus * bus, int addr, bool is_c45 )

Arguments
=========

``bus``
    the target MII bus

``addr``
    PHY address on the MII bus

``is_c45``
    If true the PHY uses the 802.3 clause 45 protocol


Description
===========

Reads the ID registers of the PHY at ``addr`` on the ``bus``, then
allocates and returns the phy_device to represent it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
