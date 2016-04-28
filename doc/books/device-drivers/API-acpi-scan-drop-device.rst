.. -*- coding: utf-8; mode: rst -*-

.. _API-acpi-scan-drop-device:

=====================
acpi_scan_drop_device
=====================

*man acpi_scan_drop_device(9)*

*4.6.0-rc5*

Drop an ACPI device object.


Synopsis
========

.. c:function:: void acpi_scan_drop_device( acpi_handle handle, void * context )

Arguments
=========

``handle``
    Handle of an ACPI namespace node, not used.

``context``
    Address of the ACPI device object to drop.


Description
===========

This is invoked by ``acpi_ns_delete_node`` during the removal of the
ACPI namespace node the device object pointed to by ``context`` is
attached to.

The unregistration is carried out asynchronously to avoid running
``acpi_device_del`` under the ACPICA's namespace mutex and the list is
used to ensure the correct ordering (the device objects must be
unregistered in the same order in which the corresponding namespace
nodes are deleted).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
