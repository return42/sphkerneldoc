.. -*- coding: utf-8; mode: rst -*-

.. _API-mdiobus-write:

=============
mdiobus_write
=============

*man mdiobus_write(9)*

*4.6.0-rc5*

Convenience function for writing a given MII mgmt register


Synopsis
========

.. c:function:: int mdiobus_write( struct mii_bus * bus, int addr, u32 regnum, u16 val )

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


NOTE
====

MUST NOT be called from interrupt context, because the bus read/write
functions may wait for an interrupt to conclude the operation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
