
.. _API-phy-disconnect:

==============
phy_disconnect
==============

*man phy_disconnect(9)*

*4.6.0-rc1*

disable interrupts, stop state machine, and detach a PHY device


Synopsis
========

.. c:function:: void phy_disconnect( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct
