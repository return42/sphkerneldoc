.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-error:

=========
phy_error
=========

*man phy_error(9)*

*4.6.0-rc5*

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

Moves the PHY to the HALTED state in response to a read or write error,
and tells the controller the link is down. Must not be called from
interrupt context, or while the phydev->lock is held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
