.. -*- coding: utf-8; mode: rst -*-

.. _API-acpi-bus-trim:

=============
acpi_bus_trim
=============

*man acpi_bus_trim(9)*

*4.6.0-rc5*

Detach scan handlers and drivers from ACPI device objects.


Synopsis
========

.. c:function:: void acpi_bus_trim( struct acpi_device * adev )

Arguments
=========

``adev``
    Root of the ACPI namespace scope to walk.


Description
===========

Must be called under acpi_scan_lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
