.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-find-setting:

================
phy_find_setting
================

*man phy_find_setting(9)*

*4.6.0-rc5*

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

Searches the settings array for the setting which matches the desired
speed and duplex, and returns the index of that setting. Returns the
index of the last setting if none of the others match.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
