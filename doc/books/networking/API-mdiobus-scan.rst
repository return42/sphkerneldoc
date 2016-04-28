.. -*- coding: utf-8; mode: rst -*-

.. _API-mdiobus-scan:

============
mdiobus_scan
============

*man mdiobus_scan(9)*

*4.6.0-rc5*

scan a bus for MDIO devices.


Synopsis
========

.. c:function:: struct phy_device * mdiobus_scan( struct mii_bus * bus, int addr )

Arguments
=========

``bus``
    mii_bus to scan

``addr``
    address on bus to scan


Description
===========

This function scans the MDIO bus, looking for devices which can be
identified using a vendor/product ID in registers 2 and 3. Not all MDIO
devices have such registers, but PHY devices typically do. Hence this
function assumes anything found is a PHY, or can be treated as a PHY.
Other MDIO devices, such as switches, will probably not be found during
the scan.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
