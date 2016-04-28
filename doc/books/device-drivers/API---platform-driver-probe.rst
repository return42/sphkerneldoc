.. -*- coding: utf-8; mode: rst -*-

.. _API---platform-driver-probe:

=======================
__platform_driver_probe
=======================

*man __platform_driver_probe(9)*

*4.6.0-rc5*

register driver for non-hotpluggable device


Synopsis
========

.. c:function:: int __platform_driver_probe( struct platform_driver * drv, int (*probe) struct platform_device *, struct module * module )

Arguments
=========

``drv``
    platform driver structure

``probe``
    the driver probe routine, probably from an __init section

``module``
    module which will be the owner of the driver


Description
===========

Use this instead of ``platform_driver_register`` when you know the
device is not hotpluggable and has already been registered, and you want
to remove its run-once ``probe`` infrastructure from memory after the
driver has bound to the device.

One typical use for this would be with drivers for controllers
integrated into system-on-chip processors, where the controller devices
have been configured as part of board setup.

Note that this is incompatible with deferred probing.

Returns zero if the driver registered and bound to a device, else
returns a negative error code and with the driver not registered.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
