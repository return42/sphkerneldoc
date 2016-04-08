
.. _API-phy-start-machine:

=================
phy_start_machine
=================

*man phy_start_machine(9)*

*4.6.0-rc1*

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

The PHY infrastructure can run a state machine which tracks whether the PHY is starting up, negotiating, etc. This function starts the timer which tracks the state of the PHY. If
you want to maintain your own state machine, do not call this function.
