
.. _API-module-driver:

=============
module_driver
=============

*man module_driver(9)*

*4.6.0-rc1*

Helper macro for drivers that don't do anything special in module init/exit. This eliminates a lot of boilerplate. Each module may only use this macro once, and calling it replaces
``module_init`` and ``module_exit``.


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
    unregister function for this driver type @...: Additional arguments to be passed to __register and __unregister.

``...``
    variable arguments


Description
===========

Use this macro to construct bus specific macros for registering drivers, and do not use it on its own.
