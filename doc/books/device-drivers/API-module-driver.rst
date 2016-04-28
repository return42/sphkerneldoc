.. -*- coding: utf-8; mode: rst -*-

.. _API-module-driver:

=============
module_driver
=============

*man module_driver(9)*

*4.6.0-rc5*

Helper macro for drivers that don't do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces ``module_init`` and
``module_exit``.


Synopsis
========

.. c:function:: module_driver( __driver, __register, __unregister, ... )

Arguments
=========

``__driver``
    driver name

``__register``
    register function for this driver type

``__unregister``
    unregister function for this driver type @...: Additional arguments
    to be passed to __register and __unregister.

``...``
    variable arguments


Description
===========

Use this macro to construct bus specific macros for registering drivers,
and do not use it on its own.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
