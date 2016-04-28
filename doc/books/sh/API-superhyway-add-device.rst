.. -*- coding: utf-8; mode: rst -*-

.. _API-superhyway-add-device:

=====================
superhyway_add_device
=====================

*man superhyway_add_device(9)*

*4.6.0-rc5*

Add a SuperHyway module


Synopsis
========

.. c:function:: int superhyway_add_device( unsigned long base, struct superhyway_device * sdev, struct superhyway_bus * bus )

Arguments
=========

``base``
    Physical address where module is mapped.

``sdev``
    SuperHyway device to add, or NULL to allocate a new one.

``bus``
    Bus where SuperHyway module resides.


Description
===========

This is responsible for adding a new SuperHyway module. This sets up a
new struct superhyway_device for the module being added if ``sdev`` ==
NULL.

Devices are initially added in the order that they are scanned (from the
top-down of the memory map), and are assigned an ID based on the order
that they are added. Any manual addition of a module will thus get the
ID after the devices already discovered regardless of where it resides
in memory.

Further work can and should be done in ``superhyway_scan_bus``, to be
sure that any new modules are properly discovered and subsequently
registered.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
