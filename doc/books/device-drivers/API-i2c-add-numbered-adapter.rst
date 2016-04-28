.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-add-numbered-adapter:

========================
i2c_add_numbered_adapter
========================

*man i2c_add_numbered_adapter(9)*

*4.6.0-rc5*

declare i2c adapter, use static bus number


Synopsis
========

.. c:function:: int i2c_add_numbered_adapter( struct i2c_adapter * adap )

Arguments
=========

``adap``
    the adapter to register (with adap->nr initialized)


Context
=======

can sleep


Description
===========

This routine is used to declare an I2C adapter when its bus number
matters. For example, use it for I2C adapters from system-on-chip CPUs,
or otherwise built in to the system's mainboard, and where
i2c_board_info is used to properly configure I2C devices.

If the requested bus number is set to -1, then this function will behave
identically to i2c_add_adapter, and will dynamically assign a bus
number.

If no devices have pre-been declared for this bus, then be sure to
register the adapter before any dynamically allocated ones. Otherwise
the required bus ID may not be available.

When this returns zero, the specified adapter became available for
clients using the bus number provided in adap->nr. Also, the table of
I2C devices pre-declared using ``i2c_register_board_info`` is scanned,
and the appropriate driver model device nodes are created. Otherwise, a
negative errno value is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
