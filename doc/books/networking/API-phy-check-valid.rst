.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-check-valid:

===============
phy_check_valid
===============

*man phy_check_valid(9)*

*4.6.0-rc5*

check if there is a valid PHY setting which matches speed, duplex, and
feature mask


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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
