
.. _API-acpi-bus-trim:

=============
acpi_bus_trim
=============

*man acpi_bus_trim(9)*

*4.6.0-rc1*

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
