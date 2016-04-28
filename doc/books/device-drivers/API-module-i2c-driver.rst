.. -*- coding: utf-8; mode: rst -*-

.. _API-module-i2c-driver:

=================
module_i2c_driver
=================

*man module_i2c_driver(9)*

*4.6.0-rc5*

Helper macro for registering a modular I2C driver


Synopsis
========

.. c:function:: module_i2c_driver( __i2c_driver )

Arguments
=========

``__i2c_driver``
    i2c_driver struct


Description
===========

Helper macro for I2C drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces ``module_init`` and
``module_exit``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
