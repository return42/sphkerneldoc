.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-start-machine:

=================
phy_start_machine
=================

*man phy_start_machine(9)*

*4.6.0-rc5*

start PHY state machine tracking


Synopsis
========

.. c:function:: void phy_start_machine( struct phy_device * phydev )

Arguments
=========

``phydev``
    the phy_device struct


Description
===========

The PHY infrastructure can run a state machine which tracks whether the
PHY is starting up, negotiating, etc. This function starts the timer
which tracks the state of the PHY. If you want to maintain your own
state machine, do not call this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
