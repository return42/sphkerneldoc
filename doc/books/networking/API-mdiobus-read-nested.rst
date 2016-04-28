.. -*- coding: utf-8; mode: rst -*-

.. _API-mdiobus-read-nested:

===================
mdiobus_read_nested
===================

*man mdiobus_read_nested(9)*

*4.6.0-rc5*

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

In case of nested MDIO bus access avoid lockdep false positives by using
``mutex_lock_nested``.


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
