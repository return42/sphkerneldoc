.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-stop-machine:

================
phy_stop_machine
================

*man phy_stop_machine(9)*

*4.6.0-rc5*

stop the PHY state machine tracking


Synopsis
========

.. c:function:: void phy_stop_machine( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Stops the state machine timer, sets the state to UP (unless it wasn't up
yet). This function must be called BEFORE phy_detach.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
