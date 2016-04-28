.. -*- coding: utf-8; mode: rst -*-

.. _API-subsys-system-register:

======================
subsys_system_register
======================

*man subsys_system_register(9)*

*4.6.0-rc5*

register a subsystem at /sys/devices/system/


Synopsis
========

.. c:function:: int subsys_system_register( struct bus_type * subsys, const struct attribute_group ** groups )

Arguments
=========

``subsys``
    system subsystem

``groups``
    default attributes for the root device


Description
===========

All 'system' subsystems have a /sys/devices/system/<name> root device
with the name of the subsystem. The root device can carry subsystem-
wide attributes. All registered devices are below this single root
device and are named after the subsystem with a simple enumeration
number appended. The registered devices are not explicitly named; only
'id' in the device needs to be set.

Do not use this interface for anything new, it exists for compatibility
with bad ideas only. New subsystems should use plain subsystems; and add
the subsystem-wide attributes should be added to the subsystem directory
itself and not some create fake root-device placed in
/sys/devices/system/<name>.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
