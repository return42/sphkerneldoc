
.. _API-builtin-driver:

==============
builtin_driver
==============

*man builtin_driver(9)*

*4.6.0-rc1*

Helper macro for drivers that don't do anything special in init and have no exit. This eliminates some boilerplate. Each driver may only use this macro once, and calling it
replaces device_initcall (or in some cases, the legacy __initcall). This is meant to be a direct parallel of ``module_driver`` above but without the __exit stuff that is not
used for builtin cases.


Synopsis
========

.. c:function:: builtin_driver( __driver, __register, ... )

Arguments
=========

``__driver``
    driver name

``__register``
    register function for this driver type @...: Additional arguments to be passed to __register

``...``
    variable arguments


Description
===========

Use this macro to construct bus specific macros for registering drivers, and do not use it on its own.
