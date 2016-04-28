.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-register-board-info:

=======================
i2c_register_board_info
=======================

*man i2c_register_board_info(9)*

*4.6.0-rc5*

statically declare I2C devices


Synopsis
========

.. c:function:: int i2c_register_board_info( int busnum, struct i2c_board_info const * info, unsigned len )

Arguments
=========

``busnum``
    identifies the bus to which these devices belong

``info``
    vector of i2c device descriptors

``len``
    how many descriptors in the vector; may be zero to reserve the
    specified bus number.


Description
===========

Systems using the Linux I2C driver stack can declare tables of board
info while they initialize. This should be done in board-specific init
code near ``arch_initcall`` time, or equivalent, before any I2C adapter
driver is registered. For example, mainboard init code could define
several devices, as could the init code for each daughtercard in a board
stack.

The I2C devices will be created later, after the adapter for the
relevant bus has been registered. After that moment, standard driver
model tools are used to bind “new style” I2C drivers to the devices. The
bus number for any device declared using this routine is not available
for dynamic allocation.

The board info passed can safely be __initdata, but be careful of
embedded pointers (for platform_data, functions, etc) since that won't
be copied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
