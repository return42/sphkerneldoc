.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-new-device:

==============
i2c_new_device
==============

*man i2c_new_device(9)*

*4.6.0-rc5*

instantiate an i2c device


Synopsis
========

.. c:function:: struct i2c_client * i2c_new_device( struct i2c_adapter * adap, struct i2c_board_info const * info )

Arguments
=========

``adap``
    the adapter managing the device

``info``
    describes one I2C device; bus_num is ignored


Context
=======

can sleep


Description
===========

Create an i2c device. Binding is handled through driver model
``probe``/``remove`` methods. A driver may be bound to this device when
we return from this function, or any later moment (e.g. maybe
hotplugging will load the driver module). This call is not appropriate
for use by mainboard initialization logic, which usually runs during an
``arch_initcall`` long before any i2c_adapter could exist.

This returns the new i2c client, which may be saved for later use with
``i2c_unregister_device``; or NULL to indicate an error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
