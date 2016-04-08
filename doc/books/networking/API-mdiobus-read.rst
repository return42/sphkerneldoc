
.. _API-mdiobus-read:

============
mdiobus_read
============

*man mdiobus_read(9)*

*4.6.0-rc1*

Convenience function for reading a given MII mgmt register


Synopsis
========

.. c:function:: int mdiobus_read( struct mii_bus * bus, int addr, u32 regnum )

Arguments
=========

``bus``
    the mii_bus struct

``addr``
    the phy address

``regnum``
    register number to read


NOTE
====

MUST NOT be called from interrupt context, because the bus read/write functions may wait for an interrupt to conclude the operation.
