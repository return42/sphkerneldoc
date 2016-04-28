.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-device-remove:

=================
phy_device_remove
=================

*man phy_device_remove(9)*

*4.6.0-rc5*

Remove a previously registered phy device from the MDIO bus


Synopsis
========

.. c:function:: void phy_device_remove( struct phy_device * phydev )

Arguments
=========

``phydev``
    phy_device structure to remove


Description
===========

This doesn't free the phy_device itself, it merely reverses the effects
of ``phy_device_register``. Use ``phy_device_free`` to free the device
after calling this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
