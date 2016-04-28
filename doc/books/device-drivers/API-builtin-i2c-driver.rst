.. -*- coding: utf-8; mode: rst -*-

.. _API-builtin-i2c-driver:

==================
builtin_i2c_driver
==================

*man builtin_i2c_driver(9)*

*4.6.0-rc5*

Helper macro for registering a builtin I2C driver


Synopsis
========

.. c:function:: builtin_i2c_driver( __i2c_driver )

Arguments
=========

``__i2c_driver``
    i2c_driver struct


Description
===========

Helper macro for I2C drivers which do not do anything special in their
init. This eliminates a lot of boilerplate. Each driver may only use
this macro once, and calling it replaces ``device_initcall``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
