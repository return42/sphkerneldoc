.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-del-driver:

==============
i2c_del_driver
==============

*man i2c_del_driver(9)*

*4.6.0-rc5*

unregister I2C driver


Synopsis
========

.. c:function:: void i2c_del_driver( struct i2c_driver * driver )

Arguments
=========

``driver``
    the driver being unregistered


Context
=======

can sleep


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
