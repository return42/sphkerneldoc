.. -*- coding: utf-8; mode: rst -*-

======
scan.c
======

.. _`acpi_scan_drop_device`:

acpi_scan_drop_device
=====================

.. c:function:: void acpi_scan_drop_device (acpi_handle handle, void *context)

    Drop an ACPI device object.

    :param acpi_handle handle:
        Handle of an ACPI namespace node, not used.

    :param void \*context:
        Address of the ACPI device object to drop.


.. _`acpi_scan_drop_device.description`:

Description
-----------

This is invoked by :c:func:`acpi_ns_delete_node` during the removal of the ACPI
namespace node the device object pointed to by ``context`` is attached to.

The unregistration is carried out asynchronously to avoid running
:c:func:`acpi_device_del` under the ACPICA's namespace mutex and the list is used to
ensure the correct ordering (the device objects must be unregistered in the
same order in which the corresponding namespace nodes are deleted).


.. _`acpi_dma_supported`:

acpi_dma_supported
==================

.. c:function:: bool acpi_dma_supported (struct acpi_device *adev)

    Check DMA support for the specified device.

    :param struct acpi_device \*adev:
        The pointer to acpi device


.. _`acpi_dma_supported.description`:

Description
-----------

Return false if DMA is not supported. Otherwise, return true


.. _`acpi_get_dma_attr`:

acpi_get_dma_attr
=================

.. c:function:: enum dev_dma_attr acpi_get_dma_attr (struct acpi_device *adev)

    Check the supported DMA attr for the specified device.

    :param struct acpi_device \*adev:
        The pointer to acpi device


.. _`acpi_get_dma_attr.description`:

Description
-----------

Return enum dev_dma_attr.


.. _`acpi_bus_scan`:

acpi_bus_scan
=============

.. c:function:: int acpi_bus_scan (acpi_handle handle)

    Add ACPI device node objects in a given namespace scope.

    :param acpi_handle handle:
        Root of the namespace scope to scan.


.. _`acpi_bus_scan.description`:

Description
-----------

Scan a given ACPI tree (probably recently hot-plugged) and create and add
found devices.

If no devices were found, -ENODEV is returned, but it does not mean that
there has been a real error.  There just have been no suitable ACPI objects
in the table trunk from which the kernel could create a device and add an
appropriate driver.

Must be called under acpi_scan_lock.


.. _`acpi_bus_trim`:

acpi_bus_trim
=============

.. c:function:: void acpi_bus_trim (struct acpi_device *adev)

    Detach scan handlers and drivers from ACPI device objects.

    :param struct acpi_device \*adev:
        Root of the ACPI namespace scope to walk.


.. _`acpi_bus_trim.description`:

Description
-----------

Must be called under acpi_scan_lock.

