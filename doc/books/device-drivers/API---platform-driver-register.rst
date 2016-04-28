.. -*- coding: utf-8; mode: rst -*-

.. _API---platform-driver-register:

==========================
__platform_driver_register
==========================

*man __platform_driver_register(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
