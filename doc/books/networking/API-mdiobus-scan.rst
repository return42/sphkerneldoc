
.. _API-mdiobus-scan:

============
mdiobus_scan
============

*man mdiobus_scan(9)*

*4.6.0-rc1*

scan a bus for MDIO devices.


Synopsis
========

.. c:function:: struct phy_device ⋆ mdiobus_scan( struct mii_bus * bus, int addr )

Arguments
=========

``bus``
    mii_bus to scan

``addr``
    address on bus to scan


Description
===========

This function scans the MDIO bus, looking for devices which can be identified using a vendor/product ID in registers 2 and 3. Not all MDIO devices have such registers, but PHY
devices typically do. Hence this function assumes anything found is a PHY, or can be treated as a PHY. Other MDIO devices, such as switches, will probably not be found during the
scan.
