
.. _API-phy-find-setting:

================
phy_find_setting
================

*man phy_find_setting(9)*

*4.6.0-rc1*

find a PHY settings array entry that matches speed & duplex


Synopsis
========

.. c:function:: unsigned int phy_find_setting( int speed, int duplex )

Arguments
=========

``speed``
    speed to match

``duplex``
    duplex to match


Description
===========

Searches the settings array for the setting which matches the desired speed and duplex, and returns the index of that setting. Returns the index of the last setting if none of the
others match.
