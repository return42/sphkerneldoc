
.. _API-phy-start:

=========
phy_start
=========

*man phy_start(9)*

*4.6.0-rc1*

start or restart a PHY device


Synopsis
========

.. c:function:: void phy_start( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Indicates the attached device's readiness to handle PHY-related work. Used during startup to start the PHY, and after a call to ``phy_stop`` to resume operation. Also used to
indicate the MDIO bus has cleared an error condition.
