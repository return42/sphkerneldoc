
.. _API-get-phy-device:

==============
get_phy_device
==============

*man get_phy_device(9)*

*4.6.0-rc1*

reads the specified PHY device and returns its ``phy_device`` struct


Synopsis
========

.. c:function:: struct phy_device ⋆ get_phy_device( struct mii_bus * bus, int addr, bool is_c45 )

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

Reads the ID registers of the PHY at ``addr`` on the ``bus``, then allocates and returns the phy_device to represent it.
