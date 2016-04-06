
.. _API---platform-driver-register:

==========================
__platform_driver_register
==========================

*man __platform_driver_register(9)*

*4.6.0-rc1*

register a driver for platform-level devices


Synopsis
========

.. c:function:: int __platform_driver_register( struct platform_driver * drv, struct module * owner )

Arguments
=========

``drv``
    platform driver structure

``owner``
    owning module/driver
