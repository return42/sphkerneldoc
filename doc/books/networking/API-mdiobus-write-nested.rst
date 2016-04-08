
.. _API-mdiobus-write-nested:

====================
mdiobus_write_nested
====================

*man mdiobus_write_nested(9)*

*4.6.0-rc1*

Nested version of the mdiobus_write function


Synopsis
========

.. c:function:: int mdiobus_write_nested( struct mii_bus * bus, int addr, u32 regnum, u16 val )

Arguments
=========

``bus``
    the mii_bus struct

``addr``
    the phy address

``regnum``
    register number to write

``val``
    value to write to ``regnum``


Description
===========

In case of nested MDIO bus access avoid lockdep false positives by using ``mutex_lock_nested``.


NOTE
====

MUST NOT be called from interrupt context, because the bus read/write functions may wait for an interrupt to conclude the operation.
