
.. _API-i2c-new-dummy:

=============
i2c_new_dummy
=============

*man i2c_new_dummy(9)*

*4.6.0-rc1*

return a new i2c device bound to a dummy driver


Synopsis
========

.. c:function:: struct i2c_client ⋆ i2c_new_dummy( struct i2c_adapter * adapter, u16 address )

Arguments
=========

``adapter``
    the adapter managing the device

``address``
    seven bit address to be used


Context
=======

can sleep


Description
===========

This returns an I2C client bound to the “dummy” driver, intended for use with devices that consume multiple addresses. Examples of such chips include various EEPROMS (like 24c04
and 24c08 models).

These dummy devices have two main uses. First, most I2C and SMBus calls except ``i2c_transfer`` need a client handle; the dummy will be that handle. And second, this prevents the
specified address from being bound to a different driver.

This returns the new i2c client, which should be saved for later use with ``i2c_unregister_device``; or NULL to indicate an error.
