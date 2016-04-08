
.. _API-phy-check-valid:

===============
phy_check_valid
===============

*man phy_check_valid(9)*

*4.6.0-rc1*

check if there is a valid PHY setting which matches speed, duplex, and feature mask


Synopsis
========

.. c:function:: bool phy_check_valid( int speed, int duplex, u32 features )

Arguments
=========

``speed``
    speed to match

``duplex``
    duplex to match

``features``
    A mask of the valid settings


Description
===========

Returns true if there is a valid setting, false otherwise.
