.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-add-adapter:

===============
i2c_add_adapter
===============

*man i2c_add_adapter(9)*

*4.6.0-rc5*

declare i2c adapter, use dynamic bus number


Synopsis
========

.. c:function:: int i2c_add_adapter( struct i2c_adapter * adapter )

Arguments
=========

``adapter``
    the adapter to add


Context
=======

can sleep


Description
===========

This routine is used to declare an I2C adapter when its bus number
doesn't matter or when its bus number is specified by an dt alias.
Examples of bases when the bus number doesn't matter: I2C adapters
dynamically added by USB links or PCI plugin cards.

When this returns zero, a new bus number was allocated and stored in
adap->nr, and the specified adapter became available for clients.
Otherwise, a negative errno value is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
