.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-del-adapter:

===============
i2c_del_adapter
===============

*man i2c_del_adapter(9)*

*4.6.0-rc5*

unregister I2C adapter


Synopsis
========

.. c:function:: void i2c_del_adapter( struct i2c_adapter * adap )

Arguments
=========

``adap``
    the adapter being unregistered


Context
=======

can sleep


Description
===========

This unregisters an I2C adapter which was previously registered by
``i2c_add_adapter`` or ``i2c_add_numbered_adapter``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
