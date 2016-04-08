
.. _API-phy-error:

=========
phy_error
=========

*man phy_error(9)*

*4.6.0-rc1*

enter HALTED state for this PHY device


Synopsis
========

.. c:function:: void phy_error( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Moves the PHY to the HALTED state in response to a read or write error, and tells the controller the link is down. Must not be called from interrupt context, or while the
phydev->lock is held.
