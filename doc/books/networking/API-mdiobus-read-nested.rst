
.. _API-mdiobus-read-nested:

===================
mdiobus_read_nested
===================

*man mdiobus_read_nested(9)*

*4.6.0-rc1*

Nested version of the mdiobus_read function


Synopsis
========

.. c:function:: int mdiobus_read_nested( struct mii_bus * bus, int addr, u32 regnum )

Arguments
=========

``bus``
    the mii_bus struct

``addr``
    the phy address

``regnum``
    register number to read


Description
===========

In case of nested MDIO bus access avoid lockdep false positives by using ``mutex_lock_nested``.


NOTE
====

MUST NOT be called from interrupt context, because the bus read/write functions may wait for an interrupt to conclude the operation.
