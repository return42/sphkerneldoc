
.. _API-acpi-bus-scan:

=============
acpi_bus_scan
=============

*man acpi_bus_scan(9)*

*4.6.0-rc1*

Add ACPI device node objects in a given namespace scope.


Synopsis
========

.. c:function:: int acpi_bus_scan( acpi_handle handle )

Arguments
=========

``handle``
    Root of the namespace scope to scan.


Description
===========

Scan a given ACPI tree (probably recently hot-plugged) and create and add found devices.

If no devices were found, -ENODEV is returned, but it does not mean that there has been a real error. There just have been no suitable ACPI objects in the table trunk from which
the kernel could create a device and add an appropriate driver.

Must be called under acpi_scan_lock.
