.. -*- coding: utf-8; mode: rst -*-

.. _API-subsys-virtual-register:

=======================
subsys_virtual_register
=======================

*man subsys_virtual_register(9)*

*4.6.0-rc5*

register a subsystem at /sys/devices/virtual/


Synopsis
========

.. c:function:: int subsys_virtual_register( struct bus_type * subsys, const struct attribute_group ** groups )

Arguments
=========

``subsys``
    virtual subsystem

``groups``
    default attributes for the root device


Description
===========

All 'virtual' subsystems have a /sys/devices/system/<name> root device
with the name of the subystem. The root device can carry subsystem-wide
attributes. All registered devices are below this single root device.
There's no restriction on device naming. This is for kernel software
constructs which need sysfs interface.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
