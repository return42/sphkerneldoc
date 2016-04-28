.. -*- coding: utf-8; mode: rst -*-

.. _API-subsys-find-device-by-id:

========================
subsys_find_device_by_id
========================

*man subsys_find_device_by_id(9)*

*4.6.0-rc5*

find a device with a specific enumeration number


Synopsis
========

.. c:function:: struct device * subsys_find_device_by_id( struct bus_type * subsys, unsigned int id, struct device * hint )

Arguments
=========

``subsys``
    subsystem

``id``
    index 'id' in struct device

``hint``
    device to check first


Description
===========

Check the hint's next object and if it is a match return it directly,
otherwise, fall back to a full list search. Either way a reference for
the returned object is taken.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
